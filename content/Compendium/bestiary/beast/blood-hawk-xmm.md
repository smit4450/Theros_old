---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Blood Hawk"]
---
# Blood Hawk
*Source: Monster Manual (2024) p. 350*  

![](Compendium/bestiary/beast/img/blood-hawk.webp#center)  
```statblock
"name": "Blood Hawk (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "7"
"hit_dice": "2d6"
"stats":
- !!int "6"
- !!int "14"
- !!int "10"
- !!int "3"
- !!int "14"
- !!int "5"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  "Perception": !!int "6"
"senses": "passive Perception 16"
"languages": ""
"cr": "1/8"
"traits":
- "desc": "The hawk has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the hawk's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 4 (1d4 + 2) Piercing damage,\
    \ or 6 (1d8 + 2) Piercing damage if the target is [Bloodied](Compendium/rules/variant-rules/bloodied-xphb.md)."
  "name": "Beak"
"source":
- "XMM"
```
^statblock