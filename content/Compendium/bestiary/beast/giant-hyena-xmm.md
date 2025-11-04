---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Hyena"]
---
# Giant Hyena
*Source: Monster Manual (2024) p. 357*  

![](Compendium/bestiary/beast/img/giant-hyena.webp#center)  
```statblock
"name": "Giant Hyena (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"stats":
- !!int "16"
- !!int "14"
- !!int "14"
- !!int "2"
- !!int "12"
- !!int "7"
"speed": "50 ft."
"skillsaves":
  "Perception": !!int "3"
"senses": "darkvision 60 ft., passive Perception 13"
"languages": ""
"cr": "1"
"actions":
- "desc": "Melee Attack: +5, reach 5 ft. Hit: 10 (2d6 + 3) Piercing damage."
  "name": "Bite"
"bonus_actions":
- "desc": "Immediately after dealing damage to a creature that was already [Bloodied](Compendium/rules/variant-rules/bloodied-xphb.md),\
    \ the hyena can move up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md),\
    \ and it makes one Bite attack."
  "name": "Rampage (1/Day)"
"source":
- "XMM"
```
^statblock