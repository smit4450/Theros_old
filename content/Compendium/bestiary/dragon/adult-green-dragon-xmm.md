---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/15
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon/chromatic
statblock: inline
aliases: ["Adult Green Dragon"]
---
# Adult Green Dragon
*Source: Monster Manual (2024) p. 153*  

![](Compendium/bestiary/dragon/img/adult-green-dragon.webp#right)  
The words of adult green dragons are as deadly as their poisonous breath. They are brilliant schemers that pride themselves on influencing communities near their lairs. They obsess over information and create vast spy networks. Many of these dragons seek magical methods of surveillance or domination, and they manipulate adventurers into hunting down lost magic to aid in such control.

## Green Dragons

*Dragons of Deceit and Derision*

- **Habitat.** Forest  
- **Treasure.** Arcana  

From forbidden forest depths, green dragons whisper evils into the world and manipulate the lives of those who listen. Elusive, conniving, and egotistical, these chromatic dragons patiently prey on the fears of shorter-lived beings, corrupting and isolating them. Green dragons might lurk amid labyrinthine wildernesses for centuries without revealing themselves; even their most devoted followers might know them only as the voice of the woodlands or a whisper in their dreams.

Despite their might, most green dragons disdain physical violence, viewing combat as servants' work and preferring to trick foes into dangerous or exploitative scenarios. These dragons collect "baubles" that embody their webs of manipulation and serve as tools of extortion, such as compromising documents, family heirlooms, and sentimental treasures.

### Green Dragon Lairs

Green dragons lair in ancient forests, often shaping stands of massive trees into compounds of interwoven branches, hollow trunks, and caverns amid mighty roots. They might also dwell amid forested ruins, particularly the former homes of those they've conquered.
## Statblock

```statblock
"name": "Adult Green Dragon (XMM)"
"size": "Huge"
"type": "dragon"
"subtype": "chromatic"
"alignment": "Lawful Evil"
"ac": !!int "19"
"hp": !!int "207"
"hit_dice": "18d12 + 90"
"stats":
- !!int "23"
- !!int "12"
- !!int "21"
- !!int "18"
- !!int "15"
- !!int "18"
"speed": "40 ft., fly 80 ft., swim 40 ft."
"saves":
  "Dexterity": !!int "6"
  "Wisdom": !!int "7"
"skillsaves":
  "Deception": !!int "9"
  "Stealth": !!int "6"
  "Perception": !!int "12"
  "Persuasion": !!int "9"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 22"
"languages": "Common, Draconic"
"cr": "15"
"traits":
- "desc": "The dragon casts one of the following spells, requiring no Material components\
    \ and using Charisma as the spellcasting ability (spell save DC 17):\n\nAt will:\
    \ [Detect Magic](Compendium/spells/detect-magic-xphb.md), [Mind Spike](Compendium/spells/mind-spike-xphb.md)\
    \ (level 3 version)\n\n1/day: [Geas](Compendium/spells/geas-xphb.md)"
  "name": "Spellcasting"
- "desc": "The dragon can breathe air and water."
  "name": "Amphibious"
- "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day, or 4/Day in Lair)"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace one attack with a use\
    \ of Spellcasting to cast [Mind Spike](Compendium/spells/mind-spike-xphb.md) (level\
    \ 3 version)."
  "name": "Multiattack"
- "desc": "Melee Attack: +11, reach 10 ft. Hit: 15 (2d8 + 6) Slashing damage\
    \ plus 7 (2d6) Poison damage."
  "name": "Rend"
- "desc": "Constitution Saving Throw: DC 18, each creature in a 60-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 56 (16d6) Poison damage. Success: Half damage."
  "name": "Poison Breath (Recharge 5-6)"
"legendary_actions":
- "desc": "The dragon uses Spellcasting to cast [Mind Spike](Compendium/spells/mind-spike-xphb.md)\
    \ (level 3 version)."
  "name": "Mind Invasion"
- "desc": "Constitution Saving Throw: DC 17, each creature in a 20-foot-radius [Sphere\
    \ [Area of Effect]](Compendium/rules/variant-rules/sphere-area-of-effect-xphb.md)\
    \ centered on a point the dragon can see within 90 feet. Failure: 7 (2d6)\
    \ Poison damage, and the target takes a -2 penalty to AC until the end of its\
    \ next turn. Failure or Success: The dragon can't take this action again until\
    \ the start of its next turn."
  "name": "Noxious Miasma"
- "desc": "The dragon moves up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md),\
    \ and it makes one Rend attack."
  "name": "Pounce"
"regional_effects":
- "desc": "The region containing an adult or ancient green dragon's lair is warped\
    \ by its presence, creating the following effects:"
  "name": ""
- "desc": "- Beast Spies. Tiny Beasts magically gain the ability to understand\
    \ Draconic and can communicate telepathically with the dragon while within 1 mile\
    \ of the lair.  \n- Poisonous Thicket. Ordinary plants growing within 1 mile\
    \ of the lair poison the air around them. Whenever a creature other than the dragon\
    \ or its allies finishes a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md)\
    \ in that area, it must succeed on a DC 15 Constitution saving throw or have the\
    \ [Poisoned](Compendium/rules/conditions.md#Poisoned) condition for 1 hour.  "
  "name": ""
- "desc": "If the dragon dies or moves its lair elsewhere, these effects end immediately."
  "name": ""
"source":
- "XMM"
```
^statblock