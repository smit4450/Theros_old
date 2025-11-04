---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/arctic
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Mammoth"]
---
# Mammoth
*Source: Monster Manual (2024) p. 365*  

![](Compendium/bestiary/beast/img/mammoth.webp#center)  
```statblock
"name": "Mammoth (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "126"
"hit_dice": "11d12 + 55"
"stats":
- !!int "24"
- !!int "9"
- !!int "21"
- !!int "3"
- !!int "11"
- !!int "6"
"speed": "50 ft."
"saves":
  "Strength": !!int "10"
  "Constitution": !!int "8"
"senses": "passive Perception 10"
"languages": ""
"cr": "6"
"actions":
- "desc": "The mammoth makes two Gore attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +10, reach 10 ft. Hit: 18 (2d10 + 7) Piercing damage.\
    \ If the target is a Huge or smaller creature and the mammoth moved 20+ feet straight\
    \ toward it immediately before the hit, the target has the [Prone](Compendium/rules/conditions.md#Prone)\
    \ condition."
  "name": "Gore"
"bonus_actions":
- "desc": "Dexterity Saving Throw: DC 18, one creature within 5 feet that has the\
    \ [Prone](Compendium/rules/conditions.md#Prone) condition. Failure: 29 (4d10\
    \ + 7) Bludgeoning damage. Success: Half damage."
  "name": "Trample"
"source":
- "XMM"
```
^statblock