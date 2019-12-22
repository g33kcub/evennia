from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dicts.skills_defs import skills
from world.kumarpg.dicts.stat_ranks import STAT_RANKS as ranks
from world.utilities.format import cap_str, trail, columns
from django.conf import settings
from evennia.utils.utils import list_to_string, wrap

_current_dungeon = "D1"
_weapons = {
    "adventurer": 2,
    "supporter": 1,
    "citizen": 0
}
_skills = {
    "adventurer": 3,
    "supporter": 5,
    "citizen": 8
}


def node_start(caller):
    text = \
        """
        Welcome to the |w{}|n character generation system. There 
        are two options for going through character generation. 1. Choose 
        a pregen template and personalize it.  Or 2. Build your own sheet 
        from scratch (advanced). 
        """.format(settings.SERVERNAME)

    options = (
        {
            "key": ("Pregen", "pregen"),
            "desc": "Start with a pre-generated template",
            "goto": "node_package"
        }
    )

    return text, options


def _preview_package(caller, raw_string, **kwargs):
    caller.ndb.pregen = {
        "pkg": kwargs.get("pkg", "elven swordsman"),
        "next": "node_view_pregen"
    }

    return "node_view_pregen"


def _get_race_weapon(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    # Set a few chargen notes about free weapon ranks
    if cg["race"].lower() == "dwarf":
        caller.ndb.pregen["weapon"] = ["hammers"]

    if cg["race"].lower() == "elf":
        caller.ndb.pregen["weapon"] = ["bow", "swords"]

    if cg["race"].lower() == "half-elf":
        caller.ndb.pregen["weapon"] = ["swords"]

    if cg["race"].lower() == "nekojin":
        caller.ndb.pregen["weapon"] = ["swords"]

    if cg["race"].lower() == "inojin":
        caller.ndb.pregen["weapon"] = ["staves"]

    _weapon_list = [weapon for weapon in cg["d1_skills"] if weapon in weapons]
    return [weapon for weapon in _weapon_list if weapon not in caller.ndb.pregen["weapon"]]


def node_package(caller):
    text = "Choose a package for more information about it.  Fluff here that we \
        want to show to the person entering the menu.  Something about pregens \
        letting them into the game world faster with some personalization. \
        Havefun! :)"
    text = wrap(text, width=78)
    options = []
    for template in sorted(pregen.PREGEN_DUNGEON_1.keys()):
        options.append({
            "desc": template,
            "goto": (_preview_package, {"pkg": template})
        })

    return text, options


def node_view_pregen(caller):

    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    weapon_count = _get_race_weapon(caller)

    try:
        _skill_list = [skill for skill in cg["skills"] if skill in skills]
    except KeyError:
        _skill_list = []

    _total_skills = [cap_str(skill) for skill in cg["d1_skills"]] + [cap_str(skill) for skill in cg["skills"]]
    _total_skills.sort()

    text = "|w Template:|n        {}".format(cg["key"]) + "\n"
    text += "|w Concept:|n         {}".format(cg["concept"]) + "\n"
    text += "|w Race:|n            {}".format(cg["race"]) + "\n"
    text += "|w Speed:|n           {}".format(cg["speed"]) + "\n"
    text += "|w Class:|n           {}".format(cg["cls"]) + "\n"
    text += "|w Languages:|n       {}".format(list_to_string([cap_str(lang) for lang in cg["languages"]])) + "\n"
    text += "|w Skills:|n          {}".format(list_to_string(_total_skills)) + "\n"
    text += "|w Weapon Choices:|n  {}".format(_weapons[cg["cls"]] - len(weapon_count)) + "\n"
    text += "|w Skill Choices:|n   {}".format(_skills[cg["cls"]] - len(_skill_list)) + "\n"
    try:
        text += "\n" + wrap(cg["desc"]) + "\n"
    except KeyError:
        pass

    options = (
        {
            "key": "Accept",
            "desc": "Choose this pregen template",
            "goto": _set_template
        },
        {
            "key": "Back",
            "desc": "Choose a different pregen template",
            "goto": "node_package"
        }
    )

    return text, options


def _set_template(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]
    caller_ndb = caller.ndb.pregen

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

    caller.ndb.pregen["weapons"] = _weapons[caller.db.cls] - len(_weapon_list)
    caller.ndb.pregen["skills"] = _skills[caller.db.cls] - len(_skill_list)

    return "node_skills"


def node_weapons(caller):
    text = \
        """
        You have {} weapon selections left to make.  Please choose from 
        the following list.
        """.format(caller.ndb.pregen["weapons"])
    options = []
    for weapon in weapons:
        if weapon not in caller.db.d1_skills:
            options.append({
                "description": weapon,
                "goto": (_set_weapon, {"weapon": weapon})
            })

    return text, options


def _set_weapon(caller, raw_string, **kwargs):
    """ Set a weapon skill and do the associated bookkeeping """
    caller.db.d1_skills[kwargs.get("weapon")]["rank"] += 1
    caller.ndb.pregen["weapons"] -= 1

    if caller.ndb.pregen["weapons"]:
        return "node_weapons"
    elif caller.ndb.pregen["skills"]:
        return "node_skills"
    else:
        return None


def _build_skill(skill, rank, length=19):
    return trail(cap_str(skill), length=length) + "|w{}|n".format(ranks["%s" % rank])


def node_skills(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [skill for skill in sorted(caller.db.skills.keys()) if caller.db.skills[skill]["rank"] > 0]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.skills[x]["rank"]), cur_skills))
    list_skills.sort()

    text = \
        """
        |n You have |w{}|n skill selections left to make.  Please choose from 
        |n the following list.
        
        |w Current Skills:|n
        
        |n  {}
        """.format(caller.ndb.pregen["skills"], columns("~".join(list_skills), cols=3, sep="~"))
    options = []
    _skill_list = sorted(skills.keys())

    for skill in map(lambda x: cap_str(x), _skill_list):
        if skill not in cg["skills"]:
            options.append({
                "desc": skill,
                "goto": (_set_skill, {"skill": skill.lower()})
            })

    return text, options


def _set_skill(caller, raw_string, **kwargs):
    """ Set a skill and do the associated bookkeeping """
    caller.db.skills[kwargs.get("skill")]["rank"] += 1
    caller.ndb.pregen["skills"] -= (caller.db.skills[kwargs.get("skill")]["rank"] + 1)

    if caller.ndb.pregen["skills"]:
        return "node_skills"
