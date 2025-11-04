---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Elk"]
---
# Elk
*Source: Monster Manual (2024) p. 353, Player's Handbook (2024) p. 349*  

![](Compendium/bestiary/beast/img/elk.webp#center)  
```statblock
"name": "Elk (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "11"
"hit_dice": "2d10"
"stats":
- !!int "16"
- !!int "10"
- !!int "11"
- !!int "2"
- !!int "10"
- !!int "6"
"speed": "50 ft."
"skillsaves":
  "Perception": !!int "2"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": ""
"cr": "1/4"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 6 (1d6 + 3) Bludgeoning damage.\
    \ If the target is a Large or smaller creature and the elk moved 20+ feet straight\
    \ toward it immediately before the hit, the target takes an extra 3 (1d6) Bludgeoning\
    \ damage and has the [Prone](Compendium/rules/conditions.md#Prone) condition."
  "name": "Ram"
"source":
- "XMM"
- "XPHB"
```
^statblock