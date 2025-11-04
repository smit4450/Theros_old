---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Swarm of Venomous Snakes"]
---
# Swarm of Venomous Snakes
*Source: Monster Manual (2024) p. 371*  

![](Compendium/bestiary/beast/img/swarm-of-venomous-snakes.webp#center)  
```statblock
"name": "Swarm of Venomous Snakes (XMM)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "36"
"hit_dice": "8d8"
"stats":
- !!int "8"
- !!int "18"
- !!int "11"
- !!int "1"
- !!int "10"
- !!int "3"
"speed": "30 ft., swim 30 ft."
"damage_resistances": "bludgeoning, piercing, slashing"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [grappled](Compendium/rules/conditions.md#Grappled), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [prone](Compendium/rules/conditions.md#Prone),\
  \ [restrained](Compendium/rules/conditions.md#Restrained), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "blindsight 10 ft., passive Perception 10"
"languages": ""
"cr": "2"
"traits":
- "desc": "The swarm can occupy another creature's space and vice versa, and the swarm\
    \ can move through any opening large enough for a Tiny snake. The swarm can't\
    \ regain [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) or gain\
    \ [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
  "name": "Swarm"
"actions":
- "desc": "Melee Attack: +6, reach 5 ft. Hit: 8 (1d8 + 4) Piercing damage—\
    or 6 (1d4 + 4) Piercing damage if the swarm is [Bloodied](Compendium/rules/variant-rules/bloodied-xphb.md)—\
    plus 10 (3d6) Poison damage."
  "name": "Bites"
"source":
- "XMM"
```
^statblock