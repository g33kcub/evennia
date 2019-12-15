"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from typeclasses.npcs import NPC


class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    """
    Skill Types
    0 = General
    1 = Weapon
    2 = Social
    3 = Crafting
    4 = Tradesman

    Crafting Skill Types:
    0 = None
    1 = Smithing
    2 = Tailoring
    3 = Production
    4 = Scholary
    5 = Chef
    """
    def at_object_creation(self):
        stat_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0 }
        skill_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 0 }
        skill_dict_weapon = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 1 }
        skill_dict_social = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 2 }
        skill_dict_crafting = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 0 }
        skill_dict_crafting1 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 1 }
        skill_dict_crafting2 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 2 }
        skill_dict_crafting3 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 3 }
        skill_dict_crafting4 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 4 }
        skill_dict_crafting5 = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 3, "group": 5 }
        skill_dict_tradesman = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False, "type": 4 }
        self.db.stats = {
            "earth": stat_dict,
            "fire": stat_dict,
            "air": stat_dict,
            "water": stat_dict,
            "void": stat_dict
        }

        self.db.skills = {
            "swords": skill_dict_weapon,
            "knives": skill_dict_weapon,
            "hammers" : skill_dict_weapon,
            "whips": skill_dict,
            "spears": skill_dict_weapon,
            "staves": skill_dict_weapon,
            "axes": skill_dict_weapon,
            "bows": skill_dict_weapon,
            "fans": skill_dict_weapon,
            "rods": skill_dict_weapon,
            "wands": skill_dict_weapon,
            "persuasion": skill_dict_social,
            "haggling": skill_dict_social,
            "intimidation": skill_dict_social,
            "empathy": skill_dict_social,
            "subterfuge":skill_dict_social,
            "leadership": skill_dict_social,
            "command": skill_dict_social,
            "socialize": skill_dict_social,
            "etiquette": skill_dict_social,
            "armor smith":skill_dict_crafting1,
            "weapon smith":skill_dict_crafting1,
            "black smith":skill_dict_crafting1,
            "jeweler":skill_dict_crafting1,
            "carpenter":skill_dict_crafting1,
            "leather working":skill_dict_crafting2,
            "seamstress":skill_dict_crafting2,
            "miner":skill_dict_crafting3,
            "forager":skill_dict_crafting3,
            "farmer":skill_dict_crafting3,
            "fisher":skill_dict_crafting3,
            "scavenger":skill_dict_crafting3,
            "animal husbandry":skill_dict_crafting3,
            "enchanter":skill_dict_crafting4,
            "scribe":skill_dict_crafting4,
            "alchemy":skill_dict_crafting5,
            "culinarian":skill_dict_crafting5,
            "appraisal":skill_dict_tradesman,
            "research":skill_dict_tradesman
        }
