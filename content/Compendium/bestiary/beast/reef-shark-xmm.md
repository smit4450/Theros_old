---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Reef Shark"]
---
# Reef Shark
*Source: Monster Manual (2024) p. 368, Player's Handbook (2024) p. 356*  

![](Compendium/bestiary/beast/img/reef-shark.webp#center)  
```statblock
"name": "Reef Shark (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d8 + 4"
"stats":
- !!int "14"
- !!int "15"
- !!int "13"
- !!int "1"
- !!int "10"
- !!int "4"
"speed": "5 ft., swim 30 ft."
"skillsaves":
  "Perception": !!int "2"
"senses": "blindsight 30 ft., passive Perception 12"
"languages": ""
"cr": "1/2"
"traits":
- "desc": "The shark has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the shark's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
- "desc": "The shark can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 7 (2d4 + 2) Piercing damage."
  "name": "Bite"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/reef-shark-xmm.webp"
```
^statblock