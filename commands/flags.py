import evennia
from evennia import default_cmds
from world.kumarpg.dicts import flags
from world.utilities.format import columns, header
class Flags(default_cmds.MuxCommand):
    """
    Manage flags on in-game objects.  As well as offering aditional
    information about the @flags system.

    Usage:
        @flags[/switch] [<target>]  -   get a list of flags set on the object, 
            or globally if no object is specified.

        @flags <target> =  [!]<flag> [<flag>]   -   perform an action on an 
            object's flags.
    
    Switches:
        /list   - List all of the flags currently available in the system.
        /info   - Get info about a flag. 
    """
    key = "@flags"
    aliases = ['flags', "flgs"]
    help_category = "admin"
    locks = "cmd:perm(builder)"

    def func(self):
        
        # Just making a shortcut.
        caller = self.caller
        target = caller.search(self.lhs)
        
        # No args, no switches. Send the index of flags.

        if not self.args:
            output =  header("|w @flags list |n", offset=5, fill="|113=|n")
            caller.msg(output)

        
