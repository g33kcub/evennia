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
    def at_object_creation(self):
        stat_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0 }
        skill_dict = { "rank" : 0, "lxp" : 0, "mp" : 0, "lxpl" : 0, "cor" : 0, "hl": False }
        self.db.stats = {
            "earth": stat_dict,
            "fire": stat_dict,
            "air": stat_dict,
            "water": stat_dict,
            "void": stat_dict
        }

        self.db.skills = {
            "swords": skill_dict,
            "knives": skill_dict,
            "hammers" : skill_dict,
            "whips": skill_dict,
            "spears": skill_dict,
            "staves": skill_dict,
            "axes": skill_dict,
            "bows": skill_dict,
            "fans": skill_dict,
            "rods": skill_dict,
            "wands": skill_dict,
            "persuasion": skill_dict,
            "haggling": skill_dict,
            "intimidation": skill_dict,
            "empathy": skill_dict,
            "subterfuge":skill_dict,
            "leadership": skill_dict,
            "command": skill_dict,
            "socialize": skill_dict,
            "etiquette": skill_dict
        }
