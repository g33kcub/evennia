from evennia import DefaultCharacter
from world.kumarpg.dict import stat_dict
"""
This is the stat file for universal stats.
"""

def universal_stats(character):
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

    character.db.skills = {
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