---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Mage"]
---
# Mage
*Source: Monster Manual (2024) p. 199*  

![](Compendium/bestiary/humanoid/img/mage.webp#right)  
Mages are accomplished spellcasters whose lives have been shaped by magic. They can use their powers to defend or dominate other creatures, or they could focus on magical research and unlocking mystical secrets.

## Mages

*Magical Scholars and Spellcasters*

- **Habitat.** Any  
- **Treasure.** Arcana, Individual  

Mages are magical wonder-workers, ranging from spellcasting overlords to reclusive witches. They study mystical secrets and possess insight into monsters, legends, omens, and other lore. Mages often gather allies or hire assistants to aid them in their research or to attain magical might.

Roll on or choose a result from the Mage Roles table to inspire different sorts of mages.

**Mage Roles**

`dice: [](mage-xmm.md#^mage-roles)`

| dice: 1d10 | The Mage Is... |
|------------|----------------|
| 1 | An astronomer who draws magic from stars. |
| 2 | An author who writes about the occult. |
| 3 | A magical engineer who creates wonders. |
| 4 | An oracle who interprets omens. |
| 5 | A prodigy with a remarkable magical heritage. |
| 6 | A psion whose powers manifest as spells. |
| 7 | A scholar investigating ancient lore. |
| 8 | A soothsayer who advises rulers. |
| 9 | A war mage who aids soldiers in battle. |
| 10 | A witch who shares secret wisdom. |
^mage-roles

> [!quote] A quote from Nathor, Thayan Refugee  
> 
> Have you gazed on the Runes of Chaos, held the Death Moon Orb in your trembling hands, entered the Devouring Portal and walked the Paths of the Doomed, or sat at the left hand of Szass Tam during the Ritual of Twin Burnings? No? Then speak not to me of wizards. Speak not to me of Thay.

## Statblock

```statblock
"name": "Mage (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "81"
"hit_dice": "18d8"
"stats":
- !!int "9"
- !!int "14"
- !!int "11"
- !!int "17"
- !!int "12"
- !!int "11"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "4"
  "Intelligence": !!int "6"
"skillsaves":
  "Perception": !!int "4"
  "History": !!int "6"
  "Arcana": !!int "6"
"senses": "passive Perception 14"
"languages": "Common and any three languages"
"cr": "6"
"traits":
- "desc": "The mage casts one of the following spells, using Intelligence as the spellcasting\
    \ ability (spell save DC 14):\n\nAt will: [Detect Magic](Compendium/spells/detect-magic-xphb.md),\
    \ [Light](Compendium/spells/light-xphb.md), [Mage Armor](Compendium/spells/mage-armor-xphb.md)\
    \ (included in AC), [Mage Hand](Compendium/spells/mage-hand-xphb.md), [Prestidigitation](Compendium/spells/prestidigitation-xphb.md)\n\
    \n1/day each: [Cone of Cold](Compendium/spells/cone-of-cold-xphb.md), [Fly](Compendium/spells/fly-xphb.md)\n\
    \n2/day each: [Fireball](Compendium/spells/fireball-xphb.md) (level 4 version),\
    \ [Invisibility](Compendium/spells/invisibility-xphb.md)"
  "name": "Spellcasting"
- "desc": "The mage casts [Misty Step](Compendium/spells/misty-step-xphb.md), using\
    \ the same spellcasting ability as Spellcasting.\n\n3/day: [Misty Step](Compendium/spells/misty-step-xphb.md)"
  "name": "Misty Step (3/Day)"
- "desc": "The mage casts [Counterspell](Compendium/spells/counterspell-xphb.md) or\
    \ [Shield](Compendium/spells/shield-xphb.md) in response to the spell's trigger,\
    \ using the same spellcasting ability as Spellcasting.\n\n3/day: [Counterspell](Compendium/spells/counterspell-xphb.md),\
    \ [Shield](Compendium/spells/shield-xphb.md)"
  "name": "Protective Magic (3/Day)"
"actions":
- "desc": "The mage makes three Arcane Burst attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Attack: +6, reach 5 ft. or range 120 ft. Hit: 16\
    \ (3d8 + 3) Force damage."
  "name": "Arcane Burst"
"source":
- "XMM"
```
^statblock