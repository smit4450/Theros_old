---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Rat"]
---
# Giant Rat
*Source: Monster Manual (2024) p. 358*  

![](Compendium/bestiary/beast/img/giant-rat.webp#center)  
```statblock
"name": "Giant Rat (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "7"
"hit_dice": "2d6"
"stats":
- !!int "7"
- !!int "16"
- !!int "11"
- !!int "2"
- !!int "10"
- !!int "4"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "5"
"skillsaves":
  "Perception": !!int "2"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": ""
"cr": "1/8"
"traits":
- "desc": "The rat has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the rat's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Attack: +5, reach 5 feet. Hit: 5 (1d4 + 3) Piercing damage."
  "name": "Bite"
"source":
- "XMM"
```
^statblock