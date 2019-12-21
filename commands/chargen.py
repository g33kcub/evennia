from commands import command
from world.kumarpg.dungeon1.dungeon1stats import dungeon1_stats
from world.kumarpg.dungeon1.dungeon1demographics import dungeon1_demographics
from world.kumarpg.universal.generalstats import universal_stats
from world.kumarpg.universal.generaldemographics import universal_demographics

_DUNGEON = "dungeon1"


class CmdChargen(command):
    """
    This is the command used to initiate the character generation
    system. Once @chargen is triggered, it will remember your progress
    so you can come back  to it later and finish if you need!

    Usage: @chargen

    If you accept using this command, it will transport you to the OOC Chargen
    room, and add you to the chargen channel.
    """

    def func(self):
        """ Actually runs the command """
        if not self.caller.db.cgen:
            # First we need to reset all of the chargen stats on the character.
            universal_stats(self.caller)
            universal_demographics(self.caller)
            self.caller.db.languages["common"]["rank"] = 5

            if _DUNGEON == "dungeon1":
                # These are the stats used only in Dungeon 1.
                dungeon1_stats(self.caller)
                dungeon1_demographics(self.caller)

            self.caller.db.cgen=True
