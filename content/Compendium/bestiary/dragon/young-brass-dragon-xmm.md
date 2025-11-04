---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Young Brass Dragon"]
---
# Young Brass Dragon
*Source: Monster Manual (2024) p. 54*  

![](Compendium/bestiary/dragon/img/young-brass-dragon.webp#right)  
Young brass dragons travel extensively, often spending a few years in a region before circling back to their lair. Some work closely with other metallic dragons, carrying information between allies.

## Brass Dragons

*Dragons of Lore and Rapport*

- **Habitat.** Desert  
- **Treasure.** Arcana  

Gregarious and outgoing, brass dragons relish sharing knowledge and stories. Although these metallic dragons favor arid lands, they cheerfully journey considerable distances to visit friendly creatures, pass on what they've learned, and collect news. Though good natured, brass dragons don't shirk from combat when necessary, thwarting foes with magical sleep and searing them with flame.

Brass dragons favor warm climes, particularly steppes and rocky or sandy deserts, and they usually dwell near prominent crossroads or oases that regularly draw visitors. They enjoy adopting Humanoid forms, disguising themselves as traveling merchants, scholars, storytellers, or anyone else invested in others' stories.

Brass dragons collect eclectic objects. While such items might seem like knickknacks, each is part of a story—perhaps a nostalgic memento or evidence of a tale passed into myth. An old friend's hat and the crown of the last ruler of a forgotten dynasty could occupy the same shelf in a brass dragon's hoard.

### Brass Dragon Lairs

Brass dragons usually dwell in secret caves and canyons near well-traveled routes.
## Statblock

```statblock
"name": "Young Brass Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Chaotic Good"
"ac": !!int "17"
"hp": !!int "110"
"hit_dice": "13d10 + 39"
"stats":
- !!int "19"
- !!int "10"
- !!int "17"
- !!int "12"
- !!int "11"
- !!int "15"
"speed": "40 ft., burrow 20 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "3"
  "Wisdom": !!int "3"
"skillsaves":
  "Stealth": !!int "3"
  "Perception": !!int "6"
  "Persuasion": !!int "5"
"damage_immunities": "fire"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 16"
"languages": "Common, Draconic"
"cr": "6"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace two attacks with a\
    \ use of Sleep Breath."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 10 ft. Hit: 15 (2d10 + 4) Slashing damage."
  "name": "Rend"
- "desc": "Dexterity Saving Throw: DC 14, each creature in a 40-foot-long, 5-foot-wide\
    \ [Line [Area of Effect]](Compendium/rules/variant-rules/line-area-of-effect-xphb.md).\
    \ Failure: 38 (11d6) Fire damage. Success: Half damage."
  "name": "Fire Breath (Recharge 5-6)"
- "desc": "Constitution Saving Throw: DC 14, each creature in a 30-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ The target has the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition until the end of its next turn, at which point it repeats the save.\
    \ {@actSaveFail 2} The target has the [Unconscious](Compendium/rules/conditions.md#Unconscious)\
    \ condition for 1 minute. This effect ends for the target if it takes damage or\
    \ a creature within 5 feet of it takes an action to wake it."
  "name": "Sleep Breath"
"source":
- "XMM"
```
^statblock