---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/8
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/chromatic
statblock: inline
aliases: ["Young Green Dragon"]
---
# Young Green Dragon
*Source: Monster Manual (2024) p. 152*  

![](Compendium/bestiary/dragon/img/young-green-dragon.webp#right)  
Young green dragons frequently control groups of ettercaps, kobolds, thieves, or other cowardly servants. These dragons do so while avoiding other evil dragons, who would sabotage them. Gradually, oppressing weaker creatures and amassing meaningless fortunes bore young green dragons, and they pursue more ambitious ways to indulge their egos.

## Green Dragons

*Dragons of Deceit and Derision*

- **Habitat.** Forest  
- **Treasure.** Arcana  

From forbidden forest depths, green dragons whisper evils into the world and manipulate the lives of those who listen. Elusive, conniving, and egotistical, these chromatic dragons patiently prey on the fears of shorter-lived beings, corrupting and isolating them. Green dragons might lurk amid labyrinthine wildernesses for centuries without revealing themselves; even their most devoted followers might know them only as the voice of the woodlands or a whisper in their dreams.

Despite their might, most green dragons disdain physical violence, viewing combat as servants' work and preferring to trick foes into dangerous or exploitative scenarios. These dragons collect "baubles" that embody their webs of manipulation and serve as tools of extortion, such as compromising documents, family heirlooms, and sentimental treasures.

### Green Dragon Lairs

Green dragons lair in ancient forests, often shaping stands of massive trees into compounds of interwoven branches, hollow trunks, and caverns amid mighty roots. They might also dwell amid forested ruins, particularly the former homes of those they've conquered.
## Statblock

```statblock
"name": "Young Green Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "chromatic"
"alignment": "Lawful Evil"
"ac": !!int "18"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"stats":
- !!int "19"
- !!int "12"
- !!int "17"
- !!int "16"
- !!int "13"
- !!int "15"
"speed": "40 ft., fly 80 ft., swim 40 ft."
"saves":
  "Dexterity": !!int "4"
  "Wisdom": !!int "4"
"skillsaves":
  "Deception": !!int "5"
  "Stealth": !!int "4"
  "Perception": !!int "7"
"damage_immunities": "poison"
"condition_immunities": "[poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "blindsight 30 ft., darkvision 120 ft., passive Perception 17"
"languages": "Common, Draconic"
"cr": "8"
"traits":
- "desc": "The dragon can breathe air and water."
  "name": "Amphibious"
"actions":
- "desc": "The dragon makes three Rend attacks."
  "name": "Multiattack"
- "desc": "Melee Attack: +7, reach 10 ft. Hit: 11 (2d6 + 4) Slashing damage\
    \ plus 7 (2d6) Poison damage."
  "name": "Rend"
- "desc": "Constitution Saving Throw: DC 14, each creature in a 30-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 42 (12d6) Poison damage. Success: Half damage."
  "name": "Poison Breath (Recharge 5-6)"
"source":
- "XMM"
```
^statblock