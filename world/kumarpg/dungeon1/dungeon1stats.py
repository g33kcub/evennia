from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dicts.d1_skills_defs import skills
from world.kumarpg.dicts.d1_stat_defs import stats
from world.kumarpg.dicts.d1_spell_defs import spells
from world.kumarpg.dicts.d1_ability_defs import abilities

"""
This is the stat file for Dungeon 1.
"""


def dungeon1_stats(character):
    """ Set base D1 stats/skills/magic/abilities """
    character.db.d1_stats = stats
    character.db.d1_weapons = weapons
    character.db.d1_skills = skills
    character.db.d1_magic = spells
    character.db.d1_abilities = abilities

