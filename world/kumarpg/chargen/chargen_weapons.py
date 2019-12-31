from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.utilities.format import cap_str,wrap
from world.kumarpg.chargen.chargen_skills import _build_skill
from world.kumarpg.chargen.chargen_utils import _skills, cgen_header, _get_race_weapon


def node_weapons(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [skill for skill in sorted(caller.db.d1_skills.keys()) if caller.db.d1_skills[skill]["rank"] > 0]
    cur_skills_race = [skill for skill in cur_skills if skill not in _get_race_weapon(caller)]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.d1_skills[x]["rank"]), cur_skills))
    list_skills.sort()

    text = "You have |w{}|n Weapon selections left to make. Please choose from the following list.\n" \
        .format(caller.ndb.pregen["weapons"])
    text = wrap(text, indent=1)
    text += "\n\n|w Current Weapons:\n|n "
    text += "\n|n ".join(list_skills)

    options = []
    _skill_list = sorted(weapons.keys())

    for skill in map(lambda x: cap_str(x), _skill_list):
        if skill not in cg["d1_skills"] and _weapon_pool(caller, skill) >= 0:
            options.append({
              "desc": skill,
              "goto": (_set_weapon, {"skill": skill.lower()})
            })

    if len(options) == 0:
        options.append({
          "key": ("Continue", "con", "c"),
          "desc": "Continue on to skills.",
          "goto": "node_skills"
        })

        options.append({
          "key": "Restart",
          "desc": "Restart this portion of character generation.",
          "goto": _reset_weapons
        })

        text = "You've selected all of your skills. You can |wcontinue|n forward to the next " \
               "section of chracter generation, or |wrestart|n and re-assign your skills."
        text = wrap(text, indent=1)
        text += "\n\n|w Current Skills:\n|n "
        text += "\n|n ".join(list_skills)

    return cgen_header("Weapons") + text, options


def node_weapons_2(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [skill for skill in sorted(caller.db.d1_skills.keys()) if caller.db.d1_skills[skill]["rank"] > 0]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.d1_skills[x]["rank"]), cur_skills))
    list_skills.sort()
    text = "|h|rYou don't have enough weapon ranks left to take that choice.|n\n\n"
    text += "You have |w{}|n Weapon selections left to make. Please choose from the following list.\n" \
        .format(caller.ndb.pregen["d1_skills"])
    text = wrap(text, indent=1)
    text += "\n\n|w Current Weapons:\n|n "
    text += "\n|n ".join(list_skills)

    options = []
    _skill_list = sorted(weapons.keys())

    for skill in map(lambda x: cap_str(x), _skill_list):
        if skill not in cg["skills"] and _weapon_pool(caller, skill) >= 0:
            options.append({
              "desc": skill,
              "goto": (_set_weapon, {"skill": skill.lower()})
            })

    if len(options) == 0:
        options.append({
          "key": ("Continue", "con", "c"),
          "desc": "Continue on to skills.",
          "goto": "node_skills"
        })

        options.append({
          "key": "Restart",
          "desc": "Restart this portion of character generation.",
          "goto": _reset_weapons
        })

        text = "You've selected all of your skills. You can |wcontinue|n forward to the next " \
               "section of chracter generation, or |wrestart|n and re-assign your skills."
        text = wrap(text, indent=1)
        text += "\n\n|w Current Skills:\n|n "
        text += "\n|n ".join(list_skills)
    return cgen_header("Skills") + text, options


def _weapon_pool(caller, skill, rank=1):
    skill = skill.lower()
    starting_rank = caller.db.d1_skills[skill]["rank"]

    return caller.ndb.pregen["weapons"] - (starting_rank + rank)


def _reset_weapons(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]
    caller.db.d1_skills = weapons

    for skill in weapons:
        try:
            caller.db.d1_skills[skill]["rank"] = cg["d1_skills"][skill]["rank"]
            caller.db.d1_skills[skill]["lxpl"] = cg["d1_skills"][skill]["lxpl"]
        except KeyError:
            pass

    _skill_list = [skill for skill in cg["d1_skills"] if skill in weapons]
    caller.ndb.pregen["weapons"] = _skills[caller.db.cls] - len(_get_race_weapon(caller))


def _set_weapon(caller, _, **kwargs):
    """ Set a skill and do the associated bookkeeping """
    pool = _weapon_pool(caller, kwargs.get("skill"))
    if pool < 0:
        # Not enough skill points left! Send them to the secondary
        # skills node with the reject message and the remaining skills
        # list.
        return "node_weapons_2"
    else:
        caller.db.d1_skills[kwargs.get("skill")]["rank"] += 1
        caller.ndb.pregen["weapons"] = pool
        if caller.ndb.pregen["weapons"]:
            return "node_skills"
