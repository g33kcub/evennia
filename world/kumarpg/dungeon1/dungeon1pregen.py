"""
This file contains the pregenned stats for all the dungeon 1 characters. 
There will be one for each race and each cls so a total of 21 total.
 
Human, Half-Elf, Elf, Pixie, Inojin, Nekojin & Dwarf
Adventurer, Supporter & Citizen

Elven Swordsman - 3 Skill Choices.
Elven Priest - 4 skill choices.
Elven Enchanter - 4 skill choices.

Human Warrior - 3 Skill Choices.
Human Paladin - 4 Skill Choices.
Human Guild Associate - 4 skill choices.

Half-Elf Archer - 3 skill Choices.
Half-Elf Scout -  4 Skill choices.
Half-Elf Beastmaster - 4 Skill Choices.

Pixie Dagger Dancer - 3 Skill Choices.
Pixie Trickster - 4 skill choices
Pixie Gatherer - 4 skill choices

Dwarven Berserker - 3 Skill Choices.
Dwarven Shield Bearer - 4 Skill Choices
Dwarven Smith - 4 skill choices.

Inojin Alpha - 3 Skill Choices
Inojin Void Stalker - 4 Skill Choices
Inojin Cartographer - 4 Skill choices.

Nekojin Dominator - 3 Skill Choices.
Nekojin Druid - 4 Skill Choices
Nekojin Merchant - 4 Skill Choices.
"""

