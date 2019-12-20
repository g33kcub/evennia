"""
This file contains the pregenned stats for all the dungeon 1 characters. 
There will be one for each race and each class so a total of 21 total.
 
Human, Half-Elf, Elf, Pixie, Inojin, Nekojin & Dwarf
Adventurer, Supporter & Citizen

Elven Swordsman - 3 Skill Choices.
Elven Priest - 4 skill choices.
Elven Enchanter - 4 skill choices.
"""

PREGEN_DUNGEON_1 = {
    "elven swordsman": {
        "race": "elf",
        "class": "adventurer",
        "concept": "elven swordsman",
        "languages": {
            "common": {
                "rank": 5,
            },
            "elven": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 1,
                "lxpl": 500
            },
            "water": {
                "rank": 1,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 2,
                "lxpl": 600
            }
        },
        "speed": 6,
        "resources": {
            "social": 15,
            "military": 20,
            "economic": 5
        },
        "currency": {
            "silver": 1200,
            "gold": 13
        },
        "d1_skills": {
            "swords": {
                "rank": 3,
                "lxpl": 1200
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500
            }
        }
    },
        "elven priest": {
        "race": "elf",
        "class": "supporter",
        "concept": "elven priest",
        "languages": {
            "common": {
                "rank": 5,
            },
            "elven": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 1,
                "lxpl": 500
            },
            "water": {
                "rank": 1,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 2,
                "lxpl": 600
            }
        },
        "speed": 6,
        "resources": {
            "social": 15,
            "military": 5,
            "economic": 20
        },
        "currency": {
            "silver": 1200,
            "gold": 23
        },
        "d1_skills": {
            "rods": {
                "rank": 1,
                "lxpl": 300
            },
            "healing energy": {
                "rank": 1,
                "lxpl": 500
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500
            }
        }
    },
        "elven enchanter": {
        "race": "elf",
        "class": "citizen",
        "concept": "elven enchanter",
        "languages": {
            "common": {
                "rank": 5,
            },
            "elven": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 1,
                "lxpl": 500
            },
            "water": {
                "rank": 1,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 2,
                "lxpl": 600
            }
        },
        "speed": 6,
        "resources": {
            "social": 25,
            "military": 5,
            "economic": 10
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "swords": {
                "rank": 1,
                "lxpl": 300
            },
            "enchanter": {
                "rank": 3,
                "lxpl": 600
            },
            "haggling": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500
            }
        }
    }
}