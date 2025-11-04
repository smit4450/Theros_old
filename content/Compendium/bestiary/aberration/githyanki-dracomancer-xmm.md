---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/16
- ttrpg-cli/monster/environment/astral
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/aberration/gith
statblock: inline
aliases: ["Githyanki Dracomancer"]
---
# Githyanki Dracomancer
*Source: Monster Manual (2024) p. 135*  

![](Compendium/bestiary/aberration/img/githyanki-dracomancer.webp#right)  
One of Gith's last deeds was to forge an alliance between the githyanki and the dragon god Tiamat. Ever since, the Dragon Queen's red dragon consort, Ephelomon, and his kind have been allies of the githyanki. Githyanki dracomancers uphold this pact and cultivate magic talents that complement the might of red dragons.

## Githyanki

*Invaders from the Astral Plane*

- **Habitat.** Planar (Astral Plane)  
- **Treasure.** Armaments  

Githyanki were once an ordinary people, but the deeds of a vile mind flayer empire etched conflict on their being. Gaunt, humanlike creatures, githyanki have serrated ears and speckled skin ranging through shades of yellow, green, and brown. While some githyanki follow their own paths, many are influenced by a past that forever altered their fates.

### History of the Gith

Ages ago, a humanlike people were conquered by an empire of mind flayers. The illithids manipulated this forgotten people through untold horrors, forced evolution, and psychic reshaping. Eventually one named Gith rose from among the captives and led a rebellion against their oppressors. Gith's followers, who became known as the gith, defeated the mind flayers and shattered their vast empire.

The victory of the gith was short-lived. As Gith was forging her own burgeoning empire, a leader named Zerthimon challenged her. Zerthimon claimed Gith's drive for vengeance and new conquests was evidence of species-wide mental programing laid by the mind flayers, biological manipulation that condemned her people to continued servitude. This claim split the gith into Gith's followers, the githyanki (meaning "followers of Gith"), and Zerthimon's followers, the githzerai (meaning "those who spurn Gith"), and sparked an ongoing conflict.

When Gith perished, her adviser, Vlaakith, assumed rule of the githyanki. Vlaakith's line has continued to the githyanki's current ruler, Vlaakith the Lich-Queen. This undead tyrant compels her people to wage endless wars against mind flayers, githzerai, and any others that threaten githyanki supremacy.
## Statblock

```statblock
"name": "Githyanki Dracomancer (XMM)"
"size": "Medium"
"type": "aberration"
"subtype": "gith"
"alignment": "Lawful Evil"
"ac": !!int "18"
"hp": !!int "255"
"hit_dice": "30d8 + 120"
"stats":
- !!int "10"
- !!int "16"
- !!int "18"
- !!int "20"
- !!int "16"
- !!int "18"
"speed": "30 ft., fly 30 ft. (hover)"
"saves":
  "Dexterity": !!int "8"
  "Wisdom": !!int "8"
  "Intelligence": !!int "10"
  "Constitution": !!int "9"
"skillsaves":
  "Perception": !!int "8"
  "Arcana": !!int "10"
"senses": "blindsight 30 ft., passive Perception 18"
"languages": "Common, Draconic, Gith"
"cr": "16"
"traits":
- "desc": "The githyanki casts one of the following spells, requiring no spell components\
    \ and using Intelligence as the spellcasting ability (spell save DC 18, +10\
    \ to hit with spell attacks):\n\nAt will: [Mage Hand](Compendium/spells/mage-hand-xphb.md)\
    \ (the hand is Invisible)\n\n2/day each: [Nondetection](Compendium/spells/nondetection-xphb.md)\
    \ (self only), [Plane Shift](Compendium/spells/plane-shift-xphb.md), [Tongues](Compendium/spells/tongues-xphb.md)"
  "name": "Spellcasting"
- "desc": "The githyanki casts [Misty Step](Compendium/spells/misty-step-xphb.md),\
    \ requiring no spell components and using the same spellcasting ability as Spellcasting.\n\
    \n3/day: [Misty Step](Compendium/spells/misty-step-xphb.md)"
  "name": "Misty Step (3/Day)"
"actions":
- "desc": "The githyanki makes three Draconic Strike attacks."
  "name": "Multiattack"
- "desc": "Melee or Ranged Attack: +10, reach 10 ft. or range 120 ft. Hit: 12\
    \ (2d6 + 5) Slashing damage plus 17 (5d6) Fire damage, and the target has\
    \ the [Frightened](Compendium/rules/conditions.md#Frightened) condition until\
    \ the start of the githyanki's next turn."
  "name": "Draconic Strike"
- "desc": "Dexterity Saving Throw: DC 18, each creature in a 90-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 27 (6d8) Fire damage plus 27 (6d8) Force damage. Success: Half damage."
  "name": "Conjured Dragon's Breath (Recharge 5-6)"
"source":
- "XMM"
```
^statblock