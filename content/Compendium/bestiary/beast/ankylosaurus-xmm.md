---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast/dinosaur
statblock: inline
aliases: ["Ankylosaurus"]
---
# Ankylosaurus
*Source: Monster Manual (2024) p. 348*  

![](Compendium/bestiary/beast/img/ankylosaurus.webp#center)  
```statblock
"name": "Ankylosaurus (XMM)"
"size": "Huge"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "68"
"hit_dice": "8d12 + 16"
"stats":
- !!int "19"
- !!int "11"
- !!int "15"
- !!int "2"
- !!int "12"
- !!int "5"
"speed": "30 ft."
"saves":
  "Strength": !!int "6"
"senses": "passive Perception 11"
"languages": ""
"cr": "3"
"actions":
- "desc": "The ankylosaurus makes two Tail attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +6, reach 10 ft. Hit: 9 (1d10 + 4) Bludgeoning damage.\
    \ If the target is a Huge or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Tail"
"source":
- "XMM"
```
^statblock