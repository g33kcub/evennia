from evennia import DefaultCharacter
"""
This file contains all the demographic items for a character.
"""

def character_demographics(character):
    """
    A function to call all fo the default demographics for a character.
    """
    character.db.race = "Human"
    character.db.rpgclass = "Citizen"
    character.db.gender = "Neutral"
    character.db.dob = ""
    character.db.concept = ""
    character.db.familia = ""
    character.db.nickname = ""
    character.db.health_status = "alive"
    character.db.currency = {"silver": 0, "gold": 0}
    character.db.resources = {"social": 0, "military": 0, "economic": 0}
    """
    Appearance Foo!
    """
    character.db.haircolor = ""
    character.db.eyecolor = ""
    character.db.skintone = ""
    character.db.height = ""
    character.db.build = ""
    """
    System Shit!
    """
    character.db.approved = False
    character.db.pvpok = False
    character.db.ooc_currency = 0
    """
    Cosmetic Crap!
    """
    character.db.playedby = ""
    character.db.title = ""
    character.db.position = ""
    """
    Hidden Stats (Never Shown to Anyone)
    """
    character.locks.add("examine:perm(Developer);tell:all();delete:perm(Developer);edit:perm(Developer)")
    character.db.rpglevel = 1
    """
    Combat System Stuff
    """
    character.db.pool_mana = {"max": 0, "cur": 0}
    character.db.pool_health = {"max": 0, "cur": 0}
    character.db.pool_fatigue = {"max": 0, "cur": 0}
    character.db.pool_ego = {"max": 0, "cur": 0}
    character.db.pool_action = {"max": 0, "cur": 0}
    """
    Equipment Stuff
    """
    character.db.equipped_gear = {
        "head": None,
        "neck": None,
        "back": None,
        "shoulders": None,
        "chest": None,
        "arms": None,
        "hands": None,
        "waist": None,
        "legs": None,
        "feet": None,
        "main hand": None,
        "off hand": None,
        "accessory 1": None,
        "accessory 2": None,
        "accessory 3": None,
        "accessory 4": None
    }
    """
    Conditions and stuff
    """
    character.db.conditions = {}



