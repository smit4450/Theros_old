---
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/small-or-medium
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Warrior Commander"]
---
# Warrior Commander
*Source: Monster Manual (2024) p. 321*  

![](Compendium/bestiary/humanoid/img/warrior-commander.webp#right)  
Skilled in both combat and leadership, warrior commanders overcome challenges through a combination of martial skill and clever tactics.

## Warriors

*Soldiers and Scrappers*

- **Habitat.** Any  
- **Treasure.** Armaments  

Warriors are professionals who make a living through their prowess in battle. They might be skilled in using a variety of tactics or trained to take advantage of unusual battlefields. Warriors often work together, whether in armies or in teams with deliberate goals.

Roll on or choose a result from the Warrior Roles table to inspire the creation of different sorts of warriors.

**Warrior Roles**

`dice: [](warrior-commander-xmm.md#^warrior-roles)`

| dice: 1d10 | The Warrior Is... |
|------------|-------------------|
| 1 | A bodyguard who protects a noble. |
| 2 | A cavalry officer with an unusual steed. |
| 3 | A crusader who fights for a divine cause. |
| 4 | A duelist who claims to be unbeatable. |
| 5 | A gate guard who asks nonsensical questions. |
| 6 | A grizzled veteran who trains new recruits. |
| 7 | A hunter skilled at slaying specific monsters. |
| 8 | A retired general who is weary of battle. |
| 9 | A volunteer with a homemade weapon. |
| 10 | A young mercenary trying to prove their skill. |
^warrior-roles

> [!quote] A quote from Minsc, Hero of Baldur's Gate  
> 
> Make way, evil! I'm armed to the teeth and packing a hamster!

## Statblock

```statblock
"name": "Warrior Commander (XMM)"
"size": "Small or Medium"
"type": "humanoid"
"alignment": "Neutral"
"ac": !!int "18"
"hp": !!int "161"
"hit_dice": "19d8 + 76"
"stats":
- !!int "21"
- !!int "20"
- !!int "18"
- !!int "14"
- !!int "16"
- !!int "14"
"speed": "30 ft."
"saves":
  "Dexterity": !!int "9"
  "Wisdom": !!int "7"
  "Strength": !!int "9"
  "Constitution": !!int "8"
"skillsaves":
  "Athletics": !!int "9"
  "Insight": !!int "7"
  "Perception": !!int "7"
"senses": "passive Perception 17"
"languages": "Common plus one other language"
"cr": "10"
"actions":
- "desc": "The warrior makes three attacks, using Greatsword or Longbow in any combination."
  "name": "Multiattack"
- "desc": "Melee Attack: +9, reach 5 ft. Hit: 19 (4d6 + 5) Slashing damage.\
    \ The warrior also creates one of the following effects:\n\n- Sap. The target\
    \ has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) on its\
    \ next attack roll before the start of the warrior's next turn.  \n- Maneuver.\
    \ One ally who can see or hear the warrior can take a [Reaction](Compendium/rules/variant-rules/reaction-xphb.md)\
    \ to move up to half the ally's [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ without provoking Opportunity Attacks.  "
  "name": "Greatsword"
- "desc": "Ranged Attack: +9, range 150/600 ft. Hit: 18 (3d8 + 5) Piercing\
    \ damage, and the target's [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ decreases by 10 feet until the end of the target's next turn."
  "name": "Longbow"
"bonus_actions":
- "desc": "The warrior moves up to half its [Speed](Compendium/rules/variant-rules/speed-xphb.md)\
    \ straight toward an enemy it can see without provoking Opportunity Attacks."
  "name": "Tactical Charge"
"reactions":
- "desc": "Trigger: The warrior is hit by an attack roll. Response: The warrior adds\
    \ 4 to its AC against that attack, possibly causing it to miss. On a miss, the\
    \ warrior can make one Greatsword or Longbow attack against the attacker."
  "name": "Counterattack"
"source":
- "XMM"
```
^statblock