from commands.command import Command
from evennia import CmdSet
from evennia.utils.evmenu import EvMenu
from world.kumarpg.chargen import chargen_general
from world.kumarpg.dungeon1.dungeon1stats import dungeon1_stats
from world.kumarpg.dungeon1.dungeon1demographics import dungeon1_demographics
from world.kumarpg.universal.generalstats import universal_stats
from world.kumarpg.universal.generaldemographics import universal_demographics
from world.utilities.format import header

_DUNGEON = "dungeon1"


class CmdChargen(Command):
    """
    This is the command used to initiate the character generation
    system. Once @chargen is triggered, it will remember your progress
    so you can come back  to it later and finish if you need!

    Usage: @chargen

    If you accept using this command, it will transport you to the OOC Chargen
    room, and add you to the chargen channel.
    """

    key = "chargen"
    aliases = ["cgen", "cg"]
    help_category = "general"

    def func(self):
        """ Actually runs the command """
        # First we need to reset all of the chargen stats on the character.
        universal_stats(self.caller)
        universal_demographics(self.caller)
        self.caller.db.languages["common"]["rank"] = 5

        if _DUNGEON == "dungeon1":
            # These are the stats used only in Dungeon 1.
            dungeon1_stats(self.caller)
            dungeon1_demographics(self.caller)

        CgMenu(self.caller, chargen_general, "node_start")


class CgMenu(EvMenu):
    def node_formatter(self, nodetext, optionstext):
        output = nodetext + "\n\n"
        if optionstext:
            output += header("|w Options |n", fill="|113-|n") + "\n"
            output += optionstext + "\n\n"
        output += header(" Type '|wQUIT|n' to quit. ", just="right", fill="|113=|n")
        return output


class CmdsetChargen(CmdSet):

    def at_cmdset_creation(self):
        self.add(CmdChargen())
