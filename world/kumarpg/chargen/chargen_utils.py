from world.utilities.format import header
from world.kumarpg.dicts.d1_weapon_defs import weapons
from world.kumarpg.dungeon1 import dungeon1pregen as pregen
_current_dungeon = "D1"
_weapons = {
    "adventurer": 2,
    "supporter": 1,
    "citizen": 0
}
_skills = {
    "adventurer": 3,
    "supporter": 5,
    "citizen": 8
}


def cgen_header(string):
    return header("|540 Character Generation System|n - |w{}|n ".format(string), fill="|113=|n")


def _get_race_weapon(caller):
    cg = pregen.PREGEN_DUNGEON_1[caller.ndb.pregen["pkg"]]

    # Set a few chargen notes about free weapon ranks
    if cg["race"].lower() == "dwarf":
        caller.ndb.pregen["weapon"] = ["hammers"]

    if cg["race"].lower() == "elf":
        caller.ndb.pregen["weapon"] = ["bow", "swords"]

    if cg["race"].lower() == "half-elf":
        caller.ndb.pregen["weapon"] = ["swords"]

    if cg["race"].lower() == "nekojin":
        caller.ndb.pregen["weapon"] = ["swords"]

    if cg["race"].lower() == "inojin":
        caller.ndb.pregen["weapon"] = ["staves"]

    _weapon_list = [weapon for weapon in cg["d1_weapons"] if weapon in weapons]
    return [weapon for weapon in _weapon_list if weapon not in caller.ndb.pregen["weapon"]]
