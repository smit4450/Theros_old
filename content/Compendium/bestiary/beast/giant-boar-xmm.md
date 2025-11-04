---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Boar"]
---
# Giant Boar
*Source: Monster Manual (2024) p. 355*  

![](Compendium/bestiary/beast/img/giant-boar.webp#center)  
```statblock
"name": "Giant Boar (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "42"
"hit_dice": "5d10 + 15"
"stats":
- !!int "17"
- !!int "10"
- !!int "16"
- !!int "2"
- !!int "7"
- !!int "5"
"speed": "40 ft."
"saves":
  "Strength": !!int "5"
"senses": "passive Perception 8"
"languages": ""
"cr": "2"
"traits":
- "desc": "The boar has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ on melee attack rolls while it is [Bloodied](Compendium/rules/variant-rules/bloodied-xphb.md)."
  "name": "Bloodied Fury"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 10 (2d6 + 3) Piercing damage.\
    \ If the target is a Large or smaller creature and the boar moved 20+ feet straight\
    \ toward it immediately before the hit, the target takes an extra 7 (2d6) Piercing\
    \ damage and has the [Prone](Compendium/rules/conditions.md#Prone) condition."
  "name": "Gore"
"source":
- "XMM"
```
^statblock