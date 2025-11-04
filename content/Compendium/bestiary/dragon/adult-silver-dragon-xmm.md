---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/16
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Adult Silver Dragon"]
---
# Adult Silver Dragon
*Source: Monster Manual (2024) p. 279*  

![](Compendium/bestiary/dragon/img/adult-silver-dragon.webp#right)  
Adult silver dragons love to spend time among various peoples. Rather than manipulating politics directly, they support individuals who have ambitious goals or who popularize the return of great universities, inspiring athletics events or festivals, and other salutary civic institutions of the past. Silver dragons often surround themselves with like-minded allies and are watchful for hidden threats.

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
"name": "Adult Silver Dragon (XMM)"
"size": "Huge"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "19"
"hp": !!int "216"
"hit_dice": "16d12 + 112"
"stats":
- !!int "27"
- !!int "10"
- !!int "25"
- !!int "16"
- !!int "13"
- !!int "22"
"speed": "40 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "5"
  "Wisdom": !!int "6"
"skillsaves":
  "Stealth": !!int "5"
  "Perception": !!int "11"
  "History": !!int "8"
"damage_immunities": "cold"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 21"
"languages": "Common, Draconic"
"cr": "16"
"traits":
- "desc": "The dragon casts one of the following spells, requiring no Material components\
    \ and using Charisma as the spellcasting ability (spell save DC 19, +11 to hit\
    \ with spell attacks):\n\nAt will: [Detect Magic](Compendium/spells/detect-magic-xphb.md),\
    \ [Hold Monster](Compendium/spells/hold-monster-xphb.md), [Ice Knife](Compendium/spells/ice-knife-xphb.md),\
    \ [Shapechange](Compendium/spells/shapechange-xphb.md) (Beast or Humanoid form\
    \ only, no [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
    \ gained from the spell, and no Concentration or [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
    \ required to maintain the spell)\n\n1/day each: [Ice Storm](Compendium/spells/ice-storm-xphb.md)\
    \ (level 5 version), [Zone of Truth](Compendium/spells/zone-of-truth-xphb.md)"
  "name": "Spellcasting"
- "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day, or 4/Day in Lair)"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace one attack with a use\
    \ of (A) Paralyzing Breath or (B) Spellcasting to cast [Ice Knife](Compendium/spells/ice-knife-xphb.md)."
  "name": "Multiattack"
- "desc": "Melee Attack: +13, reach 10 ft. Hit: 17 (2d8 + 8) Slashing damage\
    \ plus 4 (1d8) Cold damage."
  "name": "Rend"
- "desc": "Constitution Saving Throw: DC 20, each creature in a 60-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 54 (12d8) Cold damage. Success: Half damage."
  "name": "Cold Breath (Recharge 5-6)"
- "desc": "Constitution Saving Throw: DC 20, each creature in a 60-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). {@actSaveFail\
    \ 1} The target has the [Incapacitated](Compendium/rules/conditions.md#Incapacitated)\
    \ condition until the end of its next turn, when it repeats the save. {@actSaveFail\
    \ 2} The target has the [Paralyzed](Compendium/rules/conditions.md#Paralyzed)\
    \ condition, and it repeats the save at the end of each of its turns, ending the\
    \ effect on itself on a success. After 1 minute, it succeeds automatically."
  "name": "Paralyzing Breath"
"legendary_actions":
- "desc": "The dragon uses Spellcasting to cast [Hold Monster](Compendium/spells/hold-monster-xphb.md).\
    \ The dragon can't take this action again until the start of its next turn."
  "name": "Chill"
- "desc": "Dexterity Saving Throw: DC 19, each creature in a 60-foot-long, 10-foot-wide\
    \ [Line [Area of Effect]](Compendium/rules/variant-rules/line-area-of-effect-xphb.md).\
    \ Failure: 14 (4d6) Cold damage, and the target is pushed up to 30 feet straight\
    \ away from the dragon. Success: Half damage only. Failure or Success: The\
    \ dragon can't take this action again until the start of its next turn."
  "name": "Cold Gale"
- "desc": "The dragon moves up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md),\
    \ and it makes one Rend attack."
  "name": "Pounce"
"regional_effects":
- "desc": "The region containing an adult or ancient silver dragon's lair is changed\
    \ by its magic, creating the following effects:"
  "name": ""
- "desc": "- Gentle Gusts. Winds buoy creatures that fall within 1 mile of the\
    \ lair. Such creatures descend at a rate of 60 feet per round and take no damage\
    \ from falling.  \n- Sun and Storms. While in its lair, the dragon can cast\
    \ [Control Weather](Compendium/spells/control-weather-xphb.md), requiring no Material\
    \ components and using the same spellcasting ability as its Spellcasting action.\
    \  "
  "name": ""
- "desc": "If the dragon dies or moves its lair elsewhere, these effects end immediately."
  "name": ""
"source":
- "XMM"
```
^statblock