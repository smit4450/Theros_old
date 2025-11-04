---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Mage Apprentice"]
---
# Mage Apprentice
*Source: Monster Manual (2024) p. 198*  

![](Compendium/bestiary/humanoid/img/mage-apprentice.webp#right)  
Mage apprentices are spellcasters of humble skill. Some are students of accomplished mages, while others have innate powers.

## Mages

*Magical Scholars and Spellcasters*

- **Habitat.** Any  
- **Treasure.** Arcana, Individual  

Mages are magical wonder-workers, ranging from spellcasting overlords to reclusive witches. They study mystical secrets and possess insight into monsters, legends, omens, and other lore. Mages often gather allies or hire assistants to aid them in their research or to attain magical might.

Roll on or choose a result from the Mage Roles table to inspire different sorts of mages.

**Mage Roles**

`dice: [](mage-apprentice-xmm.md#^mage-roles)`

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
"name": "Mage Apprentice (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "15"
"hp": !!int "49"
"hit_dice": "9d8 + 9"
"stats":
- !!int "8"
- !!int "14"
- !!int "12"
- !!int "16"
- !!int "13"
- !!int "10"
"speed": "30 ft."
"saves":
  "Wisdom": !!int "3"
  "Intelligence": !!int "5"
"skillsaves":
  "Perception": !!int "3"
  "Arcana": !!int "5"
"senses": "passive Perception 13"
"languages": "Common plus one other language"
"cr": "2"
"traits":
- "desc": "The mage casts one of the following spells, using Intelligence as the spellcasting\
    \ ability (spell save DC 13, +5 to hit with spell attacks):\n\nAt will:\
    \ [Mage Hand](Compendium/spells/mage-hand-xphb.md), [Prestidigitation](Compendium/spells/prestidigitation-xphb.md)\n\
    \n1/day each: [Disguise Self](Compendium/spells/disguise-self-xphb.md), [Ice\
    \ Knife](Compendium/spells/ice-knife-xphb.md), [Mage Armor](Compendium/spells/mage-armor-xphb.md)\
    \ (included in AC), [Thunderwave](Compendium/spells/thunderwave-xphb.md)"
  "name": "Spellcasting"
"actions":
- "desc": "Melee or Ranged Attack: +5, reach 5 ft. or range 120 ft. Hit: 14\
    \ (2d10 + 3) Force damage."
  "name": "Arcane Burst"
"source":
- "XMM"
```
^statblock