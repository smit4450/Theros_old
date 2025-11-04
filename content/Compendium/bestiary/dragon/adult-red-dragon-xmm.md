---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/17
- ttrpg-cli/monster/environment/hill
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/dragon/chromatic
statblock: inline
aliases: ["Adult Red Dragon"]
---
# Adult Red Dragon
*Source: Monster Manual (2024) p. 255*  

![](Compendium/bestiary/dragon/img/adult-red-dragon.webp#right)  
Adult red dragons are tyrants that claim vast domains and might command armies of followers or significant magical resources. Red dragons rarely pay attention to the nations and claims of smaller creatures, and they might consider entire cities part of their realm. Most red dragons are inattentive rulers, though, spending decades focused on their own comforts, hoards, or magical concerns within their lairs. But when their attention returns to their territories, if they find matters not to their liking, whole lands might burn.

## Red Dragons

*Dragons of Greed and Devastation*

- **Habitat.** Hill, Mountain  
- **Treasure.** Any  

Red dragons take whatever they desire and burn to ash anything that stands in their way. These chromatic dragons endlessly desire more—more magic, territory, treasure, or whatever else inflames their cruel ambitions.

Red dragons make their lairs amid perilous cliffs and volcanoes. Within, they amass and fiercely protect hoards of treasure, and many have perfect recall of the hoards' contents and the locations of all they've collected. Should anything go missing, red dragons fly into rages. They don't rest until their treasures are returned and the thieves have burned.

Red dragons believe themselves to be the greatest of all dragons and, by extension, the greatest of all creatures. To them, pillaging and conquering are their right—treasures can find no more honored place than in their hoards, and other creatures are privileged to serve them.

### Red Dragon Lairs

Red dragons make their lairs in smoldering, unapproachable places such as volcanic mountains, burning wastelands, and ruins they've stolen from other creatures.
## Statblock

```statblock
"name": "Adult Red Dragon (XMM)"
"size": "Huge"
"type": "dragon"
"subtype": "chromatic"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"hp": !!int "256"
"hit_dice": "19d12 + 133"
"stats":
- !!int "27"
- !!int "10"
- !!int "25"
- !!int "16"
- !!int "13"
- !!int "23"
"speed": "40 ft., climb 40 ft., fly 80 ft."
"saves":
  "Dexterity": !!int "6"
  "Wisdom": !!int "7"
"skillsaves":
  "Stealth": !!int "6"
  "Perception": !!int "13"
"damage_immunities": "fire"
"senses": "blindsight 60 ft., darkvision 120 ft., passive Perception 23"
"languages": "Common, Draconic"
"cr": "17"
"traits":
- "desc": "The dragon casts one of the following spells, requiring no Material components\
    \ and using Charisma as the spellcasting ability (spell save DC 20, +12 to hit\
    \ with spell attacks):\n\nAt will: [Command](Compendium/spells/command-xphb.md)\
    \ (level 2 version), [Detect Magic](Compendium/spells/detect-magic-xphb.md), [Scorching\
    \ Ray](Compendium/spells/scorching-ray-xphb.md)\n\n1/day: [Fireball](Compendium/spells/fireball-xphb.md)"
  "name": "Spellcasting"
- "desc": "If the dragon fails a saving throw, it can choose to succeed instead."
  "name": "Legendary Resistance (3/Day, or 4/Day in Lair)"
"actions":
- "desc": "The dragon makes three Rend attacks. It can replace one attack with a use\
    \ of Spellcasting to cast [Scorching Ray](Compendium/spells/scorching-ray-xphb.md)."
  "name": "Multiattack"
- "desc": "Melee Attack: +14, reach 10 ft. Hit: 13 (1d10 + 8) Slashing damage\
    \ plus 5 (2d4) Fire damage."
  "name": "Rend"
- "desc": "Dexterity Saving Throw: DC 21, each creature in a 60-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ 59 (17d6) Fire damage. Success: Half damage."
  "name": "Fire Breath (Recharge 5-6)"
"legendary_actions":
- "desc": "The dragon uses Spellcasting to cast [Command](Compendium/spells/command-xphb.md)\
    \ (level 2 version). The dragon can't take this action again until the start of\
    \ its next turn."
  "name": "Commanding Presence"
- "desc": "The dragon uses Spellcasting to cast [Scorching Ray](Compendium/spells/scorching-ray-xphb.md).\
    \ The dragon can't take this action again until the start of its next turn."
  "name": "Fiery Rays"
- "desc": "The dragon moves up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md),\
    \ and it makes one Rend attack."
  "name": "Pounce"
"regional_effects":
- "desc": "The region containing an adult or ancient red dragon's lair is warped by\
    \ its presence, creating the following effects:"
  "name": ""
- "desc": "- Burning Heat. The area within 1 mile of the lair is an area of extreme\
    \ heat. A burning creature or object takes an additional 1d4 Fire damage at\
    \ the start of each of its turns.  \n- Smoldering Haze. The area within 1\
    \ mile of the lair is [Lightly Obscured](Compendium/rules/variant-rules/lightly-obscured-xphb.md)\
    \ with clouds of ash. Whenever a creature other than the dragon or one of its\
    \ allies finishes a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md)\
    \ in that area, that creature must succeed on a DC 15 Constitution saving throw\
    \ or have the [Poisoned](Compendium/rules/conditions.md#Poisoned) condition for\
    \ 1 hour.  "
  "name": ""
- "desc": "If the dragon dies or moves its lair elsewhere, these effects end immediately."
  "name": ""
"source":
- "XMM"
```
^statblock