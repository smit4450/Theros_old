---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Scout Captain"]
---
# Scout Captain
*Source: Monster Manual (2024) p. 270*  

![](Compendium/bestiary/humanoid/img/scout-captain.webp#right)  
Scout captains are experienced explorers and sharpshooters. They might lead bands of other scouts or disappear into the wilds alone for months at a time.

## Scouts

*Watchers and Wanderers*

- **Habitat.** Any  
- **Treasure.** Implements, Individual  

Scouts are warriors of the wilderness, trained in hunting and tracking. They might be explorers or trappers, or they could perform more martial roles as archers, bounty hunters, or outriders.
## Statblock

```statblock
"name": "Scout Captain (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "66"
"hit_dice": "12d8 + 12"
"stats":
- !!int "11"
- !!int "16"
- !!int "12"
- !!int "14"
- !!int "15"
- !!int "11"
"speed": "30 ft., climb 30 ft."
"saves":
  "Dexterity": !!int "5"
  "Intelligence": !!int "4"
"skillsaves":
  "Stealth": !!int "7"
  "Perception": !!int "6"
  "Survival": !!int "6"
"senses": "passive Perception 16"
"languages": "Common plus one other language"
"cr": "3"
"actions":
- "desc": "The scout makes two attacks, using Shortsword or Longbow in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 6 (1d6 + 3) Piercing damage,\
    \ plus 10 (3d6) Piercing damage if the attack was made with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)."
  "name": "Shortsword"
- "desc": "Ranged Attack: +5, range 150/600 ft. Hit: 7 (1d8 + 3) Piercing\
    \ damage, plus 10 (3d6) Piercing damage if the attack was made with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)."
  "name": "Longbow"
"bonus_actions":
- "desc": "The scout has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on the next attack roll it makes during the current turn."
  "name": "Aim"
"reactions":
- "desc": "Trigger: The scout is hit by an attack roll. Response: The scout halves\
    \ the damage (round down) it takes from that attack."
  "name": "Uncanny Dodge"
"source":
- "XMM"
```
^statblock