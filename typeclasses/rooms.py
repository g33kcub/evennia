"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
import time

class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """ 

    def wrap(self, string="", width=78):
        str_list = string.split()
        
        output = ""
        line = ""
        for w in str_list:
            if len(w + line) >= width:
                output += ("\n%s" % line).lstrip()
                line = "%s " % w
            else:
                line += "%s " % w
        output +=  " " + line
        return output

    def display_time(self, seconds):
        N = int(seconds)
        min = 60
        hour = 60 * 60
        day = 60 * 60 * 24
        output = ""
        HOUR = N // hour
        MINUTE = (N - (HOUR * hour)) // min
        SECONDS = N - ((HOUR * hour) + (MINUTE * min))
        
        if HOUR: 
            output += "%sh " % HOUR
        
        if MINUTE:
            output += "%sm " % MINUTE
        
        if seconds:
            output +=  "%ss" % SECONDS
        
        return output

    def at_object_creation(self):
        """
        Settings to be applied when a new room is dug.
        """

        self.db.ic = False
        self.db.type = "outside"
    
    def make_header(self, string):
        """
        Create a header for the different portions of the room parent.
        """
        length = 78 - (len(string) + 4)
        return "|113[|w " + string + " |113]|n" + "|113-|n" * length + "\n"


    def detail_string(self, target, looker):
        "Shows the details of the individual room description rows"

        if target.has_account:
            
            length = len(target.get_display_name(looker))

            # denote if a super user or not.
            if target.is_superuser:
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
        elif target.destination:
            alias = "%s" % target.aliases
            alias = alias.split(",")[0]
            alias = "[%s]" % alias
            return alias.upper() + " " * (6 - len(alias)) + target.get_display_name(looker) + "\n" 

    def return_appearance(self, looker):
        """
        The return from this method is what the looker sees when
        looking at this object.
        """
        visible = (con for con in self.contents if con.access(looker, "view"))
        exitsi, exitso, users, things = [], [], [], {}
        
        for con in visible:
            if con.destination:
                exitsi.append(con) if con.destination.is_indoors else exitso.append(con)
            elif con.has_account:
                users.append(con)
            else: 
                things[con].append(con)
        
        # handle room title
        string = "|540In Character - |w" if self.db.ic else "|540Out of Character - |w" 
        string +=  self.get_display_name(looker) + "|n\n"
        string += ("|113=|n" * 78 ) + "\n"


        # Description
        string += "You See Nothing Special\n" if not self.db.desc else self.wrap(self.db.desc) + "\n"
        # Secondary Description
        if self.db.sec_desc: string += self.wrap("\n%s\n" % self.db.sec_desc)

        #format the desc strings to 78 characters.

        # Character section    
        string += self.make_header("Characters")
        for user in users: string += self.detail_string(user, looker)

        # Exits
        if exitsi:
            string += self.make_header("Buildings & Residences") 
            for exit in exitsi: string += self.detail_string(exit, looker)
        
        if exitso:
            string += self.make_header("Streets & Pathways") 
            for exit in exitso: string += self.detail_string(exit, looker)
        # Ending line
        string += ("|113=|n" * 78 ) 
        return string

    @property
    def is_indoors(self):
        "Check to see if this is an interior room or not"
        return True if self.db.indoors else False


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