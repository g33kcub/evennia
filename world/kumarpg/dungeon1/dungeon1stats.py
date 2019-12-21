from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dicts.d1_stat_defs import stats
from world.kumarpg.dicts.d1_spell_defs import spells
from world.kumarpg.dicts.d1_ability_defs import abilities

"""
This is the stat file for Dungeon 1.
"""


def dungeon1_stats(character):
    for stat in stats:
        character.db.d1_stats[stat] = stats[stat]

    for weapon in weapons:
        character.db.d1_skills[weapon] = weapons[weapon]

    for spell in spells:
        character.db.d1_magic[spell] = spells[spell]

    for ability in abilities:
        character.db.d1_abilities[ability] = abilities[ability]

