---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Octopus"]
---
# Giant Octopus
*Source: Monster Manual (2024) p. 358*  

![](Compendium/bestiary/beast/img/giant-octopus.webp#center)  
```statblock
"name": "Giant Octopus (XMM)"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "45"
"hit_dice": "7d10 + 7"
"stats":
- !!int "17"
- !!int "13"
- !!int "13"
- !!int "5"
- !!int "10"
- !!int "4"
"speed": "10 ft., swim 60 ft."
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "4"
"senses": "darkvision 60 ft., passive Perception 14"
"languages": ""
"cr": "1"
"traits":
- "desc": "The octopus can breathe only underwater. It can hold its breath for 1 hour\
    \ outside water."
  "name": "Water Breathing"
"actions":
- "desc": "Melee Attack: +5, reach 10 ft. Hit: 10 (2d6 + 3) Bludgeoning damage.\
    \ If the target is a Medium or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 13) from all eight tentacles. While [Grappled](Compendium/rules/conditions.md#Grappled),\
    \ the target has the [Restrained](Compendium/rules/conditions.md#Restrained) condition."
  "name": "Tentacles"
"reactions":
- "desc": "Trigger: The octopus takes damage while underwater. Response: The octopus\
    \ releases ink that fills a 10-foot [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ centered on itself, and the octopus moves up to its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md).\
    \ The [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ is [Heavily Obscured](Compendium/rules/variant-rules/heavily-obscured-xphb.md)\
    \ for 1 minute or until a strong current or similar effect disperses the ink."
  "name": "Ink Cloud (1/Day)"
"source":
- "XMM"
```
^statblock