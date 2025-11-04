---
obsidianUIMode: preview
cssclasses: json5e-class
tags:
- ttrpg-cli/class/barbarian
- ttrpg-cli/compendium/src/5e/xphb
aliases: ["Barbarian"]
---
# Barbarian
*Source: Player's Handbook (2024) p. 50*  

> [!tldr] Class and Feature Progression
> 
> <table class="class-progression">
> <thead>
> <tr><th colspan='6'></th></tr>
> <tr class="class-progression"><th class"level">Level</th><th class"pb">PB</th><th class"feature">Features</th><th class="value">Rages</th><th class="value">Rage Damage</th><th class="value">Weapon Mastery</th></tr>
> </thead><tbody>
> <tr class="class-progression"><td class"level">1st</td><td class"pb">+2</td><td class"feature"><a href='#Rage%20(Level%201)'>Rage</a>, <a href='#Unarmored%20Defense%20(Level%201)'>Unarmored Defense</a>, <a href='#Weapon%20Mastery%20(Level%201)'>Weapon Mastery</a></td><td class="value">2</td><td class="value">+2</td><td class="value">2</td></tr>
> <tr class="class-progression"><td class"level">2nd</td><td class"pb">+2</td><td class"feature"><a href='#Danger%20Sense%20(Level%202)'>Danger Sense</a>, <a href='#Reckless%20Attack%20(Level%202)'>Reckless Attack</a></td><td class="value">2</td><td class="value">+2</td><td class="value">2</td></tr>
> <tr class="class-progression"><td class"level">3rd</td><td class"pb">+2</td><td class"feature"><a href='#Barbarian%20Subclass%20(Level%203)'>Barbarian Subclass</a>, <a href='#Primal%20Knowledge%20(Level%203)'>Primal Knowledge</a></td><td class="value">3</td><td class="value">+2</td><td class="value">2</td></tr>
> <tr class="class-progression"><td class"level">4th</td><td class"pb">+2</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%204)'>Ability Score Improvement</a></td><td class="value">3</td><td class="value">+2</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">5th</td><td class"pb">+3</td><td class"feature"><a href='#Extra%20Attack%20(Level%205)'>Extra Attack</a>, <a href='#Fast%20Movement%20(Level%205)'>Fast Movement</a></td><td class="value">3</td><td class="value">+2</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">6th</td><td class"pb">+3</td><td class"feature"><a href='#Subclass%20Feature%20(Level%206)'>Subclass Feature</a></td><td class="value">4</td><td class="value">+2</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">7th</td><td class"pb">+3</td><td class"feature"><a href='#Feral%20Instinct%20(Level%207)'>Feral Instinct</a>, <a href='#Instinctive%20Pounce%20(Level%207)'>Instinctive Pounce</a></td><td class="value">4</td><td class="value">+2</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">8th</td><td class"pb">+3</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%208)'>Ability Score Improvement</a></td><td class="value">4</td><td class="value">+2</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">9th</td><td class"pb">+4</td><td class"feature"><a href='#Brutal%20Strike%20(Level%209)'>Brutal Strike</a></td><td class="value">4</td><td class="value">+3</td><td class="value">3</td></tr>
> <tr class="class-progression"><td class"level">10th</td><td class"pb">+4</td><td class"feature"><a href='#Subclass%20Feature%20(Level%2010)'>Subclass Feature</a></td><td class="value">4</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">11th</td><td class"pb">+4</td><td class"feature"><a href='#Relentless%20Rage%20(Level%2011)'>Relentless Rage</a></td><td class="value">4</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">12th</td><td class"pb">+4</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%2012)'>Ability Score Improvement</a></td><td class="value">5</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">13th</td><td class"pb">+5</td><td class"feature"><a href='#Improved%20Brutal%20Strike%20(Level%2013)'>Improved Brutal Strike</a></td><td class="value">5</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">14th</td><td class"pb">+5</td><td class"feature"><a href='#Subclass%20Feature%20(Level%2014)'>Subclass Feature</a></td><td class="value">5</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">15th</td><td class"pb">+5</td><td class"feature"><a href='#Persistent%20Rage%20(Level%2015)'>Persistent Rage</a></td><td class="value">5</td><td class="value">+3</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">16th</td><td class"pb">+5</td><td class"feature"><a href='#Ability%20Score%20Improvement%20(Level%2016)'>Ability Score Improvement</a></td><td class="value">5</td><td class="value">+4</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">17th</td><td class"pb">+6</td><td class"feature"><a href='#Improved%20Brutal%20Strike%20(Level%2017)'>Improved Brutal Strike</a></td><td class="value">6</td><td class="value">+4</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">18th</td><td class"pb">+6</td><td class"feature"><a href='#Indomitable%20Might%20(Level%2018)'>Indomitable Might</a></td><td class="value">6</td><td class="value">+4</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">19th</td><td class"pb">+6</td><td class"feature"><a href='#Epic%20Boon%20(Level%2019)'>Epic Boon</a></td><td class="value">6</td><td class="value">+4</td><td class="value">4</td></tr>
> <tr class="class-progression"><td class"level">20th</td><td class"pb">+6</td><td class"feature"><a href='#Primal%20Champion%20(Level%2020)'>Primal Champion</a></td><td class="value">6</td><td class="value">+4</td><td class="value">4</td></tr>
> </tbody></table>
^class-progession

## Hit Points

- **Hit Dice**: 1d12 per Barbarian level
- **Hit Points at First Level:** 12 + CON
- **Hit Points at Higher Levels:** add 7 OR 1d12 + CON  (minimum of 1)

## Starting Barbarian

- **Saving Throw Proficiencies**: Constitution, Strength
- **Skill Proficiencies**: *Choose 2:* [Animal Handling](Compendium/rules/skills.md#Animal%20Handling), [Athletics](Compendium/rules/skills.md#Athletics), [Intimidation](Compendium/rules/skills.md#Intimidation), [Nature](Compendium/rules/skills.md#Nature), [Perception](Compendium/rules/skills.md#Perception), or [Survival](Compendium/rules/skills.md#Survival)
- **Weapon Proficiencies**: Simple weapons and Martial weapons
- **Armor Training**: [Light armor](Compendium/rules/item-types.md#Light%20Armor), [Medium armor](Compendium/rules/item-types.md#Medium%20Armor), and [Shields](Compendium/items/shield-xphb.md)

**Starting Equipment:** *Choose A or B:* (A) [Greataxe](Compendium/items/greataxe-xphb.md), 4 [Handaxes](Compendium/items/handaxe-xphb.md), [Explorer's Pack](Compendium/items/explorers-pack-xphb.md), and 15 GP; or (B) 75 GP

## Multiclassing Barbarian

- **Weapon Proficiencies**: Martial weapons
- **Armor Training**: [Shields](Compendium/items/shield-xphb.md)

## Barbarian

Barbarians are mighty warriors who are powered by primal forces of the multiverse that manifest as a Rage. More than a mere emotion—and not limited to anger—this Rage is an incarnation of a predator's ferocity, a storm's fury, and a sea's turmoil.

Some Barbarians personify their Rage as a fierce spirit or revered forebear. Others see it as a connection to the pain and anguish of the world, as an impersonal tangle of wild magic, or as an expression of their own deepest self. For every Barbarian, their Rage is a power that fuels not just battle prowess, but also uncanny reflexes and heightened senses.

Barbarians often serve as protectors and leaders in their communities. They charge headlong into danger so those under their protection don't have to. Their courage in the face of danger makes Barbarians perfectly suited for adventure.

## Class Features

### Rage (Level 1)

You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md) if you aren't wearing Heavy armor.

You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a [Short Rest](Compendium/rules/variant-rules/short-rest-xphb.md), and you regain all expended uses when you finish a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md).

While active, your Rage follows the rules below.

#### Damage Resistance

You have [Resistance](Compendium/rules/variant-rules/resistance-xphb.md) to Bludgeoning, Piercing, and Slashing damage.

#### Rage Damage

When you make an attack using Strength—with either a weapon or an [Unarmed Strike](Compendium/rules/variant-rules/unarmed-strike-xphb.md)—and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian, as shown in the Rage Damage column of the Barbarian Features table.

#### Strength Advantage

You have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Strength checks and Strength saving throws.

#### No Concentration or Spells

You can't maintain [Concentration](Compendium/rules/conditions.md#Concentration), and you can't cast spells.

#### Duration

The Rage lasts until the end of your next turn, and it ends early if you don Heavy armor or have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition. If your Rage is still active on your next turn, you can extend the Rage for another round by doing one of the following:

- Make an attack roll against an enemy.  
- Force an enemy to make a saving throw.  
- Take a [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md) to extend your Rage.  

Each time the Rage is extended, it lasts until the end of your next turn. You can maintain a Rage for up to 10 minutes.

### Unarmored Defense (Level 1)

While you aren't wearing any armor, your base [Armor Class](Compendium/rules/variant-rules/armor-class-xphb.md) equals 10 plus your Dexterity and Constitution modifiers. You can use a [Shield](Compendium/items/shield-xphb.md) and still gain this benefit.

### Weapon Mastery (Level 1)

Your training with weapons allows you to use the [weapon mastery properties](Compendium/rules/variant-rules/weapon-mastery-properties-xphb.md) of two kinds of Simple or Martial Melee weapons of your choice, such as [Greataxes](Compendium/items/greataxe-xphb.md) and [Handaxes](Compendium/items/handaxe-xphb.md). Whenever you finish a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md), you can practice weapon drills and change one of those weapon choices.

When you reach certain Barbarian levels, you gain the ability to use the [weapon mastery properties](Compendium/rules/variant-rules/weapon-mastery-properties-xphb.md) of more kinds of weapons, as shown in the Weapon Mastery column of the Barbarian Features table.

### Danger Sense (Level 2)

You gain an uncanny sense of when things aren't as they should be, giving you an edge when you dodge perils. You have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Dexterity saving throws unless you have the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition.

### Reckless Attack (Level 2)

You can throw aside all concern for defense to attack with increased ferocity. When you make your first attack roll on your turn, you can decide to attack recklessly. Doing so gives you [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on attack rolls using Strength until the start of your next turn, but attack rolls against you have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) during that time.

### Barbarian Subclass (Level 3)

You gain a Barbarian subclass of your choice. A subclass is a specialization that grants you features at certain Barbarian levels. For the rest of your career, you gain each of your subclass's features that are of your Barbarian level or lower.

### Primal Knowledge (Level 3)

You gain proficiency in another skill of your choice from the skill list available to Barbarians at level 1.

In addition, while your Rage is active, you can channel primal power when you attempt certain tasks; whenever you make an ability check using one of the following skills, you can make it as a Strength check even if it normally uses a different ability: [Acrobatics](Compendium/rules/skills.md#Acrobatics), [Intimidation](Compendium/rules/skills.md#Intimidation), [Perception](Compendium/rules/skills.md#Perception), [Stealth](Compendium/rules/skills.md#Stealth), or [Survival](Compendium/rules/skills.md#Survival). When you use this ability, your Strength represents primal power coursing through you, honing your agility, bearing, and senses.

### Ability Score Improvement (Level 4)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify. You gain this feature again at Barbarian levels 8, 12, and 16.

### Extra Attack (Level 5)

You can attack twice instead of once whenever you take the [Attack](Compendium/rules/actions.md#Attack) action on your turn.

### Fast Movement (Level 5)

Your speed increases by 10 feet while you aren't wearing Heavy armor.

### Subclass Feature (Level 6)

You gain a feature from your Barbarian subclass.

### Feral Instinct (Level 7)

Your instincts are so honed that you have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on [Initiative](Compendium/rules/variant-rules/initiative-xphb.md) rolls.

### Instinctive Pounce (Level 7)

As part of the [Bonus Action](Compendium/rules/variant-rules/bonus-action-xphb.md) you take to enter your Rage, you can move up to half your [Speed](Compendium/rules/variant-rules/speed-xphb.md).

### Ability Score Improvement (Level 8)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Brutal Strike (Level 9)

If you use Reckless Attack, you can forgo any [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on one Strength-based attack roll of your choice on your turn. The chosen attack roll mustn't have [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md). If the chosen attack roll hits, the target takes an extra `1d10` damage of the same type dealt by the weapon or [Unarmed Strike](Compendium/rules/variant-rules/unarmed-strike-xphb.md), and you can cause one Brutal Strike effect of your choice. You have the following effect options.

#### Forceful Blow

The target is pushed 15 feet straight away from you. You can then move up to half your [Speed](Compendium/rules/variant-rules/speed-xphb.md) straight toward the target without provoking [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack).

#### Hamstring Blow

The target's [Speed](Compendium/rules/variant-rules/speed-xphb.md) is reduced by 15 feet until the start of your next turn. A target can be affected by only one Hamstring Blow at a time—the most recent one.

### Subclass Feature (Level 10)

You gain a feature from your Barbarian subclass.

### Relentless Rage (Level 11)

Your Rage can keep you fighting despite grievous wounds. If you drop to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) while your Rage is active and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, your [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) instead change to a number equal to twice your Barbarian level.

Each time you use this feature after the first, the DC increases by 5. When you finish a [Short Rest](Compendium/rules/variant-rules/short-rest-xphb.md) or [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md), the DC resets to 10.

### Ability Score Improvement (Level 12)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Improved Brutal Strike (Level 13)

You have honed new ways to attack furiously. The following effects are now among your Brutal Strike options.

#### Staggering Blow

The target has [Disadvantage](Compendium/rules/variant-rules/disadvantage-xphb.md) on the next saving throw it makes, and it can't make [Opportunity Attacks](Compendium/rules/actions.md#Opportunity%20Attack) until the start of your next turn.

#### Sundering Blow

Before the start of your next turn, the next attack roll made by another creature against the target gains a +5 bonus to the roll. An attack roll can gain only one Sundering Blow bonus.

### Subclass Feature (Level 14)

You gain a feature from your Barbarian subclass.

### Persistent Rage (Level 15)

When you roll [Initiative](Compendium/rules/variant-rules/initiative-xphb.md), you can regain all expended uses of Rage. After you regain uses of Rage in this way, you can't do so again until you finish a [Long Rest](Compendium/rules/variant-rules/long-rest-xphb.md).

In addition, your Rage is so fierce that it now lasts for 10 minutes without you needing to do anything to extend it from round to round. Your Rage ends early if you have the [Unconscious](Compendium/rules/conditions.md#Unconscious) condition (not just the [Incapacitated](Compendium/rules/conditions.md#Incapacitated) condition) or don Heavy armor.

### Ability Score Improvement (Level 16)

You gain the [Ability Score Improvement](Compendium/feats/ability-score-improvement-xphb.md) feat or another feat of your choice for which you qualify.

### Improved Brutal Strike (Level 17)

The extra damage of your Brutal Strike increases to `2d10`. In addition, you can use two different Brutal Strike effects whenever you use your Brutal Strike feature.

### Indomitable Might (Level 18)

If your total for a Strength check or Strength saving throw is less than your Strength score, you can use that score in place of the total.

### Epic Boon (Level 19)

You gain an Epic Boon feat or another feat of your choice for which you qualify. [Boon of Irresistible Offense](Compendium/feats/boon-of-irresistible-offense-xphb.md) is recommended.

### Primal Champion (Level 20)

You embody primal power. Your Strength and Constitution scores increase by 4, to a maximum of 25.