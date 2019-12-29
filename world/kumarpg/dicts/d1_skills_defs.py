from world.kumarpg.dicts.types_defs import types

skills = {
    "skill": types["skill_dict"],
    "persuasion": types["skill_dict_social"],
    "haggling": types["skill_dict_social"],
    "intimidation": types["skill_dict_social"],
    "empathy": types["skill_dict_social"],
    "subterfuge": types["skill_dict_social"],
    "leadership": types["skill_dict_social"],
    "command": types["skill_dict_social"],
    "socialize": types["skill_dict_social"],
    "etiquette": types["skill_dict_social"],
    "armor smith": types["skill_dict_crafting1"],
    "weapon smith": types["skill_dict_crafting1"],
    "black smith": types["skill_dict_crafting1"],
    "jeweler": types["skill_dict_crafting1"],
    "tinkerer": types["skill_dict_crafting1"],
    "carpenter": types["skill_dict_crafting1"],
    "leather working": types["skill_dict_crafting2"],
    "seamstress": types["skill_dict_crafting2"],
    "miner": types["skill_dict_crafting3"],
    "forager": types["skill_dict_crafting3"],
    "farmer": types["skill_dict_crafting3"],
    "fisher": types["skill_dict_crafting3"],
    "scavenger": types["skill_dict_crafting3"],
    "animal husbandry": types["skill_dict_crafting3"],
    "enchanter": types["skill_dict_crafting4"],
    "scribe": types["skill_dict_crafting4"],
    "alchemy": types["skill_dict_crafting5"],
    "culinarian": types["skill_dict_crafting5"],
    "appraisal": types["skill_dict_tradesman"],
    "research": types["skill_dict_tradesman"],
    "survival": types["skill_dict_tradesman"]
}

persuasion_techniques = {
    "smooth talking": types["tech_dict"],
    "fast talking": types["tech_dict"]
}

leadership_techniques = {
    "inspire": types["tech_dict"]
}

animal_husbandry_techniques = {
    "good breeding": types["tech_dict"],
    "quick training": types["tech_dict"]
}

survival_techniques = {
    "track": types["tech_dict"]
}


scribe_techniques = {
    "quick writing": types["tech_dict"],
    "copy writing": types["tech_dict"]
}

research_techniques = {
    "hidden clue": types["tech_dict"]
}

alchemy_techniques = {
    "swift brewing": types["tech_dict"],
    "deep draught": types["tech_dict"]
}

socialize_techniques = {
    "sharp tongue": types["tech_dict"],
    "witty banter": types["tech_dict"]
}

culinarian_techniques = {
    "soul food": types["tech_dict"],
    "lasting meal": types["tech_dict"]
}

seamstress_techniques = {
    "reinforced stitch": types["tech_dict"],
    "swift stitching": types["tech_dict"],
}

MAGIC_SKILLS = {
    "fire magic": types["magic_dict"],
    "water magic": types["magic_dict"],
    "air magic": types["magic_dict"],
    "earth magic": types["magic_dict"],
    "shadow magic": types["magic_dict"],
    "holy magic": types["magic_dict"],
    "lightning magic": types["magic_dict"],
    "ice magic": types["magic_dict"],
    "mana magic": types["magic_dict"],
    "abjuration": types["magic_dict"],
    "healing magic": types["magic_dict"],
    "time magic": types["magic_dict"],
    "chaos magic": types["magic_dict"],
    "status magic": types["magic_dict"],
    "summoning": types["magic_dict"],
    "poison magic": types["magic_dict"]
}

poison_magic_techniques = {
    "bio": types["tech_dict"], # Poison Status
    "acid": types["tech_dict"] # Burn Status
}

summoning_techniques = {
    "undine": types["tech_dict"], # Water
    "wisp": types["tech_dict"], # Air
    "gnome": types["tech_dict"], # Earth
    "shade": types["tech_dict"], # Shadow
    "luna": types["tech_dict"], # light/Holy
    "flashbug": types["tech_dict"], # Lightning
    "shiva": types["tech_dict"], # Ice
    "magus": types["tech_dict"], # Mana
    "salamander": types["tech_dict"], # Fire
    "jinx": types["tech_dict"], # Chaos
    "toxica": types["tech_dict"] # Poison
}

lightning_magic_techniques = {
    "shockbolt": types["tech_dict"],
    "static weapon": types["tech_dict"],
    "air lense": types["tech_dict"],
    "raging thunderstorm": types["tech_dict"],
    "crimson lightning": types["tech_dict"],
    "plasma strike": types["tech_dict"]
}

status_magic_techniques = {
    "medusa's gaze": types["tech_dict"], # Paralyze
    "earshock": types["tech_dict"], # Deafen
    "blinding flash": types["tech_dict"], # Blind
    "psion wave": types["tech_dict"], # Confuse
    "white noise": types["tech_dict"], # Mute/Silence
    "attack up": types["tech_dict"],
    "defense up": types["tech_dict"],
    "armor break": types["tech_dict"],
    "power break": types["tech_dict"]
}

chaos_magic_techniques = {
    "chaosbolt": types["tech_dict"],
    "entropy field": types["tech_dict"],
    "wild weapon": types["tech_dict"],
    "chaotic bombardment": types["tech_dict"]
}

time_magic_techniques = {
    "haste": types["tech_dict"],
    "slow": types["tech_dict"],
    "stop": types["tech_dict"],
    "gravity crush": types["tech_dict"]
}

healing_magic_techniques = {
    "healing energy": types["tech_dict"],
    "liminal energy": types["tech_dict"],
    "regeneration": types["tech_dict"]
}

abjuration_techniques = {
    "protection": types["tech_dict"],
    "reflection": types["tech_dict"]
}

mana_magic_techniques = {
    "manabolt": types["tech_dict"],
    "counterspell": types["tech_dict"],
    "arcane strike": types["tech_dict"],
    "mana weapon": types["tech_dict"]
}

ice_magic_techniques = {
    "arcticbolt": types["tech_dict"],
    "snowstorm": types["tech_dict"],
    "blizzard weapon": types["tech_dict"],
    "arctic snap": types["tech_dict"]: 
}

holy_magic_techniques = {
    "lightbolt": types["tech_dict"],
    "gleaming weapon": types["tech_dict"],
    "gleaming aura": types["tech_dict"],
    "divine judgment": types["tech_dict"],
    "sanctuary": types["tech_dict"],
    "rebuke": types["tech_dict"]
}

shadow_magic_techniques = {
    "voidbolt": types["tech_dict"],
    "blackhole horizon": types["tech_dict"],
    "shadow weapon": types["tech_dict"],
    "blackhole supernova": types["tech_dict"]
}

earth_magic_techniques = {
    "geobolt": types["tech_dict"],
    "seismic tremor": types["tech_dict"],
    "sandstorm weapon": types["tech_dict"],
    "earthquake": types["tech_dict"]
}

air_magic_techniques = {
    "aerobolt": types["tech_dict"],
    "tornado weapon": types["tech_dict"],
    "windscreen": types["tech_dict"],
    "heaven's shockwave": types["tech_dict"]
}

water_magic_techniques = {
    "aquabolt": types["tech_dict"],
    "bubble screen": types["tech_dict"],
    "whirlpool weapon": types["tech_dict"],
    "tidal shockwave": types["tech_dict"]
}

fire_magic_techniques = {
    "firebolt": types["tech_dict"],
    "will-o-wisp": types["tech_dict"],
    "phoenix weapon": types["tech_dict"],
    "phoenix flare": types["tech_dict"]
}