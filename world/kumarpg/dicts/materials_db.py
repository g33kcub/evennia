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
    "cotton": {"type": "Plant", "tier": 1, "rarity": "Common"},
    "cotton, high quality": {"type": "Plant", "tier": 2, "rarity": "Uncommon"},
    "cotton, low quality": {"type": "Plant", "tier": 0, "rarity": "Common"},
    "dragon glass": {"type": "Metal", "tier": 5, "rarity": "Legendary"},
    "egg": {"type": "Ingredient", "tier": 0, "rarity": "Uncommon"},
    "egg, dragon": {"type": "Ingredient", "tier": 5, "rarity": "Epic"},
    "egg, exotic": {"type": "Ingredient", "tier": 2, "rarity": "Rare"},
    "egg, luxury": {"type": "Ingredient", "tier": 3, "rarity": "Rare"},
    "fastener": {"type": "Component", "tier": 1, "rarity": "Common"},
    "fastener, exotic": {"type": "Component", "tier": 3, "rarity": "Rare"},
    "fastener, high quality": {"type": "Component", "tier": 2, "rarity": "Uncommon"},
    "feather": {"type": "Beast Part", "tier": 1, "rarity": "Very Common"},
    "feather, exotic": {"type": "Beast Part", "tier": 3, "rarity": "Uncommon"},
    "feather, luxury": {"type": "Beast Part", "tier": 4, "rarity": "Rare"},
    "glass": {"type": "Component", "tier": 1, "rarity": "Common"},
    "glass, high quality": {"type": "Component", "tier": 2, "rarity": "Uncommon"},
    "glass, low quality": {"type": "Component", "tier": 0, "rarity": "Very Common"},
    "gemstone, imitation": {"type": "Gemstone", "tier": 0, "rarity": "Very Common"},
    "gemstone, precious": {"type": "Gemstone", "tier": 2, "rarity": "Uncommon"},
    "gemstone, semiprecious": {"type": "Gemstone", "tier": 1, "rarity": "Common"},
    "herb": {"type": "Ingredient", "tier": 0, "rarity": "Very Common"},
    "herb, exotic": {"type": "Ingredient", "tier": 3, "rarity": "Uncommon"},
    "herb, high quality": {"type": "Ingredient", "tier": 2, "rarity": "Uncommon"},
    "herb, luxury": {"type": "Ingredient", "tier": 4, "rarity": "Rare"},
    "iron, dark": {"type": "Metal", "tier": 5, "rarity": "Legendary"},
    "iron, high quality": {"type": "Metal", "tier": 2, "rarity": "Uncommon"},
    "iron": {"type": "Metal", "tier": 1, "rarity": "Common"},
    "iron, star": {"type": "Metal", "tier": 6, "rarity": "Unique"},
    "iron, stygian": {"type": "Metal", "tier": 5, "rarity": "Legendary"},
    "jade": {"type": "Gemstone", "tier": 1, "rarity": "Common"},
    "jade, black": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "jade, blue": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "jade, gold": {"type": "Gemstone", "tier": 5, "rarity": "Epic"},
    "jade, orange": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "jade, red": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "jade, silver": {"type": "Gemstone", "tier": 5, "rarity": "Epic"},
    "jade, white": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "jute": {"type": "Plant", "tier": 1, "rarity": "Common"},
    "jute, exotic": {"type": "Plant", "tier": 4, "rarity": "Rare"},
    "jute, high quality": {"type": "Plant", "tier": 3, "rarity": "Uncommon"},
    "jute, low quality": {"type": "Plant", "tier": 0, "rarity": "Very Common"},
    "lace": {"type": "Textile", "tier": 1, "rarity": "Common"},
    "lace, arcane weave": {"type": "Textile", "tier": 5, "rarity": "Rare"},
    "lace, armor weave": {"type": "Textile", "tier": 5, "rarity": "Rare"},
    "lace, exotic": {"type": "Textile", "tier": 3, "rarity": "Uncommon"},
    "lace, luxury": {"type": "Textile", "tier": 4, "rarity": "Uncommon"},
    "leather": {"type": "Textile", "tier": 1, "rarity": "Common"},
    "leather, exotic": {"type": "Textile", "tier": 3, "rarity": "Rare"},
    "leather, high quality": {"type": "Textile", "tier": 2, "rarity": "Uncommon"},
    "leather, low quality": {"type": "Textile", "tier": 0, "rarity": "Very Common"},
    "magicite, amber": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "magicite, diamond": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "magicite, emerald": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "magicite, golden": {"type": "Gemstone", "tier": 5, "rarity": "Legendary"},
    "magicite, obsidian": {"type": "Gemstone", "tier": 5, "rarity": "Legendary"},
    "magicite, opal": {"type": "Gemstone", "tier": 6, "rarity": "Unique"},
    "magicite, ruby": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "magicite, sapphire": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "magicite, topaz": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "magicite, unformed": {"type": "Gemstone", "tier": 2, "rarity": "Uncommon"},
    "meat": {"type": "Ingredient", "tier": 1, "rarity": "Common"},
    "meat, exotic": {"type": "Ingredient", "tier": 3, "rarity": "Rare"},
    "meat, high quality": {"type": "Ingredient", "tier": 2, "rarity": "Uncommon"},
    "meat, low quality": {"type": "Ingredient", "tier": 0, "rarity": "Common"},
    "meat, luxury": {"type": "Ingredient", "tier": 4, "rarity": "Legendary"},
    "metal, low quality": {"type": "Metal", "tier": 0, "rarity": "Very Common"},
    "metal, luxury": {"type": "Metal", "tier": 4, "rarity": "Rare"},
    "metal, precious": {"type": "Metal", "tier": 3, "rarity": "Rare"},
    "metal, semiprecious": {"type": "Metal", "tier": 2, "rarity": "Uncommon"},
    "oil": {"type": "Ingredient", "tier": 1, "rarity": "Common"},
    "oil, exotic": {"type": "Ingredient", "tier": 3, "rarity": "Rare"},
    "oil, high quality": {"type": "Ingredient", "tier": 2, "rarity": "Uncommon"},
    "oil, low quality": {"type": "Ingredient", "tier": 0, "rarity": "Very Common"},
    "oil, luxury": {"type": "Ingredient", "tier": 4, "rarity": "Rare"},
    "pearl": {"type": "Gemstone", "tier": 1, "rarity": "Uncommon"},
    "pearl, black": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "pearl, blue": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "pearl, gold": {"type": "Gemstone", "tier": 4, "rarity": "Epic"},
    "pearl, lavender": {"type": "Gemstone", "tier": 4, "rarity": "Rare"},
    "pearl, pink": {"type": "Gemstone", "tier": 3, "rarity": "Rare"},
    "pearl, rainbow": {"type": "Gemstone", "tier": 4, "rarity": "Legendary"},
}

MATERIAL_TABLE_VENDOR = {

}

MATERIAL_TABLE_D1 = {

}