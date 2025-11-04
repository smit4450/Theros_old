---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Berserker"]
---
# Berserker
*Source: Monster Manual (2024) p. 37*  

![](Compendium/bestiary/humanoid/img/berserker.webp#right)  
Berserkers might fight for personal glory or form motivated forces or howling hordes.

## Berserkers

*Raging Invaders and Impassioned Warriors*

- **Habitat.** Any  
- **Treasure.** Armaments, Individual  

Gripped by the adrenaline of battle, berserkers are reckless invaders, pit fighters, and other ferocious warriors.
## Statblock

```statblock
"name": "Berserker (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "13"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"stats":
- !!int "16"
- !!int "12"
- !!int "17"
- !!int "9"
- !!int "11"
- !!int "9"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
- "desc": "While [Bloodied](Compendium/rules/variant-rules/bloodied-xphb.md), the\
    \ berserker has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on attack rolls and saving throws."
  "name": "Bloodied Frenzy"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 9 (1d12 + 3) Slashing damage."
  "name": "Greataxe"
"source":
- "XMM"
```
^statblock