PREGEN_DUNGEON_1 = {
    "nekojin merchant": {
        "race": "nekojin",
        "cls": "citizen",
        "concept": "nekojin merchant",
        "languages": {
            "common": {
                "rank": 5,
            },
            "felinonese": {
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
                "rank": 2,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 20,
            "military": 5,
            "economic": 10
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "appraisal": {
                "rank": 2,
                "lxpl": 300
            },
            "haggling": {
                "rank": 2,
                "lxpl": 300
            },
            "whips": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "nekojin druid": {
        "race": "nekojin",
        "cls": "supporter",
        "concept": "nekojin druid",
        "languages": {
            "common": {
                "rank": 5,
            },
            "felinonese": {
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
                "rank": 2,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 5,
            "economic": 20
        },
        "currency": {
            "silver": 1500,
            "gold": 20
        },
        "d1_skills": {
            "geobolt": {
                "rank": 1,
                "lxpl": 500
            },
            "liminal light": {
                "rank": 1,
                "lxpl": 500
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "nekojin dominator": {
        "race": "nekojin",
        "cls": "adventurer",
        "concept": "nekojin dominator",
        "languages": {
            "common": {
                "rank": 5,
            },
            "felinonese": {
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
                "rank": 2,
                "lxpl": 500
            },
            "air": {
                "rank": 1,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 20,
            "economic": 5
        },
        "currency": {
            "silver": 1500,
            "gold": 10
        },
        "d1_skills": {
            "whips": {
                "rank": 3,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "inojin cartographer": {
        "race": "inojin",
        "cls": "citizen",
        "concept": "inojin cartographer",
        "languages": {
            "common": {
                "rank": 5,
            },
            "caninonese": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 20,
            "military": 5,
            "economic": 10
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "staves": {
                "rank": 1,
                "lxpl": 300
            },
            "scribe": {
                "rank": 3,
                "lxpl": 300
            },
            "survival": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "inojin void stalker": {
        "race": "inojin",
        "cls": "supporter",
        "concept": "inojin void stalker",
        "languages": {
            "common": {
                "rank": 5,
            },
            "caninonese": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 5,
            "economic": 20
        },
        "currency": {
            "silver": 1500,
            "gold": 20
        },
        "d1_skills": {
            "knives": {
                "rank": 1,
                "lxpl": 300
            },
            "shadow weapon": {
                "rank": 1,
                "lxpl": 500
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "inojin alpha": {
        "race": "inojin",
        "cls": "adventurer",
        "concept": "inojin alpha",
        "languages": {
            "common": {
                "rank": 5,
            },
            "caninonese": {
                "rank": 5,
            }
        },
        "d1_stats": {
            "earth": {
                "rank": 1,
                "lxpl": 500
            },
            "fire": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 20,
            "economic": 5
        },
        "currency": {
            "silver": 1500,
            "gold": 10
        },
        "d1_skills": {
            "staves": {
                "rank": 3,
                "lxpl": 300
            },
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "dwarven smith": {
        "race": "dwarf",
        "cls": "citizen",
        "concept": "dwarven smith",
        "languages": {
            "common": {
                "rank": 5,
            },
            "dwarvish": {
                "rank": 5,
            }
        },
        "size": "small",
        "d1_stats": {
            "earth": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 4,
        "resources": {
            "social": 20,
            "military": 5,
            "economic": 15
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "hammers": {
                "rank": 1,
                "lxpl": 300
            },
            "armor smith": {
                "rank": 1,
                "lxpl": 300
            },
            "weapon smith": {
                "rank": 2,
                "lxpl": 300
            },
            "black smith": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "dwarven shield bearer": {
        "race": "dwarf",
        "cls": "supporter",
        "concept": "dwarven sheild bearer",
        "languages": {
            "common": {
                "rank": 5,
            },
            "dwarvish": {
                "rank": 5,
            }
        },
        "size": "small",
        "d1_stats": {
            "earth": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 4,
        "resources": {
            "social": 10,
            "military": 5,
            "economic": 25
        },
        "currency": {
            "silver": 1500,
            "gold": 20
        },
        "d1_skills": {
            "battle shields": {
                "rank": 3,
                "lxpl": 600
            },
            "defense up": {
                "rank": 1,
                "lxpl": 500
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "dwarven berserker": {
        "race": "dwarf",
        "cls": "adventurer",
        "concept": "dwarven berserker",
        "languages": {
            "common": {
                "rank": 5,
            },
            "dwarvish": {
                "rank": 5,
            }
        },
        "size": "small",
        "d1_stats": {
            "earth": {
                "rank": 2,
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 4,
        "resources": {
            "social": 10,
            "military": 20,
            "economic": 10
        },
        "currency": {
            "silver": 500,
            "gold": 20
        },
        "d1_skills": {
            "axes": {
                "rank": 1,
                "lxpl": 300
            },
            "hammers": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "pixie gatherer": {
        "race": "pixie",
        "cls": "citizen",
        "concept": "pixie gatherer",
        "languages": {
            "common": {
                "rank": 5,
            },
            "sylvan": {
                "rank": 5,
            }
        },
        "size": "tiny",
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
                "rank": 2,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 9,
        "resources": {
            "social": 20,
            "military": 5,
            "economic": 10
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "survival": {
                "rank": 1,
                "lxpl": 300
            },
            "scanvenger": {
                "rank": 1,
                "lxpl": 300
            },
            "foraging": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "flight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "pixie trickster": {
        "race": "pixie",
        "cls": "supporter",
        "concept": "pixie trickster",
        "languages": {
            "common": {
                "rank": 5,
            },
            "sylvan": {
                "rank": 5,
            }
        },
        "size": "tiny",
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
                "rank": 2,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 9,
        "resources": {
            "social": 10,
            "military": 5,
            "economic": 20
        },
        "currency": {
            "silver": 1200,
            "gold": 23
        },
        "d1_skills": {
            "knives": {
                "rank": 1,
                "lxpl": 300
            },
            "stealth": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "flight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "pixie dagger dancer": {
        "race": "pixie",
        "cls": "adventurer",
        "concept": "pixie dagger dancer",
        "languages": {
            "common": {
                "rank": 5,
            },
            "sylvan": {
                "rank": 5,
            }
        },
        "size": "tiny",
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
                "rank": 2,
                "lxpl": 500
            },
            "void": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 9,
        "resources": {
            "social": 10,
            "military": 20,
            "economic": 5
        },
        "currency": {
            "silver": 1200,
            "gold": 13
        },
        "d1_skills": {
            "knives": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "flight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "half-elf beastmaster": {
        "race": "elf",
        "cls": "citizen",
        "concept": "half-elf beastmaster",
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 20,
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
            "animal husbandry": {
                "rank": 2,
                "lxpl": 300
            },
            "command": {
                "rank": 1,
                "lxpl": 300
            },
            "scavenger": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "half-elf scout": {
        "race": "elf",
        "cls": "supporter",
        "concept": "half-elf scout",
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 5,
            "economic": 20
        },
        "currency": {
            "silver": 1200,
            "gold": 23
        },
        "d1_skills": {
            "bows": {
                "rank": 1,
                "lxpl": 300
            },
            "survival": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "half-elf archer": {
        "race": "elf",
        "cls": "adventurer",
        "concept": "half-elf archer",
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
                "rank": 1,
                "lxpl": 300
            }
        },
        "speed": 6,
        "resources": {
            "social": 10,
            "military": 20,
            "economic": 5
        },
        "currency": {
            "silver": 300,
            "gold": 13
        },
        "d1_skills": {
            "bows": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "elven swordsman": {
        "race": "elf",
        "cls": "adventurer",
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
                "lxpl": 500,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "elven priest": {
        "race": "elf",
        "cls": "supporter",
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
            "silver": 1500,
            "gold": 20
        },
        "d1_skills": {
            "rods": {
                "rank": 1,
                "lxpl": 300
            },
            "healing energy": {
                "rank": 3,
                "lxpl": 500
            },
        },
        "d1_abilities": {
            "night sight": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "elven enchanter": {
        "race": "elf",
        "cls": "citizen",
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
                "lxpl": 500,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "human warrior": {
        "race": "human",
        "cls": "adventurer",
        "concept": "human warrior",
        "languages": {
            "common": {
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
                "rank": 1,
                "lxpl": 500
            }
        },
        "speed": 5,
        "resources": {
            "social": 20,
            "military": 30,
            "economic": 15
        },
        "currency": {
            "silver": 1200,
            "gold": 13
        },
        "d1_skills": {
            "swords": {
                "rank": 1,
                "lxpl": 300
            },
            "spears": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "adaptive": {
                "rank": 4,
                "hl": True
            },
            "battle sense": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "human paladin": {
        "race": "human",
        "cls": "supporter",
        "concept": "human paladin",
        "languages": {
            "common": {
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
                "rank": 1,
                "lxpl": 500
            }
        },
        "speed": 5,
        "resources": {
            "social": 20,
            "military": 15,
            "economic": 30
        },
        "currency": {
            "silver": 1200,
            "gold": 23
        },
        "d1_skills": {
            "swords": {
                "rank": 1,
                "lxpl": 300
            },
            "gleaming weapon": {
                "rank": 1,
                "lxpl": 500
            }
        },
        "d1_abilities": {
            "adaptive": {
                "rank": 4,
                "hl": True
            },
            "waymarks": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            },
            "waymark recall": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    },
    "human guild associate": {
        "race": "human",
        "cls": "citizen",
        "concept": "human guild associate",
        "languages": {
            "common": {
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
                "rank": 1,
                "lxpl": 500
            }
        },
        "speed": 5,
        "resources": {
            "social": 30,
            "military": 15,
            "economic": 20
        },
        "currency": {
            "silver": 500,
            "gold": 10
        },
        "d1_skills": {
            "leadership": {
                "rank": 1,
                "lxpl": 300
            },
            "appraisal": {
                "rank": 1,
                "lxpl": 300
            },
            "research": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_abilities": {
            "adaptive": {
                "rank": 4,
                "hl": True
            },
            "blissful ignorance": {
                "rank": 1,
                "lxpl": 500,
                "hl": True
            }
        }
    }
}