---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/20
- ttrpg-cli/monster/environment/beastlands
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Animal Lord; Forager"]
---
# Animal Lord; Forager
*Source: Monster Manual (2024) p. 15*  

```statblock
"name": "Animal Lord; Forager (XMM)"
"size": "Medium"
"type": "celestial"
"alignment": "Neutral"
"ac": !!int "19"
"hp": !!int "323"
"hit_dice": "34d8 + 170"
"stats":
- !!int "24"
- !!int "25"
- !!int "20"
- !!int "19"
- !!int "23"
- !!int "22"
"speed": "60 ft., fly 60 ft. (hover), swim 60 ft."
"saves":
  "Wisdom": !!int "12"
  "Constitution": !!int "11"
"skillsaves":
  "Athletics": !!int "13"
  "Stealth": !!int "13"
  "Perception": !!int "18"
  "Acrobatics": !!int "13"
"damage_resistances": "cold, fire, necrotic, psychic, radiant"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened),\
  \ [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "truesight 120 ft., passive Perception 28"
"languages": "all"
"cr": "20"
"traits":
- "desc": "The animal lord casts one of the following spells, requiring no Material\
    \ components and using Wisdom as the spellcasting ability (spell save DC 20):\n\
    \nAt will: [Animal Friendship](Compendium/spells/animal-friendship-xphb.md),\
    \ [Animal Messenger](Compendium/spells/animal-messenger-xphb.md), [Speak with\
    \ Animals](Compendium/spells/speak-with-animals-xphb.md)\n\n1/day each: [Animal\
    \ Shapes](Compendium/spells/animal-shapes-xphb.md), [Sunburst](Compendium/spells/sunburst-xphb.md)\n\
    \n2/day each: [Awaken](Compendium/spells/awaken-xphb.md), [Greater Restoration](Compendium/spells/greater-restoration-xphb.md)"
  "name": "Spellcasting"
- "desc": "An animal lord represents a Forager, Hunter, or Sage (DM's choice), which\
    \ determines certain traits in this stat block."
  "name": "Animal Lordship"
- "desc": "If the animal lord fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (4/Day)"
- "desc": "Wisdom Saving Throw: DC 20, any enemy that starts its turn in a 30-foot\
    \ [Emanation [Area of Effect]](Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
    \ originating from the animal lord. Failure: The target has the [Charmed](Compendium/rules/conditions.md#Charmed)\
    \ condition until the end of its next turn. While [Charmed](Compendium/rules/conditions.md#Charmed),\
    \ the target has the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Lordly Presence"
- "desc": "The animal lord has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on saving throws against spells and other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The animal lord makes two attacks, using Rend or Radiant Ray in any combination,\
    \ and uses Animal Spirit."
  "name": "Multiattack"
- "desc": "Melee Attack: +13, reach 5 ft. Hit: 14 (2d6 + 7) Slashing damage\
    \ plus 7 (2d6) Force damage."
  "name": "Rend"
- "desc": "Ranged Attack: +12, range 120 ft. Hit: 20 (4d6 + 6) Radiant damage."
  "name": "Radiant Ray"
- "desc": "The animal lord conjures an animal spirit that strikes at a creature and\
    \ then disappears. Dexterity Saving Throw: DC 20, one creature the animal lord\
    \ can see within 120 feet. Failure: 28 (4d10 + 6) Radiant damage. Success:\
    \ Half damage. Failure or Success: The animal lord gains 20 [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)."
  "name": "Animal Spirit"
"bonus_actions":
- "desc": "The animal lord shape-shifts into a Huge or smaller version of the animal\
    \ it represents or a Medium or Small Humanoid, or it returns to its true form.\
    \ Its game statistics, other than its size, are the same in each form. Any equipment\
    \ it is wearing or carrying isn't transformed."
  "name": "Shape-Shift"
"legendary_actions":
- "desc": "The animal lord moves up to its [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ without provoking Opportunity Attacks, and it makes one Rend attack."
  "name": "Feral Strike"
- "desc": "The animal lord makes one Radiant Ray attack."
  "name": "Radiant Strike"
"source":
- "XMM"
```
^statblock