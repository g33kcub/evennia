from world.kumarpg.dicts.types_defs import types

"""
This is the stat file for universal stats.
"""


def universal_stats(character):
    character.db.languages = {
        "common": types["lang_dict"],
        "elven": types["lang_dict"],
        "dwarvish": types["lang_dict"],
        "sylvan": types["lang_dict"],
        "caninonese": types["lang_dict"],
        "felinonese": types["lang_dict"],
        "draconic": types["lang_dict"],
        "celestial": types["lang_dict"],
        "infernal": types["lang_dict"],
        "ren alfeme": types["lang_dict"],
        "thieves cant": types["lang_dict"],
        "assassins creed": types["lang_dict"],
        "arthenor": types["lang_dict"],
        "tykeno": types["lang_dict"]
    }
