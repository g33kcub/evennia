"""
This is a database of all the materials in the system. 
More will get added as new dungeons are introduced. 
Materials are limited to a specific dungeon, will be statted as such.

Material Formatting:

NAME      = STR = A bit obvious.
Tier      = INT = This determines the generic value of it when combined with rarity.
Rarity    = STR = How often it is found during the month cycle. 
Table     = []  = Global, D1, D2, etc Can be more than one. 
TYPE      = STR = What type of material is. Plant, etc. 
Desc      = STR = Description of it. 
QUIRK     = STR = A list of any magical or unique properties. 
"""

MATERIAL_TABLE = {
    "pelt, low quality": {
        "tier": 0,
        "rarity": "common",
        "table": ['Global'],
        "type": "beast part",
        "desc": "A pelt of any animal, though badly cut from them.",
        "quirk": "none"
    },
    "pelt": {
        "tier": 1,
        "rarity": "common",
        "table": ['Global'],
        "type": "beast part",
        "desc": "A pelt of any animal, skinned by someone with some basic skill.",
        "quirk": "none"
    },
    "pelt, high quality": {
        "tier": 2,
        "rarity": "uncommon",
        "table": ['Global'],
        "type": "beast part",
        "desc": "A pelt of any animal, skinned by someone with masterful skills.",
        "quirk": "Adds +1 to armor made with it."
    },
    "pelt, exotic": {
        "tier": 3,
        "rarity": "rare",
        "table": ['Global'],
        "desc": "A pelt of a rare and exotic creature, maybe even mythical, skinned with great care.",
        "quirk": "Adds +3 to armor made with it."
    },
    "wood, low quality": {
        "tier": 0,
        "rarity": "common",
        "table": ['Global'],
        "type": "wood",
        "desc": "A piece of wood, though it is roughly hewn from its source.",
        "quirk": "none"
    }
}