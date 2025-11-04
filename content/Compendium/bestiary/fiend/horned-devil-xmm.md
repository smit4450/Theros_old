---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/11
- ttrpg-cli/monster/environment/nine-hells
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Horned Devil"]
---
# Horned Devil
*Source: Monster Manual (2024) p. 174*  

![](Compendium/bestiary/fiend/img/horned-devil.webp#right)  
## Horned Devil

*Devil of Hatred and Subjugation*

- **Habitat.** Planar (Nine Hells)  
- **Treasure.** Relics  

Horned devils, also known as cornugons or malebranche, are infernal warriors that exact the will of diabolical generals and lead other devils in battle. Their bodies and weapons are forged in the Nine Hells, and they torment their foes with diabolical flames and pernicious wounds.
```statblock
"name": "Horned Devil (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "18"
"hp": !!int "199"
"hit_dice": "19d10 + 95"
"stats":
- !!int "22"
- !!int "17"
- !!int "21"
- !!int "12"
- !!int "16"
- !!int "18"
"speed": "30 ft., fly 60 ft."
"saves":
  "Charisma": !!int "8"
  "Dexterity": !!int "7"
  "Wisdom": !!int "7"
  "Strength": !!int "10"
"damage_immunities": "fire, poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "darkvision 150 ft. (unimpeded by magical darkness), passive Perception\
  \ 13"
"languages": "Infernal; telepathy 120 ft."
"cr": "11"
"traits":
- "desc": "If the devil dies outside the Nine Hells, its body disappears in sulfurous\
    \ smoke, and it gains a new body instantly, reviving with all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
    \ somewhere in the Nine Hells."
  "name": "Diabolical Restoration"
- "desc": "The devil has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on saving throws against spells and other magical effects."
  "name": "Magic Resistance"
"actions":
- "desc": "The devil makes three attacks, using Searing Fork or Hurl Flame in any\
    \ combination. It can replace one attack with a use of Infernal Tail."
  "name": "Multiattack"
- "desc": "Melee Attack: +10, reach 10 ft. Hit: 15 (2d8 + 6) Piercing damage\
    \ plus 9 (2d8) Fire damage."
  "name": "Searing Fork"
- "desc": "Ranged Attack: +8, range 150 ft. Hit: 26 (5d8 + 4) Fire damage.\
    \ If the target is a flammable object that isn't being worn or carried, it starts\
    \ burning."
  "name": "Hurl Flame"
- "desc": "Dexterity Saving Throw: DC 17, one creature the devil can see within\
    \ 10 feet. Failure: 10 (1d8 + 6) Necrotic damage, and the target receives\
    \ an infernal wound if it doesn't have one. While wounded, the target loses 10\
    \ (3d6) [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) at the\
    \ start of each of its turns. The wound closes after 1 minute, after a spell restores\
    \ [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) to the target,\
    \ or after the target or a creature within 5 feet of it takes an action to stanch\
    \ the wound, doing so by succeeding on a DC 17 Wisdom ([Medicine](Compendium/rules/skills.md#Medicine))\
    \ check."
  "name": "Infernal Tail"
"source":
- "XMM"
```
^statblock