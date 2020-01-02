from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.utilities.format import cap_str,wrap
from world.kumarpg.chargen.chargen_skills import _build_skill
from world.kumarpg.chargen.chargen_utils import _weapons, cgen_header, _get_race_weapon


def node_weapons(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [weapon for weapon in sorted(caller.db.d1_weapons.keys()) if caller.db.d1_weapons[weapon]["rank"] > 0]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.d1_weapons[x]["rank"]), cur_skills))
    list_skills.sort()

    text = "You have |w{}|n Weapon selections left to make. Please choose from the following list.\n" \
        .format(caller.ndb.pregen["weapons"])
    text = wrap(text, indent=1)
    text += "\n\n|w Current Weapons:\n|n "
    text += "\n|n ".join(list_skills)

    options = []
    _skill_list = sorted(weapons.keys())

    for weapon in map(lambda x: cap_str(x), _skill_list):
        if weapon not in cg["d1_weapons"] and _weapon_pool(caller) >= 0:
            options.append({
              "desc": weapon,
              "goto": (_set_weapon, {"weapon": weapon.lower()})
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
        text += "\n\n|w Current Weapons:\n|n "
        text += "\n|n ".join(list_skills)

    return cgen_header("Weapons") + text, options


def _weapon_pool(caller, rank=1):
    return caller.ndb.pregen["weapons"] - rank


def _reset_weapons(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]
    caller.db.d1_weapons = weapons

    for weapon in cg["d1_weapons"]:
        try:
            caller.db.d1_weapons[weapon]["rank"] = cg["d1_weapons"][weapon]["rank"]
            caller.db.d1_weapons[weapon]["lxpl"] = cg["d1_weapons"][weapon]["lxpl"]
        except KeyError:
            pass

    _weapon_list = [weapon for weapon in cg["d1_weapons"] if weapon in weapons]
    caller.ndb.pregen["weapons"] = _weapons[caller.db.cls] - len(_get_race_weapon(caller))


def _set_weapon(caller, _, **kwargs):
    """ Set a weapon and do the associated bookkeeping """
    pool = _weapon_pool(caller, kwargs.get("weapon"))

    caller.db.d1_weapons[kwargs.get("weapon")]["rank"] += 1
    caller.ndb.pregen["weapons"] = pool
    return "node_weapons"
