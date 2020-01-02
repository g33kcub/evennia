"""
This is the demographics file for Dungeon 1.
Races:
Human, Elf, Pixie, Dwarf, Inojin, Nekojin, Half-Elf
"""


def dungeon1_demographics(character):
    character.db.d1_rpgclass = "Citizen"
    character.db.d1_titles = {}
    character.db.d1_rpglevel = 1

    """
    Combat System Stuff
    """
    character.db.d1_pool_mana = {"max": 0, "cur": 0}
    character.db.d1_pool_health = {"max": 0, "cur": 0}
    character.db.d1_pool_fatigue = {"max": 0, "cur": 0}
    character.db.d1_pool_ego = {"max": 0, "cur": 0}
    character.db.d1_conditions = {}
    """
    Other stuff
    """
    character.db.d1_milestones = {}

