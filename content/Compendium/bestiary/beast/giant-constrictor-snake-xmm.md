---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Constrictor Snake"]
---
# Giant Constrictor Snake
*Source: Monster Manual (2024) p. 355*  

![](Compendium/bestiary/beast/img/giant-constrictor-snake.webp#center)  
```statblock
"name": "Giant Constrictor Snake (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "60"
"hit_dice": "8d12 + 8"
"stats":
- !!int "19"
- !!int "14"
- !!int "12"
- !!int "1"
- !!int "10"
- !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  "Perception": !!int "2"
"senses": "blindsight 10 ft., passive Perception 12"
"languages": ""
"cr": "2"
"actions":
- "desc": "The snake makes one Bite attack and uses Constrict."
  "name": "Multiattack"
- "desc": "Melee Attack: +6, reach 10 ft. Hit: 11 (2d6 + 4) Piercing damage."
  "name": "Bite"
- "desc": "Strength Saving Throw: DC 14, one Large or smaller creature the snake\
    \ can see within 10 feet. Failure: 13 (2d8 + 4) Bludgeoning damage, and the\
    \ target has the [Grappled](Compendium/rules/conditions.md#Grappled) condition\
    \ (escape DC 14)."
  "name": "Constrict"
"source":
- "XMM"
```
^statblock