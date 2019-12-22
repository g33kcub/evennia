from random import randint

def calculate_hp(character):
    """
    This is the formula for calculating maximum HP.
    [(Earth * 5) + racial_mod + cp_level_mod + ability_mod]
    """
    max_hp = 0  
    return max_hp

def calculate_mp(character):
    """
    This is the formula for calculating maximum MP.
    [(Void * 5) + racial_mod + cp_level_mod + ability_mod]
    """
    max_mp = 0
    return max_mp

def calculate_ep(character):
    """
    This is the formula for calculating maximum EP.
    [(((Water + Fire)/2) * 5) + racial_mod + cp_level_mod + ability_mod]
    """
    max_ep = 0
    return max_ep

def calculate_fp(character):
    """
    This is the formula for calculating maximum FP.
    [(((Earth + Air)/2) * 5) + racial_mod + cp_level_mod + ability_mod]
    """
    max_ep = 0
    return max_ep

def calculate_ap(character):
    """
    This is the formula for calculating maximum AP.
    [((Earth + Air + Fire + Water + Void)/5) * 7]
    """
    max_ap = 0
    return max_ap

def cp_level_mod(character):
    """
    This function calculates the CP/Level Mod for the character.

    RPGLEVEL (The character's hidden level marker.)
    1 to 2 = 0
    3 to 4 = 1
    5 to 6 = 2
    6 to 7 = 3
    8 to 9 = 4
    10 to 12 = 5
    13 to 15 = 6
    16 to 18 = 7
    19 = 8
    20 = 9
    """
    mod = 0
    return mod

def racial_mod(character, stat):
    """
    This provides a bonus based on the character's race.

    Human: +8 to all pools.
    Elf: +5 [HP,FP], +10 [EP], +12 [MP]
    Half-Elf: +7 [HP,EP,FP], +11 [MP]
    Pixie: +16 [EP,MP]
    Dwarf: +16 [HP,FP]
    Nekojin: +10 [HP,FP], +6 [MP,EP]
    Inojin: +7 [HP,FP], +9 [MP,EP]
    """
    racial_mod = 0
    return racial_mod

def ability_mod(character, stat):
    """
    This function takes a look at qualifying abilities and adds them to the appropriate pools.
    """
    ability_mod = 0
    return ability_mod




