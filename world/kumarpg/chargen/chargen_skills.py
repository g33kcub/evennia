from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.skills_defs import skills
from world.kumarpg.dicts.stat_ranks import STAT_RANKS as ranks
from world.utilities.format import cap_str, trail, wrap
from world.kumarpg.chargen.chargen_utils import _skills, cgen_header


def _build_skill(skill, rank, length=22):
    return trail(cap_str(skill), length=length, delim=".") + "|w{}|n".format(ranks["%s" % rank])


def _skill_pool(caller, skill, rank=1):
    skill = skill.lower()
    if skill in skills:
        starting_rank = caller.db.skills[skill]["rank"]
    else:
        starting_rank = caller.db.d1_skills[skill]["rank"]

    return caller.ndb.pregen["skills"] - (starting_rank + rank)


def node_skills(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [skill for skill in sorted(caller.db.skills.keys()) if caller.db.skills[skill]["rank"] > 0]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.skills[x]["rank"]), cur_skills))
    list_skills.sort()

    text = "You have |w{}|n skill selections left to make. Please choose from the following list.\n" \
        .format(caller.ndb.pregen["skills"])
    text = wrap(text, indent=1)
    text += "\n\n|w Current Skills:\n|n "
    text += "\n|n ".join(list_skills)

    options = []
    _skill_list = sorted(skills.keys())

    for skill in map(lambda x: cap_str(x), _skill_list):
        if skill not in cg["skills"] and _skill_pool(caller, skill) >= 0:
            options.append({
              "desc": skill,
              "goto": (_set_skill, {"skill": skill.lower()})
            })

    if len(options) == 0:
        options.append({
          "key": ("Continue", "con", "c"),
          "desc": "Continue on to equipment.",
          "goto": "node_equipment"
        })

        options.append({
          "key": "Restart",
          "desc": "Restart this portion of character generation.",
          "goto": (_reset_skills, {"type": "skills"})
        })

        text = "You've selected all of your skills. You can |wcontinue|n forward to the next " \
               "section of chracter generation, or |wrestart|n and re-assign your skills."
        text = wrap(text, indent=1)
        text += "\n\n|w Current Skills:\n|n "
        text += "\n|n ".join(list_skills)
        return cgen_header("Skills") + text, options


def _reset_skills(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]
    caller.db.skills = skills

    for skill in skills:
        try:
            caller.db.skills[skill]["rank"] = cg["skills"][skill]["rank"]
            caller.db.skills[skill]["lxpl"] = cg["skills"][skill]["lxpl"]
        except KeyError:
            pass

    _skill_list = [skill for skill in cg["skills"] if skill in skills]
    caller.ndb.pregen["skills"] = _skills[caller.db.cls] - len(_skill_list)


def _set_skill(caller, _, **kwargs):
    """ Set a skill and do the associated bookkeeping """
    pool = _skill_pool(caller, kwargs.get("skill"))
    if pool < 0:
        # Not enough skill points left! Send them to the secondary
        # skills node with the reject message and the remaining skills
        # list.
        return "node_skills_2"
    else:
        caller.db.skills[kwargs.get("skill")]["rank"] += 1
        caller.ndb.pregen["skills"] = pool
        if caller.ndb.pregen["skills"]:
            return "node_skills"
