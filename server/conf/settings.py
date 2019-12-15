r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/g33kcub/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Omoide No Juumanokudo"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

######################################################################
# Guest accounts
######################################################################

# This enables guest logins, by default via "connect guest". Note that
# you need to edit your login screen to inform about this possibility.
GUEST_ENABLED = True
# Typeclass for guest account objects (linked to a character)
BASE_GUEST_TYPECLASS = "typeclasses.accounts.Guest"
# The permission given to guests
PERMISSION_GUEST_DEFAULT = "Guests"
# The default home location used for guests.
GUEST_HOME = DEFAULT_HOME
# The start position used for guest characters.
GUEST_START_LOCATION = START_LOCATION
# The naming convention used for creating new guest
# accounts/characters. The size of this list also determines how many
# guests may be on the game at once. The default is a maximum of nine
# guests, named Guest1 through Guest9.
GUEST_LIST = ["Guest" + str(s + 1) for s in range(19)]

# Help output from CmdHelp are wrapped in an EvMore call
# (excluding webclient with separate help popups). If continuous scroll
# is preferred, change 'HELP_MORE' to False. EvMORE uses CLIENT_DEFAULT_HEIGHT
HELP_MORE = False

# The access hierarchy, in climbing order. A higher permission in the
# hierarchy includes access of all levels below it. Used by the perm()/pperm()
# lock functions, which accepts both plural and singular (Admin & Admins)
PERMISSION_HIERARCHY = [
    "Newbie",
    "Player",
    "Helper",
    "Builder",
    "Staff",
    "Admin",
    "Developer",
]
# The default permission given to all new accounts
PERMISSION_ACCOUNT_DEFAULT = "Newbie"