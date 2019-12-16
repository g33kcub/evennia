from evennia import DefaultCharacter
from world.kumarpg.dict import stat_dict
"""
This is the stat file for Dungeon 1.
"""

def dungeon1_stats(character):
    character.db.d1.stats = {
      "earth": stat_dict,
      "fire": stat_dict,
      "air": stat_dict,
      "water": stat_dict,
      "void": stat_dict
    }

    character.db.d1.skills = {
        "swords": skill_dict_weapon,
        "knives": skill_dict_weapon,
        "hammers" : skill_dict_weapon,
        "whips": skill_dict_weapon,
        "spears": skill_dict_weapon,
        "staves": skill_dict_weapon,
        "axes": skill_dict_weapon,
        "bows": skill_dict_weapon,
        "fans": skill_dict_weapon,
        "rods": skill_dict_weapon,
        "wands": skill_dict_weapon
    }

    character.db.d1.magic = {
        "firebolt": magic_dict,
        "will-o-wisp": magic_dict,
        "aquabolt": magic_dict,
        "bubble screen": magic_dict,
        "aerobolt": magic_dict,
        "windscreen": magic_dict,
        "geobolt": magic_dict,
        "seismic tremor": magic_dict,
        "pheonix flare": magic_dict,
        "voidbolt": magic_dict,
        "blackhole horizon": magic_dict,
        "lightbolt": magic_dict,
        "gleaming aura": magic_dict,
        "tornado weapon": magic_dict,
        "whirlpool weapon": magic_dict,
        "sandstorm weapon": magic_dict,
        "phoenix weapon": magic_dict,
        "blizzard weapon": magic_dict,
        "shadow weapon": magic_dict,
        "shockbolt": magic_dict,
        "arcticbolt": magic_dict,
        "air lense": magic_dict,
        "snowstorm": magic_dict,
        "static weapon": magic_dict,
        "frozen weapon": magic_dict,
        "gleaming weapon": magic_dict,
        "arctic snap": magic_dict,
        "earthquake": magic_dict,
        "blackhole supernova": magic_dict,
        "heaven's shockwave": magic_dict,
        "manabolt": magic_dict,
        "protection": magic_dict,
        "reflection": magic_dict,
        "liminal light": magic_dict,
        "healing energy": magic_dict,
        "haste": magic_dict,
        "slow": magic_dict,
        "sanctuary": magic_dict,
        "gravity crush": magic_dict,
        "crimson lightning": magic_dict,
        "medusa's gaze": magic_dict,
        "blinding light": magic_dict,
        "earshock": magic_dict,
        "psion wave": magic_dict,
        "rebuke": magic_dict,
        "attack up": magic_dict,
        "defense up": magic_dict,
        "armor break": magic_dict,
        "power break": magic_dict,
        "undine": magic_dict,
        "salamander": magic_dict,
        "gnome": magic_dict,
        "luna": magic_dict,
        "wisp": magic_dict,
        "shimmer": magic_dict,
    }

    character.db.d1.abilities = {
        "flight": ability_dict,
        "night sight": ability_dict,
        "adaptive": ability_dict,
        "unnatural resistance": ability_dict,
        "mana font": ability_dict,
        "quick learner": ability_dict,
    }