---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Couatl"]
---
# Couatl
*Source: Monster Manual (2024) p. 82*  

![](Compendium/bestiary/celestial/img/couatl.webp#right)  
## Couatl

*Guardian Manifestation of the Divine*

- **Habitat.** Desert, Forest, Grassland, Urban  
- **Treasure.** Relics  

Embodiments of prophecy and protectors of divine secrets, couatls ensure fate unfolds as it should. They resemble serpents with rainbow wings, and each is a manifestation of a divine edict, a truth or fate that a righteous god decrees must hold true for all time. Most couatls appear in places of ancient power, where they guard hidden magic or ensure foretold acts do or don't come to pass. Rarely, couatls watch over communities or travel lands in disguise, interpreting omens or manipulating factors to set fate on its proper course.

Motivated by eternal mandates, couatls sometimes behave in inscrutable or antagonistic ways. They are inflexible and uncompromising, as their existences are fundamentally tied to their divine directives, but they harm other creatures only when absolutely necessary to achieve divine goals.

Each couatl goes through a period of renewal at the end of an age. In a couatl's lifecycle, an age might correspond to a celestial calendar or some divine chronology. Near the age's end, the couatl lays a wondrous, rainbow-hued egg. When the age ends, the couatl dies. For a period—perhaps a single day, perhaps until an annual solar event—the couatl's work is unattended. Once this time passes, the same couatl that laid the egg hatches from it, fully grown and renewed to serve for another age.
```statblock
"name": "Couatl (XMM)"
"size": "Medium"
"type": "celestial"
"alignment": "Lawful Good"
"ac": !!int "19"
"hp": !!int "60"
"hit_dice": "8d8 + 24"
"stats":
- !!int "16"
- !!int "20"
- !!int "17"
- !!int "18"
- !!int "20"
- !!int "18"
"speed": "30 ft., fly 90 ft."
"saves":
  "Wisdom": !!int "7"
  "Constitution": !!int "5"
"damage_resistances": "bludgeoning, piercing, slashing"
"damage_immunities": "psychic, radiant"
"senses": "truesight 120 ft., passive Perception 15"
"languages": "all; telepathy 120 ft."
"cr": "4"
"traits":
- "desc": "The couatl casts one of the following spells, requiring no spell components\
    \ and using Wisdom as the spellcasting ability (spell save DC 15):\n\nAt will:\
    \ [Detect Evil and Good](Compendium/spells/detect-evil-and-good-xphb.md), [Detect\
    \ Magic](Compendium/spells/detect-magic-xphb.md), [Detect Thoughts](Compendium/spells/detect-thoughts-xphb.md),\
    \ [Shapechange](Compendium/spells/shapechange-xphb.md) (Beast or Humanoid form\
    \ only, no [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
    \ gained from the spell, and no Concentration or [Temporary Hit Points](Compendium/rules/variant-rules/temporary-hit-points-xphb.md)\
    \ required to maintain the spell)\n\n1/day each: [Create Food and Water](Compendium/spells/create-food-and-water-xphb.md),\
    \ [Dream](Compendium/spells/dream-xphb.md), [Greater Restoration](Compendium/spells/greater-restoration-xphb.md),\
    \ [Scrying](Compendium/spells/scrying-xphb.md), [Sleep](Compendium/spells/sleep-xphb.md)"
  "name": "Spellcasting"
- "desc": "The couatl casts [Bless](Compendium/spells/bless-xphb.md), [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md),\
    \ or [Sanctuary](Compendium/spells/sanctuary-xphb.md), requiring no spell components\
    \ and using the same spellcasting ability as Spellcasting.\n\n2/day: [Bless](Compendium/spells/bless-xphb.md),\
    \ [Lesser Restoration](Compendium/spells/lesser-restoration-xphb.md), [Sanctuary](Compendium/spells/sanctuary-xphb.md)"
  "name": "Divine Aid (2/Day)"
- "desc": "The couatl's thoughts can't be read by any means, and other creatures can\
    \ communicate with it telepathically only if it allows them."
  "name": "Shielded Mind"
"actions":
- "desc": "Melee Attack: +7, reach 5 ft. Hit: 11 (1d12 + 5) Piercing damage,\
    \ and the target has the [Poisoned](Compendium/rules/conditions.md#Poisoned) condition\
    \ until the end of the couatl's next turn."
  "name": "Bite"
- "desc": "Strength Saving Throw: DC 15, one Medium or smaller creature the couatl\
    \ can see within 5 feet. Failure: 8 (1d6 + 5) Bludgeoning damage. The target\
    \ has the [Grappled](Compendium/rules/conditions.md#Grappled) condition (escape\
    \ DC 13), and it has the [Restrained](Compendium/rules/conditions.md#Restrained)\
    \ condition until the grapple ends."
  "name": "Constrict"
"source":
- "XMM"
```
^statblock