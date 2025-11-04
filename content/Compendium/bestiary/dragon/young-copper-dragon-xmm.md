---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Young Copper Dragon"]
---
# Young Copper Dragon
*Source: Monster Manual (2024) p. 78*  

![](Compendium/bestiary/dragon/img/young-copper-dragon.webp#right)  
Young copper dragons forge strong connections with a community or group of friends while flitting from one artistic fixation to the next.

## Copper Dragons

*Dragons of Curiosity and Community*

- **Habitat.** Hill  
- **Treasure.** Arcana  

Relentlessly friendly and curious, most copper dragons view the world as a place of endless wonder and possibility. These gregarious dragons are fonts of patience, hospitality, and humor, and they seek to improve the lives—or, at least, the mood—of those they interact with. If forced to fight to defend themselves or their friends, these dragons favor using their slowing breath and physical attacks to subdue antagonists. Only in cases of extreme peril or emotion do they use their deadly acid breath.

Copper dragons typically live in caverns amid picturesque hills and rock formations—particularly those that are prominent landmarks. These dragons collect gifts, though they have little interest in treasure without meaning, no matter how valuable it is. To them, thoughtfully given presents and the feelings or memories they symbolize are more important than masterpieces or magical relics.

### Copper Dragon Lairs

Copper dragons typically inhabit multichamber caves and renovated ruins.
## Statblock

```statblock
"name": "Young Copper Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Chaotic Good"
"ac": !!int "17"
"hp": !!int "119"
"hit_dice": "14d10 + 42"
"stats":
- !!int "19"
- !!int "12"
- !!int "17"
- !!int "16"
- !!int "13"
- !!int "15"
"speed": "40 ft., climb 40 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "4"
"skillsaves":
  "Deception": !!int "5"
  "Stealth": !!int "4"
  "Perception": !!int "7"
"damage_immunities": "acid"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 17"
"languages": "Common, Draconic"
"cr": "7"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace one attack with a use\
    \ of Slowing Breath."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 10 ft. Hit: 15 (2d10 + 4) Slashing damage."
  "name": "Rend"
- "desc": "Dexterity Saving Throw: DC 14, each creature in a 40-foot-long, 5-foot-wide\
    \ [Line [Area of Effect]](Compendium/rules/variant-rules/line-area-of-effect-xphb.md).\
    \ Failure: 40 (9d8) Acid damage. Success: Half damage."
  "name": "Acid Breath (Recharge 5-6)"
- "desc": "Constitution Saving Throw: DC 14, each creature in a 30-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ The target can't take Reactions; its [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ is halved; and it can take either an action or a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md)\
    \ on its turn, not both. This effect lasts until the end of its next turn."
  "name": "Slowing Breath"
"source":
- "XMM"
```
^statblock