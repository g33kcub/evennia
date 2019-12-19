from evennia import default_cmds
from world.kumarpg.dicts.flags import flags
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
    key = "flags"
    aliases = ["flgs"]
    help_category = "admin"
    locks = "cmd:perm(builder)"

    def func(self):

        def _format_flag(name, data):
            "Helper function to format flag strings"
            alias = data["aliases"] if data["aliases"] else []
            try:
                alias = alias.sort(key=len)[0]
            except TypeError:
                try:
                    alias = alias[0]
                except IndexError:
                    alias = ""
            return name + "(%s)" % alias
        
        # Just making a shortcut.
        caller = self.caller
        
        # No args, no switches. Send the index of flags.
        if not self.args and not self.switches:
            frmt_flags = map(lambda x: _format_flag(x, flags[x]), flags)
            output =  header("|w flags Database (alias) |n", fill="|113=|n")
            output += columns("|".join(frmt_flags), cols=3, offset=2, sep="|") + "\n"
            output += "|113=|n" * 78 + "\n"
            output += "|540*|n Use |wflags/info <flag>|n for more information."
            caller.msg(output.strip())
        
        # info Switch given
        elif self.switches and "info" in self.switches:
            if not self.args: caller.msg("Which flag did you want more info on?")
            
            # There was also an arg in self.args
            else:

                if self.args.lower() in flags:
                    flgs = flags[self.args.lower()]
                    lock = flgs["set"] or "newbie"
                    
                    # Only show locks that they have access.
                    if caller.locks.check_lockstring(caller, f"perm({lock})"):
                        output = header(f" Flag: |w{self.args.lower()}|n ", fill="|113=|n")
                        
                        # This one's a bit tricky.  Basically I'm telling it to take
                        # every item in the list, and highlight it.  But, if there are
                        # no items, just return an empty string.
                        output += "  Aliases: " + ",".join(map(lambda x: "|w%s|n" % x, flgs["aliases"])) + "\n" if flgs["aliases"] else "  Aliases: \n"
                        output += "  Code: |w" + flgs["code"] + "|n\n" or "  Code:\n"
                        output += "  Set: |w" + flgs["set"] + "|n\n"    or "Set:\n"
                        output += "  Unset: |w" + flgs["unset"] + "|n\n"
                        output += "  Description: |w" + flgs["desc"] + "|n\n"
                        output += "|113=|n" * 78
                        caller.msg(output)
                    else: caller.msg("Permission denied.")
                else: caller.msg("I can't find that flag.  Type |wflags|n for a list of flags.")

class FlagHandler(object):
    """
    """
    def flag_codes(self):
        "Get a string of flag codes currently set on an object."    
        return "".join(map(lambda flg: flag_types[flg]["code"], self.db.flags))

    def add(self, flag):
        if not self.db.flags.index(flag.lower()) and flag in flag_types: 
            self.db.append(flag.lower())

    def remove(self, flag): 
        if self.db.flags.index(flag.lower()): self.db.flags.remove(flag.lower())
    
    def clear(self):
        self.db.flags.clear()

    def list(self):
        return self.db.flags
    
