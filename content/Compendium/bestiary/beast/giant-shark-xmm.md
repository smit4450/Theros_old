---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Shark"]
---
# Giant Shark
*Source: Monster Manual (2024) p. 359*  

![](Compendium/bestiary/beast/img/giant-shark.webp#center)  
```statblock
"name": "Giant Shark (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "92"
"hit_dice": "8d12 + 40"
"stats":
- !!int "23"
- !!int "11"
- !!int "21"
- !!int "1"
- !!int "10"
- !!int "5"
"speed": "5 ft., swim 60 ft."
"skillsaves":
  "Perception": !!int "3"
"senses": "blindsight 60 ft., passive Perception 13"
"languages": ""
"cr": "5"
"traits":
- "desc": "The shark can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "The shark makes two Bite attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +9 (with [Advantage](Compendium/rules/variant-rules/advantage-xphb.md)\
    \ if the target doesn't have all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)),\
    \ reach 5 ft. Hit: 22 (3d10 + 6) Piercing damage."
  "name": "Bite"
"source":
- "XMM"
```
^statblock