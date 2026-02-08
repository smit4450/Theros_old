---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/12
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/mountain
- ttrpg-cli/monster/environment/swamp
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
---
# Archdruid
*Source: Volo's Guide to Monsters p. 210, Mythic Odysseys of Theros*  

Archdruids watch over the natural wonders of their domains. They seldom interact with civilized folk unless there is a great threat to the natural order. An archdruid typically has one or more pupils who are druids (see the Monster Manual for statistics), and the archdruid's lair is usually guarded by loyal beasts and fey creatures.
```statblock
"name": "Archdruid (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[[hide-armor-xphb]], [[shield-xphb]]"
"hp": !!int "132"
"hit_dice": "24d8 + 24"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "12"
  - !!int "20"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "5"
  - "wisdom": !!int "9"
"skillsaves":
  - "name": "[Medicine](Compendium/rules/skills.md#Medicine)"
    "desc": "+9"
  - "name": "[Nature](Compendium/rules/skills.md#Nature)"
    "desc": "+5"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+9"
"senses": "passive Perception 19"
"languages": "Druidic plus any two languages"
"cr": "12"
"traits":
  - "desc": "The archdruid is an 18th-level spellcaster. Its spellcasting ability\
      \ is Wisdom (spell save DC 17, +9 to hit with spell attacks). It has the following\
      \ druid spells prepared:\n\n**Cantrips (at will):** [[druidcraft-xphb]],\
      \ [[mending-xphb]], [[poison-spray-xphb]],\
      \ [[produce-flame-xphb]]\n\n**1st level (4\
      \ slots):** [[cure-wounds-xphb]], [[entangle-xphb]],\
      \ [[faerie-fire-xphb]], [[speak-with-animals-xphb]]\n\
      \n**2nd level (3 slots):** [[animal-messenger-xphb]],\
      \ [[beast-sense-xphb]], [[hold-person-xphb]]\n\
      \n**3rd level (3 slots):** [[conjure-animals-xphb]],\
      \ [[meld-into-stone-xphb]], [[water-breathing-xphb]]\n\
      \n**4th level (3 slots):** [[dominate-beast-xphb]],\
      \ [[locate-creature-xphb]], [[stoneskin-xphb]],\
      \ [[wall-of-fire-xphb]]\n\n**5th level (3 slots):**\
      \ [[commune-with-nature-xphb]], [mass\
      \ cure wounds](Compendium/spells/mass-cure-wounds-xphb.md), [[tree-stride-xphb]]\n\
      \n**6th level (1 slots):** [[heal-xphb]], [heroes'\
      \ feast](Compendium/spells/heroes-feast-xphb.md), [[sunbeam-xphb]]\n\
      \n**7th level (1 slots):** [[fire-storm-xphb]]\n\
      \n**8th level (1 slots):** [[animal-shapes-xphb]]\n\
      \n**9th level (1 slots):** [[foresight-xphb]]"
    "name": "Spellcasting"
"actions":
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 5\
      \ (1d6 + 2) slashing damage."
    "name": "Scimitar"
  - "desc": "The archdruid magically polymorphs into a beast or elemental with a challenge\
      \ rating of 6 or less, and can remain in this form for up to 9 hours. The archdruid\
      \ can choose whether its equipment falls to the ground, melds with its new form,\
      \ or is worn by the new form. The archdruid reverts to its true form if it dies\
      \ or falls [unconscious](Compendium/rules/conditions.md#Unconscious). The archdruid\
      \ can revert to its true form using a bonus action on its turn.\n\nWhile in\
      \ a new form, the archdruid retains its game statistics and ability to speak,\
      \ but its AC, movement modes, Strength, and Dexterity are replaced by those\
      \ of the new form, and it gains any special senses, proficiencies, traits, actions,\
      \ and reactions (except class features, legendary actions, and lair actions)\
      \ that the new form has but that it lacks. It can cast its spells with verbal\
      \ or somatic components in its new form.\n\nThe new form's attacks count as\
      \ magical for the purpose of overcoming resistances and immunity to nonmagical\
      \ attacks."
    "name": "Change Shape (2/Day)"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/archdruid-vgm.webp"
```
^statblock