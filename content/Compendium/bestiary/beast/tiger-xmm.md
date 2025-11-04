---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Tiger"]
---
# Tiger
*Source: Monster Manual (2024) p. 371, Player's Handbook (2024) p. 358*  

![](Compendium/bestiary/beast/img/tiger.webp#center)  
```statblock
"name": "Tiger (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "30"
"hit_dice": "4d10 + 8"
"stats":
- !!int "17"
- !!int "16"
- !!int "14"
- !!int "3"
- !!int "12"
- !!int "8"
"speed": "40 ft."
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "1"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 10 (2d6 + 3) Slashing damage.\
    \ If the target is a Large or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Rend"
"bonus_actions":
- "desc": "The tiger takes the Disengage or Hide action."
  "name": "Nimble Escape"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/tiger-xmm.webp"
```
^statblock