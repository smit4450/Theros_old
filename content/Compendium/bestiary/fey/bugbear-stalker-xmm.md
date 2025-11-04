---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/fey/goblinoid
statblock: inline
aliases: ["Bugbear Stalker"]
---
# Bugbear Stalker
*Source: Monster Manual (2024) p. 62*  

![](Compendium/bestiary/fey/img/bugbear-stalker.webp#right)  
Bugbear stalkers frequently take their victims hostage, relishing opportunities to imprison and terrorize other creatures.

## Bugbears

*Lurking Goblinoid Brutes*

- **Habitat.** Forest, Grassland, Planar (Feywild), Underdark  
- **Treasure.** Armaments, Individual  

Bugbears embody fear of the wilds and the menace of natural places. They're notoriously stealthy, and foes that venture into their territories often vanish without a trace.
## Statblock

```statblock
"name": "Bugbear Stalker (XMM)"
"size": "Medium"
"type": "fey"
"subtype": "goblinoid"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"hp": !!int "65"
"hit_dice": "10d8 + 20"
"stats":
- !!int "17"
- !!int "14"
- !!int "14"
- !!int "11"
- !!int "12"
- !!int "11"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "3"
  "Constitution": !!int "4"
"skillsaves":
  "Stealth": !!int "6"
  "Survival": !!int "3"
"senses": "darkvision 60 ft., passive Perception 11"
"languages": "Common, Goblin"
"cr": "3"
"traits":
- "desc": "The bugbear needn't spend extra movement to move a creature it is grappling."
  "name": "Abduct"
"actions":
- "desc": "The bugbear makes two Javelin or Morningstar attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Attack: +5, reach 10 ft. or range 30/120 ft. Hit:\
    \ 13 (3d6 + 3) Piercing damage."
  "name": "Javelin"
- "desc": "Melee Attack: +5 (with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ if the target is [Grappled](Compendium/rules/conditions.md#Grappled) by the\
    \ bugbear), reach 10 ft. Hit: 12 (2d8 + 3) Piercing damage."
  "name": "Morningstar"
"bonus_actions":
- "desc": "Dexterity Saving Throw: DC 13, one Medium or smaller creature the bugbear\
    \ can see within 10 feet. Failure: The target has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 13)."
  "name": "Quick Grapple"
"source":
- "XMM"
```
^statblock