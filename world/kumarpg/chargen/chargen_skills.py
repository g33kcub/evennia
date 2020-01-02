from world.kumarpg.dungeon1 import dungeon1pregen as pregen
from world.kumarpg.dicts.d1_skills_defs import skills
from world.kumarpg.dicts.stat_ranks import STAT_RANKS as RANKS
from world.utilities.format import cap_str, trail, wrap
from world.kumarpg.chargen.chargen_utils import _skills, cgen_header


def _build_skill(skill, rank, length=22):
    return trail(cap_str(skill), length=length, delim=".") + "|w{}|n".format(RANKS["%s" % rank])


def _skill_pool(caller, rank=1):

    return caller.ndb.pregen["skills"] - rank


def node_skills(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    cur_skills = [skill for skill in sorted(caller.db.d1_skills.keys()) if caller.db.d1_skills[skill]["rank"] > 0]
    list_skills = list(map(lambda x: _build_skill(x, caller.db.d1_skills[x]["rank"]), cur_skills))
    list_skills.sort()

    text = "You have |w{}|n skill selections left to make. Please choose from the following list.\n" \
        .format(caller.ndb.pregen["skills"])
    text = wrap(text, indent=1)
    text += "\n\n|w Current Skills:\n|n "
    text += "\n|n ".join(list_skills)

    options = []
    _skill_list = sorted(skills.keys())

    for skill in map(lambda x: cap_str(x), _skill_list):
        if skill not in cg["d1_skills"] and _skill_pool(caller) >= 0:
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
    caller.db.d1_skills = skills

    for skill in skills:
        try:
            caller.db.d1_skills[skill]["rank"] = cg["d1_skills"][skill]["rank"]
            caller.db.d1_skills[skill]["lxpl"] = cg["d1_skills"][skill]["lxpl"]
        except KeyError:
            pass

    _skill_list = [skill for skill in cg["d1_skills"] if skill in skills]
    caller.ndb.pregen["skills"] = _skills[caller.db.cls] - len(_skill_list)


def _set_skill(caller, _, **kwargs):
    """ Set a skill and do the associated bookkeeping """
    pool = _skill_pool(caller, kwargs.get("skill"))
    caller.db.d1_skills[kwargs.get("skill")]["rank"] += 1
    caller.ndb.pregen["skills"] = pool

    return "node_skills"
