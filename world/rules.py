from random import randint

def roll_hit():
    "roll 1d100"
    return randint(1,100)

def roll_dmg():
    "roll 1d6"
    return randint(1,6)

def check_defeat(character):
    "Checks if a character has been defeated."
    if character.db.HP <= 0:
        character.msg("You fall down, defeated!")
        character.db.HP = 100 #reset

def add_XP(character,amount):
    "Add XP to a character, tracking a level increase"
    if character.db.XP >= (character.db.level + 1) ** 2:
        character.db.leve += 1
        character.db.STR += 1
        character.db.combat += 2
        character.msg("You are now level %i!" % character.db.level)

