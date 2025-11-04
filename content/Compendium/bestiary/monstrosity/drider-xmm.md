---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Drider"]
---
# Drider
*Source: Monster Manual (2024) p. 105*  

![](Compendium/bestiary/monstrosity/img/drider.webp#right)  
## Drider

*Spiderlike Underdark Hunter*

- **Habitat.** Forest, Underdark  
- **Treasure.** Armaments  

Driders combine the features of drow and giant spiders. The wicked god Lolth is fond of transforming her drow worshipers into driders, as either a blessing or a curse. These driders often become fanatical servants of their god, or they are overwhelmed by their transformation and live only to indulge their predatory arachnid instincts.

Driders also appear when whole communities are transformed by a wicked god's wrath or other magical means, or driders might be part of a world's natural population. Most dwell underground or in dense forests where they can make the most of their spiderlike traits. Driders with non-drow features are uncommon but possible. Roll on or choose a result from the Drider Metamorphoses table to inspire how supernatural driders come into being.

**Drider Metamorphoses**

`dice: [](drider-xmm.md#^drider-metamorphoses)`

| dice: 1d6 | The Drider Gained Its Form As... |
|-----------|----------------------------------|
| 1 | A blessing from a deity of assassins, dangerous wildernesses, or the Underdark. |
| 2 | A curse from a powerful hag, vengeful witch, or strange Artifact. |
| 3 | An experiment by an aboleth, a mind flayer, or another life-shaping magic-user. |
| 4 | A magical means of escaping disaster or some worse fate. |
| 5 | A mutation after exposure to chaotic planar energies or strange Underdark radiations. |
| 6 | A punishment from a spiteful god, like Lolth or the Queen of Air and Darkness. |
^drider-metamorphoses
```statblock
"name": "Drider (XMM)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"hp": !!int "123"
"hit_dice": "13d10 + 52"
"stats":
- !!int "16"
- !!int "19"
- !!int "18"
- !!int "13"
- !!int "16"
- !!int "12"
"speed": "30 ft., climb 30 ft."
"skillsaves":
  "Stealth": !!int "10"
  "Perception": !!int "6"
"senses": "darkvision 120 ft., passive Perception 16"
"languages": "Elvish, Undercommon"
"cr": "6"
"traits":
- "desc": "The drider casts [Darkness](Compendium/spells/darkness-xphb.md), [Faerie\
    \ Fire](Compendium/spells/faerie-fire-xphb.md), or [Web](Compendium/spells/web-xphb.md),\
    \ requiring no Material components and using Wisdom as the spellcasting ability\
    \ (spell save DC 14).\n"
  "name": "Magic of the Spider Queen (Recharge 5-6)"
- "desc": "The drider can climb difficult surfaces, including along ceilings, without\
    \ needing to make an ability check."
  "name": "Spider Climb"
- "desc": "While in sunlight, the drider has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md)\
    \ on ability checks and attack rolls."
  "name": "Sunlight Sensitivity"
- "desc": "The drider ignores movement restrictions caused by webs, and the drider\
    \ knows the location of any other creature in contact with the same web."
  "name": "Web Walker"
"actions":
- "desc": "The drider makes three attacks, using Foreleg or Poison Burst in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 10 ft. Hit: 13 (2d8 + 4) Piercing damage."
  "name": "Foreleg"
- "desc": "Ranged Attack: +6, range 120 ft. Hit: 13 (3d6 + 3) Poison damage."
  "name": "Poison Burst"
"source":
- "XMM"
```
^statblock