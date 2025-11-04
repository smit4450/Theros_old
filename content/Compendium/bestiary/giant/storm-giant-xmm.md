---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/13
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Storm Giant"]
---
# Storm Giant
*Source: Monster Manual (2024) p. 302*  

![](Compendium/bestiary/giant/img/storm-giant.webp#right)  
## Storm Giant

*Giant of Seas and Skies*

- **Habitat.** Coastal, Underwater  
- **Treasure.** Armaments  

Among the tallest giants, storm giants live amid extreme forces of nature. In palaces at the bottom of the sea and castles floating amid the clouds, they revel in the power of mighty storms. When angered, they can shape the weather and call down devastating lightning. More often, though, these giants watch the rise and fall of nations and interpret supernatural omens, interfering in the world only when they're needed most.
```statblock
"name": "Storm Giant (XMM)"
"size": "Huge"
"type": "giant"
"alignment": "Chaotic Good"
"ac": !!int "16"
"hp": !!int "230"
"hit_dice": "20d12 + 100"
"stats":
- !!int "29"
- !!int "14"
- !!int "20"
- !!int "16"
- !!int "20"
- !!int "18"
"speed": "50 ft., fly 25 ft. (hover), swim 50 ft."
"saves":
  "Charisma": !!int "9"
  "Wisdom": !!int "10"
  "Strength": !!int "14"
  "Constitution": !!int "10"
"skillsaves":
  "Athletics": !!int "14"
  "Perception": !!int "10"
  "History": !!int "8"
  "Arcana": !!int "8"
"damage_resistances": "cold"
"damage_immunities": "lightning, thunder"
"senses": "darkvision 120 ft., truesight 30 ft., passive Perception 20"
"languages": "Common, Giant"
"cr": "13"
"traits":
- "desc": "The giant casts one of the following spells, requiring no Material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 18):\n\nAt will:\
    \ [Detect Magic](Compendium/spells/detect-magic-xphb.md), [Light](Compendium/spells/light-xphb.md)\n\
    \n1/day: [Control Weather](Compendium/spells/control-weather-xphb.md)"
  "name": "Spellcasting"
- "desc": "The giant can breathe air and water."
  "name": "Amphibious"
"actions":
- "desc": "The giant makes two attacks, using Storm Sword or Thunderbolt in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +14, reach 10 ft. Hit: 23 (4d6 + 9) Slashing damage\
    \ plus 13 (3d8) Lightning damage."
  "name": "Storm Sword"
- "desc": "Ranged Attack: +14, range 500 ft. Hit: 22 (2d12 + 9) Lightning\
    \ damage, and the target has the [Blinded](Compendium/rules/conditions.md#Blinded)\
    \ and [Deafened](Compendium/rules/conditions.md#Deafened) conditions until the\
    \ start of the giant's next turn."
  "name": "Thunderbolt"
- "desc": "Dexterity Saving Throw: DC 18, each creature in a 10-foot-radius, 40-foot-high\
    \ [Cylinder [Area of Effect]](Compendium/rules/variant-rules/cylinder-area-of-effect-xphb.md)\
    \ originating from a point the giant can see within 500 feet. Failure: 55 (10d10)\
    \ Lightning damage. Success: Half damage."
  "name": "Lightning Storm (Recharge 5-6)"
"source":
- "XMM"
```
^statblock