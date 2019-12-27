from world.kumarpg.dicts.d2_weapon_defs import weapons
from world.kumarpg.dicts.d1_stat_defs import stats
from world.kumarpg.dicts.d2_spell_defs import spells
from world.kumarpg.dicts.d2_ability_defs import abilities

"""
This is the stat file for Dungeon 2.
"""


def dungeon2_stats(character):
    """ Set base d2 stats/skills/magic/abilities """
    character.db.d2_stats = stats
    character.db.d2_skills = weapons
    character.db.d2_magic = spells
    character.db.d2_abilities = abilities