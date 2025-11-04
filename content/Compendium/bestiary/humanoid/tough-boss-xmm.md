---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Tough Boss"]
---
# Tough Boss
*Source: Monster Manual (2024) p. 307*  

![](Compendium/bestiary/humanoid/img/tough-boss.webp#right)  
Tough bosses leverage their street smarts, brawling prowess, and reputation to compel others to follow their demands.

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
"name": "Tough Boss (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "16"
"hp": !!int "82"
"hit_dice": "11d8 + 33"
"stats":
- !!int "17"
- !!int "14"
- !!int "16"
- !!int "11"
- !!int "10"
- !!int "11"
"speed": "30 ft."
"saves":
  "Charisma": !!int "2"
  "Strength": !!int "5"
  "Constitution": !!int "5"
"senses": "passive Perception 10"
"languages": "Common plus one other language"
"cr": "4"
"traits":
- "desc": "The tough has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the tough's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "The tough makes two attacks, using Warhammer or Heavy Crossbow in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 12 (2d8 + 3) Bludgeoning damage.\
    \ If the target is a Large or smaller creature, the tough pushes the target up\
    \ to 10 feet straight away from itself."
  "name": "Warhammer"
- "desc": "Ranged Attack: +4, range 100/400 ft. Hit: 13 (2d10 + 2) Piercing\
    \ damage."
  "name": "Heavy Crossbow"
"source":
- "XMM"
```
^statblock