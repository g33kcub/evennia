"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.utils.ansi import strip_ansi
from collections import defaultdict
from commands.flags import FlagHandler
import time
from world.utilities.format import columns, wrap, header, display_time, trail

# Define the different types of rooms here, with the exit category
# they should fall under.
_ROOM_TYPES = {
    "generic":  "Exts",
    "outside":  "Roads and Paths",
    "inside":   "Near By",
    "building": "Buildings & Residences"
}

class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """ 

    @property
    def flags(self):
        return FlagHandler(self)

    def at_object_creation(self):
        self.db.ic = False
        self.db.type = "generic"
        self.db.is_dark = False
        self.db.is_blind = False
        """
        Install the flag system handler.
        """
        self.flags = FlagHandler()
    

    def detail_string(self, target, looker):
        "Shows the details of the individual room description rows"

        if target.has_account:

            # denote if the user gets a marker or not.
            if target.locks.check_lockstring(target, "dummy:perm(builder)"): marker = "|540*|n "
            elif target.locks.check_lockstring(target, "dummy:perm(helper)"): marker = "|113!|n "
            else: marker = "  "    

            # piece together the name
            name = marker + trail(target.get_display_name(looker), length=15)   

            # short_desc
            default_desc = trail("use |wshortdesc <desc>|n to set this. Message.", length=45)  
            short_desc = trail(target.db.short_desc, length=45) if target.db.short_desc else default_desc

            # idle time.  Just show the looker 0s as time shows time since last command.
            session = target.account.sessions.get()[0]
            if target == looker:
                idle = display_time(0)    
            else:
                idle = display_time(time.time() - session.cmd_last_visible)
            
            output = name + short_desc + trail(idle,length=15, dir="right")
            return output + "\n"

        elif target.destination:

            alias = "%s" % target.aliases
            alias = alias.split(",")
            try:
                alias = alias.sort(key=len)[0]
            except TypeError:
                alias = alias[0]
            alias = "[%s]" % alias
            exit_name = target.get_display_name(looker)

            return alias.upper() + " " * (6 - len(alias)) +  exit_name

    def return_appearance(self, looker):
        """
        The return from this method is what the looker sees when
        looking at this object.
        """
        visible = (con for con in self.contents if con.access(looker, "view"))
        exits, users, things = defaultdict(list), [], defaultdict(list) 

        # Seperate out the visible room contents into different catagories
        for con in visible:
            if con.destination: exits[con.destination.db.type].append(con)
            elif con.has_account: users.append(con)
            else: things[con.key].append(con)
        
        # handle room Area
        string = "|540In Character - |w" if self.db.ic else "|540Out of Character - |w" 
        string +=  self.get_display_name(looker) + "|n\n"
        string += ("|113=|n" * 78 ) + "\n"

        # Description
        string += "You See Nothing Special\n\n" if not self.db.desc else wrap(self.db.desc) + "\n"
        # Secondary Description
        if self.db.sec_desc: string += "\n" + wrap("%s" % self.db.sec_desc) + "\n"

        # If the room is set to blind, test to see if the looker can see contents or not.
        if not self.db.is_blind or self.locks.check_lockstring(looker, "dummy:perm(builder)"):
            
            # Add an extra space if there's a secondary description
            string += "\n" if self.db.sec_desc else ""
            
            # Character section    
            string += header("|w Characters ")
            for user in users: string += self.detail_string(user, looker)

            # Exits
            for exit in exits:        
                ex = "|".join(map(lambda x: self.detail_string(x, looker), exits[exit]))
                string += header("|w %s " % _ROOM_TYPES[exit])
                string += columns(ex, sep="|") + "\n"
        
        # Ending line
        string += ("|113=|n" * 78 ) 
        return string



class Inside(Room):
    """
    This room represents any room that is going to be used
    as an indoor location.  It has the basic settings for
    all interior rooms. (buildings, dungeons, etc.)
    """

    def at_object_creation(self):
        self.db.type = "inside"
        return super().at_object_creation()
        

class Building(Room):
    def at_object_creation(self):
        self.db.type = "building"
        return super().at_object_creation()


class Outside(Room):
    """
    This room represents any exterior room.  A perfect plce to
    define weather code, etc for atmospherics.
    """

    def at_object_creation(self):
        self.db.type = "outside"
        return super().at_object_creation()