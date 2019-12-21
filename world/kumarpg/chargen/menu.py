from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dicts.skills_defs import skills
from world.utilities.format import wrap
from django.conf import settings

_current_dungeon = "D1"


def node_start(caller):
    text = \
        """
        This is the very first menu the user will see when they enter the chargen
        system.  I'm not sure if you want to put fluff here, or just something like:
        
        Welcome to the {} character generation system. There are two options for 
        going through character generation. 1. Choose a pregen template and 
        personalize it.  Or 2. Build your own sheet from scratch (advanced). 
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
    caller.ndb.pregen = {"pkg": kwargs.get("pkg", "elven swordsman")}
    return "node_view_pregen"


def node_package(caller):
    text = \
        """
        Choose a package for more information about it.  Fluff here that we
        want to show to the person entering the menu.  Something about pregens
        letting them into the game world faster with some personalization. Have fun! :)
        """
    options = []
    for template in pregen.PREGEN_DUNGEON_1:
        options.append({
            "desc": template,
            "goto": (_preview_package, {"pkg": template})
        })

    return text, options


def node_view_pregen(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen]
    text = "|wTemplate:|n   {}".format(cg) + "\n"
    text += "%s" % wrap(cg["desc"], width=50) + "\n" or ""
    text += "|wRace:|n      {}".format(cg["race"]) + "\n"
    text += "|wSpeed:|n     {}".format(cg["speed"]) + "\n"
    text += "|wClass:|n     {}".format(["cls"]) + "\n"
    text += "|wConcept:|n   {}".format(cg["concept"]) + "\n"
    text += "|wLanguages:|n {}".format(",".join([lang for lang in cg["languages"]])) + "\n"
    text += "|wSkills:|n    {}".format(",".join([skill for skill in cg["d1_skills"]])) + "\n"

    options = (
        {
            "key": "Accept",
            "desc": "Choose this pregen template",
            "goto": _set_template
        },
        {
            "key": "Decline",
            "desc": "Choose a different pregen template",
            "goto": "node_package"
        }
    )

    return text, options


def _set_template(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen]

    # Set demographics
    caller.db.template = cg["template"]
    caller.db.race = cg["race"]
    caller.db.cls = cg["cls"]
    caller.db.concept = cg["concept"]

    # set languages
    for lang in cg["languages"]:
        caller.db.languages[lang]["rank"] = cg[lang]["rank"]

    # set resources
    for resource in cg["resources"]:
        caller.db.resource[resource] = cg["resources"][resource]

    # Set currency
    for curr in cg["currency"]:
        caller.db.currency[curr] = cg["currency"][curr]

    # set stats
    for stat in cg["d1_stats"]:
        caller.db.d1_stats[stat]["rank"] = cg["d1_stats"][stat]["rank"]
        caller.db.d1_stats[stat]["lxpl"] = cg["d1_stats"][stat]["lxpl"]

    # set skills
    for skill in cg["d1_skills"]:
        caller.db.d1_skills[skill]["rank"] = cg["d1_stats"][skill]["rank"]
        caller.db.d1_skills[skill]["lxpl"] = cg["d1_stats"][skill]["lxpl"]

    # Set Abilities
    for abil in cg["d1_abilities"]:
        caller.db.d1_abilities[abil]["rank"] = cg["d1_abilities"][abil]["rank"]
        caller.db.d1_abilities[abil]["lxpl"] = cg["d1_abilities"][abil]["lxpl"]

    # Calculate how many left over chargen items to handle..

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

    _weapon_list = [weapon for weapon in caller.db.d1_skills if weapon in weapons]
    _skill_list = [skill for skill in caller.db.d1_skills if skill in skills]

    caller.ndb.pregen["weapons"] = _weapons[caller.db.cls] - len(_weapon_list)
    caller.ndb.pregen["skills"] = _skills[caller.db.cls] - len(_skill_list)

    if caller.ndb.pregen["weapons"]:
        return "node_weapons"
    elif caller.ndb.pregen["skills"]:
        return "node_skills"
    else:
        return "node"


def node_weapons(caller):
    text = \
        """
        You have {} weapon selections left to make.  Please choose from 
        the following list.
        """
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
        return None, None


def node_skills(caller):
    text = \
        """
        You have {} skill selections left to make.  Please choose from 
        the following list.
        """
    options = []
    for skill in skills:
        if skill not in caller.db.skills:
            options.append({
                "description": skill,
                "goto": (_set_weapon, {"weapon": skill})
            })

    return text, options


def _set_skill(caller, raw_string, **kwargs):
    """ Set a skill and do the associated bookkeeping """
    caller.db.skills[kwargs.get("skill")]["rank"] += 1
    caller.ndb.pregen["skills"] -= 1

    if caller.ndb.pregen["skills"]:
        return "node_skills"
    else:
        return None, None
