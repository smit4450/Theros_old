---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Young Silver Dragon"]
---
# Young Silver Dragon
*Source: Monster Manual (2024) p. 278*  

![](Compendium/bestiary/dragon/img/young-silver-dragon.webp#right)  
Young silver dragons usually have close ties with elder metallic dragons or heroic role models, helping those with great goals achieve their ambitions. They might serve as messengers for or representatives of such do-gooders.

## Silver Dragons

*Dragons of Courage and Fairness*

- **Habitat.** Mountain, Urban  
- **Treasure.** Arcana  

Silver dragons work to preserve peace and encourage greatness. They try to live as examples of decency while remaining watchful against evil.

Silver dragons typically dwell amid snow-capped mountains, though aspirations and congeniality drive some to instead live among cosmopolitan societies. Disguised as humanoids, they ally with artists, historians, knights, and humble leaders who learn from the past to create better futures.

Silver dragons take inspiration from legendary heroes and have grand ambitions. Many collect treasures that reflect these interests, such as histories, ancient art, and the gear of famous champions.

### Silver Dragon Lairs

Silver dragons typically lair in picturesque mountain retreats or on sculpted cloud "islands."
## Statblock

```statblock
"name": "Young Silver Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "18"
"hp": !!int "168"
"hit_dice": "16d10 + 80"
"stats":
- !!int "23"
- !!int "10"
- !!int "21"
- !!int "14"
- !!int "11"
- !!int "19"
"speed": "40 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "4"
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "8"
  "History": !!int "6"
"damage_immunities": "cold"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 18"
"languages": "Common, Draconic"
"cr": "9"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace one attack with a use\
    \ of Paralyzing Breath."
  "name": "Multiattack"
- "desc": "Melee Attack: +10, reach 10 ft. Hit: 15 (2d8 + 6) Slashing damage."
  "name": "Rend"
- "desc": "Constitution Saving Throw: DC 17, each creature in a 30-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 49 (11d8) Cold damage. Success: Half damage."
  "name": "Cold Breath (Recharge 5-6)"
- "desc": "Constitution Saving Throw: DC 17, each creature in a 30-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). {@actSaveFail\
    \ 1} The target has the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition until the end of its next turn, when it repeats the save. {@actSaveFail\
    \ 2} The target has the [Paralyzed](Compendium/rules/conditions.md#Paralyzed)\
    \ condition, and it repeats the save at the end of each of its turns, ending the\
    \ effect on itself on a success. After 1 minute, it succeeds automatically."
  "name": "Paralyzing Breath"
"source":
- "XMM"
```
^statblock