from evennia import default_cmds
from world.kumarpg.dicts.flags import flags
from world.utilities.format import columns, header

class Flags(default_cmds.MuxCommand):
    """
    Manage flags on in-game objects.  As well as offering aditional
    information about the flags system.

    Usage:
        flags[/switch] [<target>]  -   get a list of flags set on the object, 
            or globally if no object is specified.

        flags <target> = [!]<flag> [<flag>] - perform an action on an object's 
            flags. The system can process multiple flag additions andremovals 
            at once.
    
    Switches:
        /info   - Get info about a flag. 
    """
    key = "flags"
    aliases = ["flgs"]
    help_category = "general"
    locks = "cmd:perm(newbie)"


    def _alias_to_flag(self, alias):
        for f in flags:
            if alias in flags[f]["aliases"]: return f
            elif alias[1:] in flags[f]["aliases"]: return "!%s" % f
        return alias

    def func(self):
        # Just making a shortcut.
        caller = self.caller

        # No args, no switches. Send the index of flags the player can set.
        if not self.args and not self.switches:
            filter_flags = [f for f in flags if caller.locks.check_lockstring(caller, "dummy:{}".format(flags[f]["set"]))]
            frmt_flags = map(lambda x: f"{x.upper()}({flags[x]['code']})", filter_flags)
            output =  header("|w flags Database |n", fill="|113=|n")
            output += columns("|".join(frmt_flags), cols=2, offset=2, sep="|") + "\n"
            output += "|113=|n" * 78 + "\n"
            output += "|540*|n Use |wflags/info <flag>|n for more information."
            caller.msg(output.strip())
        
        # If there's no switches, no equal sign and a target
        elif self.args and not self.rhs and not self.switches:
            tar = caller.search(self.args)
            
            # Make sure the setter has control over the object.
            if tar and tar.access(caller, "control"):
                filter_flags = [f for f in tar.db.flags if caller.locks.check_lockstring(caller, "dummy:{}".format(flags[f]["set"]))]
                frmt_flags = map(lambda x: f"{x.upper()}({flags[x]['code']})", filter_flags)
                output =  header("|w Flags for {} |n".format(tar.name), fill="|113=|n")
                output += columns("|".join(frmt_flags), cols=2, offset=2, sep="|") + "\n"
                output += "|113=|n" * 78 + "\n"
                output += "|540*|n Use |wflags/info <flag>|n for more information."
                caller.msg(output.strip())
            else: caller.msg("Permission denied.")
        
        # There was a left and right hand side given.
        elif self.lhs and self.rhs:
            tar = caller.search(self.lhs)

            # if it's a valid target
            if tar and tar.flags:
                flgs = self.rhs.split()
                for f in flgs:
                    f_name = self._alias_to_flag(f)
                    
                    # Set the lock strings
                    try:
                        f_lock = flags[f_name]["set"]
                        f_unlock = flags[f_name]["unset"]
                    except KeyError:
                        f_lock = flags[f_name[1:]]["set"]
                        f_unlock = flags[f_name[1:]]["unset"]
                    else:
                        f_lock = "perm(builder)"
                        f_unlock = "perm(builder)"

                    # Make sure the character has access to the flag and modify the object
                    if tar.access(caller, "control"):
                        if f_name in flags:    
                            if caller.locks.check_lockstring(caller, "dummy:{}".format(f_lock)):
                                tar.flags.add(f_name)
                                caller.msg("Done. Flag '{}' added to {}".format(f_name.upper(), tar.name))
                            else: caller.msg("Permission denied.")

                        # Remove a flag
                        elif f_name[0] == "!" and f_name[1:] in flags:
                            if caller.locks.check_lockstring(caller, "dummy:{}".format(f_unlock)):
                                tar.flags.remove(f_name[1:])
                                caller.msg("Done. Flag '{}' removed from {}.".format(f_name[1:].upper(), tar.name))
                            else: caller.msg("Permission denied")
                    
                    else: caller.msg("Permission deined.")               
        
        # info Switch given
        elif self.switches and "info" in self.switches:
            if not self.args: caller.msg("Which flag did you want more info on?")
            
            # There was also an arg in self.args
            else:

                # If the flag (or alias) matches continue.
                if  self._alias_to_flag(self.args.lower()) in flags:
                    flgs = flags[self._alias_to_flag(self.args.lower())]
                    lock = flgs["set"] or "perm(player)"
                    
                    # Only show locks that they have access.
                    if caller.locks.check_lockstring(caller, "dummy:{}".format(lock)):
                        output = header(f" |wFlag:|n {self._alias_to_flag(self.args).upper()} ", fill="|113=|n")
                        
                        output += "  |wAliases:|n " + ",".join(flgs["aliases"]) + "\n" if flgs["aliases"] else "  Aliases: \n"
                        output += "  |wCode:|n " + flgs["code"] + "\n" or "\n"
                        output += "  |wSet:|n " + flgs["set"] + "\n"  or "\n"
                        output += "  |wUnset:|n " + flgs["unset"] + "\n"
                        output += "  |wDescription:|n " + flgs["desc"] + "\n"
                        output += "|113=|n" * 78
                        caller.msg(output)

                    else: caller.msg("Permission denied.")
                else: caller.msg("I can't find that flag.  Type '|wflags|n' for a list of flags.")

        # Unknown switch
        else: caller.msg("I don't recongize that request.")


class FlagHandler(object):
    """
    Handle the flag actions on an object.
    """
    def __init__(self, obj):
        "Setup internal state"
        self.obj = obj
        self.obj.db.flags = self.obj.db.flags or []

    def flag_codes(self):
        "Get a string of flag codes currently set on an object."    
        return "".join(map(lambda flg: flags[flg]["code"], self.obj.db.flags))

    def add(self, flag):
        if flag in flags:
            try:
                self.obj.db.flags.index(flag.lower())
            except ValueError:
                self.obj.db.flags.append(flag.lower())

    def remove(self, flag):
        try:
            self.obj.db.flags.index(flag.lower())
            self.obj.db.flags.remove(flag.lower())
        except ValueError:
            pass
    
    def clear(self):
        self.obj.db.flags.clear()

    def list(self):
        return self.obj.db.flags
    
