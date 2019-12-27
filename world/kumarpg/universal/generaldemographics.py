from evennia import DefaultCharacter
"""
This file contains all the demographic items for a character.
"""

def universal_demographics(character):
    """
    A function to call all fo the default demographics for a character.
    """
    character.db.race = "human"
    character.db.gender = "neutral"
    character.db.dob = ""
    character.db.concept = ""
    character.db.familia = ""
    character.db.nickname = ""
    character.db.health_status = "alive"
    character.db.currency = {"silver": 0, "gold": 0}
    character.db.resources = {"social": 0, "military": 0, "economic": 0}
    character.db.dungeon = "d1"
    character.db.dungeonlist = ['d1']
    character.db.size = "medium"
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
    character.db.ooc_currency = 0
    character.db.speed = 5
    """
    Cosmetic Crap!
    """
    character.db.playedby = ""
    character.db.position = ""
    """
    Hidden Stats (Never Shown to Anyone)
    """
    character.db.pool_action = {"max": 0, "cur": 0}
    character.locks.add("examine:perm(Developer);tell:all();delete:perm(Developer);edit:perm(Developer)")
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
    character.db.univeral_milestones = {}
    