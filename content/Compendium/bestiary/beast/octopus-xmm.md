---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/0
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Octopus"]
---
# Octopus
*Source: Monster Manual (2024) p. 365, Player's Handbook (2024) p. 353*  

![](Compendium/bestiary/beast/img/octopus.webp#center)  
```statblock
"name": "Octopus (XMM)"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "3"
"hit_dice": "1d6"
"stats":
- !!int "4"
- !!int "15"
- !!int "11"
- !!int "3"
- !!int "10"
- !!int "4"
"speed": "5 ft., swim 30 ft."
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "2"
"senses": "darkvision 30 ft., passive Perception 12"
"languages": ""
"cr": "0"
"traits":
- "desc": "The octopus can move through a space as narrow as 1 inch without expending\
    \ extra movement to do so."
  "name": "Compression"
- "desc": "The octopus can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 1 Bludgeoning damage."
  "name": "Tentacles"
"reactions":
- "desc": "Trigger: A creature ends its turn within 5 feet of the octopus while underwater.\
    \ Response: The octopus releases ink that fills a 5-foot [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ centered on itself, and the octopus moves up to its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md).\
    \ The [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ is [Heavily Obscured](Compendium/rules/variant-rules/heavily-obscured-xphb.md)\
    \ for 1 minute or until a strong current or similar effect disperses the ink."
  "name": "Ink Cloud (1/Day)"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/beast/token/octopus-xmm.webp"
```
^statblock