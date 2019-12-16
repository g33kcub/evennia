# -*- coding: utf-8 -*-
"""
Connection screen

This is the text to show the user when they first connect to the game (before
they log in).

To change the login screen in this module, do one of the following:

- Define a function `connection_screen()`, taking no arguments. This will be
  called first and must return the full string to act as the connection screen.
  This can be used to produce more dynamic screens.
- Alternatively, define a string variable in the outermost scope of this module
  with the connection string that should be displayed. If more than one such
  variable is given, Evennia will pick one of them at random.

The commands available to the user when the connection screen is shown
are defined in evennia.default_cmds.UnloggedinCmdSet. The parsing and display
of the screen is done by the unlogged-in "look" command.

"""

from django.conf import settings
from evennia import utils

CONNECTION_SCREEN = """
|113==============================================================================|n
   ___                 _     _     We run on a base core of |gEvennia {}|n.
  /___\_ __ ___   ___ (_) __| | ___   That is running the |cKumaRPG {}|n.
 //  // '_ ` _ \ / _ \| |/ _` |/ _ \
/ \_//| | | | | | (_) | | (_| |  __/ To just visit us use |wconnect guest|n
\___/ |_| |_| |_|\___/|_|\__,_|\___|    to sign into a temporary account. 
---------------------------------     __      
|wconnect <account> <password>|n     /\ \ \___  
     To login to an existing      /  \/ / _ \ 
        account                  / /\  / (_) |
|wcreate <account> <password>|n      \_\ \/ \___/
  __ To create a new account                  _              _       
  \ \ _   _ _   _ _ __ ___   __ _ _ __   ___ | | ___   _  __| | __ _ 
   \ \ | | | | | | '_ ` _ \ / _` | '_ \ / _ \| |/ / | | |/ _` |/ _` |
/\_/ / |_| | |_| | | | | | | (_| | | | | (_) |   <| |_| | (_| | (_| |
\___/ \__,_|\__,_|_| |_| |_|\__,_|_| |_|\___/|_|\_\\__,_|\__,_|\__,_|

 If you have spaces in your username, enclose it in quotes.
 Enter |whelp|n for more info. |wlook|n will re-show this screen.
|113==============================================================================|n""".format(
     utils.get_evennia_version("short"),settings.KUMAVERS
)
