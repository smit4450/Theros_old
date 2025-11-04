---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Crocodile"]
---
# Crocodile
*Source: Monster Manual (2024) p. 352, Player's Handbook (2024) p. 348*  

![](Compendium/bestiary/beast/img/crocodile.webp#center)  
```statblock
"name": "Crocodile (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "13"
"hit_dice": "2d10 + 2"
"stats":
- !!int "15"
- !!int "10"
- !!int "13"
- !!int "2"
- !!int "10"
- !!int "5"
"speed": "20 ft., swim 30 ft."
"saves":
  "Constitution": !!int "3"
"skillsaves":
  "Stealth": !!int "2"
"senses": "passive Perception 10"
"languages": ""
"cr": "1/2"
"traits":
- "desc": "The crocodile can hold its breath for 1 hour."
  "name": "Hold Breath"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 6 (1d8 + 2) Piercing damage.\
    \ If the target is a Medium or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 12). While [Grappled](Compendium/rules/conditions.md#Grappled),\
    \ the target has the [Restrained](Compendium/rules/conditions.md#Restrained) condition."
  "name": "Bite"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/crocodile-xmm.webp"
```
^statblock