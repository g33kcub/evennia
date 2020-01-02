"""
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
KUMAVERS = "0.1"

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

# The default home location used for all objects. This is used as a
# fallback if an object's normal home location is deleted. Default
# is Limbo (#2).
DEFAULT_HOME = "#2"
# The start position for new characters. Default is Limbo (#2).
#  MULTISESSION_MODE = 0, 1 - used by default unloggedin create command
#  MULTISESSION_MODE = 2, 3 - used by default character_create command
START_LOCATION = "#2"

######################################################################
# Guest accounts
######################################################################

# This enables guest logins, by default via "connect guest". Note that
# you need to edit your login screen to inform about this possibility.
GUEST_ENABLED = True
# Typeclass for guest account objects (linked to a character)
BASE_GUEST_TYPECLASS = "typeclasses.accounts.Guest"
# The permission given to guests
PERMISSION_GUEST_DEFAULT = "Guest"
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
    "Guest",  # note-only used if GUEST_ENABLED=True
    "Player",
    "Helper",
    "Builder",
    "Staff",
    "Admin",
    "Developer"
]
# The default permission given to all new accounts
PERMISSION_ACCOUNT_DEFAULT = "Player"
TIME_ZONE = "EST"
GAME_SLOGAN = "Chapter 1: Into the Darkness"


# The Evennia Game Index is a dynamic listing of Evennia games. You can add your game
# to this list also if it is in closed pre-alpha development.
GAME_INDEX_ENABLED = True
# This dict
GAME_INDEX_LISTING = {
    "game_name": SERVERNAME,
    "game_status": "pre-alpha",  # pre-alpha, alpha, beta or launched
    "short_description": GAME_SLOGAN,
    "long_description": "We are an isekai anime themed game with mud aspects and social roleplay aspects.",
    "listing_contact": "staff@omoidemush.com",  # email
    "telnet_hostname": "",  # mygame.com
    "telnet_port": "",  # 1234
    "game_website": "http://omoidemush.com",  # http://mygame.com
    "web_client_url": "http://omoidemush.com/webclient",  # http://mygame.com/webclient
}

# Different Multisession modes allow a player (=account) to connect to the
# game simultaneously with multiple clients (=sessions). In modes 0,1 there is
# only one character created to the same name as the account at first login.
# In modes 2,3 no default character will be created and the MAX_NR_CHARACTERS
# value (below) defines how many characters the default char_create command
# allow per account.
#  0 - single session, one account, one character, when a new session is
#      connected, the old one is disconnected
#  1 - multiple sessions, one account, one character, each session getting
#      the same data
#  2 - multiple sessions, one account, many characters, one session per
#      character (disconnects multiplets)
#  3 - like mode 2, except multiple sessions can puppet one character, each
#      session getting the same data.
MULTISESSION_MODE = 2
# The maximum number of characters allowed by the default ooc char-creation command
MAX_NR_CHARACTERS = 10