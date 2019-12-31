from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dicts.skills_defs import skills
from world.utilities.format import cap_str, wrap
from world.kumarpg.chargen.chargen_utils import cgen_header, _skills, _weapons, _get_race_weapon
from evennia.utils.utils import list_to_string


def _preview_package(caller, _, **kwargs):
    caller.ndb.pregen = {
      "pkg": kwargs.get("pkg", "elven swordsman"),
      "next": "node_view_pregen"
    }

    return "node_view_pregen"


def node_package(_):
    text = "Choose a package for more information about it.  Fluff here that we" \
           "want to show to the person entering the menu.  Something about pregens" \
           "letting them into the game world faster with some personalization." \
           "Havefun! :)"
    text = wrap(text, width=78, indent=1)
    options = []
    for template in sorted(map(lambda x: cap_str(x), pregen.PREGEN_DUNGEON_1.keys())):
        options.append({
          "desc": template,
          "goto": (_preview_package, {"pkg": template.lower()})
        })
    hdr =cgen_header("Pregen Packages") + "\n\n"
    return hdr + text, options


def node_view_pregen(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    weapon_count = _get_race_weapon(caller)

    try:
        _skill_list = [skill for skill in cg["skills"] if skill in skills]
    except KeyError:
        _skill_list = []

    # Dungeon specific skills and universal skills combined.
    _total_skills = [cap_str(skill) for skill in cg["d1_skills"]] + [cap_str(skill) for skill in cg["skills"]]
    _total_skills.sort()

    text = "|w Template:|n        {}".format(cg["key"]) + "\n"
    text += "|w Concept:|n         {}".format(cg["concept"]) + "\n"
    text += "|w Race:|n            {}".format(cap_str(cg["race"])) + "\n"
    text += "|w Speed:|n           {}".format(cg["speed"]) + "\n"
    text += "|w Class:|n           {}".format(cap_str(cg["cls"])) + "\n"
    text += "|w Languages:|n       {}".format(list_to_string([cap_str(lang) for lang in cg["languages"]])) + "\n"
    text += "|w Skills:|n          {}".format(list_to_string(_total_skills)) + "\n"
    text += "|w Weapon Choices:|n  {}".format(_weapons[cg["cls"]] - len(weapon_count)) + "\n"
    text += "|w Skill Choices:|n   {}".format(_skills[cg["cls"]] - len(_skill_list)) + "\n"
    try:
        text += "\n" + wrap(cg["desc"], indent=1) + "\n"
    except KeyError:
        pass

    options = (
      {
        "key": ("Accept", "a"),
        "desc": "Choose this pregen template",
        "goto": _set_template
      },
      {
        "key": ("Back", "b"),
        "desc": "Choose a different pregen template",
        "goto": "node_package"
      }
    )

    return cgen_header("Pregen Details") + "\n" + text, options


def _set_template(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    _weapon_list = _get_race_weapon(caller)

    # Set demographics
    caller.db.template = cg["key"]
    caller.db.race = cg["race"]
    caller.db.cls = cg["cls"]
    caller.db.concept = cg["concept"]

    # set languages
    for lang in cg["languages"]:
        caller.db.languages[lang]["rank"] = cg["languages"][lang]["rank"]

    # set resources
    for resource in cg["resources"]:
        caller.db.resources[resource] = cg["resources"][resource]

    # Set currency
    for curr in cg["currency"]:
        caller.db.currency[curr] = cg["currency"][curr]

    # set stats
    for stat in cg["d1_stats"]:
        caller.db.d1_stats[stat]["rank"] = cg["d1_stats"][stat]["rank"]
        caller.db.d1_stats[stat]["lxpl"] = cg["d1_stats"][stat]["lxpl"]

    # set d1_skills
    for skill in cg["d1_skills"]:
        try:
            caller.db.d1_skills[skill]["rank"] = cg["d1_skills"][skill]["rank"]
            caller.db.d1_skills[skill]["lxpl"] = cg["d1_skills"][skill]["lxpl"]
        except KeyError:
            pass

    # set skills
    for skill in cg["skills"]:
        try:
            caller.db.skills[skill]["rank"] = cg["skills"][skill]["rank"]
            caller.db.skills[skill]["lxpl"] = cg["skills"][skill]["lxpl"]
        except KeyError:
            pass
    # Set Abilities
    for abil in cg["d1_abilities"]:
        caller.db.d1_abilities[abil]["rank"] = cg["d1_abilities"][abil]["rank"]
        caller.db.d1_abilities[abil]["lxpl"] = cg["d1_abilities"][abil]["lxpl"]

    _skill_list = [skill for skill in cg["skills"] if skill in skills]
    caller.ndb.pregen["skills"] = _skills[caller.db.cls] - len(_skill_list)

    caller.ndb.pregen["weapons"] = _weapons[caller.db.cls] - len(_get_race_weapon(caller))

    return "node_weapons"
