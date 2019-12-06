from evennia import DefaultObject
from commands.zoidcmds.zoidcmd import CmdSetZoid

class Zoid(DefaultObject):
    """
    This is the default type class for a generic zoid.
    """
    def at_object_creation(self):
        """
        This is called only when object is first created.
        """
        self.cmdset.add_default(CmdSetZoid)
