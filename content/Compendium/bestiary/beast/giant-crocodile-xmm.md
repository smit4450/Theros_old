---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Crocodile"]
---
# Giant Crocodile
*Source: Monster Manual (2024) p. 356*  

![](Compendium/bestiary/beast/img/giant-crocodile.webp#center)  
```statblock
"name": "Giant Crocodile (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "85"
"hit_dice": "9d12 + 27"
"stats":
- !!int "21"
- !!int "9"
- !!int "17"
- !!int "2"
- !!int "10"
- !!int "7"
"speed": "30 ft., swim 50 ft."
"skillsaves":
  "Stealth": !!int "5"
"senses": "passive Perception 10"
"languages": ""
"cr": "5"
"traits":
- "desc": "The crocodile can hold its breath for 1 hour."
  "name": "Hold Breath"
"actions":
- "desc": "The crocodile makes one Bite attack and one Tail attack."
  "name": "Multiattack"
- "desc": "Melee Attack: +8, reach 5 ft. Hit: 21 (3d10 + 5) Piercing damage.\
    \ If the target is a Large or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 15). While [Grappled](Compendium/rules/conditions.md#Grappled),\
    \ the target has the [Restrained](Compendium/rules/conditions.md#Restrained) condition\
    \ and can't be targeted by the crocodile's Tail."
  "name": "Bite"
- "desc": "Melee Attack: +8, reach 10 ft. Hit: 18 (3d8 + 5) Bludgeoning damage.\
    \ If the target is a Large or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Tail"
"source":
- "XMM"
```
^statblock