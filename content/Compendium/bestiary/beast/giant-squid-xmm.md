---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Squid"]
---
# Giant Squid
*Source: Monster Manual (2024) p. 360*  

![](Compendium/bestiary/beast/img/giant-squid.webp#center)  
```statblock
"name": "Giant Squid (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "120"
"hit_dice": "16d12 + 16"
"stats":
- !!int "23"
- !!int "14"
- !!int "12"
- !!int "5"
- !!int "11"
- !!int "4"
"speed": "5 ft., swim 80 ft."
"saves":
  "Dexterity": !!int "5"
  "Strength": !!int "9"
"skillsaves":
  "Perception": !!int "6"
"senses": "darkvision 120 ft., passive Perception 16"
"languages": ""
"cr": "6"
"traits":
- "desc": "The squid can breathe only underwater."
  "name": "Water Breathing"
"actions":
- "desc": "The squid makes one Bite attack and one Tentacle attack."
  "name": "Multiattack"
- "desc": "Melee Attack: +9, reach 5 ft. Hit: 28 (4d10 + 6) Piercing damage."
  "name": "Bite"
- "desc": "Melee Attack: +9, reach 15 ft. Hit: 19 (3d8 + 6) Bludgeoning damage.\
    \ If the target is a Huge or smaller creature, it has the [Grappled](Compendium/rules/conditions.md#Grappled)\
    \ condition (escape DC 16) from one of two tentacles, and the squid can pull the\
    \ target up to 10 feet straight toward itself."
  "name": "Tentacle"
"reactions":
- "desc": "Trigger: The squid takes damage while underwater. Response: The squid releases\
    \ ink that fills a 15-foot [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ centered on itself, and the squid moves up to its [Swim Speed](Compendium/rules/variant-rules/swim-speed-xphb.md).\
    \ The [Cube [Area of Effect]](Compendium/rules/variant-rules/cube-area-of-effect-xphb.md)\
    \ is [Heavily Obscured](Compendium/rules/variant-rules/heavily-obscured-xphb.md)\
    \ for 1 minute or until a strong current or similar effect disperses the ink."
  "name": "Ink Cloud (1/Day)"
"source":
- "XMM"
```
^statblock