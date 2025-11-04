---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Scorpion"]
---
# Giant Scorpion
*Source: Monster Manual (2024) p. 359*  

![](Compendium/bestiary/beast/img/giant-scorpion.webp#center)  
```statblock
"name": "Giant Scorpion (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "52"
"hit_dice": "7d10 + 14"
"stats":
- !!int "16"
- !!int "13"
- !!int "15"
- !!int "1"
- !!int "9"
- !!int "3"
"speed": "40 ft."
"senses": "blindsight 60 ft., passive Perception 9"
"languages": ""
"cr": "3"
"actions":
- "desc": "The scorpion makes two Claw attacks and one Sting attack."
  "name": "Multiattack"
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 6 (1d6 + 3) Bludgeoning damage.\
    \ If the target is a Large or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 13) from one of two claws."
  "name": "Claw"
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage\
    \ plus 11 (2d10) Poison damage."
  "name": "Sting"
"source":
- "XMM"
```
^statblock