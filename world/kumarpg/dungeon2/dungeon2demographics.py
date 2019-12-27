from evennia import DefaultCharacter
"""
This is the demographics file for Dungeon 2.
Races:
Human, Jade Elf, Pixie, Dwarf, Kitsune, Ryuujin, Half-Elf
"""

def dungeon1_demographics(character):
    character.db.d2_rpgclass = "Citizen"
    character.db.d2_titles = {}
    character.db.d2_rpglevel = 1

    """
    Combat System Stuff
    """
    character.db.d2_pool_mana = {"max": 0, "cur": 0}
    character.db.d2_pool_health = {"max": 0, "cur": 0}
    character.db.d2_pool_fatigue = {"max": 0, "cur": 0}
    character.db.d2_pool_ego = {"max": 0, "cur": 0}
    character.db.d2_conditions = {}
    """
    Other stuff
    """
    character.db.d2_milestones = {}
