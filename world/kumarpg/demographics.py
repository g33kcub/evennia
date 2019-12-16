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

    _MAX = Maximum Value for the Pool
    _CUR = Current Value for the pool.

    HP = Health/Hit Points
    FP = Fatigue Points
    MP = Mana/Magic Points
    EP = Ego Points
    AP = Action Points (Not on Sheet.)
    """
    character.db.ap_max = 0
    character.db.ap_cur = 0
    character.db.ep_max = 0
    character.db.ep_cur = 0
    character.db.hp_max = 0
    character.db.hp_cur = 0
    character.db.fp_max = 0
    character.db.fp_cur = 0
    character.db.mp_max = 0
    character.db.mp_cur = 0
    """
    Equipment Stuff
    """
    character.db.slot_head = None
    character.db.slot_neck = None
    character.db.slot_shoulders = None
    character.db.slot_chest = None
    character.db.slot_arms = None
    character.db.slot_hands = None
    character.db.slot_back = None
    character.db.slot_waist = None
    character.db.slot_legs = None
    character.db.slot_feet = None
    character.db.slot_weapon = None
    character.db.slot_accessory_1 = None
    character.db.slot_accessory_2 = None
    character.db.slot_accessory_3 = None
    character.db.slot_accessory_4 = None
    """
    Conditions and stuff
    """
    character.db.conditions = {}



