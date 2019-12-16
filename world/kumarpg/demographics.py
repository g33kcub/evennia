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

