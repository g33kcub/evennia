from evennia import Command, CmdSet

class CmdBoardZoid(Command):
    """
    Boarding the Zoid.
    
    Usage:
      board <zoid name>

    This will be available to the select pilot as long as they are in the same location.
    """
    key = "board"
    locks = "cmd:all()"

    def func(self):
        self.caller.msg("You enter the cockpit of " + self.name + ".")
        self.caller.move_to(self.name)

class CmdDisembarkZoid(Command):
    """
    Leaving the Zoid.

    Usage:
      disembark

    This will be available only to the pilot in the zoid.
    """
    key = "disembark"
    locks = "cmd:all()"

    def func(self):
        zoid = self.obj
        parent = zoid.location
        self.caller.move_to(parent)

class CmdSetZoid(CmdSet):
    self.add(CmdDisembarkZoid())
    self.add(CmdBoardZoid())
    