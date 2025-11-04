---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-2
- ttrpg-cli/monster/environment/elemental
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Dust Mephit"]
---
# Dust Mephit
*Source: Monster Manual (2024) p. 206*  

![](Compendium/bestiary/elemental/img/dust-mephit.webp#right)  
Dust mephits are composed of air and fine earth. They are drawn to forsaken places, and they think everything associated with death is hilarious.

## Mephits

*Malicious Elemental Hooligans*

- **Habitat.** Planar (Elemental Planes)  
- **Treasure.** None  

Mephits are mean-spirited tricksters that dwell on the Elemental Planes. The six most prominent types of mephits resemble halfling-size gargoyles with wings, exaggerated features, and bodies composed of two elements. Most live self-interested existences, indulging their warped senses of humor or overblown egos on their home planes of existence. Some serve as messengers or spies for genies or magic-users.

Mephits resent leaving the elemental extremes where they make their homes. If loosed on the Material Plane or other realms, they lash out with nasty pranks or by tormenting weaker creatures. When destroyed, mephits explode in a burst of elemental magic.

> [!quote] A quote from Seamusxanthuszenus, smoke mephit with a typically inflated impression of itself  
> 
> I am Seamusxanthuszenus, Slayer of Fiends, Merchant Most Excellent, Purveyor of Death!

## Statblock

```statblock
"name": "Dust Mephit (XMM)"
"size": "Small"
"type": "elemental"
"alignment": "Neutral Evil"
"ac": !!int "12"
"hp": !!int "17"
"hit_dice": "5d6"
"stats":
- !!int "5"
- !!int "14"
- !!int "10"
- !!int "9"
- !!int "11"
- !!int "10"
"speed": "30 ft., fly 30 ft."
"skillsaves":
  "Stealth": !!int "4"
  "Perception": !!int "2"
"damage_vulnerabilities": "fire"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "darkvision 60 ft., passive Perception 12"
"languages": "Primordial (Auran, Terran)"
"cr": "1/2"
"traits":
- "desc": "The mephit casts the [Sleep](Compendium/spells/sleep-xphb.md) spell, requiring\
    \ no spell components and using Charisma as the spellcasting ability (spell save\
    \ DC 10).\n\n1/day: [Sleep](Compendium/spells/sleep-xphb.md)"
  "name": "Sleep (1/Day)"
- "desc": "The mephit explodes when it dies. Dexterity Saving Throw: DC 10, each\
    \ creature in a 5-foot [Emanation [Area of Effect]](Compendium/rules/variant-rules/emanation-area-of-effect-xphb.md)\
    \ originating from the mephit. Failure: 5 (2d4) Bludgeoning damage. Success:\
    \ Half damage."
  "name": "Death Burst"
"actions":
- "desc": "Melee Attack: +4, reach 5 ft. Hit: 4 (1d4 + 2) Slashing damage."
  "name": "Claw"
- "desc": "Dexterity Saving Throw: DC 10, each creature in a 15-foot [Cone [Area\
    \ of Effect]](Compendium/rules/variant-rules/cone-area-of-effect-xphb.md). Failure:\
    \ The target has the [Blinded](Compendium/rules/conditions.md#Blinded) condition\
    \ until the end of the mephit's next turn."
  "name": "Blinding Breath (Recharge 6)"
"source":
- "XMM"
```
^statblock