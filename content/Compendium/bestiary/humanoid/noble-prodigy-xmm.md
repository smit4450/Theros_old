---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Noble Prodigy"]
---
# Noble Prodigy
*Source: Monster Manual (2024) p. 227*  

![](Compendium/bestiary/humanoid/img/noble-prodigy.webp#right)  
Noble prodigies trace their lineage to a legendary hero, a demigod, a dragon, or some other ancestor that grants them magical prowess. Among some nobles, the source of a prodigy's magic might be a family secret.

## Nobles

*Royals and Rich Folk*

- **Habitat.** Any  
- **Treasure.** Individual  

Nobles encompass a variety of people with social influence. They might be rulers, wealthy merchants, callous bureaucrats, or the idle elite.
## Statblock

```statblock
"name": "Noble Prodigy (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "16"
"hp": !!int "148"
"hit_dice": "27d8 + 27"
"stats":
- !!int "8"
- !!int "16"
- !!int "12"
- !!int "15"
- !!int "14"
- !!int "19"
"speed": "30 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "7"
  "Wisdom": !!int "6"
  "Constitution": !!int "5"
"skillsaves":
  "Perception": !!int "6"
  "Persuasion": !!int "8"
"senses": "passive Perception 16"
"languages": "Common plus two other languages"
"cr": "10"
"traits":
- "desc": "The noble casts one of the following spells, requiring no Material components\
    \ and using Charisma as the spellcasting ability (spell save DC 16):\n\nAt will:\
    \ [Mage Armor](Compendium/spells/mage-armor-xphb.md) (included in AC), [Mage Hand](Compendium/spells/mage-hand-xphb.md),\
    \ [Minor Illusion](Compendium/spells/minor-illusion-xphb.md)\n\n1/day each:\
    \ [Befuddlement](Compendium/spells/befuddlement-xphb.md), [Detect Thoughts](Compendium/spells/detect-thoughts-xphb.md),\
    \ [Fly](Compendium/spells/fly-xphb.md), [Scrying](Compendium/spells/scrying-xphb.md),\
    \ [Shatter](Compendium/spells/shatter-xphb.md) (level 7 version)"
  "name": "Spellcasting"
- "desc": "The noble casts [Shield](Compendium/spells/shield-xphb.md) in response\
    \ to that spell's trigger, using the same spellcasting ability as Spellcasting.\n\
    \n2/day: [Shield](Compendium/spells/shield-xphb.md)"
  "name": "Shield (2/Day)"
"actions":
- "desc": "The noble makes three Beguiling Strike attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Attack: +8, reach 5 ft. or range 60 ft. Hit: 18 (4d6\
    \ + 4) Psychic damage, and the target has the [Charmed](Compendium/rules/conditions.md#Charmed)\
    \ condition until the start of the noble's next turn."
  "name": "Beguiling Strike"
"source":
- "XMM"
```
^statblock