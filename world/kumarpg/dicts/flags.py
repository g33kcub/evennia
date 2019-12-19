
# Just a dictionary with tag:category format.

flags = {
    "ooc": {
        "aliases": [],
        "code": "o",
        "set": "perm(player)",
        "unset": "perm(player)",
        "desc": "A flag that represents out of character status"
    },
    "approved": {
        "aliases": [],
        "code": "a",
        "set": "perm(staff)",
        "unset": "perm(staff)",
        "desc": "A flag that signifies approval status."
    },
    "incombat": {
        "aliases": ['combat','in_combat','battle'],
        "code": "c",
        "set": "perm(staff)",
        "unset": "perm(staff)",
        "desc": "A system flag that determines if a character is in combat or not."
    },
    "lookingforgroup": {
        "aliases": ['lfg','looking_for_group','party_ok','partyok'],
        "code": "g",
        "set": "perm(player)",
        "unset": "perm(player)",
        "desc": "A flag to denote that you are looking for a party or group to adventure with."
    },
    "lookingforroleplay": {
        "aliases": ['lrp','looking_for_roleplay','rpok','roleplayok','rp_ok','roleplay_ok'],
        "code": "r",
        "set": "perm(player)",
        "unset": "perm(player)",
        "desc": "A flag to denote that you are looking for Roleplay scenes."
    },
    "playervsplayerok": {
        "aliases": ['pvpok','player_vs_player_ok','pvp'],
        "code": "p",
        "set": "perm(player)",
        "unset": "perm(player)",
        "desc": "A flag to denote that you are open to player versus player combat, that may result in death."
    },
    "isdead": {
        "aliases": ['dead'],
        "code": "d",
        "set": "perm(player)",
        "unset": "perm(player)",
        "desc": "A flag to denote that a character is dead."
    }
}