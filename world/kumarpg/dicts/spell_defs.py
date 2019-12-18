"""
This the file where we define all the spells in the game, regardless of what dungeon they are in.

Required Values for a spell:
  * Cost (int): How much MP the spell costs as a base per level before modifiers.
  * Target (str): What can be hit?
     * none - No targets allowed. Area effect or summon style.
     * self - Only the caster.
     * any - Any object in the db.
     * anyobj - Any non-character object in the db.
     * anychar - Any character object in the db. 
     * other - Any object in the db, except caster.
     * otherchar - Any character in the db, execpt the caster. 
     * party - Entire caster's party.
     * eparty - Entire enemy party.
   * Spellfunction (callable): What type of spell is the spell. From spell_types.py
----------------
 The optional flags are defaulted to true. However, they are not mutually exclusive.
----------------
   * combat_spell (bool): Can the spell be used in combats?
   * pvp_spell (bool): Can the spell be used in PvP?
   * noncombat_spell (bool): Cam the spell be used outside of combat?
----------------
 The optional flags below determine special qualities of the spell and are set depending on the spell type.
----------------
   * status (str): What status will it apply?
   * status_chance (int): What percentage is there for this status to be applied.
   * status_duration (int): How long does the status last. 
   * max_targets (int): How many targets can the spell affect at the most.
   * attack_count (int): How many simulatenous attacks does the spell have? (1 default)
   * object_key (str): The object the spell summons. 
   * elemental (str): The element the spell is aligned with. (non-elemental, default)
   * dice_level (array): The dice used by default. (['4','4','6','6','8','8','10','12','20'])
   * max_hp (int): This is the base maximum damage it will take before failing.  (999 is absolute max.)
   * max_rank (int): This is the maximum rank this spell can be, default is 10(X)
----------------
 The following are required. They determine values.
----------------
   * Accuracy (int): How accurate is the spell in percents? (100 is autohit)
   * Min_DMG (int): This is the minimum damage the spell does. If the damage roll rolls less than, then this is applied.
                    If set to 0, this is a non-damaging spell. 
   * desc_start (str): This is what the description of the spell if it starts the sentence. (A jet of flame)
   * desc_inc (str): This is what the description of the spell if it is in the sentence. (jets of flame)
   * cast_action (str): This is what happens when you cast the spell. (chants default)
      * chant - chants 
      * sign - signs
      * scribe - enscribes

----------------
 System Documentation
----------------
* All spell values are given for an 1(F) spell. 
* All spell values are not modified by abilities or anything, this is the basic spell.
* All spells that deal damage use the dice_level associated with their rank for damage. 1(F)[4] to 10(X)[20].
* This means a 10(X) version of firebolt will roll 10d20 for damage, then get modified. 
* All costs are multiplied by the casting level before modified. So a 10(X) Firebolt costs 20 MP to cast.
* A duration of 999 means it ends when the HP is diminished.
* Min_DMG is the minimum damage the spell can do per level. So again a 10(X) Firebolt deals at minimum 20 HP.
* Accuracy is determined by the default value + any stat mods. It cannot exceed 100% nor can it be lower than 1%.
* Max_HP is multiplied by the casting level. 
"""

SPELLS = {
    "aquabolt": {},
    "bubble screen": {},
    "whirlpool weapon": {},
    "tidal shockwave": {},
    "undine": {},
    "aerobolt": {},
    "windscreen": {},
    "tornado weapon": {},
    "heaven's shockwave": {},
    "wisp": {},
    "geobolt": {},
    "seismic tremor": {},
    "sandstorm weapon": {},
    "earthquake": {},
    "gnome": {},
    "voidbolt": {},
    "blackhole horizon": {},
    "shadow weapon": {},
    "blackhole supernova": {},
    "shade": {},
    "lightbolt": {},
    "gleaming aura": {},
    "gleaming weapon": {},
    "divine judgment": {},
    "luna": {},
    "shockbolt": {},
    "static weapon": {},
    "air lense": {},
    "raging thunderstorm": {},
    "flashbug": {},
    "arcticbolt": {},
    "snowstorm": {},
    "blizzard weapon": {},
    "arctic snap": {},
    "shiva": {},
    "manabolt": {},
    "counterspell": {},
    "mana weapon": {},
    "arcane strike": {},
    "magus": {},
    "protection": {},
    "reflection": {},
    "liminal light": {},
    "healing energy": {},
    "haste": {},
    "slow": {},
    "sanctuary": {},
    "gravity crush": {},
    "crimson lightning": {},
    "medusa's gaze": {},
    "blinding light": {},
    "earshock": {},
    "psion wave": {},
    "rebuke": {},
    "attack up": {},
    "defense up": {},
    "armor break": {},
    "power break": {},
    "hex": {},
    "chaosbolt": {
        "spellfunction": spell_attack_wild,
        "cost": 2,
        "target": "other",
        "elemental": "chaos",

    },
    "entropy field": {},
    "chaotic bombardment": {},
    "firebolt": {
        "spellfunction": spell_attack_status,
        "cost": 2,
        "target": "other",
        "elemental": "fire",
        "status": "burning",
        "status_chance": 25,
        "status_duration": 2,
        "accuracy": 85,
        "min_dmg": 2,
        "desc_start": "A blast of flames",
        "desc_inc": "blast of flames",
        "cast_action": "chant"
    },
    "will-o-wisp": {
        "spellfuction": spell_protect,
        "cost": 5,
        "target": "anychar",
        "elemental": "fire",
        "accuracy": 100,
        "max_hp": 15,
        "min_dmg": 0,
        "status": "protect"
        "status_duration": 999,
        "status_chance": 100,
        "desc_start": "A ruby colored bubble",
        "desc_inc": "a ruby colored bubble",
        "cast_action": "signs"
    }
    "phoenix weapon": {
        "spellfunction": spell_buff_noprotect,
        "cost": 3,
        "target": "anyobj",
        "elemental": "fire",
        "accuracy": 100,
        "min_dmg": 0,
        "status": "blazing",
        "status_chance": 100,
        "status_duration": 5,
        "noncombat_spell": False,
        "desc_start": "Igniting in flames",
        "desc_inc": "ignites in flames",
        "cast_action": "scribe"
    },
    "phoenix flare": {
        "spellfunction": spell_attack_status,
        "cost": 10,
        "target": "eparty",
        "elemental": "fire",
        "min_dmg": 7,
        "status": "burning",
        "status_chance": 100,
        "status_duration": 5,
        "noncombat_spell": False,
        "desc_start": "A wave of white hot flames",
        "desc_in": "waves of white hot flames",
        "cast_action": "chant",
        "dice_level": ['10','10','10','12','12','12','20','20','20']
    },
    "salamander": {
        "spellfunction": spell_summon,
        "cost": 20,
        "target": "none",
        "min_dmg": 0,
        "object_key": "Salamander",
        "accuracy": 95,
        "pvp_spell": False,
        "desc_start": "Opens a fiery portal summoning Salamander",
        "desc_inc": "summons Salamander from within a fiery portal",
        "cast_action": "chant",
        "max_rank": 1
    }
}