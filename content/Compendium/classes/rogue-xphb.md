---
obsidianUIMode: preview
cssclasses: json5e-class
tags:
- ttrpg-cli/class/rogue
- ttrpg-cli/compendium/src/5e/xphb
aliases: ["Rogue"]
---
# Rogue
*Source: Player's Handbook (2024) p. 128. Available in the Free Rules (2024)*  

> [!tldr] Class and Feature Progression
> 
> <table class="class-progression">
> <thead>
> <tr><th colspan='4'></th></tr>
> <tr class="class-progression"><th class"level">Level</th><th class"pb">PB</th><th class"feature">Features</th><th class="value">Sneak Attack</th></tr>
> </thead><tbody>
> <tr class="class-progression"><td class"level">1st</td><td class"pb">+2</td><td class"feature"><a href='#Expertise%20(Level%201)'>Expertise</a>, <a href='#Sneak%20Attack%20(Level%201)'>Sneak Attack</a>, <a href='#Thieves'%20Cant%20(Level%201)'>Thieves' Cant</a>, <a href='#Weapon%20Mastery%20(Level%201)'>Weapon Mastery</a></td><td class="value">1d6</td></tr>
> <tr class="class-progression"><td class"level">2nd</td><td class"pb">+2</td><td class"feature"><a href='#Cunning%20Action%20(Level%202)'>Cunning Action</a></td><td class="value">1d6</td></tr>
> <tr class="class-progression"><td class"level">3rd</td><td class"pb">+2</td><td class"feature"><a href='#Rogue%20Subclass%20(Level%203)'>Rogue Subclass</a>, <a href='#Steady%20Aim%20(Level%203)'>Steady Aim</a></td><td class="value">2d6</td></tr>
> <tr class="class-progression"><td class"level">4th</td><td class"pb">+2</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%204)'>Ability Score Improvement</a></td><td class="value">2d6</td></tr>
> <tr class="class-progression"><td class"level">5th</td><td class"pb">+3</td><td class"feature"><a href='#Cunning%20Strike%20(Level%205)'>Cunning Strike</a>, <a href='#Uncanny%20Dodge%20(Level%205)'>Uncanny Dodge</a></td><td class="value">3d6</td></tr>
> <tr class="class-progression"><td class"level">6th</td><td class"pb">+3</td><td class"feature"><a href='#Expertise%20(Level%206)'>Expertise</a></td><td class="value">3d6</td></tr>
> <tr class="class-progression"><td class"level">7th</td><td class"pb">+3</td><td class"feature"><a href='#Evasion%20(Level%207)'>Evasion</a>, <a href='#Reliable%20Talent%20(Level%207)'>Reliable Talent</a></td><td class="value">4d6</td></tr>
> <tr class="class-progression"><td class"level">8th</td><td class"pb">+3</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%208)'>Ability Score Improvement</a></td><td class="value">4d6</td></tr>
> <tr class="class-progression"><td class"level">9th</td><td class"pb">+4</td><td class"feature"><a href='#Subclass%20Feature%20(Level%209)'>Subclass Feature</a></td><td class="value">5d6</td></tr>
> <tr class="class-progression"><td class"level">10th</td><td class"pb">+4</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%2010)'>Ability Score Improvement</a></td><td class="value">5d6</td></tr>
> <tr class="class-progression"><td class"level">11th</td><td class"pb">+4</td><td class"feature"><a href='#Improved%20Cunning%20Strike%20(Level%2011)'>Improved Cunning Strike</a></td><td class="value">6d6</td></tr>
> <tr class="class-progression"><td class"level">12th</td><td class"pb">+4</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%2012)'>Ability Score Improvement</a></td><td class="value">6d6</td></tr>
> <tr class="class-progression"><td class"level">13th</td><td class"pb">+5</td><td class"feature"><a href='#Subclass%20Feature%20(Level%2013)'>Subclass Feature</a></td><td class="value">7d6</td></tr>
> <tr class="class-progression"><td class"level">14th</td><td class"pb">+5</td><td class"feature"><a href='#Devious%20Strikes%20(Level%2014)'>Devious Strikes</a></td><td class="value">7d6</td></tr>
> <tr class="class-progression"><td class"level">15th</td><td class"pb">+5</td><td class"feature"><a href='#Slippery%20Mind%20(Level%2015)'>Slippery Mind</a></td><td class="value">8d6</td></tr>
> <tr class="class-progression"><td class"level">16th</td><td class"pb">+5</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%2016)'>Ability Score Improvement</a></td><td class="value">8d6</td></tr>
> <tr class="class-progression"><td class"level">17th</td><td class"pb">+6</td><td class"feature"><a href='#Subclass%20Feature%20(Level%2017)'>Subclass Feature</a></td><td class="value">9d6</td></tr>
> <tr class="class-progression"><td class"level">18th</td><td class"pb">+6</td><td class"feature"><a href='#Elusive%20(Level%2018)'>Elusive</a></td><td class="value">9d6</td></tr>
> <tr class="class-progression"><td class"level">19th</td><td class"pb">+6</td><td class"feature"><a href='#Epic%20Boon%20(Level%2019)'>Epic Boon</a></td><td class="value">10d6</td></tr>
> <tr class="class-progression"><td class"level">20th</td><td class"pb">+6</td><td class"feature"><a href='#Stroke%20of%20Luck%20(Level%2020)'>Stroke of Luck</a></td><td class="value">10d6</td></tr>
> </tbody></table>
^class-progession

## Hit Points

- **Hit Dice**: 1d8 per Rogue level
- **Hit Points at First Level:** 8 + CON
- **Hit Points at Higher Levels:** add 5 OR 1d8 + CON  (minimum of 1)

## Starting Rogue

- **Saving Throw Proficiencies**: Dexterity, Intelligence
- **Skill Proficiencies**: *Choose 4:* [Acrobatics](Compendium/rules/skills.md#Acrobatics), [Athletics](Compendium/rules/skills.md#Athletics), [Deception](Compendium/rules/skills.md#Deception), [Insight](Compendium/rules/skills.md#Insight), [Intimidation](Compendium/rules/skills.md#Intimidation), [Investigation](Compendium/rules/skills.md#Investigation), [Perception](Compendium/rules/skills.md#Perception), [Persuasion](Compendium/rules/skills.md#Persuasion), [Sleight of Hand](Compendium/rules/skills.md#Sleight%20of%20Hand), or [Stealth](Compendium/rules/skills.md#Stealth)
- **Weapon Proficiencies**: Simple weapons and Martial weapons that have the Finesse or Light property
- **Tool Proficiencies**: [Thieves' Tools](Compendium/items/thieves-tools-xphb.md)
- **Armor Training**: [Light armor](Compendium/rules/item-types.md#Light%20Armor)

**Starting Equipment:** *Choose A or B:* (A) [Leather Armor](Compendium/items/leather-armor-xphb.md), 2 [Daggers](Compendium/items/dagger-xphb.md), [Shortsword](Compendium/items/shortsword-xphb.md), [Shortbow](Compendium/items/shortbow-xphb.md), [20 Arrows](Compendium/items/arrows-20-xphb.md), [Quiver](Compendium/items/quiver-xphb.md), [Thieves' Tools](Compendium/items/thieves-tools-xphb.md), [Burglar's Pack](Compendium/items/burglars-pack-xphb.md), and 8 GP; or (B) 100 GP

## Multiclassing Rogue

- **Skill Proficiencies**: *Choose 1:* [Acrobatics](Compendium/rules/skills.md#Acrobatics), [Athletics](Compendium/rules/skills.md#Athletics), [Deception](Compendium/rules/skills.md#Deception), [Insight](Compendium/rules/skills.md#Insight), [Intimidation](Compendium/rules/skills.md#Intimidation), [Investigation](Compendium/rules/skills.md#Investigation), [Perception](Compendium/rules/skills.md#Perception), [Persuasion](Compendium/rules/skills.md#Persuasion), [Sleight of Hand](Compendium/rules/skills.md#Sleight%20of%20Hand), or [Stealth](Compendium/rules/skills.md#Stealth)
- **Tool Proficiencies**: [Thieves' Tools](Compendium/items/thieves-tools-xphb.md)
- **Armor Training**: [Light armor](Compendium/rules/item-types.md#Light%20Armor)

## Rogue

Rogues rely on cunning, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem. A few even learn magical tricks to supplement their other abilities. Many Rogues focus on stealth and deception, while others refine skills that help them in a dungeon environment, such as climbing, finding and disarming traps, and opening locks.

In combat, Rogues prioritize subtle strikes over brute strength. They would rather make one precise strike than wear an opponent down with a barrage of blows.

Some Rogues began their careers as criminals, while others used their cunning to fight crime. Whatever a Rogue's relation to the law, no common criminal or officer of the law can match the subtle brilliance of the greatest Rogues.

## Class Features

### Expertise (Level 1)

You gain [Expertise](Compendium/rules/variant-rules/expertise-xphb.md) in two of your skill proficiencies of your choice. [Sleight of Hand](Compendium/rules/skills.md#Sleight%20of%20Hand) and [Stealth](Compendium/rules/skills.md#Stealth) are recommended if you have proficiency in them.

At Rogue level 6, you gain [Expertise](Compendium/rules/variant-rules/expertise-xphb.md) in two more of your skill proficiencies of your choice.

### Sneak Attack (Level 1)

You know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra `1d6` damage to one creature you hit with an attack roll if you have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on the roll and the attack uses a Finesse or a Ranged weapon. The extra damage's type is the same as the weapon's type.

You don't need [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on the attack roll if at least one of your allies is within 5 feet of the target, the ally doesn't have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition, and you don't have [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) on the attack roll.

The extra damage increases as you gain Rogue levels, as shown in the Sneak Attack column of the Rogue Features table.

### Thieves' Cant (Level 1)

You picked up various languages in the communities where you plied your roguish talents. You know Thieves' Cant and one other language of your choice, which you choose from the language tables in "chapter 2".

### Weapon Mastery (Level 1)

Your training with weapons allows you to use the [weapon mastery properties](Compendium/rules/variant-rules/weapon-mastery-properties-xphb.md) of two kinds of weapons of your choice with which you have proficiency, such as [Daggers](Compendium/items/dagger-xphb.md) and [Shortbows](Compendium/items/shortbow-xphb.md).

Whenever you finish a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md), you can change the kinds of weapons you chose. For example, you could switch to using the [weapon mastery properties](Compendium/rules/variant-rules/weapon-mastery-properties-xphb.md) of [Scimitars](Compendium/items/scimitar-xphb.md) and [Shortswords](Compendium/items/shortsword-xphb.md).

### Cunning Action (Level 2)

Your quick thinking and agility allow you to move and act quickly. On your turn, you can take one of the following actions as a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md): [Dash](Compendium/rules/actions.md#Dash), [Disengage](Compendium/rules/actions.md#Disengage), or [Hide](Compendium/rules/actions.md#Hide).

### Rogue Subclass (Level 3)

You gain a Rogue subclass of your choice. A subclass is a specialization that grants you features at certain Rogue levels. For the rest of your career, you gain each of your subclass's features that are of your Rogue level or lower.

### Steady Aim (Level 3)

As a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md), you give yourself [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on your next attack roll on the current turn. You can use this feature only if you haven't moved during this turn, and after you use it, your [Speed](Compendium/rules/variant-rules/speed-xphb.md) is 0 until the end of the current turn.

### Ability Score Improvement (Level 4)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify. You gain this feature again at Rogue levels 8, 10, 12, and 16.

### Cunning Strike (Level 5)

You've developed cunning ways to use your Sneak Attack. When you deal Sneak Attack damage, you can add one of the following Cunning Strike effects. Each effect has a die cost, which is the number of Sneak Attack damage dice you must forgo to add the effect. You remove the die before rolling, and the effect occurs immediately after the attack's damage is dealt. For example, if you add the Poison effect, remove `1d6` from the Sneak Attack's damage before rolling.

If a Cunning Strike effect requires a saving throw, the DC equals 8 plus your Dexterity modifier and [Proficiency](Compendium/rules/variant-rules/proficiency-xphb.md).

### Poison (Cost: 1d6) (Level 5)

You add a toxin to your strike, forcing the target to make a Constitution saving throw. On a failed save, the target has the [Poisoned](Compendium/rules/conditions.md#Poisoned) condition for 1 minute. At the end of each of its turns, the [Poisoned](Compendium/rules/conditions.md#Poisoned) target repeats the save, ending the effect on itself on a success.

To use this effect, you must have a [Poisoner's Kit](Compendium/items/poisoners-kit-xphb.md) on your person.

### Trip (Cost: 1d6) (Level 5)

If the target is Large or smaller, it must succeed on a Dexterity saving throw or have the [Prone](Compendium/rules/conditions.md#Prone) condition.

### Withdraw (Cost: 1d6) (Level 5)

Immediately after the attack, you move up to half your [Speed](Compendium/rules/variant-rules/speed-xphb.md) without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack).

### Uncanny Dodge (Level 5)

When an attacker that you can see hits you with an attack roll, you can take a [Reaction](Compendium/rules/variant-rules/reaction-xphb.md) to halve the attack's damage against you (round down).

### Expertise (Level 6)

You gain [Expertise](Compendium/rules/variant-rules/expertise-xphb.md) in two of your Skill Proficiencies of your choice.

### Evasion (Level 7)

You can nimbly dodge out of the way of certain dangers. When you're subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. You can't use this feature if you have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition.

### Reliable Talent (Level 7)

Whenever you make an ability check that uses one of your skill or tool proficiencies, you can treat a `d20` roll of 9 or lower as a 10.

### Ability Score Improvement (Level 8)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Subclass Feature (Level 9)

You gain a feature from your Rogue Subclass.

### Ability Score Improvement (Level 10)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Improved Cunning Strike (Level 11)

You can use up to two Cunning Strike effects when you deal Sneak Attack damage, paying the die cost for each effect.

### Ability Score Improvement (Level 12)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Subclass Feature (Level 13)

You gain a feature from your Rogue Subclass.

### Devious Strikes (Level 14)

You've practiced new ways to use your Sneak Attack deviously. The following effects are now among your Cunning Strike options.

### Daze (Cost: 2d6) (Level 14)

The target must succeed on a Constitution saving throw, or on its next turn, it can do only one of the following: move or take an action or a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md).

### Knock Out (Cost: 6d6) (Level 14)

The target must succeed on a Constitution saving throw, or it has the [Unconscious](Compendium/rules/conditions.md#Unconscious) condition for 1 minute or until it takes any damage. The [Unconscious](Compendium/rules/conditions.md#Unconscious) target repeats the save at the end of each of its turns, ending the effect on itself on a success.

### Obscure (Cost: 3d6) (Level 14)

The target must succeed on a Dexterity saving throw, or it has the [Blinded](Compendium/rules/conditions.md#Blinded) condition until the end of its next turn.

### Slippery Mind (Level 15)

Your cunning mind is exceptionally difficult to control. You gain proficiency in Wisdom and Charisma saving throws.

### Ability Score Improvement (Level 16)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Subclass Feature (Level 17)

You gain a feature from your Rogue Subclass.

### Elusive (Level 18)

You're so evasive that attackers rarely gain the upper hand against you. No attack roll can have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) against you unless you have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition.

### Epic Boon (Level 19)

You gain an Epic Boon feat or another feat of your choice for which you qualify. [Boon of the Night Spirit](Compendium/feats/boon-of-the-night-spirit-xphb.md) is recommended.

### Stroke of Luck (Level 20)

You have a marvelous knack for succeeding when you need to. If you fail a [D20 Test](Compendium/rules/variant-rules/d20-test-xphb.md), you can turn the roll into a 20.

Once you use this feature, you can't use it again until you finish a [Short Rest](Compendium/rules/variant-rules/short-rest-xphb.md) or [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md).