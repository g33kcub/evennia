"""
This file contains the pregenned stats for all the dungeon 1 characters. 
There will be one for each race and each class so a total of 21 total.
 
Human, Half-Elf, Elf, Pixie, Inojin, Nekojin & Dwarf
Adventurer, Supporter & Citizen

Elven Swordsman
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
                ,"lxpl": 300
            },
            "fire": {
                "rank": 1,
                "lxpl": 300
            },
            "water": {
                "rank": 1,
                "lxpl": 300
            },
            "air": {
                "rank": 1,
                "lxpl": 300
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
                "lxpl": 300
            }
        }
    }
}