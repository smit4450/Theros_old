---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Wolf"]
---
# Wolf
*Source: Monster Manual (2024) p. 373, Player's Handbook (2024) p. 359*  

![](Compendium/bestiary/beast/img/wolf.webp#center)  
```statblock
"name": "Wolf (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "11"
"hit_dice": "2d8 + 2"
"stats":
- !!int "14"
- !!int "15"
- !!int "12"
- !!int "3"
- !!int "12"
- !!int "6"
"speed": "40 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": ""
"cr": "1/4"
"traits":
- "desc": "The wolf has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on attack rolls against a creature if at least one of the wolf's allies is within\
    \ 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage.\
    \ If the target is a Medium or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Bite"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/wolf-xmm.webp"
```
^statblock