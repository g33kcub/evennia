from evennia import DefaultObject

class Zoid(DefaultObject):
    """
    This is the default type class for a generic zoid.
    """
    def at_object_creation(self):
        """
        This is called only when object is first created.
        """
        pass
    