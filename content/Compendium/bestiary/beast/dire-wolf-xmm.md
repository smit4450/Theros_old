---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Dire Wolf"]
---
# Dire Wolf
*Source: Monster Manual (2024) p. 352, Player's Handbook (2024) p. 348*  

![](Compendium/bestiary/beast/img/dire-wolf.webp#center)  
```statblock
"name": "Dire Wolf (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "22"
"hit_dice": "3d10 + 6"
"stats":
- !!int "17"
- !!int "15"
- !!int "15"
- !!int "3"
- !!int "12"
- !!int "7"
"speed": "50 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "5"
"senses": "darkvision 60 ft., passive Perception 15"
"languages": ""
"cr": "1"
"traits":
- "desc": "The wolf has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on an attack roll against a creature if at least one of the wolf's allies is\
    \ within 5 feet of the creature and the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition."
  "name": "Pack Tactics"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 8 (1d10 + 3) Piercing damage.\
    \ If the target is a Large or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Bite"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/dire-wolf-xmm.webp"
```
^statblock