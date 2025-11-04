---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Giant Ape"]
---
# Giant Ape
*Source: Monster Manual (2024) p. 354*  

![](Compendium/bestiary/beast/img/giant-ape.webp#center)  
```statblock
"name": "Giant Ape (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "168"
"hit_dice": "16d12 + 64"
"stats":
- !!int "23"
- !!int "14"
- !!int "18"
- !!int "5"
- !!int "12"
- !!int "7"
"speed": "40 ft., climb 40 ft."
"skillsaves":
  "Athletics": !!int "9"
  "Perception": !!int "4"
  "Survival": !!int "4"
"senses": "passive Perception 14"
"languages": ""
"cr": "7"
"actions":
- "desc": "The ape makes two Fist attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +9, reach 10 ft. Hit: 22 (3d10 + 6) Bludgeoning damage."
  "name": "Fist"
- "desc": "The ape hurls a boulder at a point it can see within 90 feet. Dexterity\
    \ Saving Throw: DC 17, each creature in a 5-foot-radius [Sphere [Area of Effect]](Compendium/rules/variant-rules/sphere-area-of-effect-xphb.md)\
    \ centered on that point. Failure: 24 (7d6) Bludgeoning damage. If the target\
    \ is a Large or smaller creature, it has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition. Success: Half damage only."
  "name": "Boulder Toss (Recharge 6)"
"bonus_actions":
- "desc": "The ape jumps up to 30 feet by spending 10 feet of movement."
  "name": "Leap"
"source":
- "XMM"
```
^statblock