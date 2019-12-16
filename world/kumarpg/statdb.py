from evennia import DefaultCharacter
"""
This file contains all the various stats for the first dungeon.
"""

def character_stats(character):
    """
    A function to call all fo the default stats for a character.
    """
    stat_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0 }
    stat_dict_magic = {"rank": 0, "lxp": 0, "mp": 0, "lxpl": 0, "cor": 0, "hl": False}
    skill_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 0 }
    skill_dict_weapon = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 1 }
    skill_dict_social = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 2 }
    skill_dict_crafting = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 0 }
    skill_dict_crafting1 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 1 }
    skill_dict_crafting2 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 2 }
    skill_dict_crafting3 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 3 }
    skill_dict_crafting4 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 4 }
    skill_dict_crafting5 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 5 }
    skill_dict_tradesman = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 4 }
    character.db.stats = {
        "earth": stat_dict,
        "fire": stat_dict,
        "air": stat_dict,
        "water": stat_dict,
        "void": stat_dict
    }

    character.db.skills = {
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
        "wands": skill_dict_weapon,
        "persuasion": skill_dict_social,
        "haggling": skill_dict_social,
        "intimidation": skill_dict_social,
        "empathy": skill_dict_social,
        "subterfuge":skill_dict_social,
        "leadership": skill_dict_social,
        "command": skill_dict_social,
        "socialize": skill_dict_social,
        "etiquette": skill_dict_social,
        "armor smith":skill_dict_crafting1,
        "weapon smith":skill_dict_crafting1,
        "black smith":skill_dict_crafting1,
        "jeweler":skill_dict_crafting1,
        "carpenter":skill_dict_crafting1,
        "leather working":skill_dict_crafting2,
        "seamstress":skill_dict_crafting2,
        "miner":skill_dict_crafting3,
        "forager":skill_dict_crafting3,
        "farmer":skill_dict_crafting3,
        "fisher":skill_dict_crafting3,
        "scavenger":skill_dict_crafting3,
        "animal husbandry":skill_dict_crafting3,
        "enchanter":skill_dict_crafting4,
        "scribe":skill_dict_crafting4,
        "alchemy":skill_dict_crafting5,
        "culinarian":skill_dict_crafting5,
        "appraisal":skill_dict_tradesman,
        "research":skill_dict_tradesman
    }

    character.db.magic = {
        "firebolt": stat_dict_magic,
        "will-o-wisp": stat_dict_magic,
        "aquabolt": stat_dict_magic,
        "bubble screen": stat_dict_magic,
        "aerobolt": stat_dict_magic,
        "windscreen": stat_dict_magic,
        "geobolt": stat_dict_magic,
        "seismic tremor": stat_dict_magic,
        "pheonix flare": stat_dict_magic,
        "voidbolt": stat_dict_magic,
        "blackhole horizon": stat_dict_magic,
        "lightbolt": stat_dict_magic,
        "gleaming aura": stat_dict_magic,
        "tornado weapon": stat_dict_magic,
        "whirlpool weapon": stat_dict_magic,
        "sandstorm weapon": stat_dict_magic,
        "phoenix weapon": stat_dict_magic,
        "blizzard weapon": stat_dict_magic,
        "shadow weapon": stat_dict_magic,
        "shockbolt": stat_dict_magic,
        "arcticbolt": stat_dict_magic,
        "air lense": stat_dict_magic,
        "snowstorm": stat_dict_magic,
        "static weapon": stat_dict_magic,
        "frozen weapon": stat_dict_magic,
        "gleaming weapon": stat_dict_magic,
        "arctic snap": stat_dict_magic,
        "earthquake": stat_dict_magic,
        "blackhole supernova": stat_dict_magic,
        "heaven's shockwave": stat_dict_magic,
        "manabolt": stat_dict_magic,
        "protection": stat_dict_magic,
        "reflection": stat_dict_magic,
        "liminal light": stat_dict_magic,
        "healing energy": stat_dict_magic,
        "haste": stat_dict_magic,
        "slow": stat_dict_magic,
        "sanctuary": stat_dict_magic,
        "gravity crush": stat_dict_magic,
        "crimson lightning": stat_dict_magic,
        "medusa's gaze": stat_dict_magic,
        "blinding light": stat_dict_magic,
        "earshock": stat_dict_magic,
        "psion wave": stat_dict_magic,
        "rebuke": stat_dict_magic,
        "attack up": stat_dict_magic,
        "defense up": stat_dict_magic,
        "armor break": stat_dict_magic,
        "power break": stat_dict_magic,
        "undine": stat_dict_magic,
        "salamander": stat_dict_magic,
        "gnome": stat_dict_magic,
        "luna": stat_dict_magic,
        "wisp": stat_dict_magic,
        "shimmer": stat_dict_magic,
    }
