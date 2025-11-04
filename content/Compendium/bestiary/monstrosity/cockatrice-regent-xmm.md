---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Cockatrice Regent"]
---
# Cockatrice Regent
*Source: Monster Manual (2024) p. 75*  

![](Compendium/bestiary/monstrosity/img/cockatrice-regent.webp#right)  
Bolder than their smaller cousins, cockatrice regents brim with unstable magical energy they use to restrain distant foes.

## Cockatrices

*Accursed Avians with the Power to Petrify*

- **Habitat.** Grassland  
- **Treasure.** None  

Cockatrices combine the features of irate roosters and starving reptiles. They petrify those they bite, their slightest peck turning their prey to stone.
## Statblock

```statblock
"name": "Cockatrice Regent (XMM)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"stats":
- !!int "19"
- !!int "14"
- !!int "16"
- !!int "3"
- !!int "16"
- !!int "5"
"speed": "30 ft., fly 60 ft."
"saves":
  "Wisdom": !!int "6"
"condition_immunities": "[petrified](Compendium/rules/conditions.md#Petrified)"
"senses": "darkvision 120 ft., passive Perception 13"
"languages": ""
"cr": "8"
"traits":
- "desc": "The cockatrice doesn't provoke an Opportunity Attack when it flies out\
    \ of an enemy's reach."
  "name": "Flyby"
"actions":
- "desc": "The cockatrice makes one Petrifying Bite attack and two Talons attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 5 ft. Hit: 13 (2d8 + 4) Piercing damage.\
    \ If the target is a creature, it is subjected to the following effect. Constitution\
    \ Saving Throw: DC 14. {@actSaveFail 1} The target has the [Restrained](Compendium/rules/conditions.md#Restrained)\
    \ condition and repeats the save at the end of its next turn if it is still [Restrained](Compendium/rules/conditions.md#Restrained),\
    \ ending the effect on itself on a success. {@actSaveFail 2} The target has the\
    \ [Petrified](Compendium/rules/conditions.md#Petrified) condition instead of the\
    \ [Restrained](Compendium/rules/conditions.md#Restrained) condition."
  "name": "Petrifying Bite"
- "desc": "Melee Attack: +7, reach 5 ft. Hit: 18 (4d6 + 4) Slashing damage."
  "name": "Talons"
"reactions":
- "desc": "Trigger: A creature within 120 feet of the cockatrice deals damage to it.\
    \ {@actResponse d}Dexterity Saving Throw: DC 14, the triggering creature. Failure:\
    \ 13 (3d6 + 3) Force damage."
  "name": "Magical Backlash"
"source":
- "XMM"
```
^statblock