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
----------------
 The following are required. They determine values.
----------------
   * Accuracy (int): How accurate is the spell in percents? (100 is autohit)
   * Min_DMG (int): This is the minimum damage the spell does. If the damage roll rolls less than, then this is applied.
   * desc_start (str): This is what the description of the spell if it starts the sentence. (A jet of flame)
   * desc_inc (str): This is what the description of the spell if it is in the sentence. (jets of flame)
   * cast_action (str): This is what happens when you cast the spell. (chants default)
      * chant - chants 
      * sign - signs
"""