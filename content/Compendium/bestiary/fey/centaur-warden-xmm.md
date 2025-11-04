---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Centaur Warden"]
---
# Centaur Warden
*Source: Monster Manual (2024) p. 67*  

![](Compendium/bestiary/fey/img/centaur-warden.webp#right)  
Centaur wardens often lead groups of centaur troopers and act as intermediaries between Fey creatures and trespassers into their territories.

## Centaurs

*Defenders of the Feywild*

- **Habitat.** Forest, Grassland, Planar (Feywild)  
- **Treasure.** Armaments, Individual  

Centaurs are defenders of forests, plains, and sites of primeval power. With upper bodies like humans' and the lower bodies of horses, centaurs charge into battle against those who would harm their allies.
## Statblock

```statblock
"name": "Centaur Warden (XMM)"
"size": "Large"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "16"
"hp": !!int "105"
"hit_dice": "14d10 + 28"
"stats":
- !!int "18"
- !!int "14"
- !!int "14"
- !!int "9"
- !!int "18"
- !!int "11"
"speed": "50 ft."
"saves":
  "Wisdom": !!int "7"
  "Constitution": !!int "5"
"skillsaves":
  "Nature": !!int "5"
  "Athletics": !!int "7"
  "Perception": !!int "7"
"senses": "passive Perception 17"
"languages": "Druidic, Elvish, Sylvan"
"cr": "7"
"traits":
- "desc": "The centaur casts one of the following spells, using Wisdom as the spellcasting\
    \ ability (spell save DC 15):\n\nAt will: [Druidcraft](Compendium/spells/druidcraft-xphb.md),\
    \ [Speak with Animals](Compendium/spells/speak-with-animals-xphb.md)"
  "name": "Spellcasting"
"actions":
- "desc": "The centaur makes two attacks, using Forest Staff or Sun Ray in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 5 ft. Hit: 13 (2d8 + 4) Bludgeoning damage\
    \ plus 14 (4d6) Poison damage."
  "name": "Forest Staff"
- "desc": "Ranged Attack: +7, range 90 ft. Hit: 14 (3d6 + 4) Radiant damage,\
    \ and the target has the [Blinded](Compendium/rules/conditions.md#Blinded) condition\
    \ until the start of the centaur's next turn."
  "name": "Sun Ray"
"bonus_actions":
- "desc": "The centaur moves up to its [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ without provoking Opportunity Attacks. Each creature within 5 feet of the centaur\
    \ as it moves is targeted once by the following effect. Strength Saving Throw:\
    \ DC 15. Failure: 11 (2d6 + 4) Bludgeoning damage, and the target has the\
    \ [Restrained](Compendium/rules/conditions.md#Restrained) condition until the\
    \ end of its next turn."
  "name": "Entangling Trail (Recharge 5-6)"
"source":
- "XMM"
```
^statblock