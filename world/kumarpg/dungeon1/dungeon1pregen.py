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
        "desc": "A beginning whiz on the frontier market of selling their wares. You are "
                "equally at home selling new and used items to any adventurer that is interested.",
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
            }
        },
        "d1_weapons": {
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
        "desc": "Walking the fine line between ferality and civility, you are in touch with nature's power to harm "
                "and heal.",
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
            "earth magic": {
                "rank": 1,
                "lxpl": 500,
                "tech": {
                    "geobolt": {
                        "lxpl": 100
                    }
                }
            },
            "healing magic": {
                "rank": 1,
                "lxpl": 500,
                "tech": {
                    "liminal energy": {
                            "lxpl": 100
                    }
                }
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
        "desc": "There is power, then there is you. As quick witted and agile as the whip you use, you dominate the "
                "battle field with feline grace.",
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
        "d1_weapons": {
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
        "desc": "The dungeon does not map itself. You have taken upon the skills to craft maps to help save as many "
                "lives as you can. You have knowledge that few possess, yet all need.",
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
            "scribe": {
                "rank": 3,
                "lxpl": 300
            },
            "survival": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_weapons": {
            "staves": {
                "rank": 1,
                "lxpl": 300
            },
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
        "desc": "You find a safe place within the shadows. You have learned to use their dark power as your own to "
                "imbue your weapons with the stuff of darkness itself.",
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
            "shadow magic": {
                "rank": 1,
                "lxpl": 500,
                "tech": {
                    "shadow weapon": {
                        "lxpl": 100
                    }
                }
            }
        },
        "d1_weapons": {
            "knives": {
                "rank": 1,
                "lxpl": 300
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
    "inojin alpha": {
        "race": "inojin",
        "cls": "adventurer",
        "concept": "inojin alpha",
        "desc": "The leader of the pack. You are the top dog and you let no one forget it. With your trusty staff at "
                "your side no one can stop you.",
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
        "d1_weapons": {
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
        "key": "Dwarven Smith",
        "race": "dwarf",
        "cls": "citizen",
        "concept": "a dwarven smith",
        "desc": "A master-in-training at the forge, you are the epitome of the Dwarven legends.",
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
        "d1_weapons": {
            "hammers": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_skills": {
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
        "key": "Dwarven Shield Bearer",
        "race": "dwarf",
        "cls": "supporter",
        "concept": "a dwarven sheild bearer",
        "desc": "You are all that stands between those you protect and those wishing to harm them. "
                "With your shield that is designed to harm as well as protect you are force to reckon with.",
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
        "d1_weapons": {
            "battle shields": {
                "rank": 3,
                "lxpl": 600
            },
            "status magic": {
                "rank": 1,
                "lxpl": 500,
                "tech": {
                    "defense up": {
                        "lxpl": 100
                    }
                }
            }
        },
        "d1_skills": {},
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
        "key": "Dwarven Berserker",
        "race": "dwarf",
        "cls": "adventurer",
        "concept": "a dwarven berserker",
        "desc": "Rage. Pure unadultered rage. On the battlefield you are a terrible sight to see.",
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
        "d1_weapons": {
            "axes": {
                "rank": 1,
                "lxpl": 300
            },
            "hammers": {
                "rank": 2,
                "lxpl": 300
            }
        },
        "d1_skills": {},
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
        "desc": "You flit and float from one side of the field to another, gathering any and everything of value. "
                "Nothing escapes your keen eye.",
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
        "d1_weapons": {},
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
        "desc": "You are never seen until it is too late. You play all kinds of tricks on those around you. Nothing "
                "is better than a good laugh with friends, at friends.",
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
            "survival": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_weapons": {
            "knives": {
                "rank": 1,
                "lxpl": 300
            },
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
        "desc": "You might be small, but with a dagger or any knife, you are a hurricane of death and destruction -- "
                "few survive to tell stories.",
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
        "d1_skills": {},
        "d1_weapons": {
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
        "desc": "You have spent your life learning how to raise, train and breed the perfect companion beast.",
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
        "d1_weapons": {
            "swords": {
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
        "desc": "Keen eyesight, trusty bow, and quick wits are all you need. You keep an eye on the trail ahead and "
                "what the enemy is doing before they get to close.",
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
            "survival": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_weapons": {
            "bows": {
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
        "desc": "You have embraced your Elven heritage more-so than your human side. You have taken up the bow with a "
                "furver of your Elven lineage.",
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
        "d1_skills": {},
        "d1_weapons": {
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
        "desc": "Hundreds of years of mastery is shown through your movements -- You may still be new, by Elven "
                "standards, but the truth of your skill is shown. You are force to be reckoned with, with any blade "
                "in your hand.",
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
        "d1_skills": {},
        "d1_weapons": {
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
        "desc": "Faith is a powerful weapon. You are one of the Holy Priests of the Elves. You are still a young "
                "Acolyte, but you've decided to use your skills and faith to protect those within the dungeon.",
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
            "healing magic": {
                "rank": 3,
                "lxpl": 500,
                "tech": {
                    "healing energy": {
                        "lxpl": 100
                    }
                }
            },
        },
        "d1_weapons": {
            "rods": {
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
    "elven enchanter": {
        "race": "elf",
        "cls": "citizen",
        "concept": "elven enchanter",
        "desc": "You have learned the fine art of imbuing the mundane with the arcane. Your skills are still being "
                "honed, but your promise is high.",
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
            "enchanter": {
                "rank": 3,
                "lxpl": 600
            },
            "haggling": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_weapons": {
            "swords": {
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
        "desc": "You have taken up sword and spear to head into the dungeon and fight to the end of the dungeon. You "
                "are a master in training with a weapon and fight tactics.",
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
            "spears": {
                "rank": 1,
                "lxpl": 300
            }
        },
        "d1_weapons": {
            "swords": {
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
        "desc": "You have taken both martial prowess and faith as your weapons.",
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
            "holy magic": {
                "rank": 1,
                "lxpl": 500,
                "tech": {
                    "gleaming weapon": {
                        "lxpl": 100
                    }
                }
            }
        },
        "d1_weapons": {
            "swords": {
                "rank": 1,
                "lxpl": 300
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
        "desc": "You aren't an adventurer, you're their help desk. You help them figure out how to and when to. You "
                "make it your point to study the dungeon, from a purely academic standpoint, of course.",
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
