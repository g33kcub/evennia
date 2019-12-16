def character_stats(Character):
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
        "fire": stat_dict_magic,
        "water": stat_dict_magic,
        "aero": stat_dict_magic,
        "stone": stat_dict_magic,
        "cure": stat_dict_magic,
        "shield": stat_dict_magic,
        "esuna": stat_dict_magic,
        "blizzard": stat_dict_magic,
        "lightning": stat_dict_magic
    }
