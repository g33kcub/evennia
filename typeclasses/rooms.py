"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
import time
from world.utilities import columns, make_header, wrap, display_time
from evennia.contrib.rpsystem import ContribRPRoom

class Room(ContribRPRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """ 

    def at_object_creation(self):
        """
        Settings to be applied when a new room is dug.
        """

        self.db.ic = False
        self.db.type = "outside"

    def detail_string(self, target, looker):
        "Shows the details of the individual room description rows"

        if target.has_account:
            
            length = len(target.get_display_name(looker))

            # denote if a super user or not.
            if target.name:
                name = "|540*|n " + target.get_display_name(looker)
                output = name[:22] + "..." if length > 30 else  name.ljust(30)  
            else:
                name = "  " + target.get_display_name(looker)
                output = name[:20] + "..." if length > 24 else name.ljust(24)
                      
            short_desc = target.db.short_desc
            if short_desc: 
                output += (short_desc[:40] + "...") if len(short_desc) > 43  else short_desc.ljust(43) 
            else: 
                output += "use |wshortdesc <desc>|n to set this message.".ljust(47)
            
            session = target.account.sessions.get()[0]
            idle = self.display_time(time.time() - session.cmd_last_visible)

            output +=  " " * (10 - len(idle)) + "%s\n" % idle
            return output
        
        # Exits
        elif target.destination:
            alias = "%s" % target.aliases
            alias = alias.split(",")
            try:
                alias = alias.sort(key=len)[0]
            except TypeError:
                alias = alias[0]
            alias = "[%s]" % alias
            return alias.upper() + " " * (6 - len(alias)) + target.get_display_name(looker) + "\n" 

    @property
    def is_indoors(self):
        "Check to see if this is an interior room or not"
        return True if self.db.indoors else False


    def character_details(
            self, 
            character, 
            looker
        ):
        """
        Depending on what kind of character and room, display a different
        informational string about them in the general room output.
        """

        # Player, IC
        if character.location.db.ic:
            character.get_display_name(looker, pose=True, IC=True)



class Inside(Room):
    """
    This room represents any room that is going to be used
    as an indoor location.  It has the basic settings for
    all interior rooms. (buildings, dungeons, etc.)
    """

    def at_object_creation(self):
        self.db.indoors = True
        return super().at_object_creation()
        
    
class Outside(Room):
    """
    This room represents any exterior room.  A perfect plce to
    define weather code, etc for atmospherics.
    """

    def at_object_creation(self):
        self.db.indoors = False
        return super().at_object_creation()