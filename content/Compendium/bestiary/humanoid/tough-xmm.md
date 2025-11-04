---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Tough"]
---
# Tough
*Source: Monster Manual (2024) p. 307*  

![](Compendium/bestiary/humanoid/img/tough.webp#right)  
Toughs might work in groups at the direction of a leader, or individual toughs might bully weaker folk into doing what they say.

## Toughs

*Brawlers and Bullies*

- **Habitat.** Any  
- **Treasure.** Armaments  

Bodyguards, belligerents, and laborers, toughs rely on their physical strength to intimidate foes. They might be brawny criminals, rowdy tavern goers, seasoned workers, or anyone who uses their muscle to get what they want.

> [!quote]  
> 
> There are two answers to every question: ours, and the wrong one.

## Statblock

```statblock
"name": "Tough (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "12"
"hp": !!int "32"
"hit_dice": "5d8 + 10"
"stats":
- !!int "15"
- !!int "12"
- !!int "14"
- !!int "10"
- !!int "10"
- !!int "11"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common"
"cr": "1/2"
"traits":
- "desc": "The tough has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the tough's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 5 (1d6 + 2) Bludgeoning damage."
  "name": "Mace"
- "desc": "Ranged Attack: +3, range 100/400 ft. Hit: 6 (1d10 + 1) Piercing\
    \ damage."
  "name": "Heavy Crossbow"
"source":
- "XMM"
```
^statblock