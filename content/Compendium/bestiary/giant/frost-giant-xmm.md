---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Frost Giant"]
---
# Frost Giant
*Source: Monster Manual (2024) p. 124*  

![](Compendium/bestiary/giant/img/frost-giant.webp#right)  
## Frost Giant

*Giant of the Ice and Snow*

- **Habitat.** Arctic, Mountain  
- **Treasure.** Armaments  

From glacial mountain heights and vast tundras rise the homes of frost giants. These giants have skin and hair of icy hues. Their natural immunity to cold allows them to flourish in places inhospitable to most other creatures. They use this resilience to aid them when hunting and in combat, bolstering their allies with chilling war cries.

Frost giants often travel far to find food and goods. This leads many to become raiders and earn violent reputations. Others live more peaceably by hunting titanic game or creating sanctuaries from the cold (frequently featuring hot springs or snowy contests). Frost giants sometimes forge partnerships with icy Fey or fire giants dwelling underground, serving as guardians to their realms in exchange for treasure, weapons, and crafts.

> [!quote] A quote from Jarl Grugnur, Frost Giant  
> 
> The small folk have barely anything worth looting, so they shouldn't much mind when we take it from them.

```statblock
"name": "Frost Giant (XMM)"
"size": "Huge"
"type": "giant"
"alignment": "Neutral Evil"
"ac": !!int "15"
"hp": !!int "149"
"hit_dice": "13d12 + 65"
"stats":
- !!int "23"
- !!int "9"
- !!int "21"
- !!int "9"
- !!int "10"
- !!int "12"
"speed": "40 ft."
"saves":
  "Charisma": !!int "4"
  "Wisdom": !!int "3"
  "Constitution": !!int "8"
"skillsaves":
  "Athletics": !!int "9"
  "Perception": !!int "3"
"damage_immunities": "cold"
"senses": "passive Perception 13"
"languages": "Giant"
"cr": "8"
"actions":
- "desc": "The giant makes two attacks, using Frost Axe or Great Bow in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +9, reach 10 ft. Hit: 19 (2d12 + 6) Slashing damage\
    \ plus 9 (2d8) Cold damage."
  "name": "Frost Axe"
- "desc": "Ranged Attack: +9, range 150/600 ft. Hit: 17 (2d10 + 6) Piercing\
    \ damage plus 7 (2d6) Cold damage, and the target's [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ decreases by 10 feet until the end of its next turn."
  "name": "Great Bow"
"bonus_actions":
- "desc": "The giant or one creature of its choice that can see or hear it gains 16\
    \ (2d10 + 5) [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
    \ and has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on attack\
    \ rolls until the start of the giant's next turn."
  "name": "War Cry (Recharge 5-6)"
"source":
- "XMM"
```
^statblock