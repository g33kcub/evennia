"""
This is a database of all the materials in the system. 
More will get added as new dungeons are introduced. 
Materials are limited to a specific dungeon, will be statted as such.

Material Formatting:

Tier      = INT = This determines the generic value of it when combined with rarity.
Rarity    = STR = How often it is found during the month cycle. 
TYPE      = STR = What type of material is. Plant, etc. 

"""

MATERIAL_TABLE_GLOBAL = {
    "bone": {"type": "Beast Part", "tier": 1, "rarity": "Very Common"},
    "bone, dragon": {"type": "Beast Part", "tier": 4, "rarity": "Rare"},
    "bone, exotic": {"type": "Beast Part", "tier": 3, "rarity": "Uncommon"},
    "cloth": {"type": "Textile", "tier": 1, "rarity": "Common"},
    "cloth, arcane weave": {"type": "Textile", "tier": 5, "rarity": "Legendary"},
    "cloth, exotic": {"type": "Textile", "tier": 3, "rarity": "Rare"},
    "cloth, high quality": {"type": "Textile", "tier": 2, "rarity": "Uncommon"},
    "cloth, low quality": {"type": "Textile", "tier": 0, "rarity": "Very Common"},
    "cloth, luxury": {"type": "Textile", "tier": 4, "rarity": "Rare"},
    "cloth, shadow weave": {"type": "Textile", "tier": 5, "rarity": "Legendary"},
    "dragon glass": {"type": "Metal", "tier": 5, "rarity": "Legendary"},
    "egg": {"type": "Ingredient", "tier": 0, "rarity": "Uncommon"},
    "egg, dragon": {"type": "Ingredient", "tier": 5, "rarity": "Epic"},
    "egg, exotic": {"type": "Ingredient", "tier": 2, "rarity": "Rare"},
    "egg, luxury": {"type": "Ingredient", "tier": 3, "rarity": "Rare"},
    "feather": {"type": "Beast Part", "tier": 1, "rarity": "Very Common"},
    "feather, exotic": {"type": "Beast Part", "tier": 3, "rarity": "Uncommon"},
    "feather, luxury": {"type": "Beast Part", "tier": 4, "rarity": "Rare"},
    "gemstone, imitation": {"type": "Gemstone", "tier": 0, "rarity": "Very Common"},
    "gemstone, precious": {"type": "Gemstone", "tier": 2, "rarity": "Uncommon"},
    "gemstone, semiprecious": {"type": "Gemstone", "tier": 1, "rarity": "Common"},
}

MATERIAL_TABLE_D1 = {
    "egg, chimera": {"type": "Ingredient", "tier": 5, "rarity": "Rare"},
    "egg, deep serpent": {"type": "Ingredient", "tier": 5, "rarity": "Epic"},
}