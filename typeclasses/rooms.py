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
    
    

    def display_time(self, seconds):
        N = int(seconds)
        min = 60
        hour = 60 * 60
        day = 60 * 60 * 24
        output = ""
        HOUR = N // hour
        MINUT = (N - (HOUR * hour)) // min
        SECONDS = N - ((HOUR * hour) + (MINUT * min))

        if HOUR:
            output += "%sh " % HOUR
        
        if MINUT:
            output += "%sm " % MINUT
        
        if seconds:
            output +=  "%ss" % SECONDS
        
        return output

    def at_object_creation(self):
        """
        Settings to be applied when a new room is dug.
        """
        self.tags.remove("OOC")
        self.db.ic = 0
    
    def make_header(self, string):
        """
        Create a header for the different portions of the room parent.
        """
        length = 78 - (len(string) + 4)
        return "|113[|w " + string + " |113]|n" + "|113-|n" * length + "\n"


    def detail_string(self, target, looker):
        "Shows the details of the individual room description rows"

        if target.has_account:
            
            # denote if a super user or not.
            if target.is_superuser:
                name =  "|540*|n " + target.get_display_name(looker)  
            else:
                name = target.get_display_name(looker)

            output = name[:22] + "..." if len(name) > 30 else name.ljust(30)
            
            short_desc = target.db.short_desc
            if short_desc: 
                output += (short_desc[:41] + "...") if len(short_desc) > 45  else short_desc.ljust(40) 
            else: 
                output += "use |w+shortdesc <desc>|n to set this message.".ljust(45)
            session = target.account.sessions.get()[0]
            output += "%s\n".rjust(10) % self.display_time(time.time() - session.cmd_last_visible)
            return output

    def return_appearance(self, looker):
        """
        The return from this method is what the looker sees when
        looking at this object.
        """
        visible = (con for con in self.contents if con.access(looker, "view"))
        exits, users, things = [], [], {}
        
        for con in visible:
            if con.destination:
                exits.append(con)
            elif con.has_account:
                users.append(con)
            else: 
                things[con].append(con)
        
        # handle room title
        string = "|540Out of Character - |w" if not self.db.ic else "|540Out of Character - |w" 
        string +=  self.get_display_name(looker) + "|n\n"
        string += ("|113=|n" * 78 ) + "\n"

        # Description
        string += "You See Nothing Special\n" if not self.db.desc else self.db.desc + "\n"
        
        # Character section    
        string += self.make_header("Characters")
        for user in users: string += self.detail_string(user, looker)

        string += ("|113=|n" * 78 ) 
        return string