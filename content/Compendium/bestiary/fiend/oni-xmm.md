---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend
statblock: inline
aliases: ["Oni"]
---
# Oni
*Source: Monster Manual (2024) p. 232*  

![](Compendium/bestiary/fiend/img/oni.webp#right)  
## Oni

*Wickedness Drawn to the Wicked*

- **Habitat.** Forest, Urban  
- **Treasure.** Armaments  

Oni are elusive entities that inhabit dark forests and other wildernesses. By shape-shifting into the form of an innocent or moving invisibly, oni encroach on communities and lonely roads. They frequently harass people of faith, testing the limits of their piousness, or torment selfish people, punishing them for their wickedness. Wise communities often have guardian statues, annual rituals, or local superstitions meant to keep oni at bay. In rare cases, an oni might gradually befriend such communities and protect them from other threats for generations.

Oni torment villages that don't pay them or other supernatural forces respect. Roll on or choose a result from the Oni Troubles table to inspire how an oni menaces such communities.

**Oni Troubles**

`dice: [](oni-xmm.md#^oni-troubles)`

| dice: 1d4 | The Oni Torments People By... |
|-----------|-------------------------------|
| 1 | Charming people to perform nasty tricks. |
| 2 | Claiming a bridge, gate, shrine, or trail and trying to eat anyone who comes near. |
| 3 | Luring other monsters to the settlement. |
| 4 | Playing drums that keep everyone awake. |
^oni-troubles
```statblock
"name": "Oni (XMM)"
"size": "Large"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "119"
"hit_dice": "14d10 + 42"
"stats":
- !!int "19"
- !!int "11"
- !!int "16"
- !!int "14"
- !!int "12"
- !!int "15"
"speed": "30 ft., fly 30 ft. (hover)"
"saves":
  "Charisma": !!int "5"
  "Dexterity": !!int "3"
  "Wisdom": !!int "4"
  "Constitution": !!int "6"
"skillsaves":
  "Deception": !!int "8"
  "Perception": !!int "4"
  "Arcana": !!int "5"
"damage_resistances": "cold"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": "Common, Giant"
"cr": "7"
"traits":
- "desc": "The oni casts one of the following spells, requiring no Material components\
    \ and using Charisma as the spellcasting ability (spell save DC 13):\n\n1/day\
    \ each: [Charm Person](Compendium/spells/charm-person-xphb.md) (level 2 version),\
    \ [Darkness](Compendium/spells/darkness-xphb.md), [Gaseous Form](Compendium/spells/gaseous-form-xphb.md),\
    \ [Sleep](Compendium/spells/sleep-xphb.md)"
  "name": "Spellcasting"
- "desc": "The oni casts [Invisibility](Compendium/spells/invisibility-xphb.md) on\
    \ itself, requiring no spell components and using the same spellcasting ability\
    \ as Spellcasting.\n\nAt will: [Invisibility](Compendium/spells/invisibility-xphb.md)"
  "name": "Invisibility"
- "desc": "The oni regains 10 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
    \ at the start of each of its turns if it has at least 1 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
  "name": "Regeneration"
"actions":
- "desc": "The oni makes two Claw or Nightmare Ray attacks. It can replace one attack\
    \ with a use of Spellcasting."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 10 ft. Hit: 10 (1d12 + 4) Slashing damage\
    \ plus 9 (2d8) Necrotic damage."
  "name": "Claw"
- "desc": "Ranged Attack: +5, range 60 ft. Hit: 9 (2d6 + 2) Psychic damage,\
    \ and the target has the [Frightened](Compendium/rules/conditions.md#Frightened)\
    \ condition until the start of the oni's next turn."
  "name": "Nightmare Ray"
- "desc": "The oni shape-shifts into a Small or Medium Humanoid or a Large Giant,\
    \ or it returns to its true form. Other than its size, its game statistics are\
    \ the same in each form. Any equipment it is wearing or carrying isn't transformed."
  "name": "Shape-Shift"
"source":
- "XMM"
```
^statblock