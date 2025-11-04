---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Cyclops Oracle"]
---
# Cyclops Oracle
*Source: Monster Manual (2024) p. 88*  

![](Compendium/bestiary/giant/img/cyclops-oracle.webp#right)  
Cyclops oracles gaze through history to learn hidden truths. Many share these secrets with those who aid them in correcting the mistakes of the past.

## Cyclopes

*Monocular Servants of Destiny*

- **Habitat.** Coastal, Desert, Grassland, Hill, Mountain, Underdark  
- **Treasure.** Armaments  

Cyclopes are gigantic, one-eyed descendants of the gods. Using their mystical vision, cyclopes can witness how future events are likely to occur.
## Statblock

```statblock
"name": "Cyclops Oracle (XMM)"
"size": "Huge"
"type": "giant"
"alignment": "Chaotic Neutral"
"ac": !!int "16"
"hp": !!int "207"
"hit_dice": "18d12 + 90"
"stats":
- !!int "22"
- !!int "11"
- !!int "20"
- !!int "16"
- !!int "18"
- !!int "10"
"speed": "40 ft."
"saves":
  "Wisdom": !!int "8"
  "Constitution": !!int "9"
"skillsaves":
  "Perception": !!int "12"
  "History": !!int "11"
"senses": "truesight 30 ft., passive Perception 22"
"languages": "Giant"
"cr": "10"
"traits":
- "desc": "The cyclops casts one of the following spells, requiring no Material components\
    \ and using Wisdom as the spellcasting ability (spell save DC 16):\n\n1/day:\
    \ [Legend Lore](Compendium/spells/legend-lore-xphb.md)\n\n2/day each: [Arcane\
    \ Eye](Compendium/spells/arcane-eye-xphb.md), [Detect Magic](Compendium/spells/detect-magic-xphb.md),\
    \ [Locate Object](Compendium/spells/locate-object-xphb.md)"
  "name": "Spellcasting"
"actions":
- "desc": "The cyclops makes three attacks, using Radiant Strike or Flash of Light\
    \ in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +10, reach 10 ft. Hit: 22 (3d10 + 6) Radiant damage."
  "name": "Radiant Strike"
- "desc": "Ranged Attack: +10, range 120 ft. Hit: 17 (2d10 + 6) Radiant damage,\
    \ and the target has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)\
    \ on attack rolls until the end of the cyclops's next turn."
  "name": "Flash of Light"
"reactions":
- "desc": "Trigger: The cyclops or an ally it can see makes a [D20 Test](Compendium/rules/variant-rules/d20-test-xphb.md).\
    \ Response: The cyclops rolls  and chooses whether to use that roll in place\
    \ of the d20 rolled for the [D20 Test](Compendium/rules/variant-rules/d20-test-xphb.md)."
  "name": "Portent (Recharge 4-6)"
"source":
- "XMM"
```
^statblock