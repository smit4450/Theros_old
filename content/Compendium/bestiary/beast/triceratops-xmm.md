---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast/dinosaur
statblock: inline
aliases: ["Triceratops"]
---
# Triceratops
*Source: Monster Manual (2024) p. 372*  

![](Compendium/bestiary/beast/img/triceratops.webp#center)  
```statblock
"name": "Triceratops (XMM)"
"size": "Huge"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "114"
"hit_dice": "12d12 + 36"
"stats":
- !!int "22"
- !!int "9"
- !!int "17"
- !!int "2"
- !!int "11"
- !!int "5"
"speed": "50 ft."
"senses": "passive Perception 10"
"languages": ""
"cr": "5"
"actions":
- "desc": "The triceratops makes two Gore attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +9, reach 5 ft. Hit: 19 (2d12 + 6) Piercing damage.\
    \ If the target is Huge or smaller and the triceratops moved 20+ feet straight\
    \ toward it immediately before the hit, the target takes an extra 9 (2d8) Piercing\
    \ damage and has the [Prone](Compendium/rules/conditions.md#Prone) condition."
  "name": "Gore"
"source":
- "XMM"
```
^statblock