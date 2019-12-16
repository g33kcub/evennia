from evennia import DefaultCharacter
"""
This is the demographics file for Dungeon 1.
"""

def dungeon1_demographics(character):
    character.db.d1.rpgclass = "Citizen"
    character.db.d1.title = ""
    character.db.d1.rpglevel = 1
    """
    Combat System Stuff
    """
    character.db.d1.pool_mana = {"max": 0, "cur": 0}
    character.db.d1.pool_health = {"max": 0, "cur": 0}
    character.db.d1.pool_fatigue = {"max": 0, "cur": 0}
    character.db.d1.pool_ego = {"max": 0, "cur": 0}
    character.db.d1.conditions = {}

 