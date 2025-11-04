---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-4
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Sprite"]
---
# Sprite
*Source: Monster Manual (2024) p. 298, Player's Handbook (2024) p. 358*  

![](Compendium/bestiary/fey/img/sprite.webp#right)  
## Sprite

*Elusive Defender of Fey Realms*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** Armaments  

Sprites dwell in mystical forests touched by the magic of the Feywild, living peacefully with most other Fey and friends of nature. These foot-tall spirits of nature resemble elves with exaggerated, whimsical features and gossamer wings.

Sprites can sense the innate goodness or wickedness of other creatures. Those that enter their realms with good intentions might be treated to tiny feasts and celebrations. The wicked face nasty tricks and bold ambushes at the hands of [invisible](Compendium/rules/conditions.md#Invisible) sprite defenders. These woodland guardians enchant the arrows of their tiny bows with charming magic that can pierce the heart of the fiercest foe.

Sprites oppose any creatures that seek to harm places of natural magic and beauty. This can put them into conflict with would-be settlers, monsters like ettercaps, and despoilers such as goblinoids and hags. They frequently aid other good creatures of the forest, including treants and unicorns, in defending their homes.

> [!quote]  
> 
> The tree had a wee village nestled in its boughs, I swear. Next thing I knew, I was lyin' face-down in the dirt. My head was full of stars, an' when I stood up an' looked around, both the tree an' the wee village were gone.

![](Compendium/bestiary/fey/img/sprite-2.webp#center)  
```statblock
"name": "Sprite (XMM)"
"size": "Tiny"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "15"
"hp": !!int "10"
"hit_dice": "4d4"
"stats":
- !!int "3"
- !!int "18"
- !!int "10"
- !!int "14"
- !!int "13"
- !!int "11"
"speed": "10 ft., fly 40 ft."
"skillsaves":
  "Stealth": !!int "8"
  "Perception": !!int "3"
"senses": "passive Perception 13"
"languages": "Common, Elvish, Sylvan"
"cr": "1/4"
"traits":
- "desc": "The sprite casts [Invisibility](Compendium/spells/invisibility-xphb.md)\
    \ on itself, requiring no spell components and using Charisma as the spellcasting\
    \ ability.\n\nAt will: [Invisibility](Compendium/spells/invisibility-xphb.md)"
  "name": "Invisibility"
"actions":
- "desc": "Melee Attack: +6, reach 5 ft. Hit: 6 (1d4 + 4) Piercing damage."
  "name": "Needle Sword"
- "desc": "Ranged Attack: +6, range 40/160 ft. Hit: 1 Piercing damage, and the\
    \ target has the [Charmed](Compendium/rules/conditions.md#Charmed) condition until\
    \ the start of the sprite's next turn."
  "name": "Enchanting Bow"
- "desc": "Charisma Saving Throw: DC 10, one creature within 5 feet the sprite can\
    \ see (Celestials, Fiends, and Undead automatically fail the save). Failure:\
    \ The sprite knows the target's emotions and alignment."
  "name": "Heart Sight"
"source":
- "XMM"
- "XPHB"
"image": "Compendium/bestiary/fey/token/sprite-xmm.webp"
```
^statblock