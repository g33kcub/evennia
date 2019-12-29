from world.kumarpg.dicts.spell_types import spell_attack_wild, spell_attack_status, spell_protect, spell_buff_noprotect, spell_summon
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
   * elemental (str): The element the spell is aligned with. (non-elemental, default)

----------------
 The following are required. They determine values.
----------------
   * Accuracy (int): How accurate is the spell in percents? (100 is autohit)

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
    # poison spells.
    "bio": {},
    "acid": {},
    # summoning spells.
    "undine": {},
    "wisp": {},
    "gnome": {},
    "shade": {},
    "luna": {},
    "flashbug": {},
    "shiva": {},
    "magus": {},
    "salamander": {},
    "jinx": {},
    "toxica": {},
    # lightning spells.
    "shockbolt": {},
    "static weapon": {},
    "air lense": {},
    "crimson lightning": {},
    "plasma strike": {},
    # status spells
    "medusa's gaze": {},
    "earshock": {},
    "blinding flash": {},
    "white noise": {},
    "psion wave": {},
    "attack up": {},
    "defense up": {},
    "armor break": {},
    "power break": {},
    # Chaos magic.
    "chaosbolt": {},
    "entropy field": {},
    "wild weapon": {},
    "chaotic bombardment": {},
    # Time Magic
    "haste": {},
    "slow": {},
    "stop": {},
    "gravity crush": {},
    # healing magic
    "healing energy": {},
    "liminal energy": {},
    "regeneration": {},
    # abjuration magic
    "protect": {},
    "reflection": {},
    # mana magic
    "manabolt": {},
    "counterspell": {},
    "arcane strike": {},
    "mana weapon": {},
    # ice magic
    "arcticbolt": {},
    "snowstorm": {},
    "blizzard weapon": {},
    "arctic snap": {},
    # holy magic (light)
    "lightbolt": {},
    "gleaming weapon": {},
    "gleaming aura": {},
    "divine judgment": {},
    "sanctuary": {},
    "rebuke": {},
    # shadow magic
    "voidbolt": {},
    "blackhole horizon": {},
    "shadow weapon": {},
    "blackhole supernova": {},
    # earth magic
    "geobolt": {},
    "sandstorm weapon": {},
    "seismic tremor": {},
    "earthquake": {},
    # air magic
    "aerobolt": {},
    "tornado weapon": {},
    "windscreen": {},
    "heaven's shockwave": {},
    # water magic
    "aquabolt": {},
    "bubble screen": {},
    "whirlpool weapon": {},
    "tidal shockwave": {},
    # Fire magic
    "firebolt": {},
    "will-o-wisp": {},
    "phoenix weapon": {},
    "phoenix flare": {}
}