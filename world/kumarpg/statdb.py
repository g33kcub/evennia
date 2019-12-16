from evennia import DefaultCharacter
"""
This file contains all the various stats for the first dungeon.
"""

def character_stats(character):
    """
    A function to call all fo the default stats for a character.
    """
    lang_dict = {"rank": 0, "lxp": 0, "lxpl": 0, "cor": 0}
    ability_dict = {"rank": 0, "lxp": 0, "mp": 0, "lxpl": 0, "cor": 0, "hl": False}
    stat_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0 }
    magic_dict = {"rank": 0, "lxp": 0, "mp": 0, "lxpl": 0, "cor": 0, "hl": False}
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

    character.db.abilities = {
        "flight": ability_dict,
        "night sight": ability_dict,
        "adaptive": ability_dict,
        "unnatural resistance": ability_dict,
        "mana font": ability_dict,
        "quick learner": ability_dict,
    }

    character.db.languages = {
        "common": lang_dict,
        "elven": lang_dict,
        "dwarvish": lang_dict,
        "sylvan": lang_dict,
        "caninonese": lang_dict,
        "felinonese": lang_dict,
        "draconic": lang_dict,
        "celestial": lang_dict,
        "infernal": lang_dict,
        "ren alfeme": lang_dict,
        "thieves cant": lang_dict,
        "assassins creed": lang_dict,
        "arthenor": lang_dict,
        "tykeno": lang_dict
    }