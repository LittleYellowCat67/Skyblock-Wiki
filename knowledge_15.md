Source: Hypixel SkyBlock Wiki (https://hypixelskyblock.minecraft.wiki/), license: CC BY-NC-SA 3.0.
How to use this knowledge base when answering questions about Hypixel SkyBlock Wiki:
- Answer from this content only. If it is not covered, say so; never guess numbers.
- Find relevant pages in index.md by title, aliases (aka) and categories.
- [[X]] links to page X; [[X|y]] and 'y ([[X]])' are text y linking to X. Follow links and each page's 'Linked from' list to gather related facts (e.g. where an item drops or is used).
- Cite the [[Page]] each fact comes from. Reply in the user's language.

(part 15/96)

# Damage Calculation/Additive Sources
Categories: Confirmations needed
|Name|Description|Implementation|
|-|-|-|
[Swords]
|[[Hollow Wand]] Ability Ichor Pool|Grant […] +30% Damage […] Stacks up to 3 times.|Additive Buff=30×stacks|
[Bows]
|Name|Description|Implementation|
|-|-|-|
|[[Warden Helmet]] Ability: Brute Force|Halves your [[Speed]] but grants +20% base weapon damage for every 25 [[Speed]].|Additive Buff=20×Speed25+1|
|[[Magma Lord Armor]] Pieces|Damage taken from [[Magmatic]] mobs is reduced […] and damage dealt is increased by 1.3x.|Additive Buff=30×Pieces|
|[[Thunder Armor]] Pieces|Damage taken from [[Magmatic]] mobs is reduced […] and damage dealt is increased by 1.2x.|Additive Buff=20×Pieces[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
|[[Taurus Helmet]], [[Flaming Chestplate]] and [[Moogma Leggings]]|Damage taken from [[Magmatic]] mobs is reduced […] and damage dealt is increased by 1.1x.|Additive Buff=10×Pieces[Confirm]|
|[[Tuxedo]] Full Set Bonus: Dashing|Max health set to n [[Health]] . Deal +k% more [[Damage]]!; n = { 75, 150, 250 }; k = { 75, 100, 150 }|Additive Buff=k|
|[[Final Destination Armor]] Full Set Bonus: Vivacious Darkness|+100% [[Damage]] against Endermen|Additive Buff=100; Condition: Endermen ([[Enderman]]) including Zealots ([[Zealot]]), Zealot Bruisers ([[Zealot Bruiser]]), Voidling Fanatics ([[Voidling Fanatic]]), and Voidling Extremists ([[Voidling Extremist]]).[Confirm]|
|[[Maxor's Armor]]|[…] and increases your arrow damage by 5% per piece.|Additive Buff=5×Pieces|
|[[Terror Armor]]|[…] arrow attacks grant 1 stack of Hydra Strike ⁑. Each Hydra Strike ⁑ stack grants +k% Damage.; k = [ 2, 15 ]|Additive Buff=k×stacks|
|[[Crimson Armor]] (Infernal)|[…] melee attacks gain 1 stack of ᝐ Dominus.; Each ᝐ Dominus stack grants […] and 10% Damage.|Additive Buff=10×stacks; Condition: Melee Damage ([[Damage Calculation]])|
|[[Crimson Armor]] Swipe|At 10 stacks also swipe in a random direction hitting every enemy in the path of the swipe.; The first time an enemy is hit by a swipe, it takes double the usual damage.; Swipe Strength = [ 0.5, 3 ]|The initiating Hits Damage and Additive Multiplier are used to calculate the Damage of the swipe:; Damageswipe=DamageHit×Swipe Strength×100Additive MultiplierHit; Due to this, Crimson Swipe can be treated as an increase of the Additive Multiplier, separated into a second hit.|
|[[Reaper Armor]]|Trolling The Reaper: Deal +100% damage to Undead ([[Undead (Mob Type)]]) Mobs but 1% to all other Mobs.|Multiplier={Undead enemies:Additive Buff=100Non-Undead enemies:Multiplicative Multiplier=0.01|
|[[Tarantula Armor]]|Every 4th strike, deal +100% [[Damage]]|Additive Buff=200|
|[[Primordial Armor]]|Every 3rd strike, deal +50% [[Damage]]|Additive Buff=150[Confirm]|
||
||
[Necklaces]
[Belts]
[Cloaks]
[Bracelet]
[Gloves]
#### Pets
|Name|Description|Implementation|
|-|-|-|
|[[Golden Dragon Pet]] Legendary Treasure perk|Gain +k% damage for every million coins in your bank. (Max 1000·k%); k = [ 0.12625, 0.25 ]; 1000·k = [ 126.25, 250 ]|Additive Buff=min⁡(k×⌊coins in bank1000000⌋,1000×k)|
|[[Lion Pet]] King of the Jungle perk|Deal +k% damage against mobs that have attacked you.; k = [ 1.5, 150 ]|Additive Buff=k; Condition: Description accurate[Confirm].|
|[[Wither Skeleton Pet]] Perk Wither Blood|Deal k% more damage against [[Wither]] mobs.; k = [ 1, 100 ]|Additive Buff=k|
|[[Kuudra Pet]] Perk Kuudra Specialist|Increases all damage to Kuudra and his minions by 20%.|Additive Buff=20|
|[[Ender Dragon Pet]] Perk End Strike|Deal +k% more damage to [[Ender]] mobs.; k = [ 2, 200 ]|Additive Buff=k|
|[[Pigman Pet]] Perk Giant Slayer|Deal +k% damage to monsters Level 50+ and +n% damage to monsters Level 100+.|Additive Buff= {Level<50:050≤Level<100:kLevel≥100:n|
|[[Skeleton Pet]] Perk Bone Arrows|Increase arrow damage by k% which is doubled while in dungeons.; k = [ 0.1, 75 ]|Additive Buff=2×k|
|[[Tiger Pet]] Perk Apex Predator|Deal +k% damage against targets with no other mobs within 15 blocks.; k = [ 1, 100 ]|Additive Buff=k|
|[[Zombie Pet]] Perk Rotten Blade|Deal k% more damage to Undead ([[Undead (Mob Type)]]) mobs.; k = [ 26.25, 150 ]|Additive Buff=k|
|[[Lion Pet]] Perk First Pounce|[[First Strike]], [[Triple-Strike]] and [[Combo]] are k% more effective.; k = [ 1, 100 ]|[Confirm]|
|[[Megalodon Pet]] Perk Blood Scent|Deal up to +k% Damage based on the enemy's missing health.; k = [ 51, 150 ]|Additive Buff=k|
|[[T-Rex Pet]] Perk Close Combat|Deal k% more damage to enemies within 1.5 blocks.; k = [ 1.5, 150 ]|Additive Buff=k|
|[[Giraffe Pet]] Perk Long Neck|Increases your melee damage by k% if you are more than 3 blocks away from the target.; k = [ 50.5, 100 ]|Additive Buff=k|
#### Pet Items
|Name|Description|Implementation|
|Name|Description|Implementation|
|-|-|-|
|[[Ring of Love]]|Grants a 1 in X chance to deal +100% damage.|Additive Buff=100|
|[[Runeblade Talisman]], [[Runeblade Ring]] and [[Runeblade Artifact]].|Increases the [[Damage]] dealt to [[Woodland]] mobs by k%.|Additive Buff=k[Confirm]|
|[[Draconic Talisman]], [[Draconic Ring]] and [[Draconic Artifact]].|Increases damage dealt to Dragons ([[Ender Dragon]]) by k%.|Additive Buff=k|
|Name|Description|Implementation|Applied To|
|-|-|-|-|
|[[Optical Lens]] Reforge Precise ([[Reforging]])|Deal +10% extra damage when arrows hit the head of a mob.|Additive Buff=10|[[Bows]]|
|[[Kaleidoscopic Mineral]] Reforge Headstrong ([[Reforging]])|Deal +8% extra damage when arrows hit the head of a mob.|Additive Buff=8|[[Bows]]|
#### Sword
|Name|Description|Value(s)|Implementation|Described Condition Accurate|
|-|-|-|-|-|
|[[Sharpness]]|Increases melee damage dealt by k%.|5, 10, 15, 20, 30, 40, 50|Additive Buff=k|yes|
|[[Prosecute]]|Increases damage dealt by k% for every percent of health your target has.|0.1, 0.2, 0.3, 0.4, 0.7, 1|Additive Buff=k×currentHPenemymaxHPenemy|yes|
|[[Execute]]|Increases damage dealt by k% for each percent of health missing on your target.|0.2, 0.4, 0.6, 0.8, 1, 1.25|Additive Buff=k×maxHPenemy−currentHPenemymaxHPenemy|yes|
|[[Giant Killer]]|Increases damage dealt by k% for each percentage of health your target has above you, up to n%.|k = { 0.1, 0.2, 0.3, 0.4, 0.6, 0.9, 1.2 }; n = { 5, 10, 15, 20, 30, 45, 65 }|Additive Buff=; {HPenemy≥HPplayer:min⁡(k×HPenemy−HPplayer0.01×HPplayer,n)HPenemy<HPplayer:0[Confirm]|yes|
|[[Titan Killer]]|Increases damage dealt by k% for every 100 [[Defense]] your target has, up to n%.|k = { 2, 4, 6, 8, 12, 16, 20 }; n = { 6, 12, 18, 24, 40, 60, 80 }|Additive Buff=min⁡(k×⌊defenemy100⌋,n)[Confirm]|[Confirm]|
|[[First Strike]]|Increases the melee damage dealt by k% for the first hit on a mob.|25, 50, 75, 100, 125|Additive Buff=k|yes|
|[[Triple-Strike]]|Increases the melee damage dealt by k% for the first three hits on a mob.|10, 20, 30, 40, 50|Additive Buff=k|yes|
|[[One For All]]|Removes all other enchants but increases your damage by 500%.||Additive Buff=500|yes|
#### Bow
|Name|Description|Value(s)|Implementation|Described Condition Accurate|
|-|-|-|-|-|
|[[Power]]|Increases bow damage by k%.|8, 16, 24, 32, 40, 50, 65|Additive Buff=k|yes|
|[[Snipe]]|Arrows deal +k% damage for every 10 blocks traveled.|1, 2, 3, 4|Additive Buff=Δposition×k10; Δposition is the euclidean distance between the Player position and the Enemy position at the time of arrow impact. [Confirm]|yes|
#### Fishing Rod
|Name|Description|Value(s)|Implementation|Described Condition Accurate|
|-|-|-|-|-|
|[[Spiked Hook]]|Fishing rod deals k% more damage to monsters.|5, 10, 15, 20, 25, 30, 35|Additive Buff=k|[Confirm]|
#### Armor
|Name|Description|Value(s)|Implementation|Described Condition Accurate|
|-|-|-|-|-|
|[[Habanero Tactics]]|Deal +k% damage with Slayer weapons.|20, 25|Additive Buff=k|yes|
#### Other
|Name|Description|Value(s)|Implementation|Described Condition Accurate|
|-|-|-|-|-|
|[[Gravity]]|Increase damage dealt to [[Airborne]] mobs by k%.|5, 10, 15, 20, 30, 40|Additive Buff=k|yes|
|[[Impaling]]|Increase damage dealt to [[Aquatic]] mobs by k%.|5, 10, 15, 20, 30|Additive Buff=k|yes|
|[[Bane of Arthropods]]|Increase damage dealt to [[Arthropod]] mobs by k%.|5, 10, 15, 20, 30, 40, 50|Additive Buff=k|yes|
|[[Cubism]]|Increase damage dealt to Cubic ([[Cubic (Mob Type)]]) mobs by k%.|5, 10, 15, 20, 30, 40|Additive Buff=k|yes|
|[[Ender Slayer]]|Increase damage dealt to [[Ender]] mobs by k%.|5, 10, 15, 20, 30, 40, 50|Additive Buff=k|yes|
|[[Smoldering]]|Increase damage dealt to Infernal ([[Infernal (Mob Type)]]) mobs by k%.|5, 10, 15, 20, 30|Additive Buff=k|yes|
|[[Pyroclasm]]|Increase damage dealt to [[Magmatic]] mobs by k%.|10, 20, 30, 40, 60, 80|Additive Buff=k|[Confirm]|
|[[Smite]]|Increase damage dealt to [[Skeletal]], Undead ([[Undead (Mob Type)]]) and [[Wither]] mobs by k%.|5, 10, 15, 20, 30, 40, 50|Additive Buff=k|yes|
|[[Woodsplitter]]|Increase damage dealt to [[Woodland]] mobs by k%.|5, 10, 15, 20, 30, 40|Additive Buff=k|[Confirm]|
|[[Combo]]|Increases your damage by k% per kill up to n kills within m seconds.|k = { 1, 2, 3, 4, 5 }; n = { 2, 4, 6, 8, 10 }; m = { 2, 4, 6, 8, 10 }|Additive Buff=k×min⁡(Kills,n)|[Confirm]|
|[[Swarm]]|Increases your damage by k% for each enemy within 10 blocks. Maximum of 10 enemies.|2, 4, 6, 8, 10|Additive Buff=k×min⁡(Enemies in range,10)|[Confirm]|
|Name|Description|Implementation|
|-|-|-|
|[[Thorn Shard]] Dominance|Gain +k% more Damage when at full health.|Additive Buff=k|
|[[Kada Knight Shard]] Lifeline|When under 20% maximum HP, your [[Defense]] and Damage increase by k%.|Additive Buff=k[Confirm]|
|[[Spike Shard]] Payback|When hit, your next hit deals +k% damage.|Additive Buff=k|
|[[Soul of the Alpha Shard]] Combo|Deal +k% more Damage per Grandma Wolf Pet combo.; (Max 50 combo)|Additive Buff=k×min⁡(Combo Amount,50)|
|[[Skeletor Shard]] Deadeye|Increases damage from ranged weapons by +k%.|Additive Buff=k|
|[[Barbarian Duke X Shard]] Warrior|Increases melee damage by +k%.|Additive Buff=k|
|[[Power Dragon Shard]] Elite|Grants +k% more Damage against BOSS ([[Bosses]]) and Miniboss mobs.|Additive Buff=k|
#### Ruler Attributes
Ruler Attributes give +3 Additive Damage per [[Attributes|Attribute]] level, up to +30 Additive Damage. Ruler Attributes are buffed by [[Caiman Shard]] Attribute Echo of Ruler and [[Tiamat Shard]] Attribute Echo of Echoes. With both relevant Echo Attributes at MAX Level (10), Ruler Attributes are multiplied by 1.3, resulting in a maximum increase of +39 Additive Damage.
|Name|Description|Implementation|
|-|-|-|
|[[Bluebird Shard]] Airborne Ruler|Grants +k% more Damage against [[Airborne]] mobs.|Additive Buff=k|
|[[Sprawl Shard]] Animal Ruler|Grants +k% more Damage against [[Animal]] mobs.|Additive Buff=k|
|[[Duplico Shard]] Arcane Ruler|Grants +k% more Damage against [[Arcane]] mobs.|Additive Buff=k|
|[[Flaming Spider Shard]] Arthropod Ruler|Grants +k% more Damage against [[Arthropod]] mobs.|Additive Buff=k|
|[[Shrieky Tiki Shard]] Construct Ruler|Grants +k% more Damage against [[Construct]] mobs.|Additive Buff=k|
|[[Queen Ant Shard]] Elusive Ruler|Grants +k% more Damage against [[Elusive]] mobs.|Additive Buff=k|
|[[Zealot Bruiser Shard]] Ender Ruler|Grants +k% more Damage against [[Ender]] mobs.|Additive Buff=k|
|[[Polaris Shard]] Frozen Ruler|Grants +k% more Damage against Frozen ([[Frozen (Mob Type)]]) mobs.|Additive Buff=k|
|[[Wetwing Shard]] Humanoid Ruler|Grants +k% more Damage against [[Humanoid]] mobs.|Additive Buff=k|
|[[Flare Shard]] Infernal Ruler|Grants +k% more Damage against Infernal ([[Infernal (Mob Type)]]) mobs.|Additive Buff=k|
|[[Stridersurfer Shard]] Magmatic Ruler|Grants +k% more Damage against [[Magmatic]] mobs.|Additive Buff=k|
|[[Minos Hunter Shard]] Mythological Ruler|Grants +k% more Damage against [[Mythological]] mobs.|Additive Buff=k|
|[[Praying Mantis Shard]] Pest Ruler|Grants +k% more Damage against Pest ([[Pest (Mob Type)]]) mobs.|Additive Buff=k|
|[[Chill Shard]] Skeletal Ruler|Grants +k% more Damage against [[Skeletal]] mobs.|Additive Buff=k|
|[[Driftling Shard]] Subterranean Ruler|Grants +k% more Damage against [[Subterranean]] mobs.|Additive Buff=k|
|[[Zombie Soldier Shard]] Undead Ruler|Grants +k% more Damage against Undead ([[Undead (Mob Type)]]) mobs.|Additive Buff=k|
|[[Ent Shard]] Woodland Ruler|Grants +k% more Damage against [[Woodland]] mobs.|Additive Buff=k|
|Name|Description|Implementation|
|-|-|-|
|[[Combat]] Warrior perk|Deal k% more damage to mobs.; k = [ 4 , 210 ]|Additive Buff=k|
|[[Spider Tamer]] Spider Essence Shop ([[Essence Shops]]) perk Bane|Increases [[Damage]] dealt to Spiders ([[Spider]]) by k%.; k = { 3, 6, 9, 12, 15 }|Additive Buff=k|
|Archery ([[Archery Potion]]) Potion ([[Potions]])|Increases bow damage by k%.|Additive Buff=k|
|[[Berserk]] Dungeon Class Perk Lust for Blood|Every time you hit an enemy, increases the damage you deal to that enemy by m% up to a maximum of k%.|Additive Buff=min⁡(hit count×m,k)|

# Damage Calculation/Damage Abilities
Categories: Confirmations needed
|Ability Name|Item Name|Base Ability Damage|Ability Scaling|Notes|
|-|-|-|-|-|
||[[Blast o' Lantern]]|3000|0.2||
||[[Skeleton Hat]]|50|1||
|Acupuncture|[[Voodoo Doll]]|1500|1||
|Acupuncture+|[[Jinxed Voodoo Doll]]|2222|1||
|Bat Swarm|[[Witch Mask]]|4000|1||
|Bat Swarm+|[[Vampire Witch Mask]]|3000|0.2||
|Bingo Blast|[[Bingo Blaster]]|625[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|1[Confirm]||
|Burning Souls|[[Pigman Sword]]|30000|0.1|Not affected by the Additive Multiplier.[Confirm]|
|Coin Conversion|[[The Alchemist's Staff]]|10000|0.3||
|Dragon Rage|[[Aspect of the Dragons]]|12000|0.1|Not affected by the Additive Multiplier.|
|Dreadlord|[[Dreadlord Sword]]|500|0.3||
|Explode|[[Staff of the Volcano]]|24000|0.3||
|Fire Blast|[[Ember Rod]]|30|1||
|Fire Veil|[[Fire Veil Wand]]|15000|0.3||
|Firestorm|[[Fire Fury Staff]]|42000|0.3||
|Giant's Slam|[[Giant's Sword]]|100000|0.05||
|Guided Bat|[[Spirit Sceptre]]|2000|0.2||
|Guided Bat+|[[Spirit Sceptre]]|2250|0.2||
|Ice Bolt|[[Frozen Scythe]]|1000|0.3||
|Ice Bolt+|[[Glacial Scythe]]|1500|0.3||
|Ice Bolt++|[[Glacial Scythe]]|1700|0.3||
|Ice Spray|[[Ice Spray Wand]]|17000|0.1||
|Ice Spray+|[[Ice Spray Wand]]|19000|0.1||
|Ink Bomb|[[Ink Wand]]|10000|1||
|Iron Punch|[[Golem Sword]]|250|1[Confirm]||
|Leap|[[Leaping Sword]]|350|1||
|Leap+|[[Silk-Edge Sword]]|400|1||
|Lightning Strike|[[Celeste Wand]]|40|1||
|Starfall|[[Starlight Wand]]|50|1[Confirm]||
|Molten Wave|[[Midas Staff]]; [[Midas Staff]]|43400|0.3|6,000 to 40,000 and up to 43,400 using Gold's Power 200 ([[Golden Dragon Pet]])|
|Rapid-fire|[[Jerry-chine Gun]]|500|0.2||
|Runic Zap|[[Aurora Staff]]|10000|0.2||
|Showtime|[[Bonzo's Staff]]|1000|0.2||
|Showtime+|[[Bonzo's Staff]]|1100|0.2||
|Terrain Toss|[[Yeti Sword]]|15000|0.3||
|Terrain Toss+|[[Yeti Sword]]|17000|0.3||
|Wither Impact; Implosion|Wither Impact ([[Necron's Blade Scrolls]])|10000|0.3||
Linked from: [[Ability Damage]]

# Damage Calculation/Multiplicative Sources
Categories: Confirmations needed
|Name|Description|Implementation|
|-|-|-|
[Swords]
|[[Spider Sword]]|Deal +100% damage to [[Arthropod]] mobs.|Multiplicative Multiplier=2|
|[[Recluse Fang]]|Deal +150% damage to [[Arthropod]] mobs.|Multiplicative Multiplier=2.5|
|[[Tarantula Fang]]|Deal +200% damage to [[Arthropod]] mobs.|Multiplicative Multiplier=3|
|[[Scorpion Foil]]|Deal +250% damage to [[Arthropod]] mobs.|Multiplicative Multiplier=3.5|
|[[Sting]]|Deal +300% damage to [[Arthropod]] mobs.|Multiplicative Multiplier=4|
|[[End Sword]]|Deal +100% damage to [[Ender]] mobs.|Multiplicative Multiplier=2|
|[[Voidwalker Katana]]|Deal +150% damage to Endermen.|Multiplicative Multiplier=2.5; Condition: Endermen ([[Enderman]]) including Zealots ([[Zealot]]), Zealot Bruisers ([[Zealot Bruiser]]), Voidling Fanatics ([[Voidling Fanatic]]), and Voidling Extremists ([[Voidling Extremist]]).[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
|[[Voidedge Katana]]|Deal +200% damage to Endermen.|Multiplicative Multiplier=3; Condition: Endermen ([[Enderman]]) including Zealots ([[Zealot]]), Zealot Bruisers ([[Zealot Bruiser]]), Voidling Fanatics ([[Voidling Fanatic]]), and Voidling Extremists ([[Voidling Extremist]]).[Confirm]|
|[[Vorpal Katana]]|Deal +250% damage to Endermen.|Multiplicative Multiplier=3.5; Condition: Endermen ([[Enderman]]) including Zealots ([[Zealot]]), Zealot Bruisers ([[Zealot Bruiser]]), Voidling Fanatics ([[Voidling Fanatic]]), and Voidling Extremists ([[Voidling Extremist]]).[Confirm]|
|[[Atomsplit Katana]]|Deal +300% damage to Endermen.|Multiplicative Multiplier=4; Condition: Endermen ([[Enderman]]) including Zealots ([[Zealot]]), Zealot Bruisers ([[Zealot Bruiser]]), Voidling Fanatics ([[Voidling Fanatic]]), and Voidling Extremists ([[Voidling Extremist]]).[Confirm]|
|[[Firedust Dagger]]|Deal 1.2x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 1.1x damage to [[Wither]] mobs.|Multiplicative MultiplierInfernal=1.25; Multiplicative MultiplierWither=1.1|
|[[Kindlebane Dagger]]|Deal 1.5x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 1.2x damage to [[Wither]] mobs.|Multiplicative MultiplierInfernal=1.5; Multiplicative MultiplierWither=1.2|
|[[Pyrochaos Dagger]]|Deal 2x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 1.5x damage to [[Wither]] mobs.|Multiplicative MultiplierInfernal=2; Multiplicative MultiplierWither=1.5|
|[[Twilight Dagger]]|Deal 1.5x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 1.2x damage to [[Skeletal]] mobs.|Multiplicative MultiplierInfernal=1.5; Multiplicative MultiplierSkeletal=1.25|
|[[Mawdredge Dagger]]|Deal 2.5x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 1.5x damage to [[Skeletal]] mobs.|Multiplicative MultiplierInfernal=2.5; Multiplicative MultiplierSkeletal=1.5|
|[[Deathripper Dagger]]|Deal 3.5x damage to Infernal ([[Infernal (Mob Type)]]) mobs.; Deal 2x damage to [[Skeletal]] mobs.|Multiplicative MultiplierInfernal=3.5; Multiplicative MultiplierSkeletal=2|
|[[Undead Sword]]|Deals +100% damage to Undead ([[Undead (Mob Type)]]) mobs.|Multiplicative Multiplier=2|
|[[Revenant Falchion]]|Deals +150% damage to Undead ([[Undead (Mob Type)]]) mobs.|Multiplicative Multiplier=2.5|
|[[Reaper Falchion]]|Deals +200% damage to Undead ([[Undead (Mob Type)]]) mobs.|Multiplicative Multiplier=3|
|[[Halberd of the Shredded]]|Deals +250% damage to Undead ([[Undead (Mob Type)]]) mobs.|Multiplicative Multiplier=3.5|
|[[Shaman Sword]]|Deal +100% Damage against Wolves.|Multiplicative Multiplier=1|
|[[Pooch Sword]]|Deal +200% Damage against Wolves.|Multiplicative Multiplier=2|
|[[Necron's Blade (Unrefined)]] and its refinements.|Deal +50% damage to [[Wither]] mobs.|Multiplicative Multiplier=1.5|
|[[Sword of Revelations]]|Deals 1.5x damage to [[Mythological]] mobs.|Multiplicative Multiplier=1.5|
|[[Daedalus Blade]] and [[Daedalus Blade]]|Grants +n% Damage […] on [[Mythological]] mobs per [[Bestiary]] tier you have accross all of them.; [[Mythological]] Bestiary Tiers: N; +k% Damage|Multiplicative Multiplier=1+k% [Confirm]|
|[[Soul Whip]]|Deals 2x damage to [[Sea Creatures]].|Multiplicative Multiplier=2|
|[[Flaming Flay]]|Deals 3x damage to [[Sea Creatures]].|Multiplicative Multiplier=3|
|[[Prismarine Blade]]|Deals +200% damage while in water.|Multiplicative Multiplier=3|
|[[Ice Spray Wand]] and [[Ice Spray Wand]] Ability Ice Spray|[…] freezes them in place […] Frozen mobs take 10% increased damage!|Multiplicative Multiplier=1.1|
|[[Spirit Sword]]|Deals +2% more damage to Undead ([[Undead (Mob Type)]]) mobs per 1% [[Health]] the player is missing.|Multiplicative Multiplier=1+2×HPmax−HPcurrentHPmax|
|[[Hollow Wand]] Ability Raging Wind|[…] within this pool gains 1.2x Damage […]|Multiplicative Multiplier=1.2 [Confirm]|
[Bows]
|[[Wither Bow]]|Deals +100% damage to [[Wither]] mobs.|Multiplicative Multiplier=2|
|[[Savanna Bow]]|All damage dealt with this bow is doubled.|Multiplicative Multiplier=2|
|[[Sulphur Bow]]|Consumes 1 Sulphur in your Inventory or your Quiver to deal double the damage per shot.|Multiplicative Multiplier=2|
|[[Undead Bow]], [[Super Undead Bow]] and [[Death Bow]]|Deals +100% damage to Undead ([[Undead (Mob Type)]]) mobs.|Multiplicative Multiplier=2|
|[[Spirit Shortbow]]|Deals +2% more damage to Undead ([[Undead (Mob Type)]]) mobs per 1% [[Health]] the player is missing.|Multiplicative Multiplier=1+2×HPmax−HPcurrentHPmax|
|Name|Description|Implementation|
|-|-|-|
|[[Crown of Avarice]]|[…] and deal +0.015x Damage for each digit of Coins consumed.; Coins consumed: X; X = [ 0, 1,000,000,000 ] → digits( X ) = [ 0, 10 ]|Multiplicative Multiplier=1+0.015×digits(X)|
|[[Monster Hunter Armor]]|Secret Full Set Bonus: Monster Hunter: […] and deal +25% Damage when attacking Monsters.|Multiplicative Multiplier=1.25|
|[[Monster Raider Armor]]|Secret Full Set Bonus: Monster Raider: […] and deal +35% Damage when attacking Monsters.|Multiplicative Multiplier=1.35|
|[[Reaper Armor]]|Trolling The Reaper: Deal +100% damage to Undead ([[Undead (Mob Type)]]) Mobs but 1% to all other Mobs.|Multiplier={Undead enemies:Additive Buff=100Non-Undead enemies:Multiplicative Multiplier=0.01|
|Name|Description|Implementation|
|-|-|-|
[Necklaces]
[Belts]
|[[Implosion Belt]]|Consolidated: Increases all explosion damage dealt by 25%.|Multiplicative Multiplier=1.25|
[Cloaks]
|[[Dragonfade Cloak]]|Multiplies damage dealt to Dragons by 1.01x.|Multiplicative Multiplier=1.01[Confirm]|
[Bracelet]
[Gloves]
#### Pets
|Name|Description|Implementation|
|-|-|-|
|[[Hedgehog Pet]]|Spiky Quills: Deal k% more damage to Pests ([[Pest (Mob Type)]]).; k = [1, 100]|Multiplicative Multiplier=1+k%|
|[[Bat Pet]] Perk Wings of Steel|Deals +k% damage to [[Spooky]] enemies during the [[Spooky Festival]].; k = [ 0.5, 50 ]|Multiplicative Multiplier=1+k%|
|[[Rock Pet]] Perk Steady Ground|While sitting on your rock, gain +k% damage.; k = [ 0.3, 30 ]|Multiplicative Multiplier=1+k%[Confirm]|
|[[Wither Skeleton Pet]] Perk Death's Touch|Upon hitting an enemy inflict the wither effect for k% damage over 3 seconds.; k = [ 2, 200 ]|Multiplicative MultiplierDamage-Tick=k%3|
|[[Golem Pet]] Perk Last Stand|[…] deal 40% more damage.|Multiplicative Multiplier=1+k% [Confirm]|
|[[Golem Pet]] Perk Toss|Every 5 hits, throw the enemy up into the air and deal 5x damage.|Multiplicative MultiplierToss=5 [Confirm]|
|[[Magma Cube Pet]] Perk Salt Blade|Deal k% more damage to slimes.; k = [ 0.2, 25 ]|Multiplicative Multiplier=1+k% [Confirm]|
|[[Bal Pet]] Perk Cannibal|Increases damage dealt to [[Bal]] by k%.; k = [ 1, 100 ]|Multiplicative Multiplier=1+k% [Confirm]|
#### Pet Items
|Name|Description|Implementation|
|Name|Description|Implementation|
|-|-|-|
|[[Tarantula Talisman]]|Every 10th melee hit on the same enemy deals +10% damage.|Multiplicative Multiplier=1.1|
|[[Tarantula Ring]]|Every 10th melee hit on the same enemy deals +15% damage.|Multiplicative Multiplier=1.15 [Confirm]|
|[[Book of Progression]]|When you deal damage, deal +k% the amount.|Multiplicative Multiplier=1+k%|
|Name|Description|Implementation|Applied To|
|-|-|-|-|
|[[Red Scarf]] Reforge ([[Reforging]]) Loving ([[Reforging]])|Increases ability damage by +5%.|Multiplicative Multiplier=1.05; Applied on Magic Damage ([[Damage Calculation]]) (Abilities) and [[Ferocity]].|[[Chestplates]]|
|[[Dragon Claw]] Reforge ([[Reforging]]) Fabled ([[Reforging]])|Critical hits have a chance to deal up to 15% extra damage.|Multiplicative Multiplier=1+0.15×random(); where random()∈[0,1] and every value is equally likely.[Confirm]|[[Swords]]|
|Name|Description|Implementation|
|-|-|-|
|[[Overload]]|Having a [[Crit Chance]] above 100% grants a chance to perform a Mega Critical Hit dealing k% extra damage.; k = {10, 20, 30, 40, 50}|Pmega-crit=; {CritChance<100:0%100≤CritChance≤200:CritChance−100100CritChance>200:100%; Multiplicative Multipliermega-crit=1+k%|
|[[Duplex]]|Shoot a second arrow dealing k% of the first arrow's damage. Targets hit take ( 1 + m ) times fire damage for 60s.; k = {4%, 8%, 12%, 16%, 20%}; m = {10%, 20%, 30%, 40%, 50%}|Multiplicative Multipliersecond-arrow=k; This multiplier is discarded when an arrow bounces.[Confirm]; Multiplicative Multiplierfire-damage-taken=m; This means fire damage taken actually decreases.|
|[[Thunderlord]]|Every 3 hits on a monster, strike lightning, dealing k% of the hit's damage.; k = [ 8, 16, 24, 32, 40, 50, 60 ]|Multiplicative Multiplier=k100; Condition: Melee Damage ([[Damage Calculation]])|
|[[Thunderbolt]]|Every 3 hits on a monster, strike lightning, dealing k% of the hit's damage to up to 10 monsters within 2 blocks.; k = [ 4, 8, 12, 16, 20, 25, 30 ]|Multiplicative Multiplier=k100; Condition: Melee Damage ([[Damage Calculation]])|
|Name|Description|Implementation|
|-|-|-|
|[[Twilight Arrow Poison]]|Arrows apply a Poison that increases all incoming damage by 10% for 20s.|Multiplicative Multiplier=1.1|
|[[Archer]] Dungeon Class|k% Arrow Damage|Multiplicative Multiplier=k%|
|[[Berserk]] Dungeon Class|+k% Melee Damage|Multiplicative Multiplier=1+k%|
|[[Berserk]] Dungeon Class Perk Bloodlust|Your next hit after killing a mosnter deals k% increased damage.|Multiplicative Multiplier=1+k%|
|[[Berserk]] Dungeon Class Ability Ragnarok|Grants 100 [[Attack Speed]], 400 [[Speed]], and a 50% damage increase for 15 seconds.|Multiplicative Multiplier=1.5[Confirm]; Condition: Melee Damage ([[Damage Calculation]])[Confirm]|
|[[Mage]] Dungeon Class Ability Mage Staff|All your melee weapon attacks become ranged.; Those attacks deal 30%+ of their melee damage […]|Multiplicative MultiplierMage Staff=(30%+0.9×Intelligence1000)|
|Glacial ([[Glacial (Mob Type)]]) Mob Type ([[Mob Types]])|Can only be damaged with a pickaxe or drill.; Takes significant damage from [[Pickaxes]] and [[Drills]], based on [[Breaking Power]].|Multiplicative MultiplierPick/Drill=1650×BreakingPower; Condition: Holding a Pickaxe ([[Pickaxes]]) or Drill ([[Drills]])|

# Defense
Aliases: Armor Mechanics, Defence, Defense Mechanics
Categories: Confirmations needed, Unknown Zone Referenced, Pages containing missing tooltips, More info needed, Player Statistics, Outdated pages, Temp/Using Skill Aliases, Defense, Mechanics, Pages with math equations
[Defense]
Type: Stat
Uses: Reducing Damage taken.
Increasing: [[Armor]], [[Enchantments]], Reforges ([[Reforging]]), [[Pets]], [[Mining]], Hot Potato Books ([[Hot Potato Book]]) and more
[Values]
Base Value: 0
Max Value: N/A
[Symbol]
Unicode Code Point: U+E008
Icon (The icon displayed in the Equipment Menu interface.): Iron Chestplate ()
Defense is one of the core player [[Stats]]. It determines how much [[Damage]] reduction the player has. The more Defense a player has, the less damage is taken from attacks. Defense can go to 0, but that does not have have any special effect.
Defense does not reduce [[True Damage]]; that is reduced by [[True Defense]].
## Mechanics
Chart showing damage reduction.
The more Defense the player has, the less bonus damage reduction the player will have.
The formula for damage reduction is: DefDef+100
For example, with 200 Defense , the formula is: 200200+100=200300 or ~67% damage reduction, meaning with 200 Defense, the player takes 33% of the damage from monsters that would normally be taken with 0 Defense.
This leads to a misconception that Defense above 700 is useless because the damage reduction only goes up slightly. This is incorrect, for as the difference from 0% to 50% damage reduction may seem more substantial than the jump from 90% to 95%, both are equal in that they double EHP (100–200 vs. 1000–2000).
calcpage  = Calculator:Damage Reduction
 template  = Template:Calculator/Damage_Reduction
 form      = dmgReductionCalcForm
 result    = inner

 param     = defense|Your Defense|100|int|0-999999
Loading Calculator...
If the calculator fails to load up, please report to an Administrator.
### Effective Health
[[Effective Health]] (EHP) is the amount of damage enemies need to deal to the player to kill them when Defense is factored in. If one has 100 [[Health]] and 200 Defense, they will be able to take 300 damage before dying, as shown below.
The formula for EHP is: HP×Def+100100
For example, at 200 Defense 100 [[Health]], the formula is:
100×200+100100 or 100×300100 or 100×3 or
The result is 300 [[Effective Health]], meaning with 100 [[Health]] and 200 Defense, the player can take as much damage without dying as someone who has 300 [[Health]] and 0 Defense could.
EHP is a useful metric for calculating which items are better than others in allowing the player to survive attacks.
If an attack does [[True Damage]] the players [[Effective Health]] will be calulated using [[True Defense]] instead of Defense.
## Increasing Base Defense
Players do not have any base Defense by default. There are a handful of ways to permantly increase it. These methods are always active and can't be disabled.
|Source|Amount|Total|
|-|-|-|
|Leveling [[Mining]] Level 1–14|+1 per level|+106 at level 60|
|Leveling [[Mining]] Level 14–60|+2 per level|+106 at level 60|
|Forbidden Defense ([[Essence Shops]]) perk|+1 per level|+5|
|Blessing of Time (Rift) ([[Oruo The Almighty]])|+2 per level|+6|
|[[Festering Maggot]]|+1 per level|+5|
## Increasing Bonus Defense
There are several ways to gain additional bonus non-conditional Defense. These methods will increase the players Defense stat against all mobs. They include, but are not limited to:
- Equipping most types of [[Armor]]
- Holding certain weapons (eg: [[Golem Sword]], [[Earthen Blade]], [[Wither Cloak Sword]], or [[Astraea]])
- [[Accessories]] (eg: [[Gravity Talisman]])
- Equipping certain [[Pets]] (eg: [[Turtle Pet]])
- [[Reforging]] items to certain Reforges (eg: Reinforced)
- Items with [[Gemstone|Amethyst]] gemstones in their gemstone slots
- Enchantments such as [[Protection]] or [[Refrigerate]].
- Drinking the [[Resistance Potion|Resistance]] Potion or [[God Potion]]
- Abilities such as the [[Pigman Sword]]'s Burning Souls
- Attributes such as [[Attributes|Unlimited Fortitude]]
### Pets
Certain [[Pets]] grant bonus Defense. The [[Pets|Pet]] must be equipped in order to take effect.
|Slot|Name|Rarity|Stats|Source|
|-|-|-|-|-|
|[[Ammonite Pet]]|[[Ammonite Pet]]|LEGENDARY ([[Rarity]])|Ability: Gift of the Ammonite Each [[Mining]] and [[Fishing]] level grants +0.01-0.5 [[Fishing Speed]], +0.02-2 [[Speed]] and +0.02-2 Defense.|Forging ([[The Forge]]) Recipe - [[Heart of the Mountain]] Tier 4 ([[Heart of the Mountain]])|
|[[Armadillo Pet]]|[[Armadillo Pet]]|COMMON ([[Rarity]]) - MYTHIC ([[Rarity]])|+2-200 Defense|Hatching a [[Prehistoric Egg]]|
|[[Ankylosaurus Pet]]|[[Ankylosaurus Pet]]|LEGENDARY ([[Rarity]])|+0.5-50 Defense; Ability: Unyielding; Increase the effectiveness of [[Last Stand]] and Lifeline ([[Attributes]]) by 0.5-50%.|Forging ([[The Forge]]) Recipe - [[Heart of the Mountain]] Tier 7 ([[Heart of the Mountain]])|
|[[Baby Yeti Pet]]|[[Baby Yeti Pet]]|RARE ([[Rarity]]) - MYTHIC ([[Rarity]])|Ability: Cold Breeze; Increases Combat Stats ([[Stats]]) and Fishing Stats ([[Stats]]) by (0.1%-10% RARE ([[Rarity]]) 0.2%-20% EPIC ([[Rarity]]) - MYTHIC ([[Rarity]])) (Additive)[Confirm (Confirmation needed; When this info is confirmed, remove this.)] while on [[Jerry's Workshop]].|Drop - [[Yeti]]|
|[[Bee Pet]]|[[Bee Pet]]|COMMON ([[Rarity]]) - MYTHIC ([[Rarity]])|Ability: Hive For each player within 25 blocks gain: +1.02-3 (COMMON ([[Rarity]])), +1.05-6 (UNCOMMON ([[Rarity]]) - RARE ([[Rarity]])), +1.09-10 (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]])) [[Intelligence]] +1.02-3 (COMMON ([[Rarity]])), +1.04-5 (UNCOMMON ([[Rarity]]) - RARE ([[Rarity]])), +1.07-8 (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]])) [[Strength]] +1.01-2 (COMMON ([[Rarity]])), 1.02-3 (UNCOMMON ([[Rarity]]) - RARE ([[Rarity]])), +1.04-5 (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]])) Defense Max 15 players|[[NPC]] Purchase - [[Bea]]|
|[[Blaze Pet]]|[[Blaze Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+0.3-30 Defense Ability: Nether Embodiment; Increases Combat ([[Stats]]) and Miscellaneous ([[Stats]]) stats by (0.05%-5% (COMMON ([[Rarity]])), 0.08%-7.5% (UNCOMMON ([[Rarity]]) - RARE ([[Rarity]])), 0.1%-10% (EPIC ([[Rarity]]) - LEGENDARY ([[Rarity]]))) (Additive)[Confirm] while on the [[Crimson Isle]].; Ability: Bling Armor (RARE ([[Rarity]]) - LEGENDARY ([[Rarity]]) exclusive); Upgrades [[Blaze Armor]] stats and ability by (0.35%-35% RARE ([[Rarity]]), 0.4%-40% EPIC ([[Rarity]]) - LEGENDARY ([[Rarity]])). Ability: Fusion-Style Potato (LEGENDARY ([[Rarity]]) exclusive); Double effects of Hot Potato Books ([[Hot Potato Book]]).|[[Crafting]] Recipe - Blaze Rod Collection VI (6) ([[Blaze Rod]])|
|[[Blue Whale Pet]]|[[Blue Whale Pet]]|RARE ([[Rarity]]) - LEGENDARY ([[Rarity]])|Ability: Bulk; Gain +0.01-1 Defense per (30 RARE ([[Rarity]]), 25 EPIC ([[Rarity]]), 20 LEGENDARY ([[Rarity]])) Max [[Health]].|[[NPC]] Purchase - [[Oringo]]|
|[[Elephant Pet]]|[[Elephant Pet]]|COMMON ([[Rarity]]) - MYTHIC ([[Rarity]])|Ability: Stomp; Gain (+0.1-10 (COMMON ([[Rarity]])), +0.15-15 (UNCOMMON ([[Rarity]]) - RARE ([[Rarity]])), +0.2-20 (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]]))) Defense for every 100 [[Speed]].|[[NPC]] Purchase - [[Oringo]]|
|[[Ender Dragon Pet]]|[[Ender Dragon Pet]]|LEGENDARY ([[Rarity]])|Ability: Superior Increases all Combat Stats ([[Stats]]) and [[Magic Find]] by 0.1%-10% (Additive)[Confirm].|Drop - [[Ender Dragon]]|
|[[Flying Fish Pet]]|[[Flying Fish Pet]]|RARE ([[Rarity]]) - MYTHIC ([[Rarity]])|+0.5-50 Defense Ability: Water Bender; Gives (0.8-80 (RARE ([[Rarity]])), 1-100 (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]]))) [[Strength]] and Defense when near water or lava (MYTHIC ([[Rarity]]) exclusive).; Ability: Deep Sea Diver (LEGENDARY ([[Rarity]]) - MYTHIC ([[Rarity]]) exclusive); Increases the stats of [[Magma Lord Armor]] (MYTHIC ([[Rarity]]) exclusive), [[Diver's Armor]] and [[Abyssal Armor]] by 0.2%-20%.|Drop - [[The Loch Emperor]]|
|[[Guardian Pet]]|[[Guardian Pet]]|COMMON ([[Rarity]]) - MYTHIC ([[Rarity]])|+0.5-50 Defense|Drop - Superpairs ([[Experiments]])|
|[[Hermit Crab Pet]]|[[Hermit Crab Pet]]|COMMON ([[Rarity]]) - MYTHIC ([[Rarity]])|+0.2-20 Defense|[[NPC]] purchace - [[Junker Joel]]|
|[[Magma Cube Pet]]|[[Magma Cube Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+0.33-33 Defense Ability: Hot Ember (LEGENDARY ([[Rarity]]) exclusive); Buffs the stats of [[Rekindled Ember Armor]] by 0.5%-50%.|Drop - [[Magma Cube]] and [[Magma Boss]]|
|[[Mammoth Pet]]|[[Mammoth Pet]]|LEGENDARY ([[Rarity]])|+0.5-50 Defense|Forging ([[The Forge]]) Recipe - [[Heart of the Mountain]] Tier 7 ([[Heart of the Mountain]])|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|RARE ([[Rarity]]) - MYTHIC ([[Rarity]])|Ability: Subterranean Battler; Increases all Combat Stats by (0.1%-10% (RARE ([[Rarity]])), 0.2%-20% (EPIC ([[Rarity]]) - MYTHIC ([[Rarity]]))) (Additive)[Confirm] while on [[Mining Islands]].|[[Crafting]] Recipe - Mithril Collection III (3) ([[Mithril]])|
|[[Pigman Pet]]|[[Pigman Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+0.5-50 Defense|[[Crafting]] Recipe - Raw Porkchop Collection III (3) ([[Raw Porkchop]])|
|[[Rock Pet]]|[[Rock Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+2-200 Defense Ability: Fortify While sitting on your rock, gain (+0.2%-20% (RARE ([[Rarity]])), 0.25%-25% (EPIC ([[Rarity]]) - LEGENDARY ([[Rarity]]))) (Additive) Defense.|Reward - Mining Milestones ([[Rock Pet]]) [[NPC]] Purchase - [[Rusty]] (if lost)|
|[[Silverfish Pet]]|[[Silverfish Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+1-100 Defense|[[Crafting]] Recipe - Cobblestone Collection III (3) ([[Cobblestone]])|
|[[Slug Pet]]|[[Slug Pet]]|EPIC ([[Rarity]]) - LEGENDARY ([[Rarity]])|+0.2-20 Defense|Drop - [[Slug]]|
|[[Snail Pet]]|[[Snail Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+1-100 Defense|[[Crafting]] Recipe - Red Sand Collection III (3) ([[Cobblestone]])|
|[[T-Rex Pet]]|[[T-Rex Pet]]|LEGENDARY ([[Rarity]])|Ability: Tyrant; Combat stats granted by pet items on this pet are increased by 1%-100%|Forging ([[The Forge]]) Recipe - [[Heart of the Mountain]] Tier 7 ([[Heart of the Mountain]])|
|[[Turtle Pet]]|[[Turtle Pet]]|EPIC ([[Rarity]]) - LEGENDARY ([[Rarity]])|100.5-150 Defense Ability: Turtle Tactics; Gain +3.27%-30% Defense (Additive) and an additional +10% Defense (Additive) when standing still. Ability: Genius Amniote; Grants +1.01%-2.5% Defense (Additive[Confirm]) to 4 players within 50 blocks of you.|Purchase - [[Dark Auction]]|
|[[Wither Skeleton Pet]]|[[Wither Skeleton Pet]]|COMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|+0.25-25 Defense|[[Crafting]] Recipe - Coal Collection III (3) ([[Coal]])|
|[[Zombie Pet]]|[[Zombie Pet]]|LEGENDARY ([[Rarity]])|Ability: Living Dead; Increases all stats on Undead armor by 0.25%-25%.|[[Crafting]] Recipe - Rotten Fleash Collection III (3) ([[Rotten Flesh]])|
### Pet Items
Certain [[Pet Items]] grant Defense. The [[Pet Items|Pet Item]] must be equipped on the player's active [[Pets|Pet]] to take effect.
|Slot|Name|Rarity|Stats|Source|
|-|-|-|-|-|
|[[Hardened Scales]]|[[Hardened Scales]]|UNCOMMON ([[Rarity]])|+25 Defense|[[Zog]]: 1,000,000 [[Coins]]|
|[[Reinforced Scales]]|[[Reinforced Scales]]|RARE ([[Rarity]])|+40 Defense|[[Crafting]] Recipe: Recipe: [[Enchanted Gold Block]] x6 ×3 + [[Hardened Scales]] + [[Zog Anvil]] → [[Reinforced Scales]] Ingredients: 18x [[Enchanted Gold Block]] 1x [[Hardened Scales]] 1x [[Zog Anvil]]|
|[[Four-Eyed Fish]]|[[Four-Eyed Fish]]|EPIC ([[Rarity]])|+55 Defense to [[Griffin Pet]]|[[Crafting]] Recipe: Recipe: [[Enchanted Spider Eye]] x64 ×6 + [[Lucky Clover]] + [[Pre-Digestion Fish]] + [[Reinforced Scales]] → [[Four-Eyed Fish]] Ingredients: 384x (6 stacks (384 items total)) [[Enchanted Spider Eye]] 1x [[Lucky Clover]] 1x [[Reinforced Scales]] 1x [[Pre-Digestion Fish]]|
|[[Minos Relic]]|[[Minos Relic]]|EPIC ([[Rarity]])|Increases all pet stats by 33.3%|Drop - [[Minos Champion]]; (requires LEGENDARY ([[Rarity]]) - MYTHIC ([[Rarity]]) [[Griffin Pet]])|
|[[Hephaestus Relic]]|[[Hephaestus Relic]]|LEGENDARY ([[Rarity]])|Increases all pet stats by 50%|[[Crafting]] Recipe: Recipe: [[Minos Relic]] ×3 + [[Hephaestus Anvil]] → [[Hephaestus Relic]] Infredients: 3x [[Minos Relic]] 1x [[Hephaestus Anvil]]|
### Weapons
Certain [[Weapons]] grant bonus Defense. The [[Weapons|Weapon]] needs to be held in order to take effect.
|Slot|Name|Stats|Source|
|-|-|-|-|
|[[Adaptive Blade]]|[[Adaptive Blade]]|+100 Defense in [[Dungeons]] when playing tank.|Can be obtained from Dungeon Reward Chests ([[Dungeon Reward Chest]]) in [[The Catacombs - Floor II]].|
|[[Astraea]]|[[Astraea]]|+250-275 Defense; Grants +2 Defense per Catacombs level.|Recipe: [[Jolly Pink Rock]] ×8 + [[Necron's Blade (Unrefined)]]/[[Scylla]]/[[Hyperion]]/[[Valkyrie]] → [[Astraea]]|
|[[Daedalus Blade]]|[[Daedalus Blade]]|Copies the base Combat stats or your active pet ([[Pets]]).|Upgraded [[Sword of Revelations]] using Daedalus Sticks ([[Daedalus Stick]]) and Enchanted Gold Blocks ([[Enchanted Gold Block]])|
|[[Earthen Blade]]|[[Earthen Blade]]|+73-96 Defense|Drop from [[Super Tank Zombie]]|
|[[Golem Sword]]|[[Golem Sword]]|+25 Defense|[[Crafting]] Recipe - Iron Ingot Collection VIII (8) ([[Iron Ingot]])|
|[[Necromancer Sword]]|[[Necromancer Sword]]|+125-137.5 Defense|Can be obtained from Dungeon Reward Chests ([[Dungeon Reward Chest]]) in [[The Catacombs - Floor VI]].|
|[[Pigman Sword]]|[[Pigman Sword]]|Ability:Burning Souls Gain +300 Defense for 5s and cast a vortex of flames towards nearby enemies, dealing up to 30,000 damage over 5 seconds|[[Crafting]] Recipe - Raw Porkchop Collection IX (9) ([[Raw Porkchop]])|
|[[Wither Cloak Sword]]|[[Wither Cloak Sword]]|+250-275 Defense|Can be obtained from Dungeon Reward Chests ([[Dungeon Reward Chest]]) in [[The Catacombs - Floor VII]].|
### Armor
Most [[Armor]] grants bonus Defense. The [[Armor]] needs to be equiped in order to take effect.
|Armor|Stats|Source|
|-|-|-|
|[[Leather Armor]]|+35 Defense|Crafted ([[Crafting]]) with [[Leather]]|
|[[Golden Armor]]|+55 Defense|Crafted ([[Crafting]]) with Gold Ingots ([[Gold Ingot]])|
|[[Chainmail Armor]]|+69 Defense|[[NPC]] purchace - [[Iron Forger]]|
|[[Iron Armor]]|+77 Defense|Crafted ([[Crafting]]) with Iron Ingots ([[Iron Ingot]])|
|[[Diamond Armor]]|+100 Defense|Crafted ([[Crafting]]) with Diamonds ([[Diamond]])|
|[[Rosetta's Armor]]|+110 Defense|[[NPC]] purchase - [[Rosetta]]|
|[[Squire Armor]]|+115 Defense|[[NPC]] purchase - [[Rosetta]]|
|[[Celeste Armor]]|+70 Defense|[[NPC]] purchase - [[Rosetta]]|
|[[Mercenary Armor]]|+200 Defense|[[NPC]] purchase - [[Rosetta]]|
|[[Starlight Armor]]|+110 Defense|[[NPC]] purchase - [[Rosetta]]|
|[[Miner Armor]]|+60 Defense; Ability: Depth Coating; Doubles this piece's Defense while on [[Mining Islands]].|Drop - [[Miner Zombie]]|
|[[Hardened Diamond Armor]]|+330 Defense|[[Crafting]] Recipe - Diamond Collection VII (7) ([[Diamond]])|
|[[Armor of the Rising Sun]]|+45 Defense|Unobtainable|
|[[Seymour's Special Armor]]|+40 Defense|Serving [[Seymour]] on the [[The Garden]]|
|[[Fairy Armor]]|+4 Defense|Drop - [[Sea Witch]]|
|[[Rabbit Armor]]|+100 Defense|[[Crafting]] Recipe - Raw Rabbit Collection II (2) ([[Raw Rabbit]])|
|[[Speedster Armor]]|+210 Defense|[[Crafting]] Recipe - Sugar Cane Collection IV (4) ([[Sugar Cane]])|
|[[Thermodynamic Armor]]|+700 Defense|Upgraded [[Speedster Armor]] using [[Enchanted Sugar Cane]] and Cane Knots ([[Cane Knot]])|
|[[Shimmering Light Armor]]|+350-420 Defense|Crafted ([[Crafting]]) with [[X]], [[Y]] and [[Z]]|
|[[Golem Armor]]|+250 Defense|[[Crafting]] Recipe - Iron Ingot Collection VI (6) ([[Iron Ingot]])|
|[[Snow Suit Armor]]|+125 Defense; All stats of this armor piece are doubled while on [[Jerry's Workshop]]!|Opening [[Gifts]].|
|[[Ender Armor]]|+170 Defense; All stats on this armor piece are multiplied bt 2x while on the [[End Island]]|Drop - [[Enderman]]|
|[[Armor of Growth]]|+145 Defense|[[Crafting]] Recipe - Dark Oak Log Collection IX (9) ([[Dark Oak Log]])|
|[[Armor of Magma]]|+85 Defense|Unobtainable|
|[[Emerald Armor]]|+270 Defense; Full Set Bonus: Tank; Increases [[Health]] by +1 and Defense by +1 for every 3,000 Emeralds ([[Emerald]]) in your collection. Max 350 each.|[[Crafting]] Recipe - Emerald Collection IX (9) ([[Emerald]])|
|[[Ember Armor]]|+180 Defense|Unobtainable|
|[[Rekindled Ember Armor]]|+230-276 Defense|Crafted ([[Crafting]]) with Rekindled Ember Fragments ([[Rekindled Ember Fragment]])|
|[[Crystal Armor]]|+100 Defense|Crafting [[Crystal Fragment]]|
|[[Mushroom Armor]]|+15 Defense|[[Crafting]] Recipe - Mushroom Collection II (2) ([[Mushroom]])|
|[[Biohazard Armor]]|+50 Defense|[[NPC]] purchase - [[Pesthunter Phillip]]|
|[[Cactus Armor]]|+65 Defense|[[Crafting]] Recipe - Cactus Collection II (2) ([[Cactus]])|
|[[Farmhand Armor]]|+40 Defense|[[Crafting]] Recipe - Wheat Collection II (2) ([[Wheat]])|
|[[Haymaker Armor]]|+60 Defense|[[Crafting]] Recipe - Wheat Collection VI (6) ([[Wheat]]); Upgraded [[Farmhand Armor]]|
|[[Sprout Armor]]|+80 Defense|[[Crafting]] Recipe - Carrot Collection VIII (8) ([[Carrot]]); Upgraded [[Haymaker Armor]]|
|[[Tater Armor]]|+100 Defense|[[Crafting]] Recipe - Potato Collection IX (9) ([[Potato]]); Upgraded [[Sprout Armor]]|
|[[Cropie Armor]]|+120 Defense|Upgraded [[Tater Armor]] using Cropies ([[Cropie]])|
|[[Squash Armor]]|+140 Defense|Upgraded [[Cropie Armor]] using Squashes ([[Squash]])|
|[[Fermento Armor]]|+160 Defense|Upgraded [[Squash Armor]] using Condensed Fermentos ([[Condensed Fermento]])|
|[[Helianthus Armor]]|+200 Defense|Upgraded [[Fermento Armor]] using [[Condensed Helianthus]]'|
|[[Mineral Armor]]|+390 Defense|Crafted ([[Crafting]]) with [[Refined Mineral]] and [[Hardened Diamond Armor]]|
|[[Glossy Mineral Armor]]|+480 Defense|Upgraded [[Mineral Armor]] using Glossy Gemstones ([[Glossy Gemstone]])|
|[[Lapis Armor]]|+120 Defense|Drop - [[Lapis Zombie]]|
|[[Prospecting Armor]]|+100 Defense|[[Crafting]] Recipe - Iron Collection II (2) ([[Iron Ingot]])|
|[[Glacite Armor]]|+415 Defense|Drop - [[Glacite Walker]]|
|[[Heat Armor]]|+200 Defense; Ability: Pressurized Coating; Triple this pieces Defense and [[Strength]] while on [[Mining Islands]].|[[Crafting]] Recipe - Hard Stone Collection II (2) ([[Hard Stone]]); Upgraded [[Heat Armor]]|
|[[Flamebreaker Armor]]|+205 Defense|[[Crafting]] Recipe - Hard Stone Collection V (5) ([[Hard Stone]])|
|[[Yog Armor]]|+60 Defense|Upgraded [[Flamebreaker Armor]] using Yoggies ([[Yoggie]])|
|[[Armor of Divan]]|+540 Defense|Can be forged in [[The Forge]]|
|[[Canopy Armor]]|+115 Defense|[[NPC]] purchase - [[Amaury]]|
|[[Fig Armor]]|+135 Defense|[[Crafting]] Recipe - Fig Collection VII (8) ([[Fig Log]]); Upgraded [[Canopy Armor]]|
|[[Helix Armor]]|+165 Defense|[[Crafting]] Recipe - Helix Collection VII (8) ([[Helix Log]]); Upgraded [[Fig Armor]]|
|[[Angler Armor]]|+105 Defense|[[NPC]] purchase - Fish Merchant ([[Fishing Merchant]])|
|[[Backwater Armor]]|+70 Defense|[[NPC]] purchase - [[Junker Joel]]; Upgraded [[Angler Armor]]|
|[[Salmon Armor]]|+105 Defense|[[Crafting]] Recipe - Salmon Collection VI (6) ([[Salmon]])|
|[[Snorkeling Armor]]|+300 Defense|[[NPC]] purchase - [[Nemo]]|
|[[Diver's Armor]]|+280 Defense|[[Crafting]] Recipe - Sea Lumies Collection VI (6) ([[Sea Lumies]]) Upgraded [[Snorkeling Armor]]|
|[[Abyssal Armor]]|+600 Defense|[[Crafting]] Recipe - Sea Lumies Collection VIII (8) ([[Sea Lumies]]) Upgraded [[Diver's Armor]]|
|[[Nutcracker Armor]]|+145 Defense; All stats of this armor piece are doubled while on [[Jerry's Workshop]]!|Upgraded [[Snow Suit Armor]] using Walnuts ([[Walnut]])|
|[[Sponge Armor]]|+385 Defense; Full Set Bonus: Absorb; Doubles your Defense while in water.|[[Crafting]] Recipe - Sponge Collection IX (9) ([[Sponge]])|
|[[Shark Scale Armor]]|+550 Defense; Full Set Bonus: Absorb; Doubles your Defense while in water.|Upgrade [[Sponge Armor]] using Enchanted Shark Fins ([[Enchanted Shark Fin]])|
|[[Thunder Armor]]|+750-900 Defense|Crafted ([[Crafting]]) with Thunder Fragments ([[Thunder Fragment]])|
|[[Magma Lord Armor]]|+750-900 Defense|Crafted ([[Crafting]]) with Magma Lord Fragments ([[Magma Lord Fragment]])|
|[[Zombie Armor]]|+95-104.5 Defense|[[Crafting]] Recipe - Rotten Flesh Collection VIII (8) ([[Rotten Flesh]])|
|[[Rampart Armor]]|+200-220 Defense|Drop - [[Blaze]], [[Bezal]], [[Wither Skeleton]], [[Wither Spectre]] and [[Magma Cube]]|
|[[Perfect Armor]]|+500-1606 Defense|[[Crafting]] Recipe - Diamond Collection IX (9) ([[Diamond]])|
|[[Spooky Armor]]|+135 Defense|Can be purchased from the [[Fear Mongerer]]|
|[[Bat Person Armor]]|+85 Defense; All Combat Stats on this armor piece are multiplied by 2x at night, or by 3x during the [[Spooky Festival]]!|Upgraded [[Spooky Armor]] with Spooky Fragments ([[Spooky Fragment]])|
|[[Werewolf Armor]]|+700 Defense; Full Set Bonus: Regenerative Howl; Upon activating [[Ferocity]] gain +50 Defense for 5s (up to 10 stacks).|Crafted ([[Crafting]]) with [[Werewolf Skin]]|
|[[Blaze Armor]]|+465 Defense|[[Crafting]] Recipe - Blaze Rod Collection VII (7) ([[Blaze Rod]])|
|[[Frozen Blaze Armor]]|+520-572 Defense|[[Crafting]] Recipe - Ice Collection IX (9) ([[Ice]]); Upgraded [[Blaze Armor]]|
|[[Challenger's Armor]]|+170 Defense; Ability: Mythos' Might; Grants 2x this armor's stats while in Hub ([[Hub Island]]) during Diana's ([[Diana]]) [[Mythological Ritual]].|Crafted ([[Crafting]]) with Ancient Claws ([[Ancient Claw]]), Griffin Feathers ([[Griffin Feather]]) and Enchanted Gold ([[Enchanted Gold Ingot]])|
|[[Mythos Armor]]|+320 Defense; Ability: Mythos' Might; Grants 2x this armor's stats while in Hub ([[Hub Island]]) during Diana's ([[Diana]]) [[Mythological Ritual]].|Crafted ([[Crafting]]) with Enchanted Ancient Claws ([[Enchanted Ancient Claw]]), Griffin Feathers ([[Griffin Feather]]), Mythos Fragments ([[Mythos Fragment]]) and Enchanted Gold Blocks ([[Enchanted Gold Block]]); Upgraded [[Challenger's Armor]]|
|[[Young Dragon Armor]]|+500-550 Defense|Crafted ([[Crafting]]) with Young Dragon Fragment ([[Dragon Fragment]])|
|[[Old Dragon Armor]]|+500-550 Defense; Full Set Bonus: Old Blood; Increases the strength of [[Growth]], [[Protection]], [[Feather Falling]], [[Sugar Rush]], and [[True Protection]] while worn.|Crafted ([[Crafting]]) with Old Dragon Fragment ([[Dragon Fragment]])|
|[[Wise Dragon Armor]]|+500-550 Defense|Crafted ([[Crafting]]) with Wise Dragon Fragment ([[Dragon Fragment]])|
|[[Protector Dragon Armor]]|+600-660 Defense; Full Set Bonus: Protective Blood; Increases the Defense of each armor piece by +1% Defense (Additive) [Confirm]for each missing percent of HP ([[Health]]).|Crafted ([[Crafting]]) with Protector Dragon Fragment ([[Dragon Fragment]])|
|[[Strong Dragon Armor]]|+500-550 Defense|Crafted ([[Crafting]]) with Strong Dragon Fragment ([[Dragon Fragment]])|
|[[Unstable Dragon Armor]]|+500-550 Defense|Crafted ([[Crafting]]) with Unstable Dragon Fragment ([[Dragon Fragment]])|
|[[Holy Dragon Armor]]|+500-550 Defense|Crafted ([[Crafting]]) with Holy Dragon Fragment ([[Dragon Fragment]])|
|[[Superior Dragon Armor]]|+600-660 Defense; Full Set Bonus: Superior Blood; Increases all Combat stats and [[Magic Find]] by 5% (Additive)[Confirm].|Crafted ([[Crafting]]) with Superior Dragon Fragment ([[Dragon Fragment]])|
|[[Revenant Armor]]|+150 Defense|[[Crafting]] Recipe - Zombie Slayer Collection IV (4) ([[Zombie Slayer]])|
|[[Reaper Armor]]|+150 Defense|[[Crafting]] Recipe - Zombie Slayer Collection VII (7) ([[Zombie Slayer]]); Upgraded [[Revenant Armor]]|
|[[Tarantula Armor]]|+340-374 Defense|[[Crafting]] Recipe - Spider Slayer Collection IV (4) ([[Spider Slayer]])|
|[[Primordial Armor]]|+410-451 Defense|[[Crafting]] Recipe - Spider Slayer Collection VII (7) ([[Spider Slayer]]); Upgraded [[Tarantula Armor]]|
|[[Armor of the Pack]]|+280 Defense; Full Set Bonus: Armor of the Pack; Gain +35 [[Strength]] and +80 Defense for each [[Armor of the Pack]] wearer withing 30 Blocks.; Max of 3 players!|[[Crafting]] Recipe - Wolf Slayer Collection VI (6) ([[Wolf Slayer]])|
|[[Final Destination Armor]]|+400 Defense|[[Crafting]] Recipe - Enderman Slayer Collection III (3) ([[Enderman Slayer]])|
|[[Heavy Armor]]|+323-680 Defense|Drop - [[Tank Zombie]]|
|[[Skeleton Lord Armor]]|+265-340 Defense|Drop - [[Skeleton Lord]]|
|[[Skeleton Grunt Armor]]|+135-195 Defense|Drop - [[Skeleton Grunt]]|
|[[Skeleton Soldier Armor]]|+125-319 Defense|Drop - [[Skeleton Soldier]]|
|[[Skeleton Master Armor]]|+140-272 Defense|Drop - [[Skeleton Master]]|
|[[Zombie Soldier Armor]]|+279-440 Defense|Drop - [[Zombie Soldier]]|
|[[Zombie Knight Armor]]|+335-609 Defense; Full Set Bonus: Zombie Knight; Gains +50 Defense when used with the [[Zombie Knight Sword]].|Drop - [[Zombie Knight]]|
|[[Zombie Commander Armor]]|+177-270 Defense|Drop - [[Zombie Commander]]|
|[[Zombie Lord Armor]]|+218-300 Defense; Full Set Bonus: Dungeon Lord; Gains +10 [[Strength]] and Defense for every minute spent in the Dungeon.|Drop - [[Zombie Lord]]|
|[[Skeletor Armor]]|+140-249 Defense|Drop - [[Skeletor]] and [[Skeletor Prime]]|
|[[Adaptive Armor]]|+245-269.5 Defense; Grants additional bonuses based on you selected dungeon class!; Tank: +30 Defense.|Dungeon Reward Chests ([[Dungeon Reward Chest]]) on [[The Catacombs - Floor III]]|
|Fragged Adaptive Armor ([[Adaptive Armor]])|+285-313.5 Defense; Grants additional bonuses based on you selected dungeon class!; Tank: +30 Defense.|Upgraded [[Adaptive Armor]] using Scarf Fragments ([[Scarf Fragment]])|
|[[Shadow Assassin Armor]]|+330-363 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) on [[The Catacombs - Floor V]]|
|[[Super Heavy Armor]]|+343-965 Defense|Drop - [[Super Tank Zombie]]|
|[[Necromancer Lord Armor]]|+780-858 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) on [[The Catacombs - Floor VI]]|
|[[Wither Armor]]|+720-792 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) on [[The Catacombs - Floor VII]]|
|[[Maxor's Armor]]|+370-407 Defense|Upgraded [[Wither Armor]] with [[Bigfoot's Bola]]|
|[[Goldor's Armor]]|+860-946 Defense|Upgraded [[Wither Armor]] with [[Jolly Pink Rock]]|
|[[Storm's Armor]]|+370-407 Defense|Upgraded [[Wither Armor]] with [[L.A.S.R.'s Eye]]|
|[[Necron's Armor]]|+450-495 Defense|Upgraded [[Wither Armor]] with [[Diamante's Handle]]|
|[[Aurora Armor]]|+210-252 Defense|Kuudra Reward Chests ([[Kuudra]])|
|Hot Aurora Armor ([[Aurora Armor]])|+264-316.8 Defense|Upgraded [[Aurora Armor]]|
|Burning Aurora Armor ([[Aurora Armor]])|+333-399.6 Defense|Upgraded Hot Aurora Armor ([[Aurora Armor]])|
|Fiery Aurora Armor ([[Aurora Armor]])|+410-492 Defense|Upgraded Burning Aurora Armor ([[Aurora Armor]])|
|Infernal Aurora Armor ([[Aurora Armor]])|+530-636 Defense|Upgraded Fiery Aurora Armor ([[Aurora Armor]])|
|[[Crimson Armor]]|+210-252 Defense|Kuudra Reward Chests ([[Kuudra]])|
|Hot Crimson Armor ([[Crimson Armor]])|+264-316.8 Defense|Upgraded [[Crimson Armor]]|
|Burning Crimson Armor ([[Crimson Armor]])|+333-399.6 Defense|Upgraded Hot Crimson Armor ([[Crimson Armor]])|
|Fiery Crimson Armor ([[Crimson Armor]])|+410-492 Defense|Upgraded Burning Crimson Armor ([[Crimson Armor]])|
|Infernal Crimson Armor ([[Crimson Armor]])|+530-636 Defense|Upgraded Fiery Crimson Armor ([[Crimson Armor]])|
|[[Terror Armor]]|+210-252 Defense|Kuudra Reward Chests ([[Kuudra]])|
|Hot Terror Armor ([[Terror Armor]])|+264-316.8 Defense|Upgraded [[Terror Armor]]|
|Burning Terror Armor ([[Terror Armor]])|+333-399.6 Defense|Upgraded Hot Terror Armor ([[Terror Armor]])|
|Fiery Terror Armor ([[Terror Armor]])|+410-492 Defense|Upgraded Burning Terror Armor ([[Terror Armor]])|
|Infernal Terror Armor ([[Terror Armor]])|+530-636 Defense|Upgraded Fiery Terror Armor ([[Terror Armor]])|
|[[Hollow Armor]]|+230-276 Defense|Kuudra Reward Chests ([[Kuudra]])|
|Hot Hollow Armor ([[Hollow Armor]])|+288-345.6 Defense|Upgraded [[Hollow Armor]]|
|Burning Hollow Armor ([[Hollow Armor]])|+359-430.8 Defense|Upgraded Hot Hollow Armor ([[Hollow Armor]])|
|Fiery Hollow Armor ([[Hollow Armor]])|+449-538.8 Defense|Upgraded Burning Hollow Armor ([[Hollow Armor]])|
|Infernal Hollow Armor ([[Hollow Armor]])|+561-673.2 Defense|Upgraded Fiery Hollow Armor ([[Hollow Armor]])|
|[[Fervor Armor]]|+440-528 Defense|Kuudra Reward Chests ([[Kuudra]])|
|Hot Fervor Armor ([[Fervor Armor]])|+554-664.8 Defense|Upgraded [[Fervor Armor]]|
|Burning Fervor Armor ([[Fervor Armor]])|+669-838.8 Defense|Upgraded Hot Fervor Armor ([[Fervor Armor]])|
|Fiery Fervor Armor ([[Fervor Armor]])|+880-1056 Defense|Upgraded Burning Fervor Armor ([[Fervor Armor]])|
|Infernal Fervor Armor ([[Fervor Armor]])|+1109-1330.8 Defense|Upgraded Fiery Fervor Armor ([[Fervor Armor]])|
|[[Kalhuiki Mask]]|+50 Defense|[[NPC]] purchace - [[Odawa]]|
|[[Creeper Hat]]|+5 Defense|[[Crafting]] Recipe - Gunpowder Collection II (2) ([[Gunpowder]])|
|[[Cow Hat]]|+5 Defense|[[Crafting]] Recipe - Leather Collection II (2) ([[Leather]])|
|[[Head of Betrayal]]|+5 Defense|Talk to [[Jake]] while wearing a [[Cow Hat]] with a [[Cow]] in his house during [[The Great Spook]]|
|[[Magma Cube Head]]|+25 Defense|Unobtainable|
|[[Zombie Hat]]|+10-11 Defense|[[Crafting]] Recipe - Rotten Flesh Collection V (5) ([[Rotten Flesh]])|
|[[Enderman Mask]]|+1 Defense|Given by [[Guber]] when the [[End Race]] is completed in under 2 minutes|
|[[Lantern Helmet]]|+10 Defense and gain 2 Defense for every [[Farming]] skill level you have.|[[Crafting]] Recipe - Pumpkin Collection VII (7) ([[Pumpkin]])|
|[[Mole Hat]]|+10 Defense|Reward - [[NPC]] [[Molbert]]|
|[[Taurus Helmet]]|+150-180 Defense|Drop - [[Taurus]]|
|[[Water Hydra Head]]|+100 Defense|Drop - [[Water Hydra]]|
|[[Tiki Mask]]|+100 Defense|Drop - [[Wiki Tiki]]|
|[[Fallen Star Helmet]]|+30 Defense|Reward - Talking to the [[Cult of the Fallen Star]] during a meeting|
|[[Skeleton's Helmet]]|+75-82.5 Defense|[[Crafting]] Recipe - Bone Collection VIII (8) ([[Bone]])|
|[[Witch Mask]]|+111 Defense|Obtain 2,000 or more points in a [[Spooky Festival]]|
|[[Vampire Mask]]|+111 Defense|Found in Party Chests ([[Party Chest]])|
|[[Vampire Witch Mask]]|+222 Defense|Upgraded [[Vampire Mask]] and [[Witch Mask]] using [[Ectoplasm]]|
|[[Crown of Greed]]|+50 Defense|Drop - [[King Minos]]|
|[[Crown of Avarice]]|+100 Defense|Upgraded [[Crown of Greed]] using Enchanted Gold Blocks ([[Enchanted Gold Block]]), Griffin Feathers ([[Griffin Feather]]) and Avaricious Chalices ([[Avaricious Chalice]])|
|[[Crystallized Heart]]|+10-11 Defense|[[Crafting]] Recipe - Zombie Slayer Collection III (3) ([[Zombie Slayer]])|
|[[Revived Heart]]|+35-38.5 Defense|[[Crafting]] Recipe - Zombie Slayer Collection VI (6) ([[Zombie Slayer]])|
|[[Reaper Mask]]|+100-110 Defense|[[Crafting]] Recipe - Zombie Slayer Collection VII (7) ([[Zombie Slayer]])|
|[[Bonzo's Mask]]|+100-110 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) in [[The Catacombs - Floor I]]|
|[[Spirit Mask]]|+50-55 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) in The Catacombs - Floor 4 ([[The Catacombs - Floor IV]])|
|Fragged Spirit Mask ([[Spirit Mask]])|+75-82.5 Defense|Upgraded [[Spirit Mask]] using Thorn Fragments ([[Thorn Fragment]])|
|[[Precursor Eye]]|+222-244.2 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) in The Catacombs - Floor 6 ([[The Catacombs - Floor VI]])|
|[[Sniper Helmet]]|+25-33 Defense|Drop - [[Sniper]]|
|[[Warden Helmet]]|+100 Defense|[[Crafting]] Recipe - Zombie Slayer Collection VIII (8) ([[Zombie Slayer]])|
|Golden Bonzo Head ([[Golden Heads]])|+10-11 Defense; Grants 2x stats on [[The Catacombs - Floor I]].|Reward - Bonzo Collection III (3) ([[Bonzo]])|
|Golden Scarf Head ([[Golden Heads]])|+15-16.5 Defense; Grants 2x stats on [[The Catacombs - Floor II]].|Reward - Scarf Collection III (3) ([[Scarf]])|
|Golden Professor Head ([[Golden Heads]])|+20-22 Defense; Grants 2x stats on [[The Catacombs - Floor III]].|Reward - Professor Collection III (3) ([[The Professor]])|
|Golden Thorn Head ([[Golden Heads]])|+25-27.5 Defense; Grants 2x stats on [[The Catacombs - Floor IV]].|Reward - Thorn Collection II (2) ([[Thorn]])|
|Golden Livid Head ([[Golden Heads]])|+30-33 Defense; Grants 2x stats on [[The Catacombs - Floor V]].|Reward - Livid Collection II (2) ([[Livid]])|
|Golden Sadan Head ([[Golden Heads]])|+35-38.5 Defense; Grants 2x stats on [[The Catacombs - Floor VI]].|Reward - Sadan Collection II (2) ([[Sadan]])|
|Golden Necron Head ([[Golden Heads]])|+40-44 Defense; Grants 2x stats on [[The Catacombs - Floor VII]].|Reward - Necron Collection II (2) ([[Necron]])|
|Diamond Bonzo Head ([[Diamond Heads]])|+20-22 Defense; Grants 2x stats on [[The Catacombs - Floor I]].|[[Crafting]] Recipe - Bonzo Collection VI (6) ([[Bonzo]]); Upgraded Golden Bonzo Head ([[Golden Heads]])|
|Diamond Scarf Head ([[Diamond Heads]])|+30-33 Defense; Grants 2x stats on [[The Catacombs - Floor II]].|[[Crafting]] Recipe - Scarf Collection VI (6) ([[Scarf]]); Upgraded Golden Scarf Head ([[Golden Heads]])|
|Diamond Professor Head ([[Diamond Heads]])|+40-44 Defense; Grants 2x stats on [[The Catacombs - Floor III]].|[[Crafting]] Recipe - Professor Collection VI (6) ([[The Professor]]); Upgraded Golden Professor Head ([[Golden Heads]])|
|Diamond Thorn Head ([[Diamond Heads]])|+50-55 Defense; Grants 2x stats on [[The Catacombs - Floor IV]].|[[Crafting]] Recipe - Thorn Collection VI (6) ([[Thorn]]); Upgraded Golden Thorn Head ([[Golden Heads]])|
|Diamond Livid Head ([[Diamond Heads]])|+60-66 Defense; Grants 2x stats on [[The Catacombs - Floor V]].|[[Crafting]] Recipe - Livid Collection VII (7) ([[Livid]]); Upgraded Golden Livid Head ([[Golden Heads]])|
|Diamond Sadan Head ([[Diamond Heads]])|+70-77 Defense; Grants 2x stats on [[The Catacombs - Floor VI]].|[[Crafting]] Recipe - Sadan Collection VII (7) ([[Sadan]]); Upgraded Golden Sadan Head ([[Golden Heads]])|
|Diamond Necron Head ([[Diamond Heads]])|+80-88 Defense; Grants 2x stats on [[The Catacombs - Floor VII]].|[[Crafting]] Recipe - Necron Collection VII (7) ([[Necron]]); Upgraded Golden Necron Head ([[Golden Heads]])|
|[[Guardian Chestplate]]|+50 Defense|[[Crafting]] Recipe - Prismarine Crystals Collection V (5) ([[Prismarine Crystals]])|
|[[Obsidian Chestplate]]|+250 Defense|Drop - [[Obsidian Defender]]|
|[[Mithril Coat]]|+125 Defense|[[Crafting]] Recipe - Mithril Collection VII (7) ([[Mithril]])|
|[[Stone Chestplate]]|+130-143 Defense|Can be purchased from [[Ophelia]]|
|[[Metal Chestplate]]|+230-253 Defense|Can be purchased from [[Ophelia]]|
|[[Steel Chestplate]]|+330-363 Defense|Can be purchased from [[Ophelia]]|
|[[Flaming Chestplate]]|+200-240 Defense|Drop - [[Water Hydra]]|
|[[Kelly's T-Shirt]]|+30 Defense|Reward - [[NPC]] [[Kelly]]|
|[[Creeper Pants]]|+65 Defense|[[Crafting]] Recipe - Gunpowder Collection VIII (8) ([[Gunpowder]])|
|[[Stereo Pants]]|+35 Defense|[[Crafting]] Recipe - Sponge Collection VII (7) ([[Sponge]])|
|[[Moogma Leggings]]|+175-210 Defense|Drop - [[Moogma]]|
|[[Charlie's Trousers]]|+15 Defense|Reward - [[NPC]] [[Charlie]]|
|[[Spider's Boots]]|+45-49.5 Defense|[[Crafting]] Recipe - String Collection VIII (8) ([[String]])|
|[[Spirit Boots]]|+50-55 Defense|Dungeon Reward Chests ([[Dungeon Reward Chest]]) on [[The Catacombs - Floor IV]]|
|[[Farmer Boots]]|+20 Defense and gain 2 Defense and +4 [[Speed]] for every [[Farming]] skill level you have (while outside [[The Garden]]).|[[Crafting]] Recipe - Pumpkin Collection IX (9) ([[Pumpkin]])|
|[[Rancher's Boots]]|+70 Defense and gain 2 Defense and +4 [[Speed]] for every [[Farming]] skill level you have.|[[Crafting]] Recipe - Pumpkin Collection XI (11) ([[Pumpkin]])|
|[[Slug Boots]]|+125-150 Defense|Drop - [[Magma Slug]] and [[Baby Magma Slug]]|
|[[Melody's Shoes]]|+20 Defense|Reward - [[NPC]] [[Melody]]|
### Equipment
Most [[Equipment]] grants bonus Defense. The [[Equipment]] needs to be equiped in order to take effect.
|Slot|Item|Rarity|Type|Stats|Source|
|-|-|-|-|-|-|
|[[Arachne's Necklace]]/[[Arachne's Cloak]]/[[Arachne's Belt]]/[[Arachne's Gloves]]|Arachne's Set ([[Arachne's Necklace]])|RARE ([[Rarity]])|Full Set ([[Equipment]])|+5 Defense per piece.; Tiered Bonus: Arachne's Faithful; Grants +5 (2 Pieces)➜10 (3 Pieces)➜20 (4 Pieces)➜35 (5 Pieces)➜50 (6 Pieces)➜70 (7 Pieces)➜100 (8 Pieces) Defense and [[Health]]|Drop - [[Arachne's Keeper]]|
|[[Ender Necklace]]/[[Ender Cloak]]/[[Ender Belt]]/[[Ender Gauntlet]]|Ender Set ([[Ender Necklace]])|EPIC ([[Rarity]])|Full Set ([[Equipment]])|+10 Defense per piece.; All stats on this piece of equipment are multiplied by 2x while on [[The End]] Island!|Drop - [[Enderman]], Watchers ([[The Watcher]]), Obsidian Defenders ([[Obsidian Defender]]) and [[Ender Nodes]]|
|[[Molten Necklace]]/[[Molten Cloak]]/[[Molten Belt]]/[[Molten Bracelet]]|Molten Set ([[Molten Necklace]])|EPIC ([[Rarity]])|Full Set ([[Equipment]])|+20-24 Defense per piece.|Kuudra Reward Chests ([[Kuudra]])|
|[[Challenger's Armor]]|Challenger's Set ([[Challenger's Armor]])|EPIC ([[Rarity]])|Full Set ([[Equipment]])|+10 Defense per piece.; Ability: Mythos Might; Grants 2x this equipment's stats while in Hub ([[Hub Island]]) during Diana's ([[Diana]]) [[Mythological Ritual]].|Crafted ([[Crafting]]) with Griffin Feathers ([[Griffin Feather]]), Ancient Claws ([[Ancient Claw]]) and Enchanted Gold ([[Enchanted Gold Ingot]])|
|[[Mythos Armor]]|Mythos Set ([[Mythos Armor]])|LEGENDARY ([[Rarity]])|Full Set ([[Equipment]])|+15 Defense per piece.; Ability: Mythos Might; Grants 2x this equipment's stats while in Hub ([[Hub Island]]) during Diana's ([[Diana]]) [[Mythological Ritual]].|Crafted ([[Crafting]]) with Griffin Feathers ([[Griffin Feather]]), Enchanted Ancient Claws ([[Enchanted Ancient Claw]]), Mythos Fragments ([[Mythos Fragment]]) and Enchanted Gold Blocks ([[Enchanted Gold Block]])|
|[[Bone Necklace]]|[[Bone Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+35-38.5 Defense; Gain +3 Defense for each enemy within 10 blocks up to +30 Defense. Range increases to 30 blocks and the cap increases to +60 Defense when you play as Tank in dungeons.|[[Dungeon Reward Chest]] - [[The Catacombs - Floor IV]]|
|[[Bone Necklace]]|Fragged Bone Necklace ([[Bone Necklace]])|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+45-49.5 Defense; Gain +3 Defense for each enemy within 10 blocks up to +30 Defense. Range increases to 30 blocks and the cap increases to +60 Defense when you play as Tank in dungeons.|Upgraded [[Bone Necklace]] using Thorn Fragments ([[Thorn Fragment]])|
|[[Delirium Necklace]]|[[Delirium Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+1-1.1 Defense|Crafted ([[Crafting]]) with Rekindled Ember Fragments ([[Rekindled Ember Fragment]]) and Gazing Pearls ([[Gazing Pearl]])|
|[[Lava Shell Necklace]]|[[Lava Shell Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+30-36 Defense|Crafted ([[Crafting]]) with Gazing Pearls ([[Gazing Pearl]]) and Lava Shells ([[Lava Shell]])|
|[[Rift Necklace]]|[[Rift Necklace]]|LEGENDARY ([[Rarity]])|Necklace ([[Necklaces]])|+15-30 Defense|Reward - [[Elise]]; Stats increase for each Time Charm ([[Rift Timecharms]]) in the [[Rift Gallery]]|
|[[Thunderbolt Necklace]]|[[Thunderbolt Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+30 Defense|Crafted ([[Crafting]]) with Thunder Fragments ([[Thunder Fragment]])|
|[[Synthesizer v2]]|[[Synthesizer v2]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|Can synthesize [[Y]] items increasing the stats of this necklace. Current Bonuses:; 0-30/30 Defense|Upgraded [[Synthesizer v1]] using [[Y]]|
|[[Synthesizer v3]]|[[Synthesizer v3]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|Can synthesize [[Y]] items increasing the stats of this necklace. Current Bonuses:; 0-40/40 Defense|Upgraded [[Synthesizer v2]] using [[Z]]|
|[[Dragonfade Cloak]]|[[Dragonfade Cloak]]|EPIC ([[Rarity]])|Cloak ([[Cloaks]])|+5 Defense; All stats on this piece of equipment are multiplied by 3x while on [[The End]]!|Crafted ([[Crafting]]) with Absolute Ender Pearls ([[Absolute Ender Pearl]]), [[Mite Gel]] and [[Ritual Residue]]|
|[[Ghast Cloak]]|[[Ghast Cloak]]|RARE ([[Rarity]])|Cloak ([[Cloaks]])|+7-8.4 Defense|[[Crafting]] Recipe - Ghast Tear Collection IV (4) ([[Ghast Tear]])|
|[[Vanquished Ghast Cloak]]|[[Vanquished Ghast Cloak]]|EPIC ([[Rarity]])|Cloak ([[Cloaks]])|+10-12 Defense; Piece Bonus: Ghast Blaster; Kill Ghasts ([[Ghast]]) to accumulate Defense.; Piece Bonus +0-10 Defense; Next Upgrade: (0 / 1,000)|[[Crafting]] Recipe - Ghast Tear Collection VII (7) ([[Ghast Tear]]); Upgraded [[Ghast Cloak]]|
|[[Adaptive Belt]]|[[Adaptive Belt]]|EPIC ([[Rarity]])|Belt ([[Belts]])|+5-5.5 Defense; Grants additional bonuses based on your selected dungeon class! Tank: +5 [[Health]], +10 Defense|[[Dungeon Reward Chest]] - [[The Catacombs - Floor II]]|
|[[Adaptive Belt]]|[[Adaptive Belt]]|EPIC ([[Rarity]])|Belt ([[Belts]])|+10-11 Defense; Grants additional bonuses based on your selected dungeon class! Tank: +5 [[Health]], +10 Defense|Upgraded [[Adaptive Belt]] using Scarf Fragments ([[Scarf Fragment]])|
|[[Blaze Belt]]|[[Blaze Belt]]|RARE ([[Rarity]])|Belt ([[Belts]])|+7-8.4 Defense|[[Crafting]] Recipe - Blaze Rod Collection Level IV (4) ([[Blaze Rod]])|
|[[Vanquished Blaze Belt]]|[[Vanquished Blaze Belt]]|RARE ([[Rarity]])|Belt ([[Belts]])|+20-24 Defense|Upgraded [[Blaze Belt]] using Enchanted Blaze Rods ([[Enchanted Blaze Rod]]) and Nether Stars ([[Nether Star]])|
|[[Implosion Belt]]|[[Implosion Belt]]|EPIC ([[Rarity]])|Belt ([[Belts]])|+70-84 Defense|[[Crafting]] Recipe - Sulphur Collection Level IX (9) ([[Sulphur]])|
|[[Scoville Belt]]|[[Scoville Belt]]|RARE ([[Rarity]])|Belt ([[Belts]])|+30-36 Defense; Gain +50 Defense per ignited enemy within a 10 block radius up to a maximim of +1000 Defense.|Crafted ([[Crafting]]) with Rekindled Ember Fragments ([[Rekindled Ember Fragment]]) and Compact Oozes ([[Compact Ooze]])|
|[[Red Belt]]|[[Red Belt]]|SPECIAL ([[Rarity]])|Belt ([[Belts]])|+0.1 Defense|Reward - [[Master Tao]] during [[A Honk and Seek Adventure]]|
|[[White Belt]]|[[White Belt]]|COMMON ([[Rarity]])|Belt ([[Belts]])|+5-5.2 Defense|Reward - [[Master Tao]]|
|[[Yellow Belt]]|[[Yellow Belt]]|UNCOMMON ([[Rarity]])|Belt ([[Belts]])|+5-5.4 Defense|Reward - [[Master Tao]]; Upgraded [[White Belt]]|
|[[Green Belt]]|[[Green Belt]]|UNCOMMON ([[Rarity]])|Belt ([[Belts]])|+10-11.1 Defense|Reward - [[Master Tao]]; Upgraded [[Yellow Belt]]|
|[[Blue Belt]]|[[Blue Belt]]|RARE ([[Rarity]])|Belt ([[Belts]])|+15-17.3 Defense|Reward - [[Master Tao]]; Upgraded [[Green Belt]]|
|[[Brown Belt]]|[[Brown Belt]]|EPIC ([[Rarity]])|Belt ([[Belts]])|+20-24 Defense|Reward - [[Master Tao]]; Upgraded [[Blue Belt]]|
|[[Black Belt]]|[[Black Belt]]|LEGENDARY ([[Rarity]])|Belt ([[Belts]])|+25-31 Defense|Reward - [[Master Tao]]; Upgraded [[Brown Belt]]|
|[[Gauntlet of Contagion]]|[[Gauntlet of Contagion]]|EPIC ([[Rarity]])|Glove ([[Gloves]])|+10-12 Defense|Crafted ([[Crafting]]) with Enchanted Mycelium Cubes ([[Enchanted Mycelium Cube]]) and Leather Cloths ([[Leather Cloth]])|
|[[Demonslayer Gauntlet]]|[[Demonslayer Gauntlet]]|EPIC ([[Rarity]])|Glove ([[Gloves]])|+20 Defense|Crafted ([[Crafting]]) with Enchanted Rabbit Hides ([[Enchanted Rabbit Hide]]), [[Molten Powder]] and [[Enchanted Glowstone]]|
|[[Dragonfuse Glove]]|[[Dragonfuse Glove]]|EPIC ([[Rarity]])|Glove ([[Gloves]])|+5 Defense|Crafted ([[Crafting]]) with Absolute Ender Pearls ([[Absolute Ender Pearl]]), [[Mite Gel]] and [[Ritual Residue]]|
|[[Manticore Claw]]|[[Manticore Claw]]|LEGENDARY ([[Rarity]])|Glove ([[Gloves]])|Ability: Chimeric Core; Copies 10% of your active Pet's Combat stats.|Crafted ([[Crafting]]) with [[Manti-core]], Enchanted Ancient Claws ([[Enchanted Ancient Claw]]) and Enchanted Gold Blocks ([[Enchanted Gold Block]])|
### Reforges
Certain [[Reforging|Reforges]] grant bonus Defense. The item [[Reforging|Reforged]] needs to be equiped/held in order for the [[Reforging|Reforge]] bonus to take effect. [[Reforging|Reforges]] grant stats based on item [[Rarity]], so a better [[Rarity]] will grant better stats from the [[Reforging|Reforge]].
|Reforge|Stats|Applied to|Source|
|-|-|-|-|
|Clean|+5 Defense(COMMON ([[Rarity]])), +7 Defense(UNCOMMON ([[Rarity]])), +10 Defense(RARE ([[Rarity]])), +15 Defense(EPIC ([[Rarity]])), +25 Defense(LEGENDARY ([[Rarity]])), +25 Defense(MYTHIC ([[Rarity]])), +30 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Heavy|+25 Defense(COMMON ([[Rarity]])), +35 Defense(UNCOMMON ([[Rarity]])), +50 Defense(RARE ([[Rarity]])), +65 Defense(EPIC ([[Rarity]])), +80 Defense(LEGENDARY ([[Rarity]])), +110 Defense(MYTHIC ([[Rarity]])), +140 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Light|+1 Defense(COMMON ([[Rarity]])), +2 Defense(UNCOMMON ([[Rarity]])), +3 Defense(RARE ([[Rarity]])), +4 Defense(EPIC ([[Rarity]])), +5 Defense(LEGENDARY ([[Rarity]])), +6 Defense(MYTHIC ([[Rarity]])), +7 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Mythic|+2 Defense(COMMON ([[Rarity]])), +3 Defense(UNCOMMON ([[Rarity]])), +6 Defense(RARE ([[Rarity]])), +8 Defense(EPIC ([[Rarity]])), +10 Defense(LEGENDARY ([[Rarity]])), +12 Defense(MYTHIC ([[Rarity]])), +14 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Pure|+2 Defense(COMMON ([[Rarity]])), +3 Defense(UNCOMMON ([[Rarity]])), +4 Defense(RARE ([[Rarity]])), +6 Defense(EPIC ([[Rarity]])), +8 Defense(LEGENDARY ([[Rarity]])), +10 Defense(MYTHIC ([[Rarity]])), +12 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Smart|+4 Defense(COMMON ([[Rarity]])), +6 Defense(UNCOMMON ([[Rarity]])), +9 Defense(RARE ([[Rarity]])), +12 Defense(EPIC ([[Rarity]])), +15 Defense(LEGENDARY ([[Rarity]])), +20 Defense(MYTHIC ([[Rarity]])), +25 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Titanic|+10 Defense(COMMON ([[Rarity]])), +15 Defense(UNCOMMON ([[Rarity]])), +20 Defense(RARE ([[Rarity]])), +25 Defense(EPIC ([[Rarity]])), +35 Defense(LEGENDARY ([[Rarity]])), +50 Defense(MYTHIC ([[Rarity]])), +65 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[NPC]] - [[Blacksmith]]|
|Astute|+1 Defense(COMMON ([[Rarity]])), +2 Defense(UNCOMMON ([[Rarity]])), +2 Defense(RARE ([[Rarity]])), +3 Defense(EPIC ([[Rarity]])), +4 Defense(LEGENDARY ([[Rarity]])), +5 Defense(MYTHIC ([[Rarity]])), +6 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Blended|+1 Defense(COMMON ([[Rarity]])), +1 Defense(UNCOMMON ([[Rarity]])), +1 Defense(RARE ([[Rarity]])), +2 Defense(EPIC ([[Rarity]])), +3 Defense(LEGENDARY ([[Rarity]])), +3 Defense(MYTHIC ([[Rarity]])), +3 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Colossal|+3 Defense(COMMON ([[Rarity]])), +4 Defense(UNCOMMON ([[Rarity]])), +6 Defense(RARE ([[Rarity]])), +8 Defense(EPIC ([[Rarity]])), +10 Defense(LEGENDARY ([[Rarity]])), +12 Defense(MYTHIC ([[Rarity]])), +14 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Hefty|+7 Defense(COMMON ([[Rarity]])), +9 Defense(UNCOMMON ([[Rarity]])), +12 Defense(RARE ([[Rarity]])), +15 Defense(EPIC ([[Rarity]])), +20 Defense(LEGENDARY ([[Rarity]])), +25 Defense(MYTHIC ([[Rarity]])), +30 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Honored|+1 Defense(COMMON ([[Rarity]])), +2 Defense(UNCOMMON ([[Rarity]])), +2 Defense(RARE ([[Rarity]])), +3 Defense(EPIC ([[Rarity]])), +3 Defense(LEGENDARY ([[Rarity]])), +4 Defense(MYTHIC ([[Rarity]])), +4 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Soft|+1 Defense(COMMON ([[Rarity]])), +1 Defense(UNCOMMON ([[Rarity]])), +1 Defense(RARE ([[Rarity]])), +1 Defense(EPIC ([[Rarity]])), +2 Defense(LEGENDARY ([[Rarity]])), +2 Defense(MYTHIC ([[Rarity]])), +2 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Stained|+2 Defense(COMMON ([[Rarity]])), +3 Defense(UNCOMMON ([[Rarity]])), +4 Defense(RARE ([[Rarity]])), +5 Defense(EPIC ([[Rarity]])), +6 Defense(LEGENDARY ([[Rarity]])), +7 Defense(MYTHIC ([[Rarity]])), +9 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[NPC]] - [[Blacksmith]]|
|Sturdy|+3 Defense(COMMON ([[Rarity]])), +6 Defense(UNCOMMON ([[Rarity]])), +9 Defense(RARE ([[Rarity]])), +12 Defense(EPIC ([[Rarity]])), +15 Defense(LEGENDARY ([[Rarity]])), +20 Defense(MYTHIC ([[Rarity]])), +25 Defense(DIVINE ([[Rarity]]))|Mining Tool ([[Tools]])|[[NPC]] - [[Blacksmith]]|
### Reforge stones
[[Reforge Stones]] can be combine in an anvil with the item that needs to be [[Reforging|Reforged]].
|Reforge|Reforge Stone|Stats|Applied to|Source|
|-|-|-|-|-|
|Calcified|[[Calcified Heart]]|+2 Defense(COMMON ([[Rarity]])), +4 Defense(UNCOMMON ([[Rarity]])), +6 Defense(RARE ([[Rarity]])), +10 Defense(EPIC ([[Rarity]])), +14 Defense(LEGENDARY ([[Rarity]])), +18 Defense(MYTHIC ([[Rarity]])), +22 Defense(DIVINE ([[Rarity]]))|[[Armor]]|Drop - [[Banshee]]|
|Candied|[[Candy Corn]]|+1 Defense(COMMON ([[Rarity]])), +1 Defense(UNCOMMON ([[Rarity]])), +2 Defense(RARE ([[Rarity]])), +3 Defense(EPIC ([[Rarity]])), +4 Defense(LEGENDARY ([[Rarity]])), +4 Defense(MYTHIC ([[Rarity]])), +6 Defense(DIVINE ([[Rarity]]))|[[Armor]]|Fount in Trick or Treat Chests ([[Trick or Treat Chest]]) and Party Chests ([[Party Chest]])|
|Perfect|[[Diamond Atom]]|+25 Defense(COMMON ([[Rarity]])), +35 Defense(UNCOMMON ([[Rarity]])), +50 Defense(RARE ([[Rarity]])), +65 Defense(EPIC ([[Rarity]])), +80 Defense(LEGENDARY ([[Rarity]])), +110 Defense(MYTHIC ([[Rarity]])), +140 Defense(DIVINE ([[Rarity]])); Perfect Bonus: Increases Defense by 2% (Multiplicative)[Confirm]|[[Armor]]|Drop - Angry Archeologist ([[Angry Archaeologist]])|
|Renowned|[[Dragon Horn]]|+2 Defense(COMMON ([[Rarity]])), +3 Defense(UNCOMMON ([[Rarity]])), +4 Defense(RARE ([[Rarity]])), +6 Defense(EPIC ([[Rarity]])), +8 Defense(LEGENDARY ([[Rarity]])), +10 Defense(MYTHIC ([[Rarity]])), +12 Defense(DIVINE ([[Rarity]])); Grants +1% [[Magic Find]] and +1% (Additive) to ALL Combat stats.|[[Armor]]|Drop - Superior Dragon ([[Ender Dragon]])|
|Spiked|[[Dragon Scale]]|+2 Defense(COMMON ([[Rarity]])), +3 Defense(UNCOMMON ([[Rarity]])), +4 Defense(RARE ([[Rarity]])), +6 Defense(EPIC ([[Rarity]])), +8 Defense(LEGENDARY ([[Rarity]])), +10 Defense(MYTHIC ([[Rarity]])), +12 Defense(DIVINE ([[Rarity]]))|[[Armor]]|Drop - Superior Lost Adventurer ([[Lost Adventurer]])|
|Ancient|[[Precursor Gear]]|+7 Defense(COMMON ([[Rarity]])), +7 Defense(UNCOMMON ([[Rarity]])), +7 Defense(RARE ([[Rarity]])), +7 Defense(EPIC ([[Rarity]])), +7 Defense(LEGENDARY ([[Rarity]])), +7 Defense(MYTHIC ([[Rarity]])), +7 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[Dungeon Reward Chest]] - Catacombs - Floor VII ([[The Catacombs - Floor VII]])|
|Undead|[[Premium Flesh]]|+6 Defense(COMMON ([[Rarity]])), +8 Defense(UNCOMMON ([[Rarity]])), +12 Defense(RARE ([[Rarity]])), +18 Defense(EPIC ([[Rarity]])), +25 Defense(LEGENDARY ([[Rarity]])), +33 Defense(MYTHIC ([[Rarity]])), +45 Defense(DIVINE ([[Rarity]]))|[[Armor]]|Drop - All non-boss Undead ([[Undead (Mob Type)]]) enemies in The Catacombs ([[Catacombs]])|
|Reinforced|[[Rare Diamond]]|+25 Defense(COMMON ([[Rarity]])), +35 Defense(UNCOMMON ([[Rarity]])), +50 Defense(RARE ([[Rarity]])), +65 Defense(EPIC ([[Rarity]])), +80 Defense(LEGENDARY ([[Rarity]])), +110 Defense(MYTHIC ([[Rarity]])), +140 Defense(DIVINE ([[Rarity]]))|[[Armor]]|0.2% chance to drop when mining Diamonds ([[Diamond]]) in the [[Deep Caverns]]|
|Ridiculous|[[Red Nose]]|+10 Defense(COMMON ([[Rarity]])), +15 Defense(UNCOMMON ([[Rarity]])), +20 Defense(RARE ([[Rarity]])), +25 Defense(EPIC ([[Rarity]])), +35 Defense(LEGENDARY ([[Rarity]])), +50 Defense(MYTHIC ([[Rarity]])), +70 Defense(DIVINE ([[Rarity]])); Sneak to fart, granting +30 Defense for 5s.|[[Armor]]|[[Dungeon Reward Chest]] - [[The Catacombs - Floor I]]|
|Loving|[[Red Scarf]]|+4 Defense(COMMON ([[Rarity]])), +5 Defense(UNCOMMON ([[Rarity]])), +6 Defense(RARE ([[Rarity]])), +7 Defense(EPIC ([[Rarity]])), +10 Defense(LEGENDARY ([[Rarity]])), +14 Defense(MYTHIC ([[Rarity]])), +20 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[Dungeon Reward Chest]] - [[The Catacombs - Floor II]]|
|Empowered|[[Sadan's Brooch]]|+10 Defense(COMMON ([[Rarity]])), +15 Defense(UNCOMMON ([[Rarity]])), +20 Defense(RARE ([[Rarity]])), +25 Defense(EPIC ([[Rarity]])), +35 Defense(LEGENDARY ([[Rarity]])), +50 Defense(MYTHIC ([[Rarity]])), +70 Defense(DIVINE ([[Rarity]]))|[[Armor]]|[[Dungeon Reward Chest]] - [[The Catacombs - Floor VI]]|
|Fortified|[[Meteor Chunk]]|+12 Defense(COMMON ([[Rarity]])), +14 Defense(UNCOMMON ([[Rarity]])), +17 Defense(RARE ([[Rarity]])), +20 Defense(EPIC ([[Rarity]])), +25 Defense(LEGENDARY ([[Rarity]])), +30 Defense(MYTHIC ([[Rarity]])), +35 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[Crafting]] Recipe - Ghast Tear Collection Tier VI (6) ([[Ghast Tear]])|
|Blood-Soaked|[[Presumed Gallon of Red Paint]]|+1 Defense(COMMON ([[Rarity]])), +2 Defense(UNCOMMON ([[Rarity]])), +3 Defense(RARE ([[Rarity]])), +4 Defense(EPIC ([[Rarity]])), +5 Defense(LEGENDARY ([[Rarity]])), +6 Defense(MYTHIC ([[Rarity]])), +7 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[Crafting]] Recipe - Hemovibe Collection Tier VIII (8) ([[Hemovibe]])|
|Strengthened|[[Searing Stone]]|+3 Defense(COMMON ([[Rarity]])), +4 Defense(UNCOMMON ([[Rarity]])), +5 Defense(RARE ([[Rarity]])), +6 Defense(EPIC ([[Rarity]])), +8 Defense(LEGENDARY ([[Rarity]])), +10 Defense(MYTHIC ([[Rarity]])), +12 Defense(DIVINE ([[Rarity]]))|[[Equipment]]|[[Crafting]] Recipe - Magma Cream Collection Tier VI (6) ([[Magma Cream]])|
|Bulky|[[Bulky Stone]]|+4 Defense(COMMON ([[Rarity]])), +6 Defense(UNCOMMON ([[Rarity]])), +9 Defense(RARE ([[Rarity]])), +12 Defense(EPIC ([[Rarity]])), +15 Defense(LEGENDARY ([[Rarity]])), +20 Defense(MYTHIC ([[Rarity]])), +30 Defense(DIVINE ([[Rarity]]))|Sword ([[Swords]])|Found in treasure chests from the [[Treasure Hunter]]|
|Fruitful|[[Black Diamond]]|Grants +75 Defense while on [[Mining Islands]]|Mining Tool ([[Tools]])|[[NPC]] purchase - [[Mining Merchant]]|
### Enchantments
Certain [[Enchantments]] grant bonus Defense. The item that is [[Enchantments|Enchanted]] needs to be equiped/held in order for the [[Enchantments|Enchantment]] to take effect.
|Enchantment|Stats|Max Level|Applied To|Source|
|-|-|-|-|-|
|[[Protection]]|Grants +4-30 Defense (+4 Defense per level)|Level VII (7)|[[Armor]]|[[Enchantment Table]] (1-5) / [[Experimentation Table]] (3-7) / [[NPC]] purchase - [[Tomioka]] (6) / Darker Auction ([[Dark Auction]]) (7)|
|[[Counter-Strike]]|Gain +6-10 Defense for 7s on the first hit from an enemy. (+2 Defense per level)|Level V (5)|Chestplate ([[Chestplates]])|Darker Auction ([[Dark Auction]]) (5)|
|[[Hardened Vitality]]|Gain +4-40% of [[Vitality]] used near you as Defense for 10s. (+4% Defense per level) (Capped at +25 Defense)|Level X (10)|[[Armor]]|Kuudra Reward Chests ([[Kuudra]]) (1)|
|[[Chimera]] (Ultimate)|Copies +20-100% of your active pet's stats. (+20% per level)|Level V (5)|Melee Weapon ([[Weapons]])|Drop - [[Minos Inquisitor]] (1)|
|[[Last Stand]] (Ultimate)|When falling below 40% [[Health]]:; Gain +2.5-12.5% Defense (Additive)[Confirm] for 10s. (+2.5% Defense per level); (Cooldown: 30s)|Level V (5)|[[Armor]]|[[Dungeon Reward Chest]] - [[The Catacombs - Floor V]] and above. (1-2)|
|[[Legion]] (Ultimate)|Increases all Combat stats and [[Magic Find]] by 0.07-0.35% (Additive)[Confirm] per player within 30 blocks of the wielder, up to 20 players. (+0.07% per level)|Level V (5)|[[Armor]]|[[Dungeon Reward Chest]] - [[The Catacombs - Floor V]] (1)|
|[[Refrigerate]] (Ultimate)|Grants 3-6% of mana used as Defense for 10s. (+0.75% pre level) (Max +150 Defense)|Level V (5)|[[Armor]]|[[NPC]] purchace - [[Einary]] (1)|
### Accessories
Certain [[Accessories]] grant bonus Defense. An [[Accessories|Accessory]] needs to be in the [[Accessory Bag]] or the players inventory in order to take effect.
|Slot|Name|Stats|Source|
|-|-|-|-|
|[[Safety Badge]]|[[Safety Badge]]|+3 Defense|Reward - [[Security Clerk]]|
|[[Gravity Talisman]]|[[Gravity Talisman]]|Gives between +1 and +10 [[Strength]] and Defense the closer you are to the spawn of an Island!|[[Crafting]] Recipe - Obsidian Collection Tier III (3) ([[Obsidian]])|
|[[Day Crystal]]|[[Day Crystal]]|Increases your [[Strength]] and Defense by +5 during the Day.|[[Crafting]] Recipe - Nether Quartz Collection Tier VIII (8) ([[Nether Quartz]])|
|[[Night Crystal]]|[[Night Crystal]]|Increases your [[Strength]] and Defense by +5 during the Night.|[[Crafting]] Recipe - Nether Quartz Collection Tier VII (7) ([[Nether Quartz]])|
|[[Sunshine Crystal]]|[[Sunshine Crystal]]|Increases your [[Strength]] and Defense by +10 during the Day.|[[Crafting]] Recipe - Sunflower Collection Tier VIII (8) ([[Sunflower]]); Upgraded [[Day Crystal]]|
|[[Moonlight Crystal]]|[[Moonlight Crystal]]|Increases your [[Strength]] and Defense by +10 during the Night.|[[Crafting]] Recipe - Moonflower Collection Tier VIII (8) ([[Moonflower]]); Upgraded [[Night Crystal]]|
|[[Bat Person Talisman]]|[[Bat Person Talisman]]|Grants +2 Defense, [[Strength]] and [[Intelligence]] for each bat you have summoned.|Found in Trick or Treat Chests ([[Trick or Treat Chest]]) and Party Chests ([[Party Chest]])|
|[[Bat Person Ring]]|[[Bat Person Ring]]|Grants +5 Defense, [[Strength]] and [[Intelligence]] for each bat you have summoned.|Upgraded [[Bat Person Talisman]] using [[Ectoplasm]] and Spooky Fragments ([[Spooky Fragment]])|
|[[Bat Person Artifact]]|[[Bat Person Artifact]]|Grants +10 Defense, [[Strength]] and [[Intelligence]] for each bat you have summoned.|Upgraded [[Bat Person Ring]] using [[Ectoplasm]] and Spooky Fragments ([[Spooky Fragment]])|
|[[General's Medallion]]|[[General's Medallion]]|Increases the base stats of your dungeon items by 1-5% (Additive with similar buffs) while in The Catacombs for each digit on your secret count.|[[NPC]] Purchase - [[Zodd]]|
|Stat Tuning ([[Maxwell]])|Stat Tuning ([[Maxwell]])|Gain +1 Defense per Tuning Point.|For each 10 Accessory Power ([[Accessory Power]]) gain 1 Tuning Point; Tuning Box ([[Attributes]]) - 1-13 Tuning Points|
|[[Enrichments]]|Defense Enrichment ([[Enrichments]])|Enriches an accessory with the power of +1 Defense when applied to a LEGENDARY ([[Rarity]]) or higher accessory.|[[NPC]] purchase - [[Elizabeth]]|
### Accessory Powers
Certain [[Powers|Accessory Powers]] grant Defense based on the players [[Accessory Power]]. Only one [[Powers|Accessory Power]] can be active at any time.
|Slot|Name|Stats|Source|
|-|-|-|-|
|[[End Stone Shulker]]|[[End Stone Shulker]]|Stat: Defense, Stats - Adept Base: 40, Stats - Adept 250 AP ([[Accessory Power]]): 92.56, Stats - Adept 500 AP ([[Accessory Power]]): 177.24, Stats - Adept 1,000 AP ([[Accessory Power]]): 310.2, Stats - Adept 1,500 AP ([[Accessory Power]]): 411.73, Stats - Adept 2,000 AP ([[Accessory Power]]): 493.83 ‎Unique Power Bonus: +50 Defense|Found in [[Ender Nodes]]|
|[[Glacite Chunk]]|[[Glacite Chunk]]|Stat: Defense, Stats - Frozen Base: 55, Stats - Frozen 250 AP ([[Accessory Power]]): 127.27, Stats - Frozen 500 AP ([[Accessory Power]]): 243.7, Stats - Frozen 1,000 AP ([[Accessory Power]]): 426.52, Stats - Frozen 1,500 AP ([[Accessory Power]]): 566.13, Stats - Frozen 2,000 AP ([[Accessory Power]]): 679.02 ‎|Drop - [[Glacite Mutt]], [[Glacite Mage]], [[Glacite Bowman]] and [[Glacite Caver]]|
|[[Hazmat Enderman]]|[[Hazmat Enderman]]|Stat: Defense, Stats - Slender Base: 25, Stats - Slender 250 AP ([[Accessory Power]]): 57.85, Stats - Slender 500 AP ([[Accessory Power]]): 110.77, Stats - Slender 1,000 AP ([[Accessory Power]]): 193.87, Stats - Slender 1,500 AP ([[Accessory Power]]): 257.33, Stats - Slender 2,000 AP ([[Accessory Power]]): 308.64 ‎Unique Power Bonus: +100 Defense|Drop - Tier III+ [[Voidgloom Seraph]]|
|[[Obsidian Tablet]]|[[Obsidian Tablet]]|Stat: Defense, Stats - Mythical Base: 17, Stats - Mythical 250 AP ([[Accessory Power]]): 39.34, Stats - Mythical 500 AP ([[Accessory Power]]): 75.33, Stats - Mythical 1,000 AP ([[Accessory Power]]): 131.83, Stats - Mythical 1,500 AP ([[Accessory Power]]): 174.99, Stats - Mythical 2,000 AP ([[Accessory Power]]): 209.88 ‎|[[Crafting]] Recipe - Obdisian Collection Tier IX (9) ([[Obsidian]])|
|[[Precious Pearl]]|[[Precious Pearl]]|Stat: Defense, Stats - Pleasant Base: 60, Stats - Pleasant 250 AP ([[Accessory Power]]): 138.85, Stats - Pleasant 500 AP ([[Accessory Power]]): 265.86, Stats - Pleasant 1,000 AP ([[Accessory Power]]): 465.29, Stats - Pleasant 1,500 AP ([[Accessory Power]]): 617.6, Stats - Pleasant 2,000 AP ([[Accessory Power]]): 740.75 ‎|Found in Crystal Nucleus Rewards ([[Crystal Nucleus]])|
|[[Rock Candy]]|[[Rock Candy]]|Stat: Defense, Stats - Sweet Base: 45, Stats - Sweet 250 AP ([[Accessory Power]]): 104.13, Stats - Sweet 500 AP ([[Accessory Power]]): 199.39, Stats - Sweet 1,000 AP ([[Accessory Power]]): 348.97, Stats - Sweet 1,500 AP ([[Accessory Power]]): 463.2, Stats - Sweet 2,000 AP ([[Accessory Power]]): 555.56 ‎|Found in Trick or Treat Chests ([[Trick or Treat Chest]]) and Party Chests ([[Party Chest]])|
### Miscellaneous
|Slot|Name|Stats|Source|
|-|-|-|-|
|[[Hot Potato Book]]|[[Hot Potato Book]]|When applied to armor, grants +2 Defense and +4 [[Health]].; This can be applied to an item up to 10 times!|[[Crafting]] Recipe - Potato Collection Tier VIII (8) ([[Potato]])|
|[[Fuming Potato Book]]|[[Fuming Potato Book]]|When applied to armor, grants +2 Defense and +4 [[Health]].; This book bypasses the [[Hot Potato Book]] limit of 10, allowing you to upgrade an item up to 15 times!|[[Dungeon Reward Chest]] - All Floors|
|[[Dungeoneering]]|Catacombs Skill Level ([[Dungeoneering]])|Increases the base stats on Dungeon ([[Dungeons]]) items by +10-485% (Additive with similar buffs) while in a Dungeon ([[Dungeons]]).|Obtained by completing or failing a Dungeon ([[Dungeons]]) run|
|✪Upgrade Stars ([[Star Upgrades]])|Upgrade Stars ([[Star Upgrades]])|Items gain 2% (Additive with similar buffs) more base stats. While in a dungeon dungeonized items instead gain 10% (Additive with similar buffs) more stats in [[Dungeons]] per ✪ Upgrade Star ([[Star Upgrades]]) applied.|[[NPC]] - [[Malik]], [[Igor]], [[Alwin]] or [[The Hex]]|
|[[Master Star]]|Master Stars ([[Master Star]])|✪✪✪✪✪ Dungeon items gain 5% (Additive with similar buffs) more base stats in Master Mode ([[Catacombs]]) per [[Master Star]] applied. Up to 25% with 5 Master Stars ([[Master Star]]).|[[Dungeon Reward Chest]] - Master Mode Floor III (3) - VII (7) ([[Catacombs]])|
|[[Dungeon Blessing]]|[[Dungeon Blessing]]|Gain Level*2% (multiplicitive) and Level*4 Defense|Killing the final ✯ Starred mob in a room ([[Catacombs Rooms]]); Killing a Bat ([[Bat (disambiguation)]]); Opening a Dungeon Secret Chest ([[Dungeon Secrets]]) or a Dungeon Puzzle Chest ([[Catacombs Puzzle Rooms]])|
|[[Undead Essence]]|Undead Essence Shop ([[Essence Shops]])|+5-50 Defense while in [[Dungeons]].|[[NPC]] Purchase - [[Malik]]|
|[[Wither Essence]]|Wither Essence Shop ([[Essence Shops]])|Dungeon Blessings ([[Dungeon Blessing]]) are 1-10% (multiplicitive) stronger on you.|[[NPC]] Purchase - [[Malik]]|
|[[Gemstone]]|Amethyst ([[Gemstone]])|When inserted into a Amethyst Slot, ☤ Defensive Slot or ⚔ Combat Slot, grants Defense based in the items rarity and tier of gemstone.; Rough: +1 /+2 /+3 /+4 /+5 /+7; Flawed: +3 /+4 /+5 /+6 /+8 /+10; Fine: +4 /+5 /+6 /+8 /+10 /+14; Flawlwss: +5 /+7 /+10 /+14 /+18 /+22; Perfect: +6 /+9 /+13 /+18 /+24 /+30|Mining Amethyst Gemstones ([[Gemstone]]), [[Crafting]] and Forging ([[The Forge]])|
|[[End Stone Protector Shard]]|[[End Stone Protector Shard]]|Your Defense is increased by +0.2-2% (Additive).|[[Charm]] - [[End Stone Protector]]; ID Fusing ([[Attribute Fusion]]) and Chameleon Fusing ([[Attribute Fusion]])|
|[[Mimic Shard]]|[[Mimic Shard]]|Dungeon Blessings ([[Dungeon Blessing]]) are 1-10% (Multiplicitive) stronger on you.|[[Charm]] - [[Mimic]]; ID Fusing ([[Attribute Fusion]]) and Chameleon Fusing ([[Attribute Fusion]])|
|[[Kada Knight Shard]]|[[Kada Knight Shard]]|When under 20% Maximum Health ([[Health]]), your [[Damage]] and Defense is increased by +2.5-25%. (Additive)|[[Charm]] - [[Kada Knight]]; Catch with a Pocket Black Hole ([[Black Holes]]); Kuudra Reward Chests ([[Kuudra]])|
|[[Molthorn Shard]]|[[Molthorn Shard]]|Your "Unlimited" Attributes are +5-50% stronger.|Fusing ([[Attribute Fusion]]) - [[Etherdrake Shard]] with [[Jormung Shard]]|
|[[Tiamat Shard]]|[[Tiamat Shard]]|Your "Echo" Attributes are 5-50% stronger.|Fusing ([[Attribute Fusion]]) - [[Caiman Shard]] with Combat Category and EPIC ([[Rarity]]) or higher|
|[[Resistance Potion]]|[[Resistance Potion]]|Grants 5-60 Defense. Using a [[Tepid Green Tea]] instead of an [[Awkward Potion]] when brewing will increase the bonus by 10%.|Brewing ([[Potions]]) Recipe - Cactus Collection Tier III (3) ([[Cactus]]); Drinking a [[God Potion]], (Adds the Tepid Green Tea bonus)|
|[[Century Cakes]]|Pet Rock Century Cake ([[Century Cakes]])|Eating this cake grants +3 Defense for 48 hours. Does not consume the cake.|Opening a [[Random Century Cake Bundle]], [[Complete Century Cake Bundle]], Cake Slices ([[Cake Slice]]), as a Minor reward from the [[Raffle of the Century]] or from visiting another player's island who have one placed down|
|Heart of the Mountain|Lonesome Miner ([[Heart of the Mountain]])|Increases Defense by 5-27% (Multiplicative) while on [[Mining Islands]]. (+0.5% with [[Blue Cheese Goblin Omelette]])|[[Heart of the Mountain]] Tier 6 ([[Heart of the Mountain]])|
|Heart of the Forest|Galatea's Might ([[Heart of the Forest]])|Gain 0.5-25% (Additive) Combat Stats on [[Galatea]].|[[Heart of the Forest]] Tier 3 ([[Heart of the Forest]])|
|Dungeon Floor Buff ([[Dungeons]])|Dungeon Floor Buff ([[Dungeons]])|Increases the power of Dungeon Blessings ([[Dungeon Blessing]]) by 20%[More Info Needed] (More infomation needed; When this info is added, remove this.)|Applied if playing on [[The Catacombs - Floor III]] or higher|
|[[Paul]]|Mayor Paul ([[Paul]])|Dungeon Blessings ([[Dungeon Blessing]]) are 25% (multiplicitive) stronger.|Applied to everyone if [[Paul]] is in office|
|Mayor Jerry ([[Candidate Jerry]])|Mayor Jerry ([[Candidate Jerry]])|Increases all Combat and Miscellaneous stats by 10% (Additive).|Applied to everyone if Mayor Jerry ([[Candidate Jerry]]) is in office|
## Conditional Denfense
Some items can grant conditional Defense. Conditional Defense works the same as Defense but only against a certain type / group of mob / damage source, and therefore doesn't appear in the players stat screen.
### Pets
Some [[Pets]] grant conditional Defense against certain groups of mobs. The [[Pets|Pet]] needs to be equiped in order to take effect.
|Slot|Name|Rarity|Stats|Source|
|-|-|-|-|-|
|[[Wisp Pet]]|[[Wisp Pet]]|UNCOMMON ([[Rarity]]) - LEGENDARY ([[Rarity]])|Ability: Bulwark; Kill Blazes to gain Defense against them and demons.; Bonus: +0-600 & +0-60 [[True Defense]]|[[Crafting]] Recipe - Blaze Slayer Level 1/3/5/7 ([[Blaze Slayer]])|
### Armor
Some [[Armor]] grants conditional Defense against certain groups of mobs. The [[Armor]] needs to be equiped in order to take effect.
|Armor|Stats|Source|
|-|-|-|
|[[Revenant Armor]]|Piece Bonus: Zombie Bulwark; Kill Zombies to accumulate Defense against them.; Piece Bonus: +0-315|[[Crafting]] Recipe - Zombie Slayer Collection IV (4) ([[Zombie Slayer]])|
|[[Reaper Armor]]|Full Set Bonus: Trolling The Reaper; Gain +100 Defense against Undead ([[Undead (Mob Type)]]) mobs.; Piece Bonus: Zombie Bulwark; Kill Zombies to accumulate Defense against them.; Piece Bonus: +0-315|[[Crafting]] Recipe - Zombie Slayer Collection VII (7) ([[Zombie Slayer]]); Upgraded [[Revenant Armor]]|
|[[Tarantula Armor]]|Piece Bonus: Spider Bulwark; Kill Spiders to accumulate Defense against them.; Piece Bonus: +0-285|[[Crafting]] Recipe - Spider Slayer Collection IV (4) ([[Spider Slayer]])|
|[[Primordial Armor]]|(same as above)|[[Crafting]] Recipe - Spider Slayer Collection VII (7) ([[Spider Slayer]]); Upgraded [[Tarantula Armor]]|
|[[Armor of the Pack]]|Gain +50 Defense against [[Animal]] mobs. (Per piece)|[[Crafting]] Recipe - Wolf Slayer Collection VI (6) ([[Wolf Slayer]])|
|[[Final Destination Armor]]|Piece Bonus: Wnderman Bulwark; Kill Enderman to accumulate Defense against them.; Piece Bonus: +0-400|[[Crafting]] Recipe - Enderman Slayer Collection III (3) ([[Enderman Slayer]])|
### Enchantments
Some [[Enchantments]] grant conditional Defense against types of damage.
|Enchantment|Stats|Max Level|Applied To|Source|
|-|-|-|-|-|
|[[Projectile Protection]]|Grants +7-49 Defense against projectiles.|Level VII (7)|[[Armor]]|[[Enchantment Table]] (1-5) / [[Experimentation Table]] (3-7)|
|[[Blast Protection]]|Grants +30-210 Defense against projectiles.|Level VII (7)|[[Armor]]|[[Enchantment Table]] (1-5) / [[Experimentation Table]] (3-7)|
### Attributes
Some [[Attributes]] grant conditional Defense against certain types of mobs.
|Slot|Attribute|Effect|Source|ID|
|-|-|-|-|-|
|[[Howling Spirit Shard]]|Animal Resistance ([[Attributes]])|Grants +4-40 Defense on [[Animal]] Mobs.|[[Charm]] - [[Howling Spirit]] or [[Pack Spirit]]; Catch with a Pocket Black Hole ([[Black Holes]])|C6|
|[[Dumpster Diver Shard]]|Aquatic Resistance ([[Attributes]])|Grants +4-40 Defense on [[Aquatic]] Mobs.|[[Charm]] - [[Dumpster Diver]]; Catch with a Pocket Black Hole ([[Black Holes]])|C8|
|[[Voracious Spider Shard]]|Arthropod Resistance ([[Attributes]])|Grants +4-40 Defense on [[Arthropod]] Mobs.|[[Charm]] - [[Voracious Spider]]; Catch with a Pocket Black Hole ([[Black Holes]])|C15|
|[[Tank Zombie Shard]]|Undead Resistance ([[Attributes]])|Grants +4-40 Defense on Undead ([[Undead (Mob Type)]]) Mobs.|[[Charm]] - [[Tank Zombie]] or [[Super Tank Zombie]]; Catch with a Pocket Black Hole ([[Black Holes]])|C18|
|[[Zealot Shard]]|Ender Resistance ([[Attributes]])|Grants +4-40 Defense on [[Ender]] Mobs.|[[Charm]] - [[Zealot]]; Catch with a Pocket Black Hole ([[Black Holes]])|C21|
|[[Bezal Shard]]|Blazing Resistance ([[Attributes]])|Grants +4-40 Defense on Infernal ([[Infernal (Mob Type)]]) Mobs.|[[Charm]] - [[Bezal]]; Catch with a Pocket Black Hole ([[Black Holes]]); Kuudra Loot Chests ([[Kuudra]])|C30|
|[[Stag Beetle Shard]]|Woodland Resistance ([[Attributes]])|Grants +4-40 Defense on [[Woodland]] Mobs.|Catch a [[Stag Beetle]] with a Lasso ([[Lassos]])|C31|
|[[Cretan Bull Shard]]|Mythological Resistance ([[Attributes]])|Grants +4-40 Defense on [[Mythological]] Mobs.|[[Charm]] - [[Cretan Bull]]; Catch with a Pocket Black Hole ([[Black Holes]])|C39|
|[[Strongarm Shard]]|Frozen Resistance ([[Attributes]])|Grants +4-40 Defense on Frozen ([[Frozen (Mob Type)]]) Mobs.|Catch a [[Strongarm]] in a [[Critter Capsule]] in the [[Critter Safari]]; Floor Drop ([[Floor Drops/Safari]]) in the [[Critter Safari]]|C42|
|[[Haggard Shard]]|Skeletal Resistance ([[Attributes]])|Grants +4-40 Defense on [[Skeletal]] Mobs.|[[Charm]] - [[Haggard]]; Placing Hunting Traps ([[Huntraps]]) in the [[Spring Shallows]] (Underwater)|C44|
|[[Brineling Shard]]|Arcane Resistance ([[Attributes]])|Grants +4-40 Defense on [[Arcane]] Mobs.|[[Charm]] - [[Brineling]]; Placing Hunting Traps ([[Huntraps]]) in the [[Spring Shallows]] (Underwater)|C47|
|[[Blue Jay Shard]]|Airborne Resistance ([[Attributes]])|Grants +4-40 Defense on [[Airborne]] Mobs.|Catch a [[Blue Jay]] with a Lasso ([[Lassos]])|C58|
|[[Alligator Shard]]|Echo of Resistance ([[Attributes]])|Your Resistance Attributes are +2-20% stronger.|[[Charm]] - [[Alligator]] (Guaranteed); Placing Hunting Traps ([[Huntraps]]) in the [[Backwater Bayou]] (Underwater); Fusing ([[Attribute Fusion]]) - [[Crocodile Shard]] with Combat Category and RARE ([[Rarity]]) or higher|E6|
|[[Tiamat Shard]]|Echo of Echos ([[Attributes]])|Your "Echo" Attributes are 5-50% stronger.|Fusing ([[Attribute Fusion]]) - [[Caiman Shard]] with Combat Category and EPIC ([[Rarity]]) or higher|L6|
## Achieving Maximum Defense
This article needs to be reworked as its content is outdated. You can help the wiki by editing this page and reworking it.
This article was last edited by Steelhalo (contribs|logs|block) on 9:11, October 23 2026 (3 days ago)
By getting all of the following, the highest possible permanent Defense can be achieved.
- Base Defense (100 Defense )
- Maxed out [[Mining]] skill ( 104 Defense )
- [[Undead Essence|Undead]] [[Essence Shops|Essence Shop]], [[Essence Shops|Wither Essence Shop]] ( 5 Defense + 50 Defense )
- A full set of [[Perfect Armor|Perfect Armor - Tier XIII]] with the following: (2500 Defense)
  - [[Perfect Armor|Perfect Armor - Tier XIII]] (1460 Defense)
  - [[Protection|Protection VII]] (+120 Defense)
  - [[Recombobulator 3000|Recombobulated]] with 3x [[Gemstone|Perfect Amethyst Gemstones]] applied to each piece (+360 Defense)
  - 10x [[Hot Potato Book|Hot Potato Books]] applied to each piece (+80 Defense)
  - 5x [[Fuming Potato Book|Fuming Potato Books]] applied to each piece (+40 Defense)
  - Reforged with [[Diamond Atom|Diamond Atoms]] (+440 Defense)
- [[Rarity|LEGENDARY]] [[Turtle Pet]] with [[Reinforced Scales]] (+100 Defense + +40 Defense)
- Maxed [[Astraea]] with [[Catacombs|Catacombs L (50)]] : (571 Defense)
  - Weapon's base stats (250 Defense)
  - Special effects with [[Catacombs|Catacombs L (50)]] (+100 Defense)
  - Reforge [[Bulky Stone|Bulky]] (require to be [[Recombobulator 3000|Recombobulated]] for [[Rarity|MYTHIC]]) (+21 Defense)
  - [[Gemstone|Perfect Amethyst Gemstones]] (+60 Defense)
  - [[Enchanted Book|Chimera V]] (+140 Defense)
- Equipment with [[Recombobulator 3000]] and [[Meteor Chunk|Fortified]]: (150 Defense + 100 Defense)
  - [[Synthesizer v3]] +40 Defense
  - [[Molten Cloak]] +20 Defense
  - [[Implosion Belt]] +70 Defense
  - [[Molten Bracelet]] +20 Defense
- [[Accessory Power]] (2050) (957 Defense)
  - [[Precious Pearl|Pleasant]] or [[Glacite Chunk|Frozen]] (752 Defense)
  - 205 [[Maxwell|Tuning Points]] (205 Defense)
- [[Century Cakes|Pet Rock Century Cake]] (3 Defense)
- 5x [[Festering Maggot]] (5x1 Defense)
- [[Accessories]] (125 Defense)
  - [[Sunshine Crystal]]/ [[Moonlight Crystal]] (10 Defense)
  - [[Gravity Talisman]] while the player's standing in close proximity to the spawn of the island they are on (10 Defense)
  - [[Black Belt]] (25 Defense)
  - [[Relic of Power]] (15 Defense)
  - 65x [[Enrichments|Defense Enrichment]] (65 Defense)
Multiplicative:
- [[Rarity|LEGENDARY]] [[Turtle Pet]] (Turtle Tactics): Gain +30% Defense and an additional +10% Defense when standing still.
- 4 players within 50 blocks of you with a [[Rarity|LEGENDARY]] [[Turtle Pet]] (Genius Amniote): +10% Defense.
- [[Candidate Jerry]] +10%
- [[End Stone Protector Shard]] +2%
- Armor reforged with [[Diamond Atom|Diamond Atoms]] +8%
[Confirm] This setup will give 6183 Defense.
## Trivia
- When Defense approaches infinity (i.e. having the maximum defense), the damage reduction approaches 100%.
  - However, the 100% is an estimated number, due to how Effective Health is calculated.
  - To truly get infinite Effective Health, the only way is to let the naturally regenerated Effective Health outclass the [[Damage]] taken.
## History
[[SkyBlock Prototype]]:
|Jun 11, 2019|0.1|Added Defense.|
|Jun 7, 2020|0.7.10|Added [[Effective Health]] to the [[Stats]] menu under Defense.|
|Mar 18, 2024|Fixed being able to heal from taking [[Damage]] with a very high Defense amount.|
|Mar 26, 2024|Fixed another case of being able to heal from taking [[Damage]] with a high Defense value.|
|Jul 8, 2026|0.26|Updated Defense Icon|
Linked from: [[Absorption]], [[Abyssal Armor]], [[Accessories/Misc Crafts]], [[Accessories/Obtained From Collections or Recipes]], [[Accessories/Quests and Trials]], [[Adaptive Armor]], [[Adaptive Belt]], [[Adaptive Blade]], [[Admin]], [[Airborne]], [[Ammonite Pet]], [[Angler Armor]], [[Angry Archaeologist]], [[Animal]], [[Ankylosaurus Pet]], [[Apex Dragon]], [[Aquatic]], [[Arachne's Armor]], [[Arachne's Belt]], [[Arachne's Cloak]], [[Arachne's Gloves]], [[Arachne's Necklace]], [[Arcane]], [[Armadillo Pet]], [[Armor]], [[Armor of Divan]], [[Armor of Growth]], [[Armor of Magma]], [[Armor of the Pack]], [[Armor of the Rising Sun]], [[Armor of the Stars]], [[Armor/Boots]], [[Armor/Chestplates]], [[Armor/Dungeon Sets]], [[Armor/Helmets]], [[Armor/Leggings]], [[Armor/Sets]], [[Arrows]], [[Arthropod]], [[Astraea]] (+520 more)

# Drop Chance
Aliases: Drop chance, Drops, Mob Drop, Mob drop, Odds
Categories: Confirmations needed, Mechanics, Slayer, Pages with math equations
Drop Chance or Odds is the in-game denotation of how common a drop is from a [[Mob]]. Drop chances can be viewed through the bestiary when the player has gained enough kills against the mob.
## Bestiary Mobs
- All drops, 6Rare Loot or up, will still shows "Rare Drop!" in chat even if that is not the rarity.
- Bestiary mobs do not share the same item drop chances:
|Odds 2Common Loot 4Uncommon Loot 6Rare Loot 8Legendary Loot|Drop Chance 30.01%-100% 1.01%-30% 0.11%-1% 0.02%-0.1%|
|-|-|
|10RNGesus Loot|≤0.01%|
## RNG Meter and Slayer
All drops, 3Occasional or up, will still shows "Rare Drop!" in chat even if that is not the rarity.
|Odds|Drop Chance|Examples|
|-|-|-|
|1Guaranteed|100%|[[Revenant Flesh]] [[Tarantula Web]] [[Wolf Tooth]] Most [[Mob]] drops|
|3Occasional|20%|[[Foul Flesh]] [[Toxic Arrow Poison]] Hamster Wheels ([[Hamster Wheel]])|
|5Rare|5%|Pestilence Rune ([[Runes]]) [[Null Atom]]|
|7Extraordinary|1%|[[Hazmat Enderman]] [[Revenant Catalyst]]|
|9Pray RNGesus|<1%|[[Overflux Capacitor]] [[High Class Archfiend Dice]]|
|11RNGesus Incarnate|<<1%|[[Warden Heart]] [[Primordial Eye]] [[Exceedingly Rare Ender Artifact Upgrade]]|
## Increasing drop chances
Drops from killing a mob that is not a [[Slayer|Slayer Boss]] are generally affected by the following modifiers:
- [[Looting]] (all items except pets)
- [[Luck]] (armor pieces only)
Certain other sources, such as the [[Pity and RNG Meters|RNG Meter]] for slayers, [[Hound Pet]], or [[Mole Pet]] can also increase the base drop chance of certain items.
Most items with drop chances that are lower than 5% after the above modifications are generally affected by [[Magic Find]] (as well as [[Pet Luck]] if it is a pet).
A general formula is as follows (with non-applicable buffs being set to 0):
Base Chance×(1+Looting Level×0.15)×(1+Luck Level×0.05)×(1+Magic Find + Pet Luck100)
For drops from [[Pests]], [[Looting]] and [[Luck]] do not apply even if the player swaps to a weapon with those enchantments. Additionally, instead of [[Magic Find]], [[Overbloom]] is used. The formula looks like this:
Base Chance×(1+Overbloom100)
Note that guaranteed drops from Pests use [[Farming Fortune]] and [[Crop Fortune]] with a different scaling formula.
## Pet drop chances
[[Pets|Pet]] drops are calculated/rolled in a way that causes the true statistical chance to differ considerably from the chances shown in the [[Bestiary]]:
1. rolls for whether a pet drops at all using the pet's most common rarity's drop chance [Confirm (Confirmation needed; This is the presumed generalization, for Scathas it is confirmed to use the rare chance; When this info is confirmed, remove this.)]
2. if 1. succeeded, rolls for the rarity using their respective weights
This means that for any given rarity, the statistical chance can be calculated using the following formula:
Most Common Rarity Chance×(Rarity ChanceSum of all Rarity's Chances)
The ratio between the chances displayed in the [[Bestiary]] and the true drop rates can be calculated as Most Common Rarity ChanceSum of all Rarity's Chances.
e.g. [[Scatha Pet]]: 0.24%0.4%=0.6=60%, meaning [[Scatha Pet]] drop rates are only 60% of what the [[Bestiary]] claims.
## History
[[SkyBlock Prototype]]:
|Jun 11, 2019|0.1|Added Drop Chance.|
Linked from: [[Abyssal Miner]], [[Acacia Log]], [[Admin]], [[Agarimoo]], [[Agarimoo Tongue]], [[Alligator]], [[Alligator Skin]], [[Ancient Claw]], [[Ancient Rose]], [[Angry Archaeologist]], [[Ant]], [[Antique Remedies]], [[Apostle]], [[Aquamarine Dye]], [[Arachne's Brood]], [[Arachne's Calling]], [[Arachne's Keeper]], [[Archfiend Dice]], [[Areita]], [[Arrow Poison]], [[Ashfang]], [[Atmospheric Filter]], [[Atoll Croaker]], [[Atoned Champion]], [[Atoned Revenant]], [[Automaton]], [[Autonull]], [[Azure]], [[Baby Magma Slug]], [[Baby Yeti Pet]], [[Bacte]], [[Bacte Fragment]], [[Bal]], [[Bald Blaze]], [[Bambuleaf]], [[Banshee]], [[Barbarian]], [[Barbarian Duke X]], [[Barbarian Guard]], [[Barking Wolf]] (+987 more)

# Dungeon Score
Aliases: S+, Score
Categories: Confirmations needed, Dungeons, Catacombs, Pages with math equations
[Dungeon Score]
Highest Dungeon Score possible (in normal circumstances, and without Mimics ([[Mimic]])). The small skulls between headline and score represent the Dungeon floor the rank has been achieved on.
Dungeon Score is a number granted at the end of a [[Dungeons]] run in [[Catacombs|The Catacombs]]. Earning a higher score allows more [[Dungeon Reward Chest|Dungeon Reward Chests]] to be claimed and more [[Catacombs|Catacombs XP]] and [[Classes|Class XP]] to be rewarded.
## Rankings
There are six different rankings that correspond to different score ranges.
|Ranking|Score Needed|
|-|-|
|D (Score between 0 and 99 points.)|0-99|
|C (Score between 100 and 159 points.)|100-159|
|B (Score between 160 and 229 points.)|160-229|
|A (Score between 230 and 269 points.)|230-269.4|
|S (Score between 270 and 299 points.)|269.5-299|
|S+ (Score above 300 points.)|≥300|
## Calculation
### Skill
Every death subtracts 2 points from the final skill score. Additionally, every failed [[Dungeon Puzzle Rooms|puzzle]] subtracts 14 points from the score.
If the first player to die in a Dungeon run has a [[Rarity|LEGENDARY]] [[Spirit Pet]] in their pets menu, the score penalty for their death is reduced to 1.
This formula only works with complete runs.:
  Skill=⌊100−Deaths×2−Failed Puzzles×14⌋
### Explore
A room is considered complete when all star mobs of the room have been defeated. In the case of Trap rooms, they are considered complete when the last secret within them is found. This is the upper chest in the 3-secret variation, and the chest in the right hand side room in the 4-secret variation. Completed rooms are marked with a white tick on the [[Magical Map]].
60 points of the base score is multiplied by the percentage of cleared rooms in a dungeon run (displayed in the sidebar). The other 40 points of the explore score is a maximum of 40 points for [[Dungeon Secrets|secrets]].
SecretRequirement={30%on Floor 140%on Floor 250%on Floor 360%on Floor 470%on Floor 585%on Floor 6100%on Floor 7 and Master Mode
Explore=⌊60×Cleared RoomsTotal Rooms⌋+⌊40×Secrets FoundSecret Requirement×Total Secrets(Max 40)⌋
[Confirm (Confirmation needed; When this info is confirmed, remove this.)]
### Speed
Players have a set amount of minutes to clear a dungeon before the Speed score starts to decrease.
|Floor|Time (minute) Normal Mode|Time (minute) Master Mode|
|-|-|-|
|1|10|8|
|2|10|8|
|3|10|8|
|4|12|8|
|5|10|8|
|6|12|10|
|7|14|14|
After this, speed is deducted by 1 every 12 seconds until 90, every 24 seconds until 80, every 30 seconds until 70, and every 40 seconds onwards.[Confirm]
This applies only if they win the dungeon run. If they do not beat the final boss, the speed score is the percentage of the dungeon rooms that have been cleared.
  T={Total Seconds−120on Floor 1, 2, 3, 5Total Seconds−240on Floor 4, 6Total Seconds−360on Floor 7Total Secondson Master Mode Floor 1-5Total Seconds−120on Master Mode Floor 6Total Seconds−360on Master Mode Floor 7
  Speed={100T<480⌈140−(1/12)T⌉480≤T<600⌈115−(1/24)T⌉600≤T<840⌈108−(1/30)T⌉840≤T<1140⌈98.5−(1/40)T⌉1140≤T<39400T≥3940[Confirm]
### Bonus
Up to 5 bonus Score is awarded for killing [[Crypt Undead|Crypt Undeads]] in blown up Crypts.
  Bonus={5Crypts Cleared>5Crypts Clearedotherwise
On [[The Catacombs - Floor VI]] and above, killing the [[Mimic]] grants 2 bonus Score.
If [[Paul]] is mayor and his EZPZ perk is active, then 10 bonus Score will be awarded in addition to the crypt bonus.
If a player who has [[Attributes|Reborn]] attribute kills a [[Prince]], there is a 10%–100% chance to add 1 Bonus score to the Dungeon Run. This is capped at 1 trigger per run.
If a player who has [[Attributes|Rekindle]] attribute kills a [[Bat (Catacombs)|Bat]], there is a 10%–100% chance to add 1 Bonus score to the Dungeon Run. This is said to be capped at 1 trigger per run, but is actually capped at 1 trigger per player per run, up to a total of 5 Score, possibly due to a bug.
### Score Calculator
calcpage  = Calculator:Dungeon Score
 template  = Template:Calculator/Dungeon Score
 form      = DungeonScoreCalcForm
 result    = inner

 param     = floor|Floor||select|Floor 1, Floor 2, Floor 3, Floor 4, Floor 5, Floor 6, Floor 7, Master Mode
 param     = deaths|Deaths|0|int
 param     = failedpuzzles|Failed Puzzles|0|int
 param     = dungeonclear|Dungeon Clear|100|int
 param     = secretsfound|Secrets Found|100|number
 param     = time|Time|600|int
 param     = crypts|Crypts|5|int
 param     = mimics|Mimics|0|int
 param     = ezpz|Paul EZPZ|Inactive|select|Active, Inactive
 param     = prince|Prince Attribute triggered|No|select|Yes, No
 param     = murkbat|Murkbat Attribute triggers|0|int
Loading Calculator...
If the calculator fails to load up, please report to an Administrator.
## Trivia
- Many people once thought that killing fairies would decrease the final Dungeon Score. However, this has been proven to be a misconception.
- If the boss is not killed, Dungeon Score will be reduced by 30%.
- The maximum amount of deaths a party can have and still get S+ is 2 on floors 0-5, and 3 in floor 6 and 7.
  - If Paul is mayor, the maximum number of deaths is increased by 5.
  - If the first person to die in a run had a [[Rarity|LEGENDARY]] [[Spirit Pet]], the maximum number of deaths wouldn't be affected by that death. Every death after the first death counts.
- An indication that calculates Dungeon Score for each dungeon run so far has been added to the scoreboard(to the right of "Cleared:" section).
## Data
The following table represents a selected dataset of many dungeon runs to test theories about how certain scores could have been calculated. Once all 4 formulas are confirmed and working this dataset becomes obsolete and may be deleted. https://docs.google.com/spreadsheets/d/1Pw5u6je86vw6XS-PVB3CHdebTq0ZFKTUZOl5cEk5ihg/edit?usp=sharing
You can help the wiki by adding data to this table through the provided Google Form!
Having not enough data for correctly reverse engineering the formulas, there has been created a google form to ask the community for help. Maybe one day we have enough data to successfully replicate the formulas.
Link to the form: https://forms.gle/FhKD23cB3nKqBJQa6
The data collected is then available to everyone over the following link: https://docs.google.com/spreadsheets/d/1B7nXJwEYINS6B4DT2N8XA8FUIORRQFlVcPHMmN1emQw/edit?usp=sharing
## History
[[SkyBlock Prototype]]:
|Jul 7, 2020|0.8|Added Dungeon Score.|
Linked from: [[Adaptive Armor]], [[Adaptive Belt]], [[Adaptive Blade]], [[Apex Dragon Shard]], [[Auto Recombobulator]], [[Balloon Snake]], [[Bank (Enchantment)]], [[Bonzo]], [[Bonzo Shard]], [[Bonzo's Mask]], [[Bonzo's Staff]], [[Catacombs]], [[Changelog]], [[Changelog/2021/March 30]], [[Combo]], [[Corrupt Wither Goggles Helmet Skin]], [[Dark Claymore]], [[Dark Goggles]], [[Dark Orb]], [[Dungeon Reward Chest]], [[Dungeon Secrets]], [[Dungeons]], [[Feather Falling]], [[Fel Skull]], [[Fire Sale]], [[Fire Sale/Events]], [[Fire Sale/Events/2024]], [[Fire Sale/Search]], [[Fuming Potato Book]], [[Giant Tooth]], [[Giant's Sword]], [[Goldor the Fish]], [[Helmet Skins]], [[Helmet Skins/2024]], [[Hot Potato Book]], [[Infinite Quiver]], [[King Midas]], [[Kismet Feather]], [[Last Breath]], [[Last Stand]] (+88 more)

# Dwarven Metals
Aliases: Dwarven Metal
Categories: Confirmations needed
Dwarven Metals are a set of mineable blocks found in the [[Dwarven Mines]], [[Crystal Hollows]], [[Glacite Tunnels]] and [[Glacite Mineshafts]].
They are affected by [[Mining Fortune]], [[Dwarven Metal Fortune]] and [[Mining Spread]], which can all be upgraded via the [[Heart of the Mountain]].
## List
|Slot|Block|[[Breaking Power]]|Block Strength|Base Mining XP ([[Mining]])|Location|
|-|-|-|-|-|-|
|[[Mithril]]|[[Mithril]]|4 [[Breaking Power]]|800|45|[[Dwarven Mines]] [[Crystal Hollows]] [[Glacite Tunnels]] [[Glacite Mineshafts]]|
|[[Titanium]]|[[Titanium]]|5 [[Breaking Power]]|2,000|100|[[Dwarven Mines]] [[Glacite Tunnels]] [[Glacite Mineshafts]]|
|[[Umber]]|[[Umber]]|9 [[Breaking Power]]|5,600|75|[[Glacite Tunnels]] [[Glacite Mineshafts]]|
|[[Tungsten]]|[[Tungsten]]|9 [[Breaking Power]]|5,600|75|[[Glacite Tunnels]] [[Glacite Mineshafts]]|
|[[Glacite]]|[[Glacite]]|9 [[Breaking Power]]|6,000|80|[[Glacite Tunnels]] [[Glacite Mineshafts]]|
### Ticks Thresholds
|Mining Time (in Ticks)|[[Mining Speed]] while mining… [[Mithril]]|[[Mining Speed]] while mining… [[Titanium]]|[[Mining Speed]] while mining… [[Umber]] [[Tungsten]]|[[Mining Speed]] while mining… [[Glacite]]|
|-|-|-|-|-|
|60|248 397 744|992|2777|2976|
|50|298 476 892|1189|3327|3565|
|40|371 593 1112|1482|4149|4445|
|30|492 788 1476|1968|5509|5902|
|29|509 814 1526|2034|5695|6102|
|28|527 843 1579|2106|5895|6316|
|27|546 873 1637|2182|6110|6546|
|26|567 906 1699|2265|6340|6793|
|25|589 942 1765|2353|6589|7059|
|24|613 980 1837|2449|6858|7347|
|23|639 1022 1915|2554|7149|7660|
|22|667 1067 2001|2667|7467|8001|
|21|698 1117 2094|2791|7814|8373|
|20 (1 second)|732 1171 2196|2927|8196|8781|
|19|770 1231 2308|3077|8616|9231|
|18|811 1298 2433|3244|9082|9730|
|17|858 1372 2572|3429|9601|10286|
|16|910 1455 2728|3637|10182|10910|
|15|968 1549 2904|3871|10839|11613|
|14|1035 1656 3105|4138|11587|12414|
|13|1112 1778 3334|4445|12445|13334|
|12|1201 1921 3601|4801|13441|14401|
|11|1305 2087 3914|5218|14609|15653|
|10|1429 2286 4286|5715|16001|17143|
|9|1579 2527 4737|6316|17685|18948|
|8|1765 2824 5295|7060|19765|21177|
|7|2001 3201 6001|8001|22401|24001|
|6|2308 3693 6924|9231|25847|27693|
|5|2728 4364 8182|10910|30546|32728|
|4 (Softcap)|3334 5334 10001|13334|37334|40001|
|3|||||
|2|||||
|1 (Instamine)|30001 48001 90001|120001[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|336001[Confirm]|360001[Confirm]|
## Gallery
- An example of a Mithril vein An example of a [[Mithril]] vein
- An example of an Umber vein An example of an [[Umber]] vein
- An example of a Tungsten vein An example of a [[Tungsten]] vein
- An example of a Glacite vein An example of a [[Glacite]] vein
## History
[[Alpha Hypixel Network]]:
|Mar 21, 2024|Added Umber.|
|Mar 21, 2024|Added Tungsten.|
|Mar 21, 2024|Added Glacite.|
|Aug 20, 2024|Added Dwarven Metals.|
|Aug 20, 2024|Added [[Dwarven Metal Fortune]].|
|Aug 20, 2024|Recategorized above [[Ores]] as Dwarven Metals.|
[SkyBlock Prototype]
|Jan 15, 2021|0.11|Added Mithril.|
|Apr 9, 2024|0.20|Added Umber.|
|Apr 9, 2024|0.20|Added Tungsten.|
|Apr 9, 2024|0.20|Added Glacite.|
|Sep 17, 2024|0.20.6|Added Dwarven Metals.|
|Sep 17, 2024|0.20.6|Added [[Dwarven Metal Fortune]].|
|Sep 17, 2024|0.20.6|Recategorized above [[Ores]] as Dwarven Metals.|
Linked from: [[Andesite Whetstone]], [[Block Strength]], [[Blocks]], [[Cole]], [[Commissions]], [[Currency]], [[Dwarven (disambiguation)]], [[Dwarven Metal Fortune]], [[Dwarven Mines]], [[Fragilis]], [[Glacite Tunnels]], [[Golden Goblin]], [[Heart of the Mountain]], [[Item Types]], [[Mining Fiesta]], [[Mining Speed]], [[Mithril]], [[Mithril (disambiguation)]], [[Ores]], [[Player]], [[Raffle of the Century]], [[Refined Mineral]], [[Rock Pet]], [[Stats]], [[Suspicious Scrap]], [[Tungsten]], [[Umber]]

# Easter Eggs
Categories: Confirmations needed, Hypixel SkyBlock
An Easter Egg is a hidden message in a game. This page holds a list of Easter Eggs in [[SkyBlock]].
## The Owner of the Midas' Sword
The [[Midas' Sword]] is named after a king in Greek Mythology called Midas. Midas is the name of at least three members of the royal house of Phrygia. King Midas is popularly remembered in Greek mythology for his ability to turn everything he touched into gold. This came to be called the golden touch, also known as the Midas touch. This is also where the ability Ability: Greed came from game from, since Midas's powers led him to riches.
## Maddox's Phone Number
Upon reaching [[Wolf Slayer|Wolf Slayer IV (4)]], the player obtains a [[Maddox Batphone]]. In the past, if one previewed it and clicked on the crafting recipe, it said that the player would need 60 [[Enchanted Cobblestone]], a [[Redstone Minion|Redstone Minion VIII]], and [[Maddox's Phone Number]], the latter being an [[Glitched Items|unobtainable item]]. This has since been removed.
## Flower Pot
In the [[Birch Park]], there is a flower pot. The player can get the [[Achievements|Empty Flower Pot?]] secret achievement if the player keep clicking with an [[Flowers|Oxeye Daisy]] on it for 5 minutes.
## Fishing for Updates
If the player fishes in the end portal to the [[Private Island]] in the [[Hub Island|Hub]], it will say Sorry, no updates here :(.
## Somewhere in Hypixel
When the player is in a party and some of their friends travel to a different island, it may show as someone is traveling to "Somewhere in Hypixel."[Confirm (Confirmation needed; When this info is confirmed, remove this.)]
## Bloody Butcher Shop
There is a little bloody piggy bank on top of the auction house.[Confirm (Confirmation needed; Hub revamp; When this info is confirmed, remove this.)]
## Tal Ker
Using a [[Vacuums|vacuum]] on [[Tal Ker]] in the [[The Garden]] once you have accepted his offer will result in him making a humorous remark about not being a [[Pests|Pest]], before leaving the [[The Garden|Garden]] and providing you the rewards anyways.

# Farming
Aliases: +1 Farming Level Cap, Farming 60, Farming Cap, Farming Level, Farming Level Cap, Farming Skill, Farming Speed, Farming Xp, Farming cap, Farming level, Farming skill, Farming speed, Farming xp
Categories: Confirmations needed, More info needed, Pages with UIs, Potions, Skills, Farming
Farming is one of the [[Skills]] available for players to level up as they perform certain actions that give them Farming XP.
[[Roman Numerals]] are used to express its levels in-game.
Although Farming goes from levels 1–50 (I – L) by default, there is +50 Farming XP required to reach the first level, meaning there is a "level 0", just like all other [[Skills]].
The [[Farming|Farming Level Cap]] can be increased through [[Jacob's Farming Contest|Jacob's Farming Contests]], to a maximum of Level 60 (LX). In order to reach this cap, players must place in the GOLD bracket of a unique crop type, then purchase the upgrade from [[Anita]] in the [[Farmhouse]]. This can be done 10 times, increasing the cap one level for each unique crop type mastered.
## Mechanics
### Public Islands
Farming on Public Islands serves mostly as an introduction to the skill and the means to unlock various collections. It ranges across:
  - the [[Hub Island|Hub]] (in the [[Village]], [[Mountain]] and [[Farm]] areas);
  - the [[The Farming Islands (disambiguation)|Farming Islands]] (in [[The Barn]] and [[Mushroom Desert]], on the later of which are [[Glowing Mushroom|Glowing Mushrooms]])
  - to the [[Crimson Isle]] (featuring [[Nether Wart|Nether Warts]] as well as the unique crops of [[Mushroom Spore|Mushroom Spores]] and [[Red Thornleaf]] which require [[Spore Harvester]] and [[Thornleaf Scythe]] respectively to be collected).
More focused or thorough Farming is done better on the [[The Garden]], if the crops allow it.
Inside the [[Rift Dimension]] players can also find the unique crops of [[Riftwart Roots]], [[Agaricus Cap]], [[Caducous Stem]], [[Half-Eaten Carrot]] and [[Wilted Berberis]], which can only be harvested using the [[Wand of Farming]].
- Those crops cannot be planted on the Garden, but fortunately, comparatively fewer are required.
The [[The Farming Islands (disambiguation)|Farming Islands]] also feature mobs of the [[Animal]] type, which grant Farming XP when slain, and have their own farming collections.
- Those cannot be grinded efficiently, and as such [[Minions]] are recommended.
- For manual grinding, [[Animal Axes]] allow the player who wishes to finish their collections manually.
### Private Islands
- Before the release of [[The Garden]], players would build Farms on their own [[Private Island]], as it was significantly more efficient than Farming on Public Islands, whether it was for [[Collections|Collection]], Farming XP or [[Coins]].
- The addition of [[The Garden]] made the building of farms much easier and farming itself much more efficient.
  - Once it has been unlocked — which requires [[SkyBlock Levels|SkyBlock Level 5]] and is then accessed via [[Sam]] who appears on player's [[Private Island]] — Farming on [[The Garden]] is the only viable way to Farm, as Public islands frequently have multiple people and don't allow for custom farms; and on [[Private Island]], player's [[Farming Fortune]] is disabled.
  - Unlocking plots on it requires [[Compost]], obtained from [[Composter]] and before being able to use unlocked plots, players first need to clean them. This can be done with vanilla tools or via [[Sam's Scythe]], [[Garden Scythe]] or [[Plot Eraser]].
  - It offers presets for each of the crops, ready to paste.
    - Despite this, players have conceived and perfected their own farm designs, seeking for smaller space, accessibility and the maximum number of crops broken per second.
    - Players can build Farms using [[Tools]] such as the [[Builder's Wand]], the [[Builder's Ruler]], the [[InfiniDirt™ Wand]], the [[Magical Water Bucket]] or the [[Block Zapper]], as well as vanilla tools enchanted with [[Efficiency]].
- Crops, similarly to vanilla Minecraft, require [[Vanilla Objects/Blocks|Water]] to grow, they however don't require a light source.
  - Crops each require a different Substrate, such as Tilled Dirt for [[Wheat]] or [[Carrot|Carrots]], or [[Soul Sand]] for [[Nether Wart]].
  - Dirt can be tilled en masse via [[Hoe of Great Tilling]], [[Hoe of Greater Tilling]] and [[Hoe of Greatest Tilling]].
  - Crops can be planted manually or using [[Basket of Seeds]] and [[Nether Wart Basket|Nether Wart Pouch]]. [[Mushroom|Red]] and [[Mushroom|Brown Mushrooms]] however cannot be planted using these items and can only be done manually.
  - The [[Replenish]] enchant, obtained from [[Cocoa Beans|Cocoa Beans VIII (8)]], automatically replants crops upon every harvest.
  - The [[Delicate]] enchantment, obtained from [[Anita]], prevents the breaking of Pumpkin & Melon stems, as well as crops that are not fully grown.
#### Farming Tools
There are 12 unique Farming Tools.
- They can stored in the [[Farming Toolkit]], which is a Consumable purchased from [[The Garden|SkyMart]] for 500 [[Copper]]. Once consumed it can be accessed with:
  - /FarmingToolkit;
  - by ⇧ Shift+Right-Clicking a tool that has been donated to the Toolkit;
  - the storage menu.
- They are crop specific and grant extra [[Crop Fortune]] to their specialised [[Crops (disambiguation)|Crop]].
- They can be leveled up to increases their stats, amount of [[Gemstone Slot|Gemstone Slots]] and [[Rarity]] by:
  - gaining Farming XP while farming using the Tool;
  - applying [[Tool Exp Capsule|Tool Exp Capsules]], these level the tool up to level 40 by default. This limit can be increased to 50 using a total of 10 [[Overclocker 3000|Overclocker 3000s]].
#### Pests
By reaching Garden 5, players unlock a new unique mechanic — Pests.
- When farming on [[The Garden]], one of 13 (one for every crop) pests may spawn. The same happens once for every real-life hour of [[The Garden]] being unloaded.
- Up to 8 can be spawned at the same time, and the more of them there are, the more is player's [[Farming Fortune]] reduced.
- [[Pest Repellent|Pest Repellents]] slow their spawning, but it is recommended to instead kill them using [[Vacuums]], as each pest drops Crops as well as unique items which can help players farm. Additionally, by slaying Pests players obtain a special currency — [[Pests (Currency)|Pests]] — which can be traded with [[Pesthunter Phillip]] for Pest-related items.
This mechanic has been introduced to fight against scripting.
#### Greenhouse
The [[Greenhouse]] is a plot in [[The Garden]].
- It can be accessed at Garden 7 (Ⅶ) after accepting the [[Carpenter]] as a [[The Garden|Visitor]] and obtaining the [[Greenhouse Blueprint]].
- The size of useable [[Farmland]] inside the [[Greenhouse]] can be increased by using [[Ethereal Vine|Ethereal Vines]], which can be obtained when harvesting [[Mutations]] and [[Crops (disambiguation)|Crops]] inside the [[Greenhouse]].
- Up to 3 [[Greenhouse]] plots can be placed at once.
- Most of the [[Crops (disambiguation)|Crops]] and [[Mutations]] require water while growing in the [[Greenhouse]].
  - They can be watered with the use of a [[HydroCan™ 1000]] or its upgrades.
  - If not watered, the plant has a chance to not grow, and if it reaches 0, die.
  - The status of plants within the [[Greenhouse]] can be viewed with a [[Plant Diagnostics Tool]].
###### Mutations
- [[Mutations]] can be grown in the [[Greenhouse]] when [[Crops (disambiguation)|Crops]] and other [[Mutations]] meet specific requirements within the [[Greenhouse]].
### Stats
|Stat|Effect|Some sources|Notes|
|-|-|-|-|
[The Farming skill has many Stats which when maxed can make farming more efficient.]
|[[Bonus Pest Chance]]|Grants a percentage chance, equal to the stat value, of spawning another Pest ([[Pests]]) when Farming.; For every 100 [[Bonus Pest Chance]], players can have 1 extra Pest spawned, without losing [[Farming Fortune]].|Slug ([[Slug Pet]]) and Mosquito Pets ([[Mosquito Pet]]); [[Pesthunter Badge]] and its upgrades; [[Sprayonator]] Vermin Vaporizer Chip ([[Garden Chips]]) [[Tater Armor]] and its upgrades as well as [[Biohazard Armor]] [[Pesthunter's Set]]; [[Pesterminator]] enchantment.[[Mantid Claw]] Armor reforge.|Can be disabled with [[Pesthunter Badge]] and its upgrades.|
|[[Farming Fortune]]|Grants extra drops obtained from Farming for all vanilla[1] crops, including those dropped from [[Greenhouse]] and [[Pests]]; Increases the chance to obtain rare drops from [[Pests]]|Farming levels; Cropshot Chip ([[Garden Chips]]); Farming Tools; [[Harvesting]]; [[Tater Armor]] and its upgrades; Bee ([[Bee Pet]]), Mooshroom ([[Mooshroom Cow Pet]]), Elephant ([[Elephant Pet]]) and Rose Dragon Pets ([[Rose Dragon Pet]]); Peridot Gemstone ([[Gemstone]])|Disabled on player's [[Private Island]]|
|[[Crop Fortune]]|Grants extra drops from their respective crops, including those from [[Greenhouse]][Confirm (Confirmation needed; When this info is confirmed, remove this.)] and [[Pests]]; Increases the chance to obtain rare drops from their respective [[Pests]]|Farming Tools; [[Anita]]'s Personal Best perk; [[Carrolyn]]; Garden Crop Upgrades ([[The Garden]])|Disabled on player's [[Private Island]]|
[On top of stats that belong to the Farming stats category, certain other stats and other non-stat values also provide a benefit to players when farming.]
|[[Speed]]|Depending on one's farm design, different [[Speed]] values are optimal. Players can set a limit to their Speed via [[Rancher's Boots]] or [[Sundial]].|[[God Potion]] [[Tater Armor]] and its upgrades; Farmer ([[Farmer Boots]]) and [[Rancher's Boots]]||
|[[Strength]]|When using [[Mooshroom Cow Pet]], players receive a bonus to their [[Farming Fortune]] based on their [[Strength]].|[[God Potion]]; Forceful ([[Power Stones]]) Power; Stats Tunings ([[Maxwell]]); [[Enrichments]]||
|[[Farming Wisdom]]|Increases Farming XP gain, details below.|[[God Potion]] [[Booster Cookie]] Lunar ([[Reforging]]) reforge on equipment; Sunny ([[Reforging]]) reforge on armor; Blessed ([[Reforging]]) reforge on farming tools; [[Rabbit Pet]] Sowledge Chip ([[Garden Chips]]) [[Cultivating]] Enchantment||
|Pest Cooldown|Decreases the time between possible spawns.|[[Finnegan]]'s Pest eradicator perk; Squeaky ([[Reforging]]) reforge on [[Equipment]]; Pesthunter Equipment ([[Pesthunter's Set]])||
|Crop Growth|Increases how fast Crops grow on player's [[The Garden]]|Garden levels; DNA Analysis Milestone ([[Crop Analyzer]])||
### [[Speed]] for Farming Crops
One of the criteria optimized while Farming is the rate at which the player breaks crops or Blocks per Second or BpS. Because Minecraft Time flows at 20 ticks per second and that the player can break at most 1 block per tick, this means the upper bound for Blocks per Second is 20.
To attain this 20 BpS bound, one can adjust:
- their farm design (e.g. planting 4 rows of crops instead of 3);
- their orientation (e.g. looking up, looking down);
- their controls (e.g. pressing W and D at once, pressing D only);
- their motion (e.g. walking on [[Soul Sand]], adjust the [[Speed]] value).
With time, several [[Speed]] values have been found to be optimal depending on multiple factors. The table below provides them at a glance.
Optimal [[Speed]] values:
|Farming Style|Controls|Velocity|Block Depth 1|Block Depth 2|Block Depth 3|Block Depth 4|Block Depth 5|Block Depth 6|Use Examples|
|-|-|-|-|-|-|-|-|-|-|
|Walking sideways, perpendicularly to a wall|D or A|4.3171|464 [[Speed]]|232 [[Speed]]|155 [[Speed]]|116 [[Speed]]|93 [[Speed]]|78 [[Speed]]|[More Info Needed] (More infomation needed; When this info is added, remove this.)|
|Walking diagonally, perpendicularly to a wall|D+W or A+W or D+S or A+S|4.4052|455 [[Speed]]|228 [[Speed]]|152 [[Speed]]|114 [[Speed]]|91 [[Speed]]|76 [[Speed]]|(same as above)|
|Sprinting forward, no wall|W+Sprint|5.6123|357 [[Speed]]|179 [[Speed]]|119 [[Speed]]|90 [[Speed]]|72 [[Speed]]|60 [[Speed]]|(same as above)|
|Sprinting diagonally, no wall|D+W+Sprint or A+W+Sprint|5.7268|350 [[Speed]]|175 [[Speed]]|117 [[Speed]]|88 [[Speed]]|70 [[Speed]]|59 [[Speed]]|(same as above)|
|Walking diagonally, at a 45° angle against a wall|D or A|3.0527|656 [[Speed]]|328 [[Speed]]|219 [[Speed]]|164 [[Speed]]|132 [[Speed]]|110 [[Speed]]|(same as above)|
|Walking sideways, at a 45° angle against a wall|D+W or A+W or D+S or A+S|3.1150|643 [[Speed]]|322 [[Speed]]|215 [[Speed]]|161 [[Speed]]|129 [[Speed]]|108 [[Speed]]|(same as above)|
Notes:
- Velocity is the speed at which the player walks (different of the [[Speed]] stat), measured in Blocks per Second. It is assumed that the player is not slowed down by the blocks they're walking through.
- Block Depth is the amount of blocks the player will break before moving to the next block.
## Leveling XP
### Crops
The following table lists all the obtainable crops and Farming XP yield of each item.
|Item|XP|Minion XP|Zone|
|-|-|-|-|
|[[Wheat]]|+4|+0.3|[[Village]]; [[Farm]]; [[The Barn]]; Garden ([[The Garden]])|
|[[Potato]]|+4|+0.1|[[Farm]]; [[The Barn]]; Garden ([[The Garden]])|
|[[Carrot]]|+4|+0.1|[[Farm]]; [[The Barn]]; [[Mountain]]; Garden ([[The Garden]])|
|[[Melon]]|+4|+0.1|[[The Barn]]; Garden ([[The Garden]])|
|[[Pumpkin]]|+4.5|+0.3|[[The Barn]]; Garden ([[The Garden]])|
|[[Sugar Cane]]|+2|+0.1|[[Mushroom Desert]]; Garden ([[The Garden]])|
|[[Cactus]]|+2|+0.2|[[Mushroom Desert]]; Garden ([[The Garden]])|
|Red Mushroom ([[Mushroom]])|+6|+0.3|[[Mushroom Desert]]; Garden ([[The Garden]])|
|Brown Mushroom ([[Mushroom]])|+6|+0.3|[[Mushroom Desert]]; Garden ([[The Garden]])|
|[[Cocoa Beans]]|+4|+0.2|[[Mushroom Desert]]; [[Jungle Island]]; Garden ([[The Garden]])|
|[[Nether Wart]]|+4|+0|[[Village]]; [[Stronghold]]; Garden ([[The Garden]])|
|[[Mushroom Spore]]|+6||[[Mystic Marsh]]|
|[[Red Thornleaf]]|+0||[[Burning Desert]]|
|[[Glowing Mushroom]]|+6||[[Glowing Mushroom Cave]]|
|[[Moonflower]]|+4|0.2 [Confirm]|[[The Garden]]; Garden ([[The Garden]])|
|[[Sunflower]]|+4|0.2 [Confirm]|[[The Garden]]; Garden ([[The Garden]])|
|[[Wild Rose]]|+4|0.2 [Confirm]|[[The Garden]]; Garden ([[The Garden]])|
|[[Raw Porkchop]]|+2|+0.2|[[The Barn]]|
|[[Leather]]|+2|+0.2|[[The Barn]]|
|[[Raw Beef]]|+1|+0.1|[[The Barn]]|
|[[Raw Chicken]]|+2|+0.1|[[The Barn]]|
|[[Feather]]|+2|+0.2|[[The Barn]]|
|[[Egg]]|+2|+0.2|[[The Barn]]|
|[[Raw Rabbit]]|+2|+0.1|[[Mushroom Desert]]|
|[[Rabbit Hide]]|+2|+0.2|[[Mushroom Desert]]|
|[[Rabbit's Foot]]|+2|+0.2|[[Mushroom Desert]]|
|[[Raw Mutton]]|+2|+0.1|[[Mushroom Desert]]|
|[[Wool]]|+2|+0.1|[[Mushroom Desert]]|
IMPORTANT NOTE: Farming XP is received per crop block broken, not per item obtained. This means that [[Farming Fortune]] and [[Crop Fortune]] do not affect the rate of XP gain.
### Garden Milestones
Garden Milestones grant players a flat amount of Farming XP when reaching a new tier. For Crop Milestones, this ranges from +50,000 Farming XP and for Unique Visitors Served it ranges from +30,000 Farming XP and for Offers Accepted it ranges from +50,000 Farming XP.
This XP gain is not affected by [[Farming Wisdom]].
### Pests
All [[Pests]] grant a raw amount of +1,500 Farming XP, except for [[Field Mouse]] which grants +6,000 Farming XP.
### Visitors
- Accepting visitors on the [[The Garden|Garden]] grants Farming XP.
- Farming XP is determined with this formula: Farming XP=Base Items×Item Farming XP×Visitor Rarity Multiplier[Confirm].
  - Base Items is from the Requests formula)
  - Visitor Rarity Multiplier is determined by the Visitor's Rarity:
    - UNCOMMON: ×0.05
    - RARE: ×0.06
    - LEGENDARY: ×0.75
### Farming XP Boosts
Players can increase their farming XP gained by increasing [[Farming Wisdom]], which can be increased by:
- [[Booster Cookie]]: 25 [[Farming Wisdom]]
- Drinking [[Potions|Farming XP Boost]] potions: 5–20 [[Farming Wisdom]].
  - [[God Potion|God Potions]] include the [[Potions|Farming XP Boost III]] effect, and has significantly higher duration.
- [[Rabbit Pet]]: When at [Lv100], the [[Rarity|RARE]] Rabbit Pet grants 25 [[Farming Wisdom]] while the [[Rarity|EPIC]], [[Rarity|LEGENDARY]], and [[Rarity|MYTHIC]] variants grant 30 [[Farming Wisdom]].
- Farming Tools give 1–3 [[Farming Wisdom]]. They can also be upgraded with the [[Reforging|Blessed]] reforge and the [[Cultivating]] Enchantment. A maxed Farming tool can grant 18 [[Farming Wisdom]], which can be increased by 5% if the tool is an Axe, via the [[Essence Shops|Forest Essence Shop]].
- The [[Dragonfly Shard]]'s [[Attributes|Garden Wisdom]] attribute grants 0.5–5 [[Farming Wisdom]], which can be increased 20% with the [[Attributes|Echo of Wisdom]], which can be upgraded by 50% with [[Attributes|Echo of Echoes]] to a total of 6.5 [[Farming Wisdom]].
- The [[Fruit Bowl]] consumable can be used to gain 1 [[Farming Wisdom]].
- The [[Not Very Moldy Bread]] and [[Not Very Moldy Bread|Very Moldy Bread]] consumables can be used to gain up to [[Farming Wisdom|+30 ☯ Farming Wisdom for 60m]], consuming [[Not Very Moldy Bread|Very Moldy Bread]] grants a permanent +1 [[Farming Wisdom|☯ Farming Wisdom]]. The permanent buff can only be gained 5 times.
## Farming Levels
### Leveling Rewards
As any [[Skills|Skill]], Farming requires Experience to be leveled. Total of 3,022,425, 55,172,425 and +111,672,425 Farming XP is required to reach Farming XXV (25), Farming L (50) and Farming LX (60) respectively. Each Farming Level grants [[SkyBlock Levels|SkyBlock XP]], [[Health]], [[Coins]] and a level of Farmhand, which grants [[Farming Fortune]].
Show/Hide Farming Leveling Requirements and Rewards
|Level|XP Level|XP Total|Coins Level|Coins Total|Health Level|Health Total|Farming Fortune Level|Farming Fortune Total|SkyBlock XP Level|SkyBlock XP Total|Other|
|-|-|-|-|-|-|-|-|-|-|-|-|
|1|50|50|100 [[Coins]]|100 [[Coins]]|+2 [[Health]]|+2 [[Health]]|+4 [[Farming Fortune]]|+4 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+5 XP ([[SkyBlock Levels]])|Access to [[The Barn]]; Unlock 1 item: [[Rookie Hoe]]|
|2|125|175|250 [[Coins]]|350 [[Coins]]|+2 [[Health]]|+4 [[Health]]|+4 [[Farming Fortune]]|+8 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+10 XP ([[SkyBlock Levels]])|Unlock 1 item: [[Hoe of Great Tilling]]|
|3|200|375|500 [[Coins]]|850 [[Coins]]|+2 [[Health]]|+6 [[Health]]|+4 [[Farming Fortune]]|+12 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+15 XP ([[SkyBlock Levels]])|Unlock 4 items: [[Farmhand Armor]]|
|4|300|675|750 [[Coins]]|1.6k [[Coins]]|+2 [[Health]]|+8 [[Health]]|+4 [[Farming Fortune]]|+16 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+20 XP ([[SkyBlock Levels]])||
|5|500|1,175|1k [[Coins]]|2.6k [[Coins]]|+2 [[Health]]|+10 [[Health]]|+4 [[Farming Fortune]]|+20 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+25 XP ([[SkyBlock Levels]])|Access to [[Mushroom Desert]]; Unlock 6 items: [[Basic Gardening Hoe]], [[Hoe of Greater Tilling]], [[Cactus Armor]]|
|6|750|1,925|2k [[Coins]]|4.6k [[Coins]]|+2 [[Health]]|+12 [[Health]]|+4 [[Farming Fortune]]|+24 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+30 XP ([[SkyBlock Levels]])||
|7|1,000|2,925|3k [[Coins]]|7.6k [[Coins]]|+2 [[Health]]|+14 [[Health]]|+4 [[Farming Fortune]]|+28 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+35 XP ([[SkyBlock Levels]])|Unlock 5 items: [[Advanced Gardening Hoe]], [[Mushroom Armor]]|
|8|1,500|4,425|4k [[Coins]]|11.6k [[Coins]]|+2 [[Health]]|+16 [[Health]]|+4 [[Farming Fortune]]|+32 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+40 XP ([[SkyBlock Levels]])||
|9|2,000|6,425|5k [[Coins]]|16.6k [[Coins]]|+2 [[Health]]|+18 [[Health]]|+4 [[Farming Fortune]]|+36 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+45 XP ([[SkyBlock Levels]])||
|10|3,500|9,925|7.5k [[Coins]]|24.1k [[Coins]]|+2 [[Health]]|+20 [[Health]]|+4 [[Farming Fortune]]|+40 [[Farming Fortune]]|+5 XP ([[SkyBlock Levels]])|+50 XP ([[SkyBlock Levels]])|Unlock 21 items: Cactus Knife Mk. I ([[Cactus Knife]]), Cocoa Chopper Mk. I ([[Cocoa Chopper]]), Eclipse Sickle Mk. I ([[Eclipse Sickle]]), Euclid's Wheat Sickle Mk. I ([[Euclid's Wheat Sickle]]), Fungi Cutter Mk. I ([[Fungi Cutter]]), Gauss Carrot Shovel Mk. I ([[Gauss Carrot Shovel]]), [[Hoe of Greatest Tilling]], [[Peony Set]], Melon Dicer Mk. I ([[Melon Dicer]]), Newton Nether Wart Cutter Mk. I ([[Newton Nether Wart Cutter]]), Pumpkin Dicer Mk. I ([[Pumpkin Dicer]]), Pythagorean Potato Shovel Mk. I ([[Pythagorean Potato Shovel]]), Turing Sugar Cane Cutter Mk. I ([[Turing Sugar Cane Cutter]]), Wild Rose Cutter Mk. I ([[Wild Rose Cutter]]), [[Haymaker Armor]]|
|11|5,000|14,925|10k [[Coins]]|34.1k [[Coins]]|+2 [[Health]]|+22 [[Health]]|+4 [[Farming Fortune]]|+44 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+60 XP ([[SkyBlock Levels]])||
|12|7,500|22,425|15k [[Coins]]|49.1k [[Coins]]|+2 [[Health]]|+24 [[Health]]|+4 [[Farming Fortune]]|+48 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+70 XP ([[SkyBlock Levels]])||
|13|10,000|32,425|20k [[Coins]]|69.1k [[Coins]]|+2 [[Health]]|+26 [[Health]]|+4 [[Farming Fortune]]|+52 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+80 XP ([[SkyBlock Levels]])||
|14|15,000|47,425|25k [[Coins]]|94.1k [[Coins]]|+2 [[Health]]|+28 [[Health]]|+4 [[Farming Fortune]]|+56 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+90 XP ([[SkyBlock Levels]])||
|15|20,000|67,425|30k [[Coins]]|124.1k [[Coins]]|+3 [[Health]]|+31 [[Health]]|+4 [[Farming Fortune]]|+60 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+100 XP ([[SkyBlock Levels]])|Unlock 23 items: Cactus Knife Mk. II ([[Cactus Knife]]), [[Advanced Chicken Axe]], Cocoa Chopper Mk. II ([[Cocoa Chopper]]), [[Advanced Cow Axe]], Eclipse Sickle Mk. II ([[Eclipse Sickle]]), Euclid's Wheat Sickle Mk. II ([[Euclid's Wheat Sickle]]), Fungi Cutter Mk. II ([[Fungi Cutter]]), Gauss Carrot Shovel Mk. II ([[Gauss Carrot Shovel]]), [[Lantern Helmet]], Melon Dicer Mk. II ([[Melon Dicer]]), [[Advanced Mooshroom Axe]], Newton Nether Wart Cutter Mk. II ([[Newton Nether Wart Cutter]]), [[Advanced Pig Axe]], Pumpkin Dicer Mk. II ([[Pumpkin Dicer]]), Pythagorean Potato Shovel Mk. II ([[Pythagorean Potato Shovel]]), [[Advanced Rabbit Axe]], [[Advanced Sheep Axe]], Turing Sugar Cane Cutter Mk. II ([[Turing Sugar Cane Cutter]]), Wild Rose Cutter Mk. II ([[Wild Rose Cutter]]), [[Sprout Armor]]|
|16|30,000|97,425|40k [[Coins]]|164.1k [[Coins]]|+3 [[Health]]|+34 [[Health]]|+4 [[Farming Fortune]]|+64 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+110 XP ([[SkyBlock Levels]])||
|17|50,000|147,425|50k [[Coins]]|214.1k [[Coins]]|+3 [[Health]]|+37 [[Health]]|+4 [[Farming Fortune]]|+68 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+120 XP ([[SkyBlock Levels]])||
|18|75,000|222,425|65k [[Coins]]|279.1k [[Coins]]|+3 [[Health]]|+40 [[Health]]|+4 [[Farming Fortune]]|+72 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+130 XP ([[SkyBlock Levels]])|Unlock 1 item: [[Farmer Boots]]|
|19|100,000|322,425|80k [[Coins]]|359.1k [[Coins]]|+3 [[Health]]|+43 [[Health]]|+4 [[Farming Fortune]]|+76 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+140 XP ([[SkyBlock Levels]])||
|20|200,000|522,425|100k [[Coins]]|459.1k [[Coins]]|+4 [[Health]]|+47 [[Health]]|+4 [[Farming Fortune]]|+80 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+150 XP ([[SkyBlock Levels]])|Unlock 20 items: [[Blossom Set]], Cactus Knife Mk. III ([[Cactus Knife]]), Cocoa Chopper Mk. III ([[Cocoa Chopper]]), Eclipse Sickle Mk. III ([[Eclipse Sickle]]), Euclid's Wheat Sickle Mk. III ([[Euclid's Wheat Sickle]]), Fungi Cutter Mk. III ([[Fungi Cutter]]), Gauss Carrot Shovel Mk. III ([[Gauss Carrot Shovel]]), Melon Dicer Mk. III ([[Melon Dicer]]), Newton Nether Wart Cutter Mk. III ([[Newton Nether Wart Cutter]]), Pumpkin Dicer Mk. III ([[Pumpkin Dicer]]), Pythagorean Potato Shovel Mk. III ([[Pythagorean Potato Shovel]]), Turing Sugar Cane Cutter Mk. III ([[Turing Sugar Cane Cutter]]), Wild Rose Cutter Mk. III ([[Wild Rose Cutter]]), [[Tater Armor]]|
|21|300,000|822,425|125k [[Coins]]|584.1k [[Coins]]|+4 [[Health]]|+51 [[Health]]|+4 [[Farming Fortune]]|+84 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+160 XP ([[SkyBlock Levels]])|Unlock 1 item: [[Rancher's Boots]]|
|22|400,000|1,222,425|150k [[Coins]]|734.1k [[Coins]]|+4 [[Health]]|+55 [[Health]]|+4 [[Farming Fortune]]|+88 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+170 XP ([[SkyBlock Levels]])||
|23|500,000|1,722,425|175k [[Coins]]|909.1k [[Coins]]|+4 [[Health]]|+59 [[Health]]|+4 [[Farming Fortune]]|+92 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+180 XP ([[SkyBlock Levels]])||
|24|600,000|2,322,425|200k [[Coins]]|1.1M [[Coins]]|+4 [[Health]]|+63 [[Health]]|+4 [[Farming Fortune]]|+96 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+190 XP ([[SkyBlock Levels]])||
|25|700,000|3,022,425|225k [[Coins]]|1.3M [[Coins]]|+4 [[Health]]|+67 [[Health]]|+4 [[Farming Fortune]]|+100 [[Farming Fortune]]|+10 XP ([[SkyBlock Levels]])|+200 XP ([[SkyBlock Levels]])||
|26|800,000|3,822,425|250k [[Coins]]|1.6M [[Coins]]|+5 [[Health]]|+72 [[Health]]|+4 [[Farming Fortune]]|+104 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+220 XP ([[SkyBlock Levels]])||
|27|900,000|4,722,425|275k [[Coins]]|1.9M [[Coins]]|+5 [[Health]]|+77 [[Health]]|+4 [[Farming Fortune]]|+108 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+240 XP ([[SkyBlock Levels]])||
|28|1,000,000|5,722,425|300k [[Coins]]|2.2M [[Coins]]|+5 [[Health]]|+82 [[Health]]|+4 [[Farming Fortune]]|+112 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+260 XP ([[SkyBlock Levels]])||
|29|1,100,000|6,822,425|325k [[Coins]]|2.5M [[Coins]]|+5 [[Health]]|+87 [[Health]]|+4 [[Farming Fortune]]|+116 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+280 XP ([[SkyBlock Levels]])||
|30|1,200,000|8,022,425|350k [[Coins]]|2.8M [[Coins]]|+5 [[Health]]|+92 [[Health]]|+4 [[Farming Fortune]]|+120 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+300 XP ([[SkyBlock Levels]])|Unlock 4 items: [[Cropie Armor]]|
|31|1,300,000|9,322,425|375k [[Coins]]|3.2M [[Coins]]|+5 [[Health]]|+97 [[Health]]|+4 [[Farming Fortune]]|+124 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+320 XP ([[SkyBlock Levels]])||
|32|1,400,000|10,722,425|400k [[Coins]]|3.6M [[Coins]]|+5 [[Health]]|+102 [[Health]]|+4 [[Farming Fortune]]|+128 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+340 XP ([[SkyBlock Levels]])||
|33|1,500,000|12,222,425|425k [[Coins]]|4M [[Coins]]|+5 [[Health]]|+107 [[Health]]|+4 [[Farming Fortune]]|+132 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+360 XP ([[SkyBlock Levels]])||
|34|1,600,000|13,822,425|450k [[Coins]]|4.5M [[Coins]]|+5 [[Health]]|+112 [[Health]]|+4 [[Farming Fortune]]|+136 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+380 XP ([[SkyBlock Levels]])||
|35|1,700,000|15,522,425|475k [[Coins]]|5M [[Coins]]|+5 [[Health]]|+117 [[Health]]|+4 [[Farming Fortune]]|+140 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+400 XP ([[SkyBlock Levels]])|Unlock 4 items: [[Squash Armor]]|
|36|1,800,000|17,322,425|500k [[Coins]]|5.5M [[Coins]]|+5 [[Health]]|+122 [[Health]]|+4 [[Farming Fortune]]|+144 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+420 XP ([[SkyBlock Levels]])||
|37|1,900,000|19,222,425|550k [[Coins]]|6M [[Coins]]|+5 [[Health]]|+127 [[Health]]|+4 [[Farming Fortune]]|+148 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+440 XP ([[SkyBlock Levels]])||
|38|2,000,000|21,222,425|600k [[Coins]]|6.6M [[Coins]]|+5 [[Health]]|+132 [[Health]]|+4 [[Farming Fortune]]|+152 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+460 XP ([[SkyBlock Levels]])||
|39|2,100,000|23,322,425|650k [[Coins]]|7.3M [[Coins]]|+5 [[Health]]|+137 [[Health]]|+4 [[Farming Fortune]]|+156 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+480 XP ([[SkyBlock Levels]])||
|40|2,200,000|25,522,425|700k [[Coins]]|8M [[Coins]]|+5 [[Health]]|+142 [[Health]]|+4 [[Farming Fortune]]|+160 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+500 XP ([[SkyBlock Levels]])|Unlock 4 items: [[Fermento Armor]]|
|41|2,300,000|27,822,425|750k [[Coins]]|8.7M [[Coins]]|+5 [[Health]]|+147 [[Health]]|+4 [[Farming Fortune]]|+164 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+520 XP ([[SkyBlock Levels]])||
|42|2,400,000|30,222,425|800k [[Coins]]|9.5M [[Coins]]|+5 [[Health]]|+152 [[Health]]|+4 [[Farming Fortune]]|+168 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+540 XP ([[SkyBlock Levels]])||
|43|2,500,000|32,722,425|850k [[Coins]]|10.4M [[Coins]]|+5 [[Health]]|+157 [[Health]]|+4 [[Farming Fortune]]|+172 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+560 XP ([[SkyBlock Levels]])||
|44|2,600,000|35,322,425|900k [[Coins]]|11.3M [[Coins]]|+5 [[Health]]|+162 [[Health]]|+4 [[Farming Fortune]]|+176 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+580 XP ([[SkyBlock Levels]])||
|45|2,750,000|38,072,425|1M [[Coins]]|12.3M [[Coins]]|+5 [[Health]]|+167 [[Health]]|+4 [[Farming Fortune]]|+180 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+600 XP ([[SkyBlock Levels]])||
|46|2,900,000|40,972,425|1M [[Coins]]|13.3M [[Coins]]|+5 [[Health]]|+172 [[Health]]|+4 [[Farming Fortune]]|+184 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+620 XP ([[SkyBlock Levels]])||
|47|3,100,000|44,072,425|1M [[Coins]]|14.3M [[Coins]]|+5 [[Health]]|+177 [[Health]]|+4 [[Farming Fortune]]|+188 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+640 XP ([[SkyBlock Levels]])||
|48|3,400,000|47,472,425|1M [[Coins]]|15.3M [[Coins]]|+5 [[Health]]|+182 [[Health]]|+4 [[Farming Fortune]]|+192 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+660 XP ([[SkyBlock Levels]])||
|49|3,700,000|51,172,425|1M [[Coins]]|16.3M [[Coins]]|+5 [[Health]]|+187 [[Health]]|+4 [[Farming Fortune]]|+196 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+680 XP ([[SkyBlock Levels]])||
|50|4,000,000|55,172,425|1M [[Coins]]|17.3M [[Coins]]|+5 [[Health]]|+192 [[Health]]|+4 [[Farming Fortune]]|+200 [[Farming Fortune]]|+20 XP ([[SkyBlock Levels]])|+700 XP ([[SkyBlock Levels]])|Unlock 4 items: [[Helianthus Armor]]|
|51|4,300,000|59,472,425|1M [[Coins]]|18.3M [[Coins]]|+5 [[Health]]|+197 [[Health]]|+4 [[Farming Fortune]]|+204 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+730 XP ([[SkyBlock Levels]])||
|52|4,600,000|64,072,425|1M [[Coins]]|19.3M [[Coins]]|+5 [[Health]]|+202 [[Health]]|+4 [[Farming Fortune]]|+208 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+760 XP ([[SkyBlock Levels]])||
|53|4,900,000|68,972,425|1M [[Coins]]|20.3M [[Coins]]|+5 [[Health]]|+207 [[Health]]|+4 [[Farming Fortune]]|+212 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+790 XP ([[SkyBlock Levels]])||
|54|5,200,000|74,172,425|1M [[Coins]]|21.3M [[Coins]]|+5 [[Health]]|+212 [[Health]]|+4 [[Farming Fortune]]|+216 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+820 XP ([[SkyBlock Levels]])||
|55|5,500,000|79,672,425|1M [[Coins]]|22.3M [[Coins]]|+5 [[Health]]|+217 [[Health]]|+4 [[Farming Fortune]]|+220 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+850 XP ([[SkyBlock Levels]])||
|56|5,800,000|85,472,425|1M [[Coins]]|23.3M [[Coins]]|+5 [[Health]]|+222 [[Health]]|+4 [[Farming Fortune]]|+224 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+880 XP ([[SkyBlock Levels]])||
|57|6,100,000|91,572,425|1M [[Coins]]|24.3M [[Coins]]|+5 [[Health]]|+227 [[Health]]|+4 [[Farming Fortune]]|+228 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+910 XP ([[SkyBlock Levels]])||
|58|6,400,000|97,972,425|1M [[Coins]]|25.3M [[Coins]]|+5 [[Health]]|+232 [[Health]]|+4 [[Farming Fortune]]|+232 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+940 XP ([[SkyBlock Levels]])||
|59|6,700,000|104,672,425|1M [[Coins]]|26.3M [[Coins]]|+5 [[Health]]|+237 [[Health]]|+4 [[Farming Fortune]]|+236 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+970 XP ([[SkyBlock Levels]])||
|60|7,000,000|111,672,425|1M [[Coins]]|27.3M [[Coins]]|+5 [[Health]]|+242 [[Health]]|+4 [[Farming Fortune]]|+240 [[Farming Fortune]]|+30 XP ([[SkyBlock Levels]])|+1000 XP ([[SkyBlock Levels]])||
### Increasing Level Cap
Increasing the player's Farming Level Cap requires mastery in a unique crop type. Mastery comes in the form of [[Jacob's Farming Contest|Jacob's Farming Contests]], earning a [[Medals|Gold Medal]] in up to 10 unique Crops is required for purchasing additional Farming levels from [[Anita]].
The cost of increasing the player's Farming Level Cap increases for each level.
|Farming Skill Cap|Requirement|Cost|Cumulative|
|-|-|-|-|
|Farming LI (51)|Win GOLD in 1 collection!|1 Gold Medal ([[Medals]])|1 Gold Medal ([[Medals]])|
|Farming LII (52)|Win GOLD in 2 collections!|1 Gold Medal ([[Medals]]) 50x [[Jacob's Ticket]]|2 Gold Medals ([[Medals]]) 50x [[Jacob's Ticket]]|
|Farming LIII (53)|Win GOLD in 3 collections!|1 Gold Medal ([[Medals]]) 50x [[Jacob's Ticket]]|3 Gold Medals ([[Medals]]) 100x (1 stack plus 36 (100 in total)) [[Jacob's Ticket]]|
|Farming LIV (54)|Win GOLD in 4 collections!|1 Gold Medal ([[Medals]]) 100x [[Jacob's Ticket]]|4 Gold Medals ([[Medals]]) 200x (3 stacks plus 8 (200 in total)) [[Jacob's Ticket]]|
|Farming LV (55)|Win GOLD in 5 collections!|1 Gold Medal ([[Medals]]) 100x [[Jacob's Ticket]]|5 Gold Medals ([[Medals]]) 300x (4 stacks plus 44 (300 in total)) [[Jacob's Ticket]]|
|Farming LVI (56)|Win GOLD in 6 collections!|2 Gold Medals ([[Medals]]) 150x (2 stacks plus 22 (150 in total)) [[Jacob's Ticket]]|7 Gold Medals ([[Medals]]) 450x (7 stacks plus 2 (450 in total)) [[Jacob's Ticket]]|
|Farming LVII (57)|Win GOLD in 7 collections!|2 Gold Medals ([[Medals]]) 150x [[Jacob's Ticket]]|9 Gold Medals ([[Medals]]) 600x (9 stacks plus 24 (600 in total)) [[Jacob's Ticket]]|
|Farming LVIII (58)|Win GOLD in 8 collections!|2 Gold Medals ([[Medals]]) 200x [[Jacob's Ticket]]|11 Gold Medals ([[Medals]]) 800x (12 stacks plus 32 (800 in total)) [[Jacob's Ticket]]|
|Farming LIX (59)|Win GOLD in 9 collections!|2 Gold Medals ([[Medals]]) 250x (3 stacks plus 58 (250 in total)) [[Jacob's Ticket]]|13 Gold Medals ([[Medals]]) 1,050x (16 stacks plus 26 (1,050 in total)) [[Jacob's Ticket]]|
|Farming LX (60)|Win GOLD in 10 collections!|3 Gold Medals ([[Medals]]) 500x (7 stacks plus 52 (500 in total)) [[Jacob's Ticket]]|16 Gold Medals ([[Medals]]) 1,550x (24 stacks plus 14 (1,550 in total)) [[Jacob's Ticket]]|
### Item Abilities
Abilities of some items gain a bonus depending on player's Farming level
- [[Farmer Boots]] gain 2 [[Defense]] and 4 [[Speed]]. Additionally, it gains 1 [[Farming Fortune]] per Farming level while on [[The Garden]].
- [[Rancher's Boots]] gain 2 [[Defense]] and 4 [[Speed]]. Additionally, it gains 1 [[Farming Fortune]] per Farming level while on [[The Garden]].
- [[Lantern Helmet]] gains 2 [[Defense]] and 4 [[Health]]. Additionally, it gains 1 [[Farming Fortune]] per Farming level while holding an axe.
- [[Rose Dragon Pet]] grants the player 3 [[Farming Fortune]] per Farming level.
## Notes
[1] All custom Crops, except [[Mushroom Spore|Mushroom Spores]] are not affected. [2] If the players have the now-unobtainable sale, gained from Contributing to the [[City Projects/Farm Merchant's Dwelling|Farm Merchant's Dwelling]] City Project, this cost is reduced by either 5% or 10%.
## History
[[SkyBlock Prototype]]:
|Jun 11, 2019|0.1|Added Farming Skill.|
|Nov 6, 2020|0.9.11|Added [[Farmhouse]] Building in the Hub and many new Farming tools.|
|Nov 6, 2020|0.9.11|Added [[Jacob's Farming Contest]].|
|Nov 6, 2020|0.9.11|Farming Skill can now go up to level 60.|
Linked from: [[Achievements]], [[Advanced Chicken Axe]], [[Advanced Cow Axe]], [[Advanced Gardening Axe]], [[Advanced Gardening Hoe]], [[Advanced Mooshroom Axe]], [[Advanced Pig Axe]], [[Advanced Rabbit Axe]], [[Advanced Sheep Axe]], [[Agronomy Sack]], [[All-in Aloe]], [[Animal]], [[Animal Axes]], [[Anita]], [[Ant]], [[Ant's Cave]], [[Archaeological Site]], [[Armor]], [[Armor & Equipment]], [[Armor/Boots]], [[Armor/Helmets]], [[Ashwreath]], [[Attributes]], [[Attributes/List/Farming]], [[Basic Gardening Axe]], [[Basic Gardening Hoe]], [[Bazaar]], [[Bee Pet]], [[Beetle]], [[Belts]], [[Bingo]], [[Bingo/Tasks]], [[Blastberry]], [[Blossom Belt]], [[Blossom Bracelet]], [[Blossom Cloak]], [[Blossom Necklace]], [[Boots]], [[Bracelets]], [[Breakable Blocks]] (+313 more)

# Frozen Corpses
Aliases: Corpse, Corpses, Frozen Corpse, Lapis Corpse, Tungsten Corpse, Umber Corpse, Vanguard, Vanguard Corpse
Categories: Confirmations needed, Pages with UIs, Dwarven Mines
[Frozen Corpses]
Frozen Corpses are special entities found inside [[Glacite Mineshafts]] that can be interacted with to grant loot. They can be found in numerous positions, such as laying down, buried in ice, or buried in rock.
## Spawning
Frozen Corpses can spawn in any [[Glacite Mineshafts|Glacite Mineshaft]]. Depending on the size, 1-3 corpses will spawn: an additional Frozen Corpse can spawn in with [[Heart of the Mountain|Dead Man's Chest]] (+0.5-25%) and [[Grandpa Wolf|Frozen Corpse Milestones II (2)]]-[[Grandpa Wolf|Frozen Corpse Milestones V (5)]] (+10-20%), raising the maximum number of Frozen Corpses in a Glacite Mineshaft up to 4.
## Types of Corpses
There are 4 different kinds of Frozen Corpses that can generate in any given [[Glacite Mineshafts|Mineshaft]]. All Frozen Corpses need to be unlocked with certain Keys except for Lapis Corpses, which can be unlocked for free.
|Type|Key|Spawn Chance|Base Loot|
|-|-|-|-|
|Lapis||50%|500 ᠅ [[Glacite Powder]][Confirm (Confirmation needed; When this info is confirmed, remove this.)] +100 HotM EXP ([[Heart of the Mountain]])|
|Umber|[[Umber Key]]|25%|5,000 ᠅ [[Glacite Powder]][Confirm] +1,000 HotM EXP ([[Heart of the Mountain]])|
|Tungsten|[[Tungsten Key]]|25%|5,000 ᠅ [[Glacite Powder]][Confirm] +1,000 HotM EXP ([[Heart of the Mountain]])|
|Vanguard|[[Skeleton Key]]|100% (while in the Fairy mineshaft)|25,000 ᠅ [[Glacite Powder]][Confirm] +5,000 HotM EXP ([[Heart of the Mountain]])|
If the [[Researcher Beryl|Resourceful]] perk activates, the following dialogue displays:
LUCKY! Your Resourceful perk saved your key from being consumed!
### Lapis Corpses
Lapis Frozen Corpses do not require a key to obtain loot from them.
Upon looting a Lapis Frozen Corpse 3-6 (uniform distribution with an average of 4.5 Rolls) of the below drops will be selected. With [[Heart of the Mountain]] perk Gifts from the Departed at level 100 + [[Drills|Drill]] with [[Blue Cheese Goblin Omelette]] and level 6 [[Grandpa Wolf|Corpse Milestone]], there is a 40.2% chance to gain an additional drop (bringing the average to 4.902).
There is also a 0.0004% (1 in 250,000) chance for each roll to be a [[Frostbitten Dye]] instead, which can be boosted by [[Vincent]] to be 2x or 3x higher.
Lapis Corpse Loot Table:
|Item|Weight|Chance Per Roll|Probability Per Corpse Base (4.5 rolls)|Probability Per Corpse Max (4.902 rolls)|
|-|-|-|-|-|
|20 Flawed Onyx Gemstone ([[Gemstone]])|1000|5.97% (1 in 16.75 rolls)|24.2% (1 in 4.13 corpses)|26.05% (1 in 3.84 corpses)|
|40 Flawed Onyx Gemstone ([[Gemstone]])|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|1 Fine Onyx Gemstone ([[Gemstone]])|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|2 Fine Onyx Gemstone ([[Gemstone]])|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|20 Flawed Peridot Gemstone ([[Gemstone]])|1000|5.97% (1 in 16.75 rolls)|24.2% (1 in 4.13 corpses)|26.05% (1 in 3.84 corpses)|
|40 Flawed Peridot Gemstone ([[Gemstone]])|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|1 Fine Peridot Gemstone ([[Gemstone]])|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|2 Fine Peridot Gemstone ([[Gemstone]])|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|20 Flawed Citrine Gemstone ([[Gemstone]])|1000|5.97% (1 in 16.75 rolls)|24.2% (1 in 4.13 corpses)|26.05% (1 in 3.84 corpses)|
|40 Flawed Citrine Gemstone ([[Gemstone]])|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|1 Fine Citrine Gemstone ([[Gemstone]])|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|2 Fine Citrine Gemstone ([[Gemstone]])|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|20 Flawed Aquamarine Gemstone ([[Gemstone]])|1000|5.97% (1 in 16.75 rolls)|24.2% (1 in 4.13 corpses)|26.05% (1 in 3.84 corpses)|
|40 Flawed Aquamarine Gemstone ([[Gemstone]])|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|1 Fine Aquamarine Gemstone ([[Gemstone]])|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|2 Fine Aquamarine Gemstone ([[Gemstone]])|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|1 [[Suspicious Scrap]]|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|1 [[Goblin Egg]]|800|4.78% (1 in 20.94 rolls)|19.77% (1 in 5.06 corpses)|21.33% (1 in 4.69 corpses)|
|2 [[Goblin Egg]]|400|2.39% (1 in 41.88 rolls)|10.31% (1 in 9.7 corpses)|11.17% (1 in 8.95 corpses)|
|4 [[Goblin Egg]]|200|1.19% (1 in 83.75 rolls)|5.26% (1 in 19.0 corpses)|5.72% (1 in 17.49 corpses)|
|1 [[Green Goblin Egg]]|700|4.18% (1 in 23.93 rolls)|17.48% (1 in 5.72 corpses)|18.88% (1 in 5.3 corpses)|
|2 [[Green Goblin Egg]]|350|2.09% (1 in 47.86 rolls)|9.07% (1 in 11.03 corpses)|9.83% (1 in 10.17 corpses)|
|4 [[Green Goblin Egg]]|175|1.04% (1 in 95.71 rolls)|4.62% (1 in 21.66 corpses)|5.02% (1 in 19.93 corpses)|
|1 [[Yellow Goblin Egg]]|700|4.18% (1 in 23.93 rolls)|17.48% (1 in 5.72 corpses)|18.88% (1 in 5.3 corpses)|
|2 [[Yellow Goblin Egg]]|350|2.09% (1 in 47.86 rolls)|9.07% (1 in 11.03 corpses)|9.83% (1 in 10.17 corpses)|
|4 [[Yellow Goblin Egg]]|175|1.04% (1 in 95.71 rolls)|4.62% (1 in 21.66 corpses)|5.02% (1 in 19.93 corpses)|
|1 [[Red Goblin Egg]]|700|4.18% (1 in 23.93 rolls)|17.48% (1 in 5.72 corpses)|18.88% (1 in 5.3 corpses)|
|2 [[Red Goblin Egg]]|350|2.09% (1 in 47.86 rolls)|9.07% (1 in 11.03 corpses)|9.83% (1 in 10.17 corpses)|
|4 [[Red Goblin Egg]]|175|1.04% (1 in 95.71 rolls)|4.62% (1 in 21.66 corpses)|5.02% (1 in 19.93 corpses)|
|1 [[Enchanted Umber]]|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|2 [[Enchanted Umber]]|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|4 [[Enchanted Umber]]|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|1 [[Enchanted Tungsten]]|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|2 [[Enchanted Tungsten]]|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|4 [[Enchanted Tungsten]]|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|1 [[Enchanted Glacite]]|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|2 [[Enchanted Glacite]]|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|4 [[Enchanted Glacite]]|125|0.75% (1 in 134.0 rolls)|3.31% (1 in 30.17 corpses)|3.61% (1 in 27.74 corpses)|
|1 [[Refined Umber]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
|1 [[Refined Tungsten]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
|1 [[Glacite Amalgamation]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
|1 [[Umber Key]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
|1 [[Tungsten Key]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
|1 [[Glacite Jewel]]|500|2.99% (1 in 33.5 rolls)|12.75% (1 in 7.84 corpses)|13.8% (1 in 7.24 corpses)|
|2 [[Glacite Jewel]]|250|1.49% (1 in 67.0 rolls)|6.54% (1 in 15.28 corpses)|7.11% (1 in 14.07 corpses)|
|1 [[Bejeweled Handle]]|100|0.6% (1 in 167.5 rolls)|2.66% (1 in 37.61 corpses)|2.89% (1 in 34.57 corpses)|
|2 [[Bejeweled Handle]]|50|0.3% (1 in 335.0 rolls)|1.34% (1 in 74.83 corpses)|1.45% (1 in 68.74 corpses)|
|4 [[Bejeweled Handle]]|25|0.15% (1 in 670.0 rolls)|0.67% (1 in 149.28 corpses)|0.73% (1 in 137.08 corpses)|
### Umber/Tungsten Corpses
Umber and Tungsten Frozen Corpses share the same loot table. The only functional difference between the two is which key is required to loot them. Umber Frozen Corpses require the use of an [[Umber Key]] to obtain loot from them. Tungsten Frozen Corpses require the use of a [[Tungsten Key]] to obtain loot from them.
Upon looting a Umber or Tungsten Frozen Corpse 4-7 (uniform distribution with an average of 5.5 Rolls) of the below drops will be selected. With [[Heart of the Mountain]] perk Gifts from the Departed at level 100 + [[Drills|Drill]] with [[Blue Cheese Goblin Omelette]] and level 6 [[Grandpa Wolf|Corpse Milestone]], there is a 40.2% chance to gain an additional drop (bringing the average to 5.902).
There is also a 0.001% (1 in 100,000) chance for each roll to be a [[Frostbitten Dye]] instead, which can be boosted by [[Vincent]] to be 2x or 3x higher.
Umber/Tungsten Corpses Loot Table:
|Item|Weight|Chance Per Roll|Probability Per Corpse Base (5.5 rolls)|Probability Per Corpse Max (5.902 rolls)|
|-|-|-|-|-|
|4 Fine Onyx Gemstone ([[Gemstone]])|700|10.7% (1 in 9.34 rolls)|46.35% (1 in 2.16 corpses)|48.73% (1 in 2.05 corpses)|
|8 Fine Onyx Gemstone ([[Gemstone]])|350|5.35% (1 in 18.69 rolls)|26.1% (1 in 3.83 corpses)|27.72% (1 in 3.61 corpses)|
|16 Fine Onyx Gemstone ([[Gemstone]])|175|2.68% (1 in 37.37 rolls)|13.86% (1 in 7.22 corpses)|14.79% (1 in 6.76 corpses)|
|1 Flawless Onyx Gemstone ([[Gemstone]])|25|0.38% (1 in 261.6 rolls)|2.08% (1 in 47.97 corpses)|2.24% (1 in 44.74 corpses)|
|4 Fine Peridot Gemstone ([[Gemstone]])|700|10.7% (1 in 9.34 rolls)|46.35% (1 in 2.16 corpses)|48.73% (1 in 2.05 corpses)|
|8 Fine Peridot Gemstone ([[Gemstone]])|350|5.35% (1 in 18.69 rolls)|26.1% (1 in 3.83 corpses)|27.72% (1 in 3.61 corpses)|
|16 Fine Peridot Gemstone ([[Gemstone]])|175|2.68% (1 in 37.37 rolls)|13.86% (1 in 7.22 corpses)|14.79% (1 in 6.76 corpses)|
|1 Flawless Peridot Gemstone ([[Gemstone]])|25|0.38% (1 in 261.6 rolls)|2.08% (1 in 47.97 corpses)|2.24% (1 in 44.74 corpses)|
|4 Fine Citrine Gemstone ([[Gemstone]])|700|10.7% (1 in 9.34 rolls)|46.35% (1 in 2.16 corpses)|48.73% (1 in 2.05 corpses)|
|8 Fine Citrine Gemstone ([[Gemstone]])|350|5.35% (1 in 18.69 rolls)|26.1% (1 in 3.83 corpses)|27.72% (1 in 3.61 corpses)|
|16 Fine Citrine Gemstone ([[Gemstone]])|175|2.68% (1 in 37.37 rolls)|13.86% (1 in 7.22 corpses)|14.79% (1 in 6.76 corpses)|
|1 Flawless Citrine Gemstone ([[Gemstone]])|25|0.38% (1 in 261.6 rolls)|2.08% (1 in 47.97 corpses)|2.24% (1 in 44.74 corpses)|
|4 Fine Aquamarine Gemstone ([[Gemstone]])|700|10.7% (1 in 9.34 rolls)|46.35% (1 in 2.16 corpses)|48.73% (1 in 2.05 corpses)|
|8 Fine Aquamarine Gemstone ([[Gemstone]])|350|5.35% (1 in 18.69 rolls)|26.1% (1 in 3.83 corpses)|27.72% (1 in 3.61 corpses)|
|16 Fine Aquamarine Gemstone ([[Gemstone]])|175|2.68% (1 in 37.37 rolls)|13.86% (1 in 7.22 corpses)|14.79% (1 in 6.76 corpses)|
|1 Flawless Aquamarine Gemstone ([[Gemstone]])|25|0.38% (1 in 261.6 rolls)|2.08% (1 in 47.97 corpses)|2.24% (1 in 44.74 corpses)|
|2 [[Suspicious Scrap]]|700|10.7% (1 in 9.34 rolls)|46.35% (1 in 2.16 corpses)|48.73% (1 in 2.05 corpses)|
|4 [[Suspicious Scrap]]|350|5.35% (1 in 18.69 rolls)|26.1% (1 in 3.83 corpses)|27.72% (1 in 3.61 corpses)|
|1 [[Enchanted Book]] (Ice Cold I ([[Ice Cold]]))|80|1.22% (1 in 81.75 rolls)|6.55% (1 in 15.28 corpses)|7.01% (1 in 14.27 corpses)|
|1 [[Blue Goblin Egg]]|80|1.22% (1 in 81.75 rolls)|6.55% (1 in 15.28 corpses)|7.01% (1 in 14.27 corpses)|
|1 [[Refined Umber]]|20|0.31% (1 in 327.0 rolls)|1.67% (1 in 59.86 corpses)|1.79% (1 in 55.82 corpses)|
|1 [[Refined Tungsten]]|20|0.31% (1 in 327.0 rolls)|1.67% (1 in 59.86 corpses)|1.79% (1 in 55.82 corpses)|
|1 [[Glacite Amalgamation]]|20|0.31% (1 in 327.0 rolls)|1.67% (1 in 59.86 corpses)|1.79% (1 in 55.82 corpses)|
|1 [[Umber Plate]]|5|0.08% (1 in 1308.0 rolls)|0.42% (1 in 238.23 corpses)|0.45% (1 in 222.04 corpses)|
|1 [[Tungsten Plate]]|5|0.08% (1 in 1308.0 rolls)|0.42% (1 in 238.23 corpses)|0.45% (1 in 222.04 corpses)|
|1 [[Umber Key]]|10|0.15% (1 in 654.0 rolls)|0.84% (1 in 119.32 corpses)|0.9% (1 in 111.23 corpses)|
|1 [[Tungsten Key]]|10|0.15% (1 in 654.0 rolls)|0.84% (1 in 119.32 corpses)|0.9% (1 in 111.23 corpses)|
|1 [[Mithril Plate]]|10|0.15% (1 in 654.0 rolls)|0.84% (1 in 119.32 corpses)|0.9% (1 in 111.23 corpses)|
|1 [[Frozen Scute]]|4|0.06% (1 in 1635.0 rolls)|0.34% (1 in 297.68 corpses)|0.36% (1 in 277.44 corpses)|
|1 [[Dwarven O's Metallic Minis]]|20|0.31% (1 in 327.0 rolls)|1.67% (1 in 59.86 corpses)|1.79% (1 in 55.82 corpses)|
|1 [[Skeleton Key]]|4|0.06% (1 in 1635.0 rolls)|0.34% (1 in 297.68 corpses)|0.36% (1 in 277.44 corpses)|
|1 [[Caged Wisp]]|2|0.03% (1 in 3270.0 rolls)|0.17% (1 in 594.95 corpses)|0.18% (1 in 554.46 corpses)|
|1 Opal Crystal ([[Gemstone Crystals]])|40|0.61% (1 in 163.5 rolls)|3.32% (1 in 30.14 corpses)|3.56% (1 in 28.12 corpses)|
|1 Onyx Crystal ([[Gemstone Crystals]])|40|0.61% (1 in 163.5 rolls)|3.32% (1 in 30.14 corpses)|3.56% (1 in 28.12 corpses)|
|1 Peridot Crystal ([[Gemstone Crystals]])|40|0.61% (1 in 163.5 rolls)|3.32% (1 in 30.14 corpses)|3.56% (1 in 28.12 corpses)|
|1 Citrine Crystal ([[Gemstone Crystals]])|40|0.61% (1 in 163.5 rolls)|3.32% (1 in 30.14 corpses)|3.56% (1 in 28.12 corpses)|
|1 Aquamarine Crystal ([[Gemstone Crystals]])|40|0.61% (1 in 163.5 rolls)|3.32% (1 in 30.14 corpses)|3.56% (1 in 28.12 corpses)|
### Vanguard Corpses
Vanguard Frozen Corpses require the use of a [[Skeleton Key]] to obtain loot from them and only appear in the Fairy Mineshaft variation of the [[Glacite Mineshafts]].
Upon looting a Vanguard Frozen Corpse 5-8 (uniform distribution with an average of 6.5 Rolls) of the below drops will be selected. With [[Heart of the Mountain]] perk Gifts from the Departed at level 100 + [[Drills|Drill]] with [[Blue Cheese Goblin Omelette]] and level 6 [[Grandpa Wolf|Corpse Milestone]], there is a 40.2% chance to gain an additional drop (bringing the average to 6.902).
There is also a 0.01% (1 in 10,000) chance for each roll to be a [[Frostbitten Dye]] instead, which can be boosted by [[Vincent]] to be 2x or 3x higher.
Vanguard Corpses Loot Table:
|Item|Weight|Chance Per Roll|Probability Per Corpse Base (6.5 rolls)|Probability Per Corpse Max (6.902 rolls)|
|-|-|-|-|-|
|1 Flawless Onyx Gemstone ([[Gemstone]])|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 Flawless Onyx Gemstone ([[Gemstone]])|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 Flawless Citrine Gemstone ([[Gemstone]])|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 Flawless Citrine Gemstone ([[Gemstone]])|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 Flawless Peridot Gemstone ([[Gemstone]])|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 Flawless Peridot Gemstone ([[Gemstone]])|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 Flawless Aquamarine Gemstone ([[Gemstone]])|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 Flawless Aquamarine Gemstone ([[Gemstone]])|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 [[Dwarven O's Metallic Minis]]|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
|8 [[Suspicious Scrap]]|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|16 [[Suspicious Scrap]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 [[Enchanted Book]] (Ice Cold I ([[Ice Cold]]))|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|1 [[Blue Goblin Egg]]|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 [[Blue Goblin Egg]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 [[Refined Umber]]|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 [[Refined Umber]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 [[Refined Tungsten]]|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 [[Refined Tungsten]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|1 [[Glacite Amalgamation]]|160|4.55% (1 in 21.97 rolls)|26.13% (1 in 3.83 corpses)|27.5% (1 in 3.64 corpses)|
|2 [[Glacite Amalgamation]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|4 [[Glacite Amalgamation]]|40|1.14% (1 in 87.88 rolls)|7.17% (1 in 13.95 corpses)|7.6% (1 in 13.17 corpses)|
|1 [[Mithril Plate]]|60|1.71% (1 in 58.58 rolls)|10.59% (1 in 9.45 corpses)|11.2% (1 in 8.93 corpses)|
|1 [[Umber Plate]]|30|0.85% (1 in 117.17 rolls)|5.42% (1 in 18.45 corpses)|5.74% (1 in 17.41 corpses)|
|1 [[Tungsten Plate]]|30|0.85% (1 in 117.17 rolls)|5.42% (1 in 18.45 corpses)|5.74% (1 in 17.41 corpses)|
|1 [[Umber Key]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|2 [[Umber Key]]|40|1.14% (1 in 87.88 rolls)|7.17% (1 in 13.95 corpses)|7.6% (1 in 13.17 corpses)|
|4 [[Umber Key]]|20|0.57% (1 in 175.75 rolls)|3.64% (1 in 27.46 corpses)|3.86% (1 in 25.89 corpses)|
|1 [[Tungsten Key]]|80|2.28% (1 in 43.94 rolls)|13.9% (1 in 7.19 corpses)|14.69% (1 in 6.81 corpses)|
|2 [[Tungsten Key]]|40|1.14% (1 in 87.88 rolls)|7.17% (1 in 13.95 corpses)|7.6% (1 in 13.17 corpses)|
|4 [[Tungsten Key]]|20|0.57% (1 in 175.75 rolls)|3.64% (1 in 27.46 corpses)|3.86% (1 in 25.89 corpses)|
|1 [[Skeleton Key]]|10|0.28% (1 in 351.5 rolls)|1.83% (1 in 54.5 corpses)|1.95% (1 in 51.36 corpses)|
|1 [[Frozen Scute]]|10|0.28% (1 in 351.5 rolls)|1.83% (1 in 54.5 corpses)|1.95% (1 in 51.36 corpses)|
|1 [[Caged Wisp]]|10|0.28% (1 in 351.5 rolls)|1.83% (1 in 54.5 corpses)|1.95% (1 in 51.36 corpses)|
|1 [[Shattered Locket]]|5|0.14% (1 in 703.0 rolls)|0.92% (1 in 108.58 corpses)|0.98% (1 in 102.28 corpses)|
|1 Opal Crystal ([[Gemstone Crystals]])|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
|1 Onyx Crystal ([[Gemstone Crystals]])|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
|1 Peridot Crystal ([[Gemstone Crystals]])|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
|1 Citrine Crystal ([[Gemstone Crystals]])|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
|1 Aquamarine Crystal ([[Gemstone Crystals]])|120|3.41% (1 in 29.29 rolls)|20.21% (1 in 4.95 corpses)|21.32% (1 in 4.69 corpses)|
Opening a Vanguard Corpse with maxed amount of rolls results in -5,104,953.2331128 [[Coins]] average profit/loss.
This calculator is not accounting for the fraction of the price of the [[Frostbitten Dye]], RNG Meter and refund from the [[Researcher Beryl|Resourceful Fossil Essence Perk]].
## Frozen Corpse Milestones
Frozen Corpse Milestones are milestones that reward you for reaching specific amounts of frozen corpses opened, unlocked after talking to [[Grandpa Wolf]].
|Milestone|Corpses Required Lapis|Corpses Required Umber|Corpses Required Tungsten|Corpses Required Vanguard|Rewards|
|-|-|-|-|-|-|
|1|10||||[[Organ Donor Talisman]]; +10,000 ᠅ [[Glacite Powder]]; +1,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +5 SkyBlock XP ([[SkyBlock Levels]])|
|2|25|1|1||Gain a +10% chance to spawn +1 Frozen Corpse when entering [[Glacite Mineshafts]] you summoned.; +25,000 ᠅ [[Glacite Powder]]; +2,500 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +10 SkyBlock XP ([[SkyBlock Levels]])|
|3|50|5|5||Gain a +10% chance to get +1 item when looting a Frozen Corpse.; +50,000 ᠅ [[Glacite Powder]]; +5,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +15 SkyBlock XP ([[SkyBlock Levels]])|
|4|100|10|10|1|[[Organ Donor Ring]] Upgrade; +75,000 ᠅ [[Glacite Powder]]; +10,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +20 SkyBlock XP ([[SkyBlock Levels]])|
|5|250|25|25|5|Gain a +10% chance to spawn +1 Frozen Corpse when entering [[Glacite Mineshafts]] you summoned.; +100,000 ᠅ [[Glacite Powder]]; +25,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +25 SkyBlock XP ([[SkyBlock Levels]])|
|6|500|50|50|10|Gain a +10% chance to get +1 item when looting a Frozen Corpse.; +150,000 ᠅ [[Glacite Powder]]; +50,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +30 SkyBlock XP ([[SkyBlock Levels]])|
|7|1000|100|100|20|[[Organ Donor Artifact]] Upgrade; +200,000 ᠅ [[Glacite Powder]]; +100,000 Frozen Corpse RNG Meter XP ([[Pity and RNG Meters]]); +35 SkyBlock XP ([[SkyBlock Levels]])|
## Frozen Corpse RNG Meter
The Frozen Corpses RNG Meter increases the drop rate of certain items from the list below.
- Looting a [[Frozen Corpses|Frozen Corpse]] grants varying amounts of Frozen Corpse XP depending on its type:
  - +500 per Lapis corpse;
  - +2,500 per Umber corpse;
  - +2,500 per Tungsten corpse;
  - +25,000 per Vanguard corpse.
- Items in the Frozen Corpse RNG Meter have predefined amounts of Frozen Corpse XP required to guarantee to roll. The amount of Frozen Corpse XP is roughly based on drop chance.
- When a bundle is rolled, the selected item has an increased weight with the following formula. If enough Frozen Corpse XP is stored within the Frozen Corpse RNG Meter, the selected item is guaranteed to drop.
  New Weight=Item Weight×(1+min⁡(2×Stored Frozen Corpse XPRequired Frozen Corpse XP,2))
- The menu can be accessed through [[Grandpa Wolf]] or the /corpsemilestones command: /corpsemilestones ——> [[Pity and RNG Meters|RNG Meter]]
Frozen Corpses RNG Meter XP Values:
|Loot|Frozen Corpse XP|
|-|-|
|[[Dead Man's Chestplate]]|12,000|
|Flawless Onyx Gemstone ([[Gemstone]])|60,000|
|Flawless Citrine Gemstone ([[Gemstone]])|60,000|
|Flawless Peridot Gemstone ([[Gemstone]])|60,000|
|Flawless Aquamarine Gemstone ([[Gemstone]])|60,000|
|[[Refined Umber]]|60,000|
|[[Refined Tungsten]]|60,000|
|[[Glacite Amalgamation]]|60,000|
|[[Enchanted Book]] (Ice Cold I ([[Ice Cold]]))|60,000|
|[[Blue Goblin Egg]]|60,000|
|Opal Crystal ([[Gemstone Crystals]])|75,000|
|Onyx Crystal ([[Gemstone Crystals]])|75,000|
|Peridot Crystal ([[Gemstone Crystals]])|75,000|
|Aquamarine Crystal ([[Gemstone Crystals]])|75,000|
|Citrine Crystal ([[Gemstone Crystals]])|75,000|
|[[Dwarven O's Metallic Minis]]|75,000|
|[[Umber Key]]|100,000|
|[[Tungsten Key]]|100,000|
|[[Mithril Plate]]|150,000|
|[[Umber Plate]]|300,000|
|[[Tungsten Plate]]|300,000|
|[[Frozen Scute]]|750,000|
|[[Caged Wisp]]|1,250,000|
|[[Skeleton Key]]|1,250,000|
|[[Shattered Locket]]|2,500,000|
|[[Frostbitten Dye]]|5,000,000|
## Tips
- Players can use /viewfrozencorpsemilestones or /corpsemilestones to access the milestone menu remotely.
- Players should unlock and max [[Heart of the Mountain|Gifts from the Departed perk in Heart of the Mountain]] before progressing this milestone.
## Trivia
- The total cost of keys for maxed Frozen Corpse milestone is .
## History
[[Alpha Hypixel Network]]:
|Mar 21, 2024|Added Frozen Corpses.|
|Feb 18, 2026|0.24.2 RC|Added Frozen Corpse Milestones.|
|Feb 18, 2026|0.24.2 RC|Added Frozen Corpse RNG Meter ([[Pity and RNG Meters]]).|
|Feb 18, 2026|0.24.2 RC|Adjusted Frozen Corpse loot table.|
|Sep 30, 2026|Frozen Corpse ([[Frozen Corpses]]) RNG Meter ([[Pity and RNG Meters]]) now display increased drop chances for selected drops.|
|Sep 30, 2026|Fixed an issue causing certain drops to not have their odds increased by the Frozen Corpse ([[Frozen Corpses]]) RNG Meter ([[Pity and RNG Meters]]).|
[SkyBlock Prototype]
|Apr 11, 2024|Added Frozen Corpses.|
|Feb 24, 2026|0.24.2|Added Frozen Corpse Milestones.|
|Feb 24, 2026|0.24.2|Added Frozen Corpse RNG Meter ([[Pity and RNG Meters]]).|
|Feb 24, 2026|0.24.2|Adjusted Frozen Corpse loot table.|
|Oct 6, 2026|0.27.2|Frozen Corpse ([[Frozen Corpses]]) RNG Meter ([[Pity and RNG Meters]]) now display increased drop chances for selected drops.|
|Oct 6, 2026|0.27.2|Fixed an issue causing certain drops to not have their odds increased by the Frozen Corpse ([[Frozen Corpses]]) RNG Meter ([[Pity and RNG Meters]]).|
|Oct 6, 2026|0.27.2|Added [[Dead Man's Chestplate]] to Frozen Corpse loot table.|
Linked from: [[Accessories/Other]], [[Ananke Feather]], [[Ananke Feather/RNG Meter XP Values]], [[Bejeweled Handle]], [[Blue Goblin Egg]], [[Caged Wisp]], [[Changelog]], [[Commissions]], [[Consumables]], [[Currency]], [[Dead Man's Chestplate]], [[Dead Man's Hunt]], [[Dwarven Mines]], [[Dwarven O's Metallic Minis]], [[Enchanted Glacite]], [[Enchanted Tungsten]], [[Enchanted Umber]], [[Enchantments]], [[Enchantments/Armor]], [[Enchantments/List]], [[Fossil Excavator]], [[Frostbitten Dye]], [[Frozen (disambiguation)]], [[Frozen Scute]], [[Gemstone]], [[Gemstone Crystals]], [[Glacite Amalgamation]], [[Glacite Golem Pet]], [[Glacite Jewel]], [[Glacite Mineshafts]], [[Glacite Powder]], [[Glacite Tunnels]], [[Goblin Egg]], [[Grandpa Wolf]], [[Grandpa Wolf's Cave]], [[Green Goblin Egg]], [[Heart of the Mountain]], [[Ice Cold]], [[Key (disambiguation)]], [[Lapis (disambiguation)]] (+27 more)

# Griffin Burrows
Aliases: Burrow, Griffin Burrow
Categories: Confirmations needed
[Griffin Burrows]
Griffin Burrows are a feature that only appear while the Mythological Ritual perk from [[Diana]] is active.
## Usage
Griffin Burrows can only be seen while the player is holding an [[Ancestral Spade]], [[Archaic Spade]], or [[Deific Spade]]. The Echo ability points the player in the direction of the nearest Griffin Burrow: players can excavate these Burrows, which will either uncover a [[Mythological]] [[Mob]] or treasure. After defeating the [[Mob]] or claiming the treasure, an arrow pointing to the next Burrow in the chain appears.
For each rarity level the player's [[Griffin Pet]] is, new creatures can spawn from Griffin Burrows. Each Griffin Burrow comes in chains of four, six, eight, or ten each. Burrows only spawn on grass blocks on the [[Hub Island]]. The treasure hunt consists of a number of steps, each listed below.
|Spade|Burrow 1|Burrow 2|Burrow 3|Burrow 4|Burrow 5|Burrow 6|Burrow 7|Burrow 8|Burrow 9|Burrow 10|
|-|-|-|-|-|-|-|-|-|-|-|
|[[Ancestral Spade]]|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|||||||
|[[Archaic Spade]]|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|||||
|[[Ancestral Spade]] (Erudite ([[Reforging]]))|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|||||
|[[Deific Spade]]|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|||
|[[Archaic Spade]] (Erudite ([[Reforging]]))|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|||
|[[Deific Spade]] (Erudite ([[Reforging]]))|Arrow|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|Mob Treasure|
When a Griffin Burrow displays an arrow, it will consist of yellow, red, or black particles. The color telegraphs the player's distance from the next Burrow.
When digging up a [[Mythological]] creature, the [[Mob]] must be defeated before the Burrow can be excavated to continue the chain.
The first Griffin Burrow is guaranteed to summon an arrow. All subsequent burrows have a 75% (3 in 4) chance to spawn a [[Mob]] and a 25% (1 in 4) chance to contain treasure.
## Item Loot
The available loot from treasure burrows is as follows, depending on the tier of the spade. It does not depend on the rarity of the player's [[Griffin Pet]].
### Ancestral Spade
|Slot|Item|Weight|Chance per Treasure|Chance per Burrow No Reforge|Chance per Burrow Erudite ([[Reforging]])|
|-|-|-|-|-|-|
|[[Griffin Feather]]|[[Griffin Feather]]|64|66.67% (1 in 1.5 treasures)|12.50% (1 in 8 burrows)|13.89% (1 in 7.2 burrows)|
|[[Coins]] x2500|2,500 [[Coins]]|15|15.62% (1 in 6.4 treasures)|2.93% (1 in 34.13 burrows)|3.26% (1 in 30.72 burrows)|
|[[Coins]] x5000|5,000 [[Coins]]|10|10.42% (1 in 9.6 treasures)|1.95% (1 in 51.2 burrows)|2.17% (1 in 46.08 burrows)|
|[[Coins]] x10k|10,000 [[Coins]]|5|5.21% (1 in 19.2 treasures)|0.98% (1 in 102.4 burrows)|1.09% (1 in 92.16 burrows)|
|[[Coins]] x25k|25,000 [[Coins]]|2|2.08% (1 in 48 treasures)|0.39% (1 in 256 burrows)|0.43% (1 in 230.4 burrows)|
|[[Myth the Fish]]|[[Myth the Fish]]||0.01% (1 in 10,000 treasures)|0.0019% (1 in 53,333.33 burrows)|0.0021% (1 in 48,000 burrows)|
### Archaic Spade
|Slot|Item|Weight|Chance per Treasure|Chance per Burrow No Reforge|Chance per Burrow Erudite ([[Reforging]])|
|-|-|-|-|-|-|
|[[Griffin Feather]]|[[Griffin Feather]]|375|63.34% (1 in 1.58 treasures)|13.20% (1 in 7.58 burrows)|14.34% (1 in 6.97 burrows)|
|[[Coins]] x5000|5,000 [[Coins]]|100|16.89% (1 in 5.92 treasures)|3.52% (1 in 28.42 burrows)|3.82% (1 in 26.15 burrows)|
|[[Coins]] x10k|10,000 [[Coins]]|40|6.76% (1 in 14.8 treasures)|1.41% (1 in 71.04 burrows)|1.53% (1 in 65.37 burrows)|
|[[Mythos Fragment]]|[[Mythos Fragment]]|40|6.76% (1 in 14.8 treasures)|1.41% (1 in 71.04 burrows)|1.53% (1 in 65.37 burrows)|
|[[Coins]] x25k|25,000 [[Coins]]|20|3.38% (1 in 29.6 treasures)|0.70% (1 in 142.08 burrows)|0.76% (1 in 130.74 burrows)|
|[[Coins]] x50k|50,000 [[Coins]]|10|1.69% (1 in 59.2 treasures)|0.35% (1 in 284.16 burrows)|0.38% (1 in 261.49 burrows)|
|[[Coins]] x100k|100,000 [[Coins]]|5|0.84% (1 in 118.4 treasures)|0.18% (1 in 568.32 burrows)|0.19% (1 in 522.97 burrows)|
|[[Coins]] x250k|250,000 [[Coins]]|2|0.34% (1 in 296 treasures)|0.07% (1 in 1,420.8 burrows)|0.07% (1 in 1,353.14 burrows)|
|[[Myth the Fish]]|[[Myth the Fish]]||0.01% (1 in 10,000 treasures)|0.0021% (1 in 48,000 burrows)|0.0022% (1 in 45,714.29 burrows)|
### Deific Spade
|Slot|Item|Weight|Chance per Treasure|Chance per Burrow No Reforge|Chance per Burrow Erudite ([[Reforging]])|
|-|-|-|-|-|-|
|[[Griffin Feather]]|[[Griffin Feather]]|2,020|62.71% (1 in 1.59 treasures)|13.72% (1 in 7.29 burrows)|14.11% (1 in 7.09 burrows)|
|[[Coins]] x10k|10,000 [[Coins]]|500|15.52% (1 in 6.44 treasures)|3.40% (1 in 29.45 burrows)|3.49% (1 in 28.63 burrows)|
|[[Mythos Fragment]]|[[Mythos Fragment]]|300|9.31% (1 in 10.74 treasures)|2.04% (1 in 49.08 burrows)|2.10% (1 in 47.72 burrows)|
|[[Coins]] x25k|25,000 [[Coins]]|200|6.21% (1 in 16.1 treasures)|1.36% (1 in 73.62 burrows)|1.40% (1 in 71.58 burrows)|
|[[Coins]] x50k|50,000 [[Coins]]|100|3.10% (1 in 32.21 treasures)|0.70% (1 in 147.25 burrows)|0.70% (1 in 143.16 burrows)|
|[[Coins]] x100k|100,000 [[Coins]]|50|1.55% (1 in 64.42 treasures)|0.34% (1 in 294.49 burrows)|0.35% (1 in 286.31 burrows)|
|[[Coins]] x250k|250,000 [[Coins]]|25|0.78% (1 in 128.84 treasures)|0.17% (1 in 588.98 burrows)|0.17% (1 in 572.62 burrows)|
|[[Coins]] x500k|500,000 [[Coins]]|15|0.47% (1 in 214.73 treasures)|0.10% (1 in 981.64 burrows)|0.10% (1 in 954.37 burrows)|
|[[Coins]] x1m|1,000,000 [[Coins]]|10|0.31% (1 in 322.1 treasures)|0.07% (1 in 1,472.46 burrows)|0.07% (1 in 1,431.56 burrows)|
|[[Braided Griffin Feather]]|[[Braided Griffin Feather]]|1|0.03% (1 in 3,221 treasures)|0.0068% (1 in 14,724.57 burrows)|0.0070% (1 in 14,315.56 burrows)|
|[[Myth the Fish]]|[[Myth the Fish]]||0.01% (1 in 10,000 treasures)|0.0022% (1 in 45,714.29 burrows)|0.0022% (1 in 44,444.44 burrows)|
## Mobs
The types of [[Mythological]] mobs that can be dig up from a [[Griffin Burrows|Griffin Burrow]] varies depending on the rarity of the player's [[Griffin Pet]].
Listed spawn chances are base chances. [[Tracking]] increases the weight of [[Elusive]] mobs. For example, having 15 [[Tracking]] would multiply their weights by 1.15x.
In addition to the stats listed below, all [[Mythological]] mobs have 50% resistance to [[Damage Calculation|Magic Damage]].
[[Gaia Construct|Gaia Constructs]] as well as all mobs that first appear in [[Rarity|EPIC]] tier or above are immune to damage from bows,[Confirm (Confirmation needed; When this info is confirmed, remove this.)] with the exception of [[King Minos]]' hit shield.
### Common
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv15] [[Minos Hunter]]|[[Mythological]] [[Humanoid]]|4,000 [[Health]] 40 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|50%; (1 in 2 mobs)|
|[Lv15] Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|2,500 [[Health]] 30 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|50%; (1 in 2 mobs)|
### Uncommon
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv25] Blessed Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|15,000 [[Health]] 125 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|27.78%; (1 in 3.6 mobs)|
|[Lv25] Blessed Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|12,500 [[Health]] 75 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|27.78%; (1 in 3.6 mobs)|
|[Lv40] Blessed Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|20,000 [[Health]] 100 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|22.22%; (1 in 4.5 mobs)|
|[Lv40] Blessed Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|25,000 [[Health]] 100 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|22.22%; (1 in 4.5 mobs)|
### Rare
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv60] Stalwart Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|100,000 [[Health]] 500 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|20.83%; (1 in 4.8 mobs)|
|[Lv55] Stalwart Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|75,000 [[Health]] 350 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|20.83%; (1 in 4.8 mobs)|
|[Lv70] Stalwart Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|125,000 [[Health]] 250 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|16.67%; (1 in 6 mobs)|
|[Lv70] Stalwart Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|150,000 [[Health]] 400 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|16.67%; (1 in 6 mobs)|
|[Lv85] Stalwart Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|200,000 [[Health]] 750 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|12.50%; (1 in 8 mobs)|
|[Lv85] Stalwart Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|175,000 [[Health]] 600 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|12.50%; (1 in 8 mobs)|
### Epic
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv80] Venerable Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|350,000 [[Health]] 1,250 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.86%; (1 in 5.6 mobs)|
|[Lv85] Venerable Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|250,000 [[Health]] 1,000 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.86%; (1 in 5.6 mobs)|
|[Lv95] Venerable Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|400,000 [[Health]] 750 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|14.29%; (1 in 7 mobs)|
|[Lv95] Venerable Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|500,000 [[Health]] 800 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|14.29%; (1 in 7 mobs)|
|[Lv140] Venerable Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|750,000 [[Health]] 1,500 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.71%; (1 in 9.33 mobs)|
|[Lv140] Venerable Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|650,000 [[Health]] 2,000 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.71%; (1 in 9.33 mobs)|
|[Lv45] Venerable Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|1,500,000 [[Health]] 350 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|7.14%; (1 in 14 mobs)|
|[Lv175] Venerable Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|2,000,000 [[Health]] 1,000 [[Damage]]|[[Minos Relic]]|✕ No|400|7.14%; (1 in 14 mobs)|
### Legendary
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv125] Exalted Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|1,000,000 [[Health]] 2,750 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.39%; (1 in 5.75 mobs)|
|[Lv155] Exalted Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|750,000 [[Health]] 2,250 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.39%; (1 in 5.75 mobs)|
|[Lv150] Exalted Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|1,250,000 [[Health]] 1,750 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|13.91%; (1 in 7.19 mobs)|
|[Lv150] Exalted Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|1,500,000 [[Health]] 2,000 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|13.91%; (1 in 7.19 mobs)|
|[Lv175] Exalted Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|2,000,000 [[Health]] 3,750 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.43%; (1 in 9.58 mobs)|
|[Lv175] Exalted Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|1,500,000 [[Health]] 3,500 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.43%; (1 in 9.58 mobs)|
|[Lv120] Exalted Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|8,000,000 [[Health]] 500 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|6.96%; (1 in 14.38 mobs)|
|[Lv310] Exalted Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|12,500,000 [[Health]] 1,750 [[Damage]]|[[Minos Relic]]|✕ No|400|6.96%; (1 in 14.38 mobs)|
|[Lv750] Exalted Sphinx ([[Sphinx]])|[[Mythological]] [[Humanoid]] [[Elusive]]|40,000,000 [[Health]] 4,000 [[Damage]]|[[Brain Food]]|✔ Yes ([[Sphinx Shard]])|75|1.30%; (1 in 76.67 mobs)|
|[Lv750] Exalted Minos Inquisitor ([[Minos Inquisitor]])|[[Mythological]] [[Humanoid]] [[Elusive]]|50,000,000 [[Health]] 750 [[Damage]]|[[Enchanted Book]] (Chimera I ([[Chimera]]))|✕ No|75|1.30%; (1 in 76.67 mobs)|
### Mythic
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv200] Empyrean Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|1,750,000 [[Health]] 4,000 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.30%; (1 in 5.78 mobs)|
|[Lv200] Empyrean Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|1,250,000 [[Health]] 3,000 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.30%; (1 in 5.78 mobs)|
|[Lv250] Empyrean Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|2,500,000 [[Health]] 2,500 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|13.84%; (1 in 7.22 mobs)|
|[Lv250] Empyrean Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|3,000,000 [[Health]] 2,750 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|13.84%; (1 in 7.22 mobs)|
|[Lv325] Empyrean Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|3,750,000 [[Health]] 6,500 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.38%; (1 in 9.63 mobs)|
|[Lv325] Empyrean Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|3,500,000 [[Health]] 5,000 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.38%; (1 in 9.63 mobs)|
|[Lv210] Empyrean Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|15,500,000 [[Health]] 1,000 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|6.92%; (1 in 14.45 mobs)|
|[Lv550] Empyrean Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|25,000,000 [[Health]] 2,500 [[Damage]]|[[Minos Relic]]|✕ No|400|6.92%; (1 in 14.45 mobs)|
|[Lv1,250] Empyrean Sphinx ([[Sphinx]])|[[Mythological]] [[Humanoid]] [[Elusive]]|65,000,000 [[Health]] 7,000 [[Damage]]|[[Brain Food]]|✔ Yes ([[Sphinx Shard]])|75|1.30%; (1 in 77.07 mobs)|
|[Lv1,250] Empyrean Minos Inquisitor ([[Minos Inquisitor]])|[[Mythological]] [[Humanoid]] [[Elusive]]|80,000,000 [[Health]] 1,000 [[Damage]]|[[Enchanted Book]] (Chimera I ([[Chimera]]))|✕ No|75|1.30%; (1 in 77.07 mobs)|
|[Lv1,750] Empyrean Manticore ([[Manticore]])|[[Mythological]] [[Animal]] [[Elusive]]|125,000,000 [[Health]] 8,000 [[Damage]]|[[Fateful Stinger]] [[Manti-core]]|✕ No|15|0.26%; (1 in 385.33 mobs)|
|[Lv1,750] Empyrean King Minos ([[King Minos]])|[[Mythological]] [[Humanoid]] [[Elusive]]|100,000,000 [[Health]] 2,500 [[Damage]]|[[Crown of Greed]] [[Shimmering Wool]]|✔ Yes ([[King Minos Shard]])|15|0.26%; (1 in 385.33 mobs)|
## Game Message
|Condition|Dialogue|
|-|-|
|Digging out the first to third burrow in a chain|You dug out a Griffin Burrow! (#/4)|
|Digging out the last burrow in a chain|You finished the Griffin burrow chain! (4/4)|
|Digging out coins|Wow! You dug out # coins!|
|Digging out treasure|RARE DROP! You dug out a <treasure>!|
|Attempting to dig out a burrow before killing the mobs|Defeat the burrow defenders in order to dig it!|
|Condition|Random Dialogue|
|Digging out a mob|Danger! You dug out a [mob]!|
|Digging out a mob|Oi! You dug out a [mob]!|
|Digging out a mob|Uh oh! You dug out a [mob]!|
|Digging out a mob|Woah! You dug out a [mob]!|
|Digging out a mob|Yikes! You dug out a [mob]!|
|Digging out a mob|Good Grief! You dug out a [mob]!|
## Gallery
- A Griffin Burrow
- A Griffin Burrow guaranteed to spawn a Mob A Griffin Burrow guaranteed to spawn a [[Mob]]
- A Griffin Burrow guaranteed to grant treasure
- An arrow after digging a Griffin Burrow
## Trivia
- Multiple Griffin Burrow chains can be open at once and finished in any order.
## History
[[SkyBlock Prototype]]:
|Sep 8, 2020|0.9|Added Griffin Burrows.|
|Dec 11, 2023|Fixed a bug that caused particles for a lot of Griffin Burrow locations to be active at once.|
Linked from: [[Ancestral Spade]], [[Animal]], [[Aquatic]], [[Archaic Spade]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Combat]], [[Attributes/List/Epic]], [[Attributes/Search]], [[Bits]], [[Braided Griffin Feather]], [[Changelog/2021/December 16]], [[Coins]], [[Construct]], [[Cretan Bull]], [[Crown of Avarice]], [[Crown of Greed]], [[Deific Spade]], [[Doug]], [[Elusive]], [[Events]], [[Events/Mayor Events Table]], [[Feather (disambiguation)]], [[Four-Eyed Fish]], [[Fragment (disambiguation)]], [[Gaia Construct]], [[Golden Fleece]], [[Griffin Feather]], [[Griffin Pet]], [[Harpy]], [[Humanoid]], [[King Minos]], [[King Minos Shard]], [[Manticore]], [[Minos Champion]], [[Minos Hunter]], [[Minos Inquisitor]], [[Minotaur]], [[Mob Types/List/Animal]], [[Mob Types/List/Aquatic]] (+19 more)

# Guesting
Aliases: Guest
Categories: Confirmations needed, Pages with UIs, Mechanics
[Guesting]
Guesting is a feature that allows players to visit islands of other players.
## Mechanics
While guesting, most item abilities such as the [[Aspect of the End]]'s teleport and [[Ember Rod]]'s fireball are disabled. Some items like the [[Grappling Hook]] are exceptions to this.
Guest Limit:
|Rank|Limit|
|-|-|
|1Default ([[Ranks]])|1|
|2[VIP] ([[Ranks]])|3|
|4[MVP] ([[Ranks]])|5|
|6[MVP++] ([[Ranks]])|7|
|7[YOUTUBE] ([[Ranks]])/34[PIG++] ([[Ranks]])|15|
|8[PIG+++] ([[Ranks]])|20[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
You can purchase guest limit upgrades at [[Elizabeth]]. The first additional slot is free, but the next 4 upgrades each cost 50 [[SkyBlock Gems]].
Note: 6[[Ranks|[MVP++]]] can bypass the guesting limit, but only 10 above the normal limit. If you are in a [[Co-op]], your guesting limit is that of the player with the highest rank.
### Commands
There are various [[Commands]] that a player can use for guesting:
- To visit another player: /visit (In Game Name)
- To invite someone to guest to your island: /invite (In Game Name).
Players talking in chat while guesting will have their messages prefaced with a [✌] symbol.
## Interface
Guesting setting can be found in [[SkyBlock Menu]] → [[Settings]] → Guest Management.
Tip: click on certain slots to change the UI or go to another article!
## History
[[SkyBlock Prototype]]:
|Jul 9, 2019|0.6|Added Guesting.|
|Sep 8, 2020|0.9|Added an upgrade through [[Elizabeth]] which increases the maximum guest limit.|
|Oct 9, 2022|Disabled all forms of Guesting.|
|Oct 9, 2022|Re-enabled Guesting.|
Linked from: [[Account & Profile Upgrades]], [[Changelog/2020/November 12]], [[Commands]], [[Egg (disambiguation)]], [[Garden Visitors]], [[Ghost]], [[Island (disambiguation)]], [[Scion]], [[The Garden]], [[Xalx]]

# Habanero Tactics
Categories: Confirmations needed, Enchantments, Craftable items, Chili Pepper Collection
[Habanero Tactics]
Type: Enchantment ([[Enchantments]])
Rarity: COMMON ([[Rarity]])-UNCOMMON ([[Rarity]])
Collection ([[Collections]]): Chili Pepper VIII (8) ([[Chili Pepper]])
[Enchantment Requirements]
Minimum Level: IV
Maximum Level: V
Req. [[Enchanting]] Level: Enchanting XXVIII (28) ([[Enchanting]])
[Item Properties]
Salable (Whether or not the item(s) can be sold to an NPC. If an item is not salable but has enchantments on it, it becomes salable.): ✕ No
Tradeable: ✔ Yes
Auctionable: ✕ No
Museum (Whether or not the item(s) can be donated to the Museum): ✕ No
[Item Metadata]
Item ID: ENCHANTMENT_ULTIMATE_HABANERO_TACTICS
Tooltip: Combinable in Anvil; Habanero Tactics IV ℏ Heal +6% more from wands.; ℏ Deal +20% damage with Slayer weapons.; ℏ Gain +10☯ Combat Wisdom with Slayer weapons.; ℏ With Smoldering Polarization, gain 10 Magic Find on your slayer weapon.; You can only have 1 Ultimate Enchantment on an item!; Applicable on: Armor Apply Cost: 250 Exp Levels; COMMON
Habanero Tactics is an Ultimate [[Ultimate Enchantments|Enchantment]].
## Obtaining
### Crafting
|Requirement|Ingredients|[[Crafting]] recipe|
|-|-|-|
|Chili Pepper VIII (8) ([[Chili Pepper]])|4x [[Plasma]] 4x [[Stuffed Chili Pepper]] 16x [[Enchanted Rabbit Hide]] 28x [[Enchanted Brown Mushroom Block]]|Recipe: [[Stuffed Chili Pepper]] ×4 + [[Enchanted Brown Mushroom Block]] x14 ×2 + [[Enchanted Rabbit Hide]] x8 ×2 + [[Plasma]] x4 → Enchanted Book|
[[Enchanted Book]] (Habanero Tactics IV) can be combined in an [[Anvil]], up to Habanero Tactics V.
### Bazaar
The Habanero Tactics [[Ultimate Enchantments|Enchantment]] can be traded through the [[Bazaar]].
|Enchantment|Tier|
|-|-|
|Habanero Tactics|IV|
|Habanero Tactics|V|
## Ability
- Heal +6-7.5% more from wands.
- Deal +20-25% damage with Slayer weapons.
- Gain +2.5-5 [[Combat Wisdom]] with Slayer weapons.
- With [[Re-heated Gummy Polar Bear|Smoldering Polarization]], gain +10-15 [[Magic Find]] on your slayer weapon.
## Applying
The Habanero Tactics [[Ultimate Enchantments|Enchantment]] can be applied to any [[Armor]] piece. It requires [[Enchanting|Enchanting XXVIII (28)]] to apply.
Anvil:
|Tier|Cost|
|-|-|
|Ⅳ|223 [[Experience]]|
|Ⅴ|266 [[Experience]]|
## Trivia
- The name of the [[Ultimate Enchantments|Enchantment]] is a reference to the habanero pepper, which is a hot variety of chili.
## History
[[Alpha Hypixel Network]]:
|Mar 23, 2026|Reduced craft cost of Habanero Tactics IV from 128 (2 stacks) [[Enchanted Brown Mushroom Block]] to 28 [[Enchanted Brown Mushroom Block]].|
|Sep 30, 2026|(Not mentioned) Fixed Habanero Tactics [[Damage]] multiplier applying against every [[Mob]].|
|Sep 30, 2026|(Not mentioned) Restricted Habanero Tactics to apply against SLAYER BOSSES ([[Slayer]]) only instead of SLAYER BOSSES ([[Slayer]]) and SLAYER MINIBOSSES ([[Minibosses]]).|
[SkyBlock Prototype]
|Aug 5, 2022|Added Habanero Tactics IV.|
|Aug 5, 2022|Added Habanero Tactics V.|
|Dec 3, 2024|0.20.9|Adjusted recipe: 32 [[Stuffed Chili Pepper]] → 4 [[Stuffed Chili Pepper]] 16 [[Enchanted Brown Mushroom Block]] → 128 [[Enchanted Brown Mushroom Block]] 4 [[Volta]] → 4 [[Plasma]]|
|Jan 21, 2025|0.21.1|Buffed Habanero Tactics.|
|Jan 23, 2025|Added [[Combat Wisdom]] to Habanero Tactics.|
|Mar 31, 2026|0.24.3|Reduced craft cost of Habanero Tactics IV from 128 [[Enchanted Brown Mushroom Block]] to 28 [[Enchanted Brown Mushroom Block]].|
Linked from: [[Axes]], [[Bazaar]], [[Bazaar/Item List]], [[Changelog]], [[Chili Pepper]], [[Collections]], [[Collections/List]], [[Combat Wisdom]], [[Consumables]], [[Damage Calculation]], [[Damage Calculation/Additive Sources]], [[Enchanted Book/Bazaar (Ultimate)]], [[Enchanted Brown Mushroom Block]], [[Enchanted Rabbit Hide]], [[Enchanting]], [[Enchanting/Leveling Rewards]], [[Enchantments]], [[Magic Find]], [[Magic Find/Alpha]], [[Magic Find/Table]], [[Plasma]], [[Re-heated Gummy Polar Bear]], [[Slayer Weapons]], [[Stuffed Chili Pepper]], [[Ultimate Enchantments]], [[Volta]], [[Wand of Atonement]], [[Wand of Healing]], [[Wand of Mending]], [[Wand of Restoration]]

# Harvest Feast
Aliases: Farming Feast, Farming feast, Grand Feast, Grand Feast Milestone, Grand Harvest, Grand harvest, Great Feast, Great feast, Harvest, Harvest Feast Milestone
Categories: Confirmations needed, Events
Harvest Feast
:
Countdown:
Dates and times based on browser time.
The Harvest Feast is an event that takes place every [[Time Systems|SkyBlock Year]] for 3 months between Early Autumn, Autumn, and Late Autumn. During the event, 4 crops will be in season: harvesting in-season crops has a chance to drop [[Rare Crops]] and [[Seasoning]]. The crops in season get changed to a different 4 new crops every SkyBlock month (or 10 hours and 20 minutes). Upcoming in-season crops can be previewed at [[Feast Chef Ted]].
[[Feast Chef Ted]] runs the [[Communal Stew]] on the [[Hub Island]]. Upon collecting [[Seasoning]], it will automatically be donated to the Communal Stew and contributes to the player's Feast Milestones. Feast Milestones reward [[Feast Flask|Feast Flasks]] (that can be crafted into the [[Celestial Mason Jar]]), [[Carnival Ticket|Carnival Tickets]] and a [[Commemorative Mason Jar]] at [[Harvest Feast|Harvest Feast Milestone V (5)]], or a [[Grand Commemorative Mason Jar]] at [[Harvest Feast|Grand Feast Milestone IX (9)]].
## Feast Milestones
Harvest Feast Milestones:
|Tier|[[Seasoning]] Required|Reward Individual|Reward Cumulative|
|-|-|-|-|
|I|5|1 [[Feast Flask]]|1 [[Feast Flask]]|
|II|25|1 [[Feast Flask]]|2 Feast Flasks ([[Feast Flask]])|
|III|75|2 Feast Flasks ([[Feast Flask]])|4 Feast Flasks ([[Feast Flask]])|
|IV|150|2 Feast Flasks ([[Feast Flask]])|6 Feast Flasks ([[Feast Flask]])|
|V|250|2x Feast Flasks ([[Feast Flask]]) [[Commemorative Mason Jar]]|8x Feast Flasks ([[Feast Flask]]) [[Commemorative Mason Jar]]|
Grand Feast Milestones:
|Tier|[[Seasoning]] Required|Reward Individual|Reward Cumulative|
|-|-|-|-|
|I|5|1 [[Feast Flask]]; 25 [[Kernels]]|1 [[Feast Flask]]; 25 [[Kernels]]|
|II|25|1 [[Feast Flask]]; 50 [[Kernels]]|2 [[Feast Flask]]; 75 [[Kernels]]|
|III|75|2 Feast Flasks ([[Feast Flask]]); 75 [[Kernels]]|4 [[Feast Flask]]; 150 [[Kernels]]|
|IV|150|2 Feast Flasks ([[Feast Flask]]); 100 [[Kernels]]|6 [[Feast Flask]]; 250 [[Kernels]]|
|V|250|2 Feast Flasks ([[Feast Flask]]); 125 [[Kernels]]|8 [[Feast Flask]]; 375 [[Kernels]]|
|VI|350|2 Feast Flasks ([[Feast Flask]]); 150 [[Kernels]]|10 [[Feast Flask]]; 525 [[Kernels]]|
|VII|450|2 Feast Flasks ([[Feast Flask]]); 175 [[Kernels]]|12 [[Feast Flask]]; 700 [[Kernels]]|
|VIII|550|2 Feast Flasks ([[Feast Flask]]); 200 [[Kernels]]|14 [[Feast Flask]]; 900 [[Kernels]]|
|IX|750|2 Feast Flasks ([[Feast Flask]]); 225 [[Kernels]]; [[Grand Commemorative Mason Jar]]|16 [[Feast Flask]]; 1,125 [[Kernels]]; [[Grand Commemorative Mason Jar]]|
Every milestone also grants 5 [[Carnival Ticket|Carnival Tickets]].
Additionally, the [[Doug|Leftovers]] perk from the [[Carnival]] also grants 1-2 [[Feast Flask|Feast Flasks]] if the player reaches the final Milestone.
## Grand Feast
While [[Finnegan]] is in office with the Grand Feast perk, the Harvest Feast becomes the Grand Feast with the following changes:
- The Grand Feast now runs for an entire [[Time Systems|SkyBlock Year]], with the crops rotating every season as usual.
- [[Kernels]] are obtained by donating [[Seasoning]] to the Communal Stew during a Grand Feast and by obtaining Feast Milestones.
- [[Feast Baker Scott]] appears at the [[Communal Stew]] to sell exclusive items.
- There are now 9 Feast Milestones instead of 5, each milestone also gives [[Kernels]], and the last milestone grants a [[Grand Commemorative Mason Jar]].
## Rare Crops
While harvesting crops that are in-season, there is a 0.006% (1 in 18,000) chance for Harvest Feast [[Rare Crops]] to drop. [[Pests]] that drop in-season crops have a 15% (1 in 6.67) chance to drop their respective Rare Crop. [[Field Mouse]] has a 30% (1 in 3.33) to drop any in-season crop.
[[Seasoning]], despite being classified as a [[Rare Crops|Rare Crop]], has a 0.04% (1 in 2,250) chance to drop and does not appear as a physical item.
[[Overbloom]] increases the chance to drop [[Rare Crops]].
|Slot|Name|Crop|Pest|Craftable Items|
|-|-|-|-|-|
|[[Cornucopia]]|[[Cornucopia]]|[[Wheat]]|[[Fly]]|[[Cornucopia Crystal]] [[Feast Burger with a Side of Deepfries]] [[Not Very Moldy Bread]]|
|[[Carrot Zest]]|[[Carrot Zest]]|[[Carrot]]|[[Cricket]]|[[Poignant Carrot Bait]] [[Carrot-Colored Vinyl Set]]|
|[[Deepfries]]|[[Deepfries]]|[[Potato]]|[[Locust]]|[[Feast Burger with a Side of Deepfries]] [[Hashbrown]]|
|[[Aggourdian]]|[[Aggourdian]]|[[Pumpkin]]|[[Rat]]|[[Overpriced Drink]] [[Turbo Gourd]] [[Enchanted Turbo Gourd]]|
|[[Cane Knot]]|[[Cane Knot]]|[[Sugar Cane]]|[[Mosquito]]|[[Speed Relic]] [[Thermodynamic Armor]] [[Unalloyed Speed]]|
|[[Melon Juice]]|[[Melon Juice]]|[[Melon Slice]]|[[Earthworm]]|[[Melon Juice Mixin]] [[Trunk Polish]]|
|[[Cactus Flower]]|[[Cactus Flower]]|[[Cactus]]|[[Mite]]|[[Blooming Thorns]] [[Prickly Creeper]] [[Potted Cactus]]|
|[[Designer Coffee Beans]]|[[Designer Coffee Beans]]|[[Cocoa Beans]]|[[Moth]]|Bug Blender I ([[Bug Blender]]) [[Cocoaleech Shard]] [[Overpriced Drink]]|
|[[Feastfungus]]|[[Feastfungus]]|[[Mushroom]]|[[Slug]]|[[Feast Burger with a Side of Deepfries]] "Fragranced" Brown Mushroom Paste ([["Fragranced" Brown Mushroom "Paste"]]) [[Fungal Tip Jar]]|
|[[Botroot]]|[[Botroot]]|[[Nether Wart]]|[[Beetle]]|[[Super Jacob Entertainment System]] [[Buzzybee's Fantabulous Disco Destination]]|
|[[Salted Sunflower Seeds]]|[[Salted Sunflower Seeds]]|[[Sunflower]]|[[Dragonfly]]|[[Sunflower Butter]] [[Salty Nozzle]]|
|[[Crystalized Moonlight]]|[[Crystalized Moonlight]]|[[Moonflower]]|[[Firefly]]|[[Moondew]]|
|[[Floral Gelatin]]|[[Floral Gelatin]]|[[Wild Rose]]|[[Praying Mantis]]|[[Royal Jelly]] [[Orchid Mantis Pet]]|
## Game Message
|Condition|Message|
|-|-|
|Harvest Feast starts|HARVEST FEAST! The event has started! Speak with Feast Chef Ted in the Hub to learn what crops are in season!|
|Grand Feast starts|GRAND FEAST! The event has started! Speak with Feast Chef Ted in the Hub to learn what crops are in season!|
## Trivia
- [[Glowing Mushroom|Glowing Mushrooms]] may provide [[Feastfungus]][Confirm (Confirmation needed; When this info is confirmed, remove this.)] and [[Seasoning]] if [[Mushroom]] are in-season.
## History
[[Alpha Hypixel Network]]:
|Mar 31, 2026|0.24.3|Added Harvest Feast.|
|Mar 31, 2026|0.24.3|Added Grand Feast.|
|Jul 15, 2026|Changed amount of in-season crops to 4 instead of 3.|
|Jul 15, 2026|Added 5 Carnival Tickets ([[Carnival Ticket]]) to each Feast Milestone.|
[SkyBlock Prototype]
|Apr 28, 2026|0.24.4|Added Harvest Feast.|
|Apr 28, 2026|0.24.4|Added Grand Feast.|
|May 14, 2026|Harvest Feast [[Rare Crops]] now also drop from [[Pests]].|
|Jun 19, 2026|Removed Grand Feast ([[Harvest Feast]]) as perk provided by [[Finnegan]] when selected by [[Candidate Jerry]]'s Perkpocolypse.|
|Jul 22, 2026|0.26.1|Changed amount of in-season crops to 4 instead of 3.|
|Jul 22, 2026|0.26.1|Added 5 Carnival Tickets ([[Carnival Ticket]]) to each Feast Milestone.|
Linked from: [[Aggourdian]], [[Baker (disambiguation)]], [[Beetle]], [[Bonus Pest Chance]], [[Botroot]], [[Bread Bowl]], [[Burger (disambiguation)]], [[Cactus Flower]], [[Calendar]], [[Candidate Jerry]], [[Cane Knot]], [[Carnival Ticket]], [[Carnival Tokens]], [[Carrot Zest]], [[Celestial Mason Jar]], [[Changelog]], [[Coffee (disambiguation)]], [[Collectable Items]], [[Commemorative Mason Jar]], [[Communal Stew]], [[Consumables]], [[Cornucopia]], [[Cricket]], [[Crystalized Moonlight]], [[Currency]], [[Deepfries]], [[Designer Coffee Beans]], [[Doug]], [[Dragonfly]], [[Earthworm]], [[Events]], [[Events/Yearly Events Table]], [[Farm]], [[Farming Contest Display]], [[Farming Fortune]], [[Feast Baker Scott]], [[Feast Chef Ted]], [[Feast Flask]], [[Feastfungus]], [[Finn's Focaccia]] (+30 more)

# Helmets
Aliases: Chainmail Helmet, Diamond Helmet, Golden Helmet, Helmet, Iron Helmet, Leather Helmet
Categories: Confirmations needed, Armor, Armor Sets, Cosmetics, Helmet
[Helmets]
Type: [[Armor]]
The Helmet slot is one of the four [[Armor]] slots. There are many standalone pieces for this slot.
All items that use a custom player head as a texture can be placed on the player's head.
## Individual helmets
Helmets that are not part of a set.
|Icon|Name|Rarity|Stats|Ability|
|-|-|-|-|-|
|[[Blaze Hat]]|[[Blaze Hat]]|COMMON ([[Rarity]])|[[Strength]] +20||
|[[Chicken Hat]]|[[Chicken Hat]]|COMMON ([[Rarity]])|[[Health]] +20|Lay Eggs ([[Egg]]) when you sneak! Has a cooldown of 5 seconds. Also reduces fall damage by 5.0%.|
|[[Creeper Hat]]|[[Creeper Hat]]|COMMON ([[Rarity]])|[[Strength]] +5; [[Crit Chance]] +5%; [[Crit Damage]] +5%; [[Health]] +5; [[Defense]] +5; [[Intelligence]] +5|Grants immunity to explosion damage.|
|[[Cow Hat]]|[[Cow Hat]]|COMMON ([[Rarity]])|[[Health]] +10; [[Defense]] +5|Grants immunity to de-buffs when equipped.|
|[[Ghast Head]]|[[Ghast Head]]|COMMON ([[Rarity]])|[[Health]] +100|Restores +5 [[Health]] every second while worn.|
|[[Fish Hat]]|[[Fish Hat]]|COMMON ([[Rarity]])|[[Health]] +5|Ability: Splash Crouch to splash some water around.; Mana Cost ([[Intelligence]]): 10; Cooldown: 1s|
|[[Magma Cube Head]]|[[Magma Cube Head]]|COMMON ([[Rarity]])|[[Health]] +25; [[Defense]] +25||
|[[Pufferfish Hat]]|[[Pufferfish Hat]]|COMMON ([[Rarity]])|[[Strength]] +10; [[Health]] +20|Ability: Spiky While wearing, your attacks have a chance to deal 10 damage + 20% of your [[Strength]] to nearby enemies!|
|[[Salmon Hat]]|[[Salmon Hat]]|COMMON ([[Rarity]])|[[Strength]] +15; [[Speed]] +2||
|[[Skeleton Hat]]|[[Skeleton Hat]]|COMMON ([[Rarity]])|[[Speed]] +2; [[Intelligence]] +10|Your arrows have a 20% chance to explode on impact dealing 50 base Magic Damage to enemies within 8 blocks.|
|[[Slime Hat]]|[[Slime Hat]]|COMMON ([[Rarity]])|[[Health]] +50|Grants immunity to [[Knockback]] from mobs.|
|[[Spider Hat]]|[[Spider Hat]]|COMMON ([[Rarity]])|[[Crit Chance]] +25%|When worn, [[Arthropod]] mobs deal -30% damage.|
|[[Squid Hat]]|[[Squid Hat]]|COMMON ([[Rarity]])|[[Speed]] +1|Extra chance to fish up Squids ([[Squid]])!|
|[[Zombie Hat]]|[[Zombie Hat]]|COMMON ([[Rarity]])|[[Defense]] +10|Gives +10 [[Defense]] for each [[Zombie]] within 8 blocks.|
|[[Golem Hat]]|[[Golem Hat]]|COMMON ([[Rarity]])||Drops an [[Iron Ingot]] when you sneak!; Cooldown: 5s|
|[[Blobfish Hat]]|[[Blobfish Hat]]|UNCOMMON ([[Rarity]])|[[Strength]] +25; [[Intelligence]] -10||
|[[Tropical Fish Hat]]|[[Tropical Fish Hat]]|UNCOMMON ([[Rarity]])|[[Intelligence]] +50||
|[[Magmafish Hat]]|[[Magmafish Hat]]|UNCOMMON ([[Rarity]])|[[Intelligence]] +50|Ability: Splash Crouch to splash some magma around.; Mana Cost ([[Intelligence]]): 20; Cooldown: 1s|
|[[Sea Lantern Hat]]|[[Sea Lantern Hat]]|UNCOMMON ([[Rarity]])||Breathe 5x longer underwater when wearing!|
|[[Enderman Mask]]|[[Enderman Mask]]|UNCOMMON ([[Rarity]])|[[Strength]] +1; [[Health]] +1; [[Defense]] +1; [[Intelligence]] -99|(Hidden) You can look at an [[Enderman]] in the eyes and it will not attack you. [Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
|[[Lantern Helmet]]|[[Lantern Helmet]]|UNCOMMON ([[Rarity]])|[[Health]] +20; [[Defense]] +10|For every [[Farming]] level, this Helmet gains: +2 [[Defense]]+4 [[Health]]+1 [[Farming Fortune]] (Holding an Axe)|
|[[Rabbit Hat]]|[[Rabbit Hat]]|UNCOMMON ([[Rarity]])|[[Speed]] +5; [[Intelligence]] +5|Grants Jump Boost IV ([[Jump Boost Potion]]) while equipped.|
|[[Happy Mask]]|[[Happy Mask]]|UNCOMMON ([[Rarity]])||(Hidden) Allowed the player to access [[Official Buildings]] when [[Dante]] was the elected mayor ([[Mayor Election]]).|
|[[Crystallized Heart]]|[[Crystallized Heart]]|RARE ([[Rarity]])|[[Health]] +50; [[Defense]] +10; [[Intelligence]] +50 [[Vitality]] +40[[Mending]] +40||
|[[Skeleton's Helmet]]|[[Skeleton's Helmet]]|RARE ([[Rarity]])|[[Defense]] +75|Ability: Bone Shield A Bone Shield will surround you, nullifying damage you take but consuming a bone in the process. Bones regenerate every 30 seconds.|
|[[Taurus Helmet]]|[[Taurus Helmet]]|RARE ([[Rarity]])|[[Crit Damage]] +20%; [[Sea Creature Chance]] +3%; [[Health]] +175; [[Defense]] +150|Damage taken from [[Magmatic]] mobs is reduced by 5% and damage dealt is increased by 1.1x.|
|[[Witch Mask]]|[[Witch Mask]]|EPIC ([[Rarity]])|[[Health]] +66; [[Defense]] +111|Ability: Bat Swarm Summons two bats ([[Bat (disambiguation)]]) that will follow you and attack nearby enemies, dealing 4,000 damage upon exploding. Your bats will not spawn on your island.|
|[[Vampire Mask]]|[[Vampire Mask]]|RARE ([[Rarity]])|[[Defense]] +111|Ability: Rejuvenate While wearing, drains 5 health per second from all monsters within 8 blocks.|
|[[Vampire Witch Mask]]|[[Vampire Witch Mask]]|EPIC ([[Rarity]])|[[Health]] +132; [[Defense]] +222|Ability: Bat Swarm Summons two bats that will follow you and attack nearby enemies, dealing 3,000 damage upon exploding. Your bats will not spawn on your island. Ability: Rejuvenate While wearing, drains 5 health per second from all monsters within 8 blocks.|
|[[Zombie's Heart]]|[[Zombie's Heart]]|RARE ([[Rarity]])|[[Health]] +50 [[Vitality]] +30[[Mending]] +30||
|[[Krampus Helmet]]|[[Krampus Helmet]]|EPIC ([[Rarity]])||Gains +1 [[Health]] per 50 [[Gifts]] given by wearer. Max 500 [[Health]] . (Also functions as a Minion Upgrade ([[Minion Upgrades]]))|
|[[Reaper Mask]]|[[Reaper Mask]]|LEGENDARY ([[Rarity]])|[[Health]] +150; [[Defense]] +100; [[Intelligence]] +100 [[Vitality]] +60[[Mending]] +60|Ability: Evil Incarnate [[Zombie Armor]] triggers on all hits. Store 2 extra necromancer souls. Summon 2 more necromancy mobs.|
|[[Revived Heart]]|[[Revived Heart]]|EPIC ([[Rarity]])|[[Health]] +100; [[Defense]] +35; [[Intelligence]] +100 [[Vitality]] +50[[Mending]] +50||
|[[Spirit Mask]]|[[Spirit Mask]]|EPIC ([[Rarity]])|[[Health]] +100; [[Defense]] +50; [[Speed]] +15; [[Intelligence]] +20|Ability: Second Wind Instead of dying, gain +50[[Speed]] and damage immunity for 3 seconds.; Cooldown: 30s|
|[[Water Hydra Head]]|[[Water Hydra Head]]|EPIC ([[Rarity]])|[[Health]] +100; [[Defense]] +100; SCC ([[Sea Creature Chance]]) +2||
|[[Crown of Greed]]|[[Crown of Greed]]|LEGENDARY ([[Rarity]])|[[Health]] +100; [[Defense]] +50|Ability: Indulgence Gain 2x Coins from Griffin Burrows and +10 [[Magic Find]] on [[Mythological]] mobs, but you take 1.25x damage from them.|
|[[Warden Helmet]]|[[Warden Helmet]]|LEGENDARY ([[Rarity]])|[[Health]] +300; [[Defense]] +100|Ability: Brute Force Halves your [[Speed]] but grants +20% base weapon damage for every 25 [[Speed]].|
|[[Pig Mask]]|[[Pig Mask]]|LEGENDARY ([[Rarity]])|[[Speed]] +1||
|[[Clover Helmet]]|[[Clover Helmet]]|LEGENDARY ([[Rarity]])|[[Magic Find]] +5%; All others: -5%||
|[[Racing Helmet]]|[[Racing Helmet]]|LEGENDARY ([[Rarity]])|[[Speed]] +400|Grants +100 Speed Cap.|
### Dungeon Helmets
These are Helmets that are not part of any armor set that only come in Dungeon variants.
|Icon|Name|Rarity|Stats|Ability|
|-|-|-|-|-|
|[[Mender Helmet]]|[[Mender Helmet]]|RARE ([[Rarity]])|[[Health]] +80|Grants +50 [[Mending]] while in [[Dungeons]].|
|[[Sniper Helmet]]|[[Sniper Helmet]]|RARE ([[Rarity]])|[[Health]] +100; [[Defense]] +10|Increases the damage your [[Arrows]] deal by 1% for every 2 blocks traveled above 20 blocks.|
|[[Dark Goggles]]|[[Dark Goggles]]|RARE ([[Rarity]])|[[Intelligence]] +150; [[Ability Damage]] +25%||
|[[Bonzo's Mask]]|[[Bonzo's Mask]]|RARE ([[Rarity]])|[[Health]] +100; [[Defense]] +100; [[Intelligence]] +100|Ability: Clownin' Around Instead of dying, gain damage immunity and +20 [[Strength]] for 3s and fully replenish your health. The cooldown and Strength bonus you receive improve based on your Dungeoneering Skill level. This ability only works while in The Catacombs!; Cooldown: 360s|
|[[Mender Fedora]]|[[Mender Fedora]]|EPIC ([[Rarity]])|[[Health]] +220|Grants +50 [[Mending]] and [[Vitality]] while in [[Dungeons]].|
|[[Shadow Goggles]]|[[Shadow Goggles]]|EPIC ([[Rarity]])|[[Intelligence]] +200; [[Ability Damage]] +35%||
|[[Mender Crown]]|[[Mender Crown]]|EPIC ([[Rarity]])|[[Health]] +270|Grants +80 [[Mending]] and [[Vitality]] while in [[Dungeons]].|
|[[Wither Goggles]]|[[Wither Goggles]]|EPIC ([[Rarity]])|[[Intelligence]] +300; [[Ability Damage]] +45%||
|[[Precursor Eye]]|Precursor ([[Precursor Eye]]) Eye ([[Precursor Eye]])|LEGENDARY ([[Rarity]])|[[Health]] +222; [[Defense]] +222; [[Intelligence]] +222|Ability: Eye Beam Fire a laser in front of you dealing 4,000 damage and costing 40 [[Mana]]. The damage increases by 100% every second for 5 seconds and the mana cost increases by 25% every second. You can sneak again to de-activate the laser. Mana is consumed on damage.|
|[[Golden Heads]]|Golden Bonzo Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +5; [[Health]] +20; [[Defense]] +10|Grants 2x stats on The Catacombs Floor I ([[The Catacombs - Floor I]]).|
|[[Diamond Heads]]|Diamond Bonzo Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +10; [[Health]] +50; [[Defense]] +20|Grants 2x stats on The Catacombs Floor I ([[The Catacombs - Floor I]]).|
|[[Golden Heads]]|Golden Scarf Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +10; [[Health]] +30; [[Defense]] +15|Grants 2x stats on The Catacombs Floor II ([[The Catacombs - Floor II]]).|
|[[Diamond Heads]]|Diamond Scarf Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +15; [[Health]] +70; [[Defense]] +30|Grants 2x stats on The Catacombs Floor II ([[The Catacombs - Floor II]]).|
|[[Golden Heads]]|Golden Professor Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +10; [[Health]] +40; [[Defense]] +20|Grants 2x stats on The Catacombs Floor III ([[The Catacombs - Floor III]]).|
|[[Diamond Heads]]|Diamond Professor Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +20; [[Health]] +100; [[Defense]] +40|Grants 2x stats on The Catacombs Floor III ([[The Catacombs - Floor III]]).|
|[[Golden Heads]]|Golden Thorn Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +15; [[Health]] +50; [[Defense]] +25|Grants 2x stats on The Catacombs Floor IV ([[The Catacombs - Floor IV]]).|
|[[Diamond Heads]]|Diamond Thorn Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +25; [[Health]] +130; [[Defense]] +50|Grants 2x stats on The Catacombs Floor IV ([[The Catacombs - Floor IV]]).|
|[[Golden Heads]]|Golden Livid Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +15; [[Health]] +60; [[Defense]] +30|Grants 2x stats on The Catacombs Floor V ([[The Catacombs - Floor V]]).|
|[[Diamond Heads]]|Diamond Livid Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +30; [[Health]] +160; [[Defense]] +60|Grants 2x stats on The Catacombs Floor V ([[The Catacombs - Floor V]]).|
|[[Golden Heads]]|Golden Sadan Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +15; [[Health]] +70; [[Defense]] +35|Grants 2x stats on The Catacombs Floor VI ([[The Catacombs - Floor VI]]).|
|[[Diamond Heads]]|Diamond Sadan Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +35; [[Health]] +190; [[Defense]] +70|Grants 2x stats on The Catacombs Floor VI ([[The Catacombs - Floor VI]]).|
|[[Golden Heads]]|Golden Necron Head ([[Golden Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +15; [[Health]] +80; [[Defense]] +40|Grants 2x stats on The Catacombs Floor VII ([[The Catacombs - Floor VII]]).|
|[[Diamond Heads]]|Diamond Necron Head ([[Diamond Heads]])|SPECIAL ([[Rarity]])|[[Strength]] +40; [[Health]] +220; [[Defense]] +80|Grants 2x stats on The Catacombs Floor VII ([[The Catacombs - Floor VII]]).|
### Rift Helmets
These are Helmets that are not part of any armor set that can only be accessed in [[Rift Dimension|The Rift]].
|Icon|Name|Rarity|Stats|Ability|
|-|-|-|-|-|
|[[Not-Dead-Gehog Mask]]|[[Not-Dead-Gehog Mask]]|UNCOMMON ([[Rarity]])|[[Rift Time]] +30s; [[Intelligence]] +15|Ability: Helmets All The Way Up Regain +1 [[Rift Time]] when killing a monster.|
|[[Agaricus Cap Cap]]|[[Agaricus Cap Cap]]|RARE ([[Rarity]])|[[Rift Time]] +50s; [[Intelligence]] +15|Ability: Helmets All The Way Down Regain +2 [[Rift Time]] when killing a monster.|
|[[Used Detransfigured Face]]|[[Used Detransfigured Face]]|EPIC ([[Rarity]])|[[Rift Time]] +80s; [[Intelligence]] +20|Ability: Faces All The Way Down Regain +2 [[Rift Time]] when killing a monster.|
|[[Anti-Bite Scarf]]|[[Anti-Bite Scarf]]|LEGENDARY ([[Rarity]])|[[Rift Time]] +100s; [[Hearts]] +1; [[Intelligence]] +20|Ability: Helmets All The Way Around Regain +2 [[Rift Time]] when killing a monster.; If you would take [[Hearts]] damage, take 0.3 [[Hearts]] less.|
|[[Anti-Bite Scarf]]|[[Anti-Bite Scarf]]|MYTHIC ([[Rarity]])|[[Rift Time]] +110s; [[Hearts]] +1; [[Intelligence]] +22|Ability: Helmets All The Way Around Regain +2 [[Rift Time]] when killing a monster. If you would take [[Hearts]] damage, take 0.5 [[Hearts]] less.; Hold and left-click to pick color!|
|[[Warm Wizard Face]]|[[Warm Wizard Face]]|LEGENDARY ([[Rarity]])|[[Rift Time]] +130s [[Hearts]] +1 [[Intelligence]] +26|Ability: Wizards All The Way Around Regain +2 [[Rift Time]] when killing a monster.; If you would take [[Hearts]] damage, take 0.3 [[Hearts]] less.|
|[[Warmer Wizard Face]]|[[Warmer Wizard Face]]|MYTHIC ([[Rarity]])|[[Rift Time]] +130s [[Hearts]] +1 [[Intelligence]] +26|Ability: Wizards All The Way Around Regain +2 [[Rift Time]] when killing a monster. If you would take [[Hearts]] damage, take 0.5 [[Hearts]] less.; Hold and left-click to pick color!|
### Armor Sets
Helmets are also a part of the following armor sets: Show/Hide List
- [[5th Anniversary Balloon Hat]]
- [[6th Anniversary Balloon Hat]]
- [[7th Anniversary Cake Hat]]
- [[Abyssal Armor]]
- [[Adaptive Armor]]
- [[Admin's Warm Sweater]]
- [[Agaricus Cap Cap]]
- [[Angler Armor]]
- [[Anti-Bite Scarf]]
- [[Arachne's Armor]]
- [[Armadillo Mask]]
- [[Armor & Equipment]]
- [[Armor of Divan]]
- [[Armor of Growth]]
- [[Armor of Magma]]
- [[Armor of the Pack]]
- [[Armor of the Rising Sun]]
- [[Armor of the Stars]]
- [[Aurora Armor]]
- [[Backwater Armor]]
- [[Bat Person Armor]]
- [[Bee Mask]]
- [[Berserker Armor]]
- [[Biohazard Armor]]
- [[Blaze Armor]]
- [[Bouncy Armor]]
- [[Bronze Hunter Armor]]
- [[Burned Pants]]
- [[Cactus Armor]]
- [[Canopy Armor]]
- [[Celeste Armor]]
- [[Chainmail Armor]]
- [[Challenger's Armor]]
- [[Charlie's Trousers]]
- [[Chicken Leggs]]
- [[Crimson Armor]]
- [[Cropie Armor]]
- [[Crown of Avarice]]
- [[Crypt Witherlord Armor]]
- [[Crystal Armor]]
- [[Diamond Armor]]
- [[Diamond Heads]]
- [[Diamond Hunter Armor]]
- [[Diver's Armor]]
- [[Dragon Armor]]
- [[Eleanor's Armor]]
- [[Ember Armor]]
- [[Ember Ash Armor]]
- [[Emerald Armor]]
- [[Ender Armor]]
- [[Equipment Menu]]
- [[Estranged Taikan Mask]]
- [[EtalptsehC norI]]
- [[Exceedingly Comfy Sneakers]]
- [[Exotics]]
- [[Fairy Armor]]
- [[Farmhand Armor]]
- [[Fermento Armor]]
- [[Fervor Armor]]
- [[Fig Armor]]
- [[Final Destination Armor]]
- [[Flamebreaker Armor]]
- [[Frog Mask]]
- [[Frozen Blaze Armor]]
- [[Ghast Armor]]
- [[Glacite Armor]]
- [[Glossy Mineral Armor]]
- [[Goblin Armor]]
- [[Gold Hunter Armor]]
- [[Golden Armor]]
- [[Golden Heads]]
- [[Goldor's Armor]]
- [[Golem Armor]]
- [[Great Spook Armor]]
- [[Gunther's Sneakers]]
- [[Hardened Diamond Armor]]
- [[Haymaker Armor]]
- [[Head of Betrayal]]
- [[Heat Armor]]
- [[Heavy Armor]]
- [[Helianthus Armor]]
- [[Helix Armor]]
- [[Hollow Armor]]
- [[Holy Dragon Armor]]
- [[Iron Armor]]
- [[Kalhuiki Mask]]
- [[Kelly's T-Shirt]]
- [[Kuudra Follower Armor]]
- [[Lapis Armor]]
- [[Lava Sea Creature Armor]]
- [[Leaflet Armor]]
- [[Leather Armor]]
- [[Magma Lord Armor]]
- [[Magmafish Hat]]
- [[Mastiff Armor]]
- [[Maxor's Armor]]
- [[Melody's Shoes]]
- [[Mercenary Armor]]
- [[Miner Armor]]
- [[Mineral Armor]]
- [[Mole Hat]]
- [[Monster Hunter Armor]]
- [[Monster Raider Armor]]
- [[Mushroom Armor]]
- [[Mythos Armor]]
- [[Necromancer Lord Armor]]
- [[Necron's Armor]]
- [[Not-Dead-Gehog Mask]]
- [[Nutcracker Armor]]
- [[Old Dragon Armor]]
- [[Park Armor]]
- [[Parrot Mask]]
- [[Party Top Hat]]
- [[Perfect Armor]]
- [[Pig Mask]]
- [[Primal Dragon Armor]]
- [[Primordial Armor]]
- [[Prospecting Armor]]
- [[Protector Dragon Armor]]
- [[Rabbit Armor]]
- [[Rampart Armor]]
- [[Rekindled Ember Armor]]
- [[Retro-Encabulating Visor]]
- [[Revenant Armor]]
- [[Rosetta's Armor]]
- [[Rotten Armor]]
- [[Salmon Armor]]
- [[Salmon Mask]]
- [[Secret Armor Sets]]
- [[Seymour's Special Armor]]
- [[Shadow Assassin Armor]]
- [[Shark Scale Armor]]
- [[Shimmering Light Armor]]
- [[Silver Hunter Armor]]
- [[Skeleton Grunt Armor]]
- [[Skeleton Lord Armor]]
- [[Skeleton Master Armor]]
- [[Skeleton Soldier Armor]]
- [[Skeletor Armor]]
- [[Sloth Hat of Celebration]]
- [[Snake-in-a-Boot]]
- [[Snorkeling Armor]]
- [[Snow Suit Armor]]
- [[Snowman Mask]]
- [[Sorrow Armor]]
- [[Speedster Armor]]
- [[Sponge Armor]]
- [[Spooky Armor]]
- [[Sprout Armor]]
- [[Squash Armor]]
- [[Squire Armor]]
- [[Starlight Armor]]
- [[Storm's Armor]]
- [[Strong Dragon Armor]]
- [[Sunflower Head]]
- [[Super Heavy Armor]]
- [[Superior Dragon Armor]]
- [[Tarantula Armor]]
- [[Tater Armor]]
- [[Terror Armor]]
- [[Thermodynamic Armor]]
- [[Thunder Armor]]
- [[Titan's Armor]]
- [[Tropical Fish Hat]]
- [[Unstable Dragon Armor]]
- [[Used Detransfigured Face]]
- [[Vanguard Armor]]
- [[W Logo]]
- [[Warm Wizard Face]]
- [[Warmer Wizard Face]]
- [[Werewolf Armor]]
- [[Wise Dragon Armor]]
- [[Wither Armor]]
- [[Wizard Face]]
- [[Wyld Armor]]
- [[Yog Armor]]
- [[Young Dragon Armor]]
- [[Zombie Armor]]
- [[Zombie Commander Armor]]
- [[Zombie Knight Armor]]
- [[Zombie Lord Armor]]
- [[Zombie Mask]]
- [[Zombie Soldier Armor]]
## Skins
Helmet Skins are cosmetic items that are able to be applied to [[Helmets]] to change their appearance. They can be purchased from [[Fire Sale|Fire Sales]] for [[SkyBlock Gems]].
A Helmet Skin can be added on a [[Helmets|Helmet]] by combining the desired Skin with a compatible Helmet in an [[Anvil]].
## History
[[SkyBlock Prototype]]:
|Jun 11, 2019|0.1|Added Helmet.|
Linked from: [[Ability Damage]], [[Absorption]], [[Agaricus Cap Cap]], [[Anti-Bite Scarf]], [[Anubis]], [[Aqua Affinity]], [[Arenjey God]], [[Armor]], [[Armor & Equipment]], [[Armor/Sets]], [[Auction House]], [[Autocap]], [[Big Brain]], [[Blaze Hat]], [[Blobfish Hat]], [[Bonzo's Mask]], [[Boss (helmet)]], [[Chainmail Armor]], [[Chicken (disambiguation)]], [[Chicken Hat]], [[Clover Helmet]], [[Clover Helmet/Alpha]], [[Cold Resistance]], [[Combat Wisdom]], [[Cow Hat]], [[Creeper Hat]], [[Crown of Avarice]], [[Crown of Greed]], [[Crystallized Heart]], [[Diamond]], [[Diamond Armor]], [[Diamond Froggles]], [[Diamond Heads]], [[Dwarf Turtle Shelmet]], [[Emperor Head]], [[Enderman Mask]], [[Estranged Taikan Mask]], [[Eye (disambiguation)]], [[Fallen Star Helmet]], [[Fancy Tuxedo]] (+118 more)

# Item Status
Categories: Confirmations needed, Glitches, Items, Blacklisted Items
Item Status is the state of an item in Hypixel SkyBlock. The most well-known versions are Safe, Blacklisted, and Neutral. These determine how the item reacts when changing servers, being held, and being dropped.
Menu Glass
## Safe Items
Safe items are the most abundant types of items. These items can be dropped, held, and can be moved between servers safely. Some items, like the [[Dwarven Tankard]], can even be placed! Safe items can become [[Blacklisted Items|Blacklisted]] when two of the same type of item have the same UUID.
## Neutral Items
Neutral Items are items that can be moved between servers, but cannot be swapped to in your hotbar or dropped as they will revert. Having an outdated item when opening an npc shop will also cause it to revert. Neutral items can be moved with your mouse cursor, and stored in chests, other vanilla containers, and all furniture containers and item frames.
They are commonly found in the form of GUI items stolen from menus, or other glitched items such as [[Glitched Items|Coin Heads]].
There are also miscellaneous forms of neutral items, such as the [[Arrows|Weaponsmith Arrows]], which when taken out of the quiver, if dropped, can't be recovered if the player has the quiver unlocked. Other items, like the [[Spirit Bow]], will 'disintegrate' when dropped, removing it permanently.
## Blacklisted Items
[[Blacklisted Items]] are a small group of items that were likely never intended to exist. These items get removed on a timer, making it difficult to move them around or store them safely.
The timer that removes these items seems to check your inventory, wardrobe, ender chest, backpacks, island chests, and armor every 2 minutes. An easy way to tell when the timer is going to activate is to put some common blacklisted item, such as menu glass, armor stands, or barriers, and when they blacklist you are safe to move around other blacklisted items for a short amount of time.
There seems to be an extra blacklist tick right after joining a server, making it more difficult to move these items. Items with the same SkyBlock id that also have the same UUID will be blacklisted as well, on a different, shorter timer. [Confirm (Confirmation needed; When this info is confirmed, remove this.)]
Blacklisted Items can likely be held, dropped, and moved between servers safely, assuming they don't get removed by the blacklist timer. Items can be blacklisted as well as outdated/neutral. Some examples of this are menu glass and anvil barriers, which are both blacklisted and neutral. Banners are an example of a blacklisted and outdated item.
## Negative Items
Negative Items are items with a count less than one. These items are limited by both Minecraft's restrictions as well as Hypixel's. These items can not be picked up directly. Instead, you need to use indirect methods to move them around, such as double-clicking on another of the same item, or using hotkeys. These items revert to a stack of 1 if on your head slot, as well as in your inventory [Confirm], your enderchest, and your backpacks.
They now blacklist in all vanilla containers, reverting to a stack of 1. Custom containers often have trouble with them, and they can't be placed in item frames. They also don't blacklist in wardrobe slots, which are the only currently safe places to store them.
They can be safely traded by just clicking on them however, and if you are quick enough you can transfer these items to other accounts.
## Outdated Items
Arguably the most strict of all the item statuses, outdated items will revert/be removed when swapping servers, when being held, and when being dropped. Some examples of outdated items are items whos name/lore has changed through an update, or items that are more dangerous such as banners.
The [[Sinful Dice]] is constantly outdated, and whenever it updates it changes its skin. Moving servers changes it, as well as holding it and dropping it.
Items like the [[Redstone Key]] and the [[Spirit Bow]] (from [[Thorn]]'s bossfight) are also outdated, but not in the normal way. Instead, these items delete only when swapping servers, as they have the NBT tag "dontSaveToProfile:1b" that deletes them.
## History
[[SkyBlock Prototype]]:
|Jun 11, 2019|0.1|Added Item Status.|

# Lassos
Aliases: Lasso, Lassoes
Categories: Confirmations needed, Tools
[Lassos]
Lassos are a type of [[Hunting]] tool. They can be used in [[Hunting|Forest Hunts]] to catch forest creatures.
## Lassos
|Slot|Name|Rarity|Source|
|-|-|-|-|
|[[Abysmal Lasso]]|[[Abysmal Lasso]]|COMMON ([[Rarity]])|[[Auryon]]; Vinesap I (1) ([[Vinesap]])|
|[[Vinerip Lasso]]|[[Vinerip Lasso]]|UNCOMMON ([[Rarity]])|Vinesap II (2) ([[Vinesap]])|
|[[Entangler Lasso]]|[[Entangler Lasso]]|RARE ([[Rarity]])|Vinesap IV (4) ([[Vinesap]])|
|[[Everstretch Lasso]]|[[Everstretch Lasso]]|EPIC ([[Rarity]])|Vinesap VI (6) ([[Vinesap]])|
## Usage
A Lasso can be thrown at forest creatures to catch them. While attached, a stamina bar appears over the mob's head. When the bar reaches 20%[Confirm (Confirmation needed; When this info is confirmed, remove this.)], a prompt to reel appears. Right-clicking depletes the stamina bar and pulls the mob in. If the mob has multiple layers to its stamina bar, it instead removes 1 layer and needs to have the process repeated again.
A Lasso can detach from a mob by reeling in too early, looking away, or not reeling in time. This allows the mob to regenerate its stamina.
## Tips
- The [[Attributes|Hunter's Suppress]] [[Attributes|Attribute]] causes the stamina of [[Mob|Mobs]] to deplete faster. This can be increased with [[Attributes|Echo of Hunter]] and [[Attributes|Echo of Echoes]] to a total of +26%.
## History
[[Alpha Hypixel Network]]:
|Jun 5, 2025|Added Lassos.|
[SkyBlock Prototype]
|Jun 23, 2025|0.23|Added Lassos.|
Linked from: [[Abysmal Lasso]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Alchemy]], [[Attributes/List/Combat]], [[Attributes/List/Common]], [[Attributes/List/Epic]], [[Attributes/List/Farming]], [[Attributes/List/Fishing]], [[Attributes/List/Foraging]], [[Attributes/List/Global]], [[Attributes/List/Legendary]], [[Attributes/List/Mining]], [[Attributes/List/Rare]], [[Attributes/List/Uncommon]], [[Attributes/Search]], [[Auryon]], [[Beeheemoth]], [[Beeheemoth Shard]], [[Beetle]], [[Beetle Shard]], [[Behemoth Pot of Honeycomb]], [[Birries]], [[Birries Shard]], [[Blue Jay]], [[Blue Jay Shard]], [[Bunbun]], [[Bunbun Shard]], [[Chapters]], [[Chapters/Torrhus Canyon]], [[Charm Chance]], [[Cheesebite]], [[Cinderbat]], [[Cinderbat Shard]], [[Coralot]], [[Coralot Shard]], [[Cricket]], [[Cricket Shard]], [[Critter Safari]], [[Critters]] (+100 more)

# Loadouts
Aliases: Loadout
Categories: Confirmations needed
[Loadouts]
Loadouts are a system that allow the player to customize their builds. It includes the functionality to swap between one's equipped [[Armor]], [[Equipment]], summoned [[Pets]], [[Heart of the Mountain|HotM]] and [[Heart of the Forest|HotF]] trees, and selected [[Accessory Power]] and [[Maxwell|Tuning Points]] distribution. It can be accessed via /loadout, /loadouts, and /ld.
## Overview
Players can customize their Loadouts to match the playstyle they desire. This includes their:
- [[Wardrobe|Armor Wardrobe]] Slot ([[Helmets|Helmet]], [[Chestplates|Chestplate]], [[Leggings]], [[Boots]])
- [[Equipment Wardrobe]] Slot ([[Necklaces|Necklace]], [[Cloaks|Cloak]], [[Belts|Belt]], [[Gloves]]/[[Bracelets|Bracelet]])
- [[Pets|Pet]]
- [[Heart of the Mountain]] Tree
- [[Heart of the Forest]] Tree
- [[Power Stones|Power Stone]]
- [[Maxwell|Tuning Template]]
There is a 10m cooldown between swapping [[Heart of the Mountain|HotM]] and [[Heart of the Forest|HotF]] trees. This cooldown does not apply to any other items affected by swapping a Loadout: however, if the player selects a Loadout that changes their HotM tree, the cooldown will still apply.[Confirm (Confirmation needed; When this info is confirmed, remove this.)]
Amount of Loadout Slots unlocked depends on the player's [[Ranks|Rank]].
|Rank|Slots|
|-|-|
|1Default ([[Ranks]])|4|
|2[VIP] ([[Ranks]])|6|
|3[VIP+] ([[Ranks]])|10|
|4[MVP] ([[Ranks]])|14|
|5[MVP+] ([[Ranks]])|18|
Loadout Slots can also be upgraded by [[Elizabeth]] at the [[Community Center]]:
|Slots|Cost|Cumulative Cost|Duration|
|-|-|-|-|
|+1|500 [[SkyBlock Gems]]|500 [[SkyBlock Gems]]|6 days|
|+2|500 [[SkyBlock Gems]]|1,000 [[SkyBlock Gems]]|6 days|
|+3|500 [[SkyBlock Gems]]|1,500 [[SkyBlock Gems]]|6 days|
|+4|500 [[SkyBlock Gems]]|2,000 [[SkyBlock Gems]]|6 days|
|+5|500 [[SkyBlock Gems]]|2,500 [[SkyBlock Gems]]|6 days|
|+6|500 [[SkyBlock Gems]]|3,000 [[SkyBlock Gems]]|6 days|
|+7|500 [[SkyBlock Gems]]|3,500 [[SkyBlock Gems]]|6 days|
|+8|500 [[SkyBlock Gems]]|4,000 [[SkyBlock Gems]]|6 days|
|+9|500 [[SkyBlock Gems]]|4,500 [[SkyBlock Gems]]|6 days|
## Trivia
- A Loadout cannot be renamed to null.
## History
[[Alpha Hypixel Network]]:
|Jun 24, 2026|Added Loadouts.|
|Jun 24, 2026|Removed the 30s cooldown on swapping Loadouts. The cooldown remains on swapping HotM and HotF trees.|
[SkyBlock Prototype]
|Jul 8, 2026|0.26|Added Loadouts.|
|Oct 14, 2026|Fixed favorite Fishing Bait ([[Bait]]) resetting when switching Loadouts.|
Linked from: [[Account & Profile Upgrades]], [[Armor]], [[Armor & Equipment]], [[Bait]], [[Changelog]], [[Equipment]], [[Equipment Wardrobe]], [[Garden Visitors]], [[Minister Election]], [[Ranks]], [[Wardrobe]]

# Magic Find
Categories: Confirmations needed, Player Statistics, Outdated pages, Magic Find, Mechanics
[Magic Find]
Type: Stat
Uses: Increasing the drop rate of most items from mobs.
Increasing: [[God Potion]], [[Booster Cookie]], [[Enrichments]], [[Pets]], [[Armor]], Reforges ([[Reforging]]), [[Enchantments]], and More
[Values]
Base Value: 0
Max Value: 900
[Symbol]
Symbol: ✯
Unicode Code Point: U+272F
Icon (The icon displayed in the Equipment Menu interface.): Stick ()
Magic Find (MF) is one of the core player statistics. It is a [[Stats|Stat]] that affects the drop chance of obtaining rare drops from monsters and bosses.
## Mechanics
Magic Find increases the chance to loot rare drops from enemies, provided their Base Chance is strictly below 5% after [[Looting]] is applied.
- If the drop is not a [[Pets|Pet]], then the following formula is used: Chance=BaseChance×(1+Magic Find100)
- If the drop is a [[Pets|Pet]], then the following formula is used instead: Chance=BaseChance×(1+Magic Find+Pet Luck100)
When a rare item is dropped, the amount of Magic Find the player currently has is displayed at the end of the drop message, accompanied by a sound cue. This can be toggled with the /togglerds command.
## Increasing Base Magic Find
Players have 0 Magic Find by default.
## Increasing Bonus Magic Find
### Pets
Certain [[Pets]] grant Magic Find. The [[Pets|Pet]] must be equipped in order to take effect.
|Icon|Item|Rarity|Type|Magic Find|
|-|-|-|-|-|
|[[Golden Dragon Pet]]|[[Golden Dragon Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|+5.05➡10 Shining Scales: Grants +2.2 for each digit in [[Gold Ingot]] collection. (up to +20 )|
|[[Ender Dragon Pet]]|[[Ender Dragon Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Superior: Increases Magic Find by +0.1➡10%.|
|[[Black Cat Pet]]|[[Black Cat Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|Supernatural: Grants +0.15➡15 Magic Find|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|MYTHIC ([[Rarity]])|Mining Pet ([[Pets]])|Refined Senses: Grants +0.1-10% Magic Find while on [[Mining Islands]].|
|[[Blaze Pet]]|[[Blaze Pet]]|COMMON ([[Rarity]])-LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Nether Embodiment Increases Magic Find by +0.05➡10% (based on rarity) while on the [[Crimson Isle]].|
|[[Megalodon Pet]]|[[Megalodon Pet]]|EPIC ([[Rarity]]) and LEGENDARY ([[Rarity]])|Fishing Pet ([[Pets]])|+0.1➡10 Enhancer Scales: Doubles the pet's base stats during the [[Fishing Festival]].|
|[[Griffin Pet]]; [[Griffin Pet]]|[[Griffin Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|King of Kings: Grants +0.2➡20 Magic Find on [[Mythological]] mobs.|
|[[Spider Pet]] [[Tarantula Pet]]|[[Spider Pet]][[Tarantula Pet]]|MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|Web Battlefield: Killing mobs grants +0.01➡1 Magic Find for 40s to all players staying within 20 blocks of where they died. (stacks up to 10 times)|
|[[Grandma Wolf Pet]]|[[Grandma Wolf Pet]]|COMMON ([[Rarity]]) to LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|+0.1➡9% depending on the [[Rarity]] and kill combo This buff is unique since it's the only multiplier that also affects Bestiary Magic Find ([[Bestiary]])|
|[[Rat Pet]]|[[Rat Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Morph ([[Pets]])|Rat's Blessing: Has a chance to grant a random player (other than yourself) +2.05➡7 for 20.4➡60 seconds after finding a yummy piece of Cheese!|
|[[Goblin Pet]]|[[Goblin Pet]]|LEGENDARY ([[Rarity]])|Mining Pet ([[Pets]])|+0.07➡7|
|[[Mole Pet]]|[[Mole Pet]]|LEGENDARY ([[Rarity]])|Mining Pet ([[Pets]])|+0.05➡5|
|[[Mammoth Pet]]|[[Mammoth Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Tusk Luck: Gain +0.005➡0.5 for every 100 [[Mining Fortune]], doubled in the [[Glacite Tunnels]] and [[Glacite Mineshafts]]|
|[[Baby Yeti Pet]]; [[Baby Yeti Pet]]|[[Baby Yeti Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Fishing Pet ([[Pets]])|Frosty Familiarity: Grants +0.1➡10 Magic Find against Winter Sea Creatures.|
|[[Jade Dragon Pet]]|[[Jade Dragon Pet]]|LEGENDARY ([[Rarity]])|Foraging Pet ([[Pets]])|+5.05➡10|
### Pet Items
Certain [[Pet Items]] grant Magic Find. The [[Pet Items|Pet Item]] must be equipped on the player's active [[Pets|Pet]] to take effect.
|Slot|Name|Rarity|Magic Find|Source|
|-|-|-|-|-|
|[[Minos Relic]]|[[Minos Relic]]|EPIC ([[Rarity]])|Increases all pet stats by 33.3%.|Drop from [[Minos Champion]] (requires LEGENDARY ([[Rarity]]) [[Griffin Pet]])|
|[[Hephaestus Relic]]|[[Hephaestus Relic]]|LEGENDARY ([[Rarity]])|Increases all pet stats by 50%.|Recipe: [[Minos Relic]] ×3 + [[Hephaestus Anvil]] → [[Hephaestus Relic]]|
|[[Four-Eyed Fish]]|[[Four-Eyed Fish]]|EPIC ([[Rarity]])|+13 to [[Griffin Pet]]|Recipe: [[Enchanted Spider Eye]] x64 ×6 + [[Lucky Clover]] + [[Pre-Digestion Fish]] + [[Reinforced Scales]] → [[Four-Eyed Fish]]|
|[[Lucky Clover]]|[[Lucky Clover]]|EPIC ([[Rarity]])|+7|Recipe: [[Enchanted Emerald]] x32 ×8 + [[Lucky Clover Core]] → [[Lucky Clover]]|
|[[Poignant Lucky Clover]]|[[Poignant Lucky Clover]]|LEGENDARY ([[Rarity]])|+13|[[Carrot King Avatar]]|
|[[Grandma's Knitting Needle]]|[[Grandma's Knitting Needle]]|RARE ([[Rarity]])|+5% at 50+ combo to [[Grandma Wolf Pet]]|[[Oruo The Almighty]]: 50 [[Sun Gecko Essence]]|
|Icon|Item|Rarity|Type|Magic Find|
|-|-|-|-|-|
|[[Sword of Revelations]]|[[Sword of Revelations]]|EPIC ([[Rarity]])|Weapon ([[Weapons]])|Grants +5 Magic Find on [[Mythological]] mobs.|
|[[Daedalus Blade]]|[[Daedalus Blade]]|LEGENDARY ([[Rarity]])|Weapon ([[Weapons]])|Grants +0.2 (+0.3 when upgraded) on [[Mythological]] mobs per [[Bestiary]] tier you have across all of them. (max +69 )|
|Icon|Item|Rarity|Type|Magic Find|
|-|-|-|-|-|
|[[Superior Dragon Armor]]; [[Superior Dragon Armor]]; [[Superior Dragon Armor]]; [[Superior Dragon Armor]]|[[Superior Dragon Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5% set bonus|
|[[Sorrow Armor]]; [[Sorrow Armor]]; [[Sorrow Armor]]; [[Sorrow Armor]]|[[Sorrow Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5 per piece (Max is +20 )|
|[[Nutcracker Armor]]; [[Nutcracker Armor]]; [[Nutcracker Armor]]; [[Nutcracker Armor]]|[[Nutcracker Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|Full Set Bonus: Battalion:; +1 to everyone within 30 blocks (stacks up to 5 times)|
|[[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Necklace]]|[[Magma Lord Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+20 (4 Pieces)➜30 (5 Pieces) on [[Magmatic]] mobs.|
|[[Mythos Armor]]; [[Mythos Armor]]; [[Mythos Armor]]; [[Mythos Armor]]|[[Mythos Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+10 (2 Pieces)➜15 (3 Pieces)➜20 on [[Mythological]] mobs.|
|[[Crown of Greed]]|[[Crown of Greed]]|LEGENDARY ([[Rarity]])|[[Armor]]|+10 on [[Mythological]] mobs|
|[[Crown of Avarice]]|[[Crown of Avarice]]|LEGENDARY ([[Rarity]])|[[Armor]]|+2.5 to 25 against [[Mythological]] mobs|
|[[Clover Helmet]]|[[Clover Helmet]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5%|
|[[Crab Hat of Celebration]]; [[Sloth Hat of Celebration]]; [[5th Anniversary Balloon Hat]]/[[6th Anniversary Balloon Hat]]; [[7th Anniversary Cake Hat]]|[[Crab Hat of Celebration]]; or; [[Sloth Hat of Celebration]]; or; Anniversary Balloon Hat ([[5th Anniversary Balloon Hat]]); or; [[7th Anniversary Cake Hat]]|SPECIAL ([[Rarity]])|Hatcessory ([[Hatcessories]])|+1|
|Icon|Item|Rarity|Type|Magic Find|
|-|-|-|-|-|
|[[Delirium Necklace]]|[[Delirium Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+1 , up to +1.2 when starred ([[Star Upgrades]]).|
|[[Shriveled Bracelet]]|[[Shriveled Bracelet]]|EPIC ([[Rarity]])|Glove ([[Gloves]])|Grants +10 Magic Find on [[Arthropod]] mobs.|
|[[Rift Necklace]]|[[Rift Necklace]]|LEGENDARY ([[Rarity]])|Necklace ([[Necklaces]])|+1 to +8 , depending on the number of [[Rift Timecharms]].|
|[[Destruction Cloak]]|[[Destruction Cloak]]|EPIC ([[Rarity]])|Cloak ([[Cloaks]])|+1|
|[[Annihilation Cloak]]|[[Annihilation Cloak]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+2|
|[[David's Cloak]]|[[David's Cloak]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+2|
|[[Golden Fleece]]|[[Golden Fleece]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+5 on [[Mythological]] mobs.|
|Icon|Item|Rarity|Type|Magic Find|
|-|-|-|-|-|
|[[Pulse Ring]]|[[Pulse Ring]]|UNCOMMON ([[Rarity]]) to LEGENDARY ([[Rarity]])|Accessory ([[Accessories]])|+0.25 +0.5 +0.75 +1|
|[[Crab Hat of Celebration]]; [[Sloth Hat of Celebration]]; [[5th Anniversary Balloon Hat]]/[[6th Anniversary Balloon Hat]]; [[7th Anniversary Cake Hat]]|[[Crab Hat of Celebration]]; or; [[Sloth Hat of Celebration]]; or; Anniversary Balloon Hat ([[5th Anniversary Balloon Hat]]); or; [[7th Anniversary Cake Hat]]|SPECIAL ([[Rarity]])|Hatcessory ([[Hatcessories]])|+1 , only one Hatcessory ([[Hatcessories]]) gives Magic Find while in accessory bag.|
|[[Anguish Talisman]]|[[Anguish Talisman]]|RARE ([[Rarity]])|Accessory ([[Accessories]])|+1 Magic Find|
|[[Anguish Ring]]|[[Anguish Ring]]|EPIC ([[Rarity]])|Accessory ([[Accessories]])|+2 Magic Find|
|[[Anguish Artifact]]|[[Anguish Artifact]]|LEGENDARY ([[Rarity]])|Accessory ([[Accessories]])|+3 Magic Find|
|Icon|Item|Tier|Type|Magic Find|
|-|-|-|-|-|
|[[Magic Find Potion]]|[[Magic Find Potion]]|I|Potion ([[Potions]])|+10|
|[[Magic Find Potion]]|[[Magic Find Potion]]|II|Potion ([[Potions]])|+25|
|[[Magic Find Potion]]|[[Magic Find Potion]]|III|Potion ([[Potions]])|+50|
|[[Magic Find Potion]]|[[Magic Find Potion]]|IV|Potion ([[Potions]])|+75|
|[[Slayer© Energy Drink]]|[[Slayer© Energy Drink]]|[[Slayer© Energy Drink]]|Brew ([[Brews]])|+10 to Critical Potions ([[Critical Potion]]) brewed with this|
|[[Jerry Candy]]|[[Jerry Candy]]|[[Jerry Candy]]|Consumable|+3|
|[[God Potion]]|[[God Potion]]|[[God Potion]]|Consumable|+88 from [[Magic Find Potion]], [[Critical Potion]] with [[Slayer© Energy Drink]] and from [[Jerry Candy]]|
|[[Wolf Fur Mixin]]|[[Wolf Fur Mixin]]|[[Wolf Fur Mixin]]|Mixin ([[Mixins]])|+7 when a mob is killed in one hit|
|[[Celestial Mason Jar]]|[[Celestial Mason Jar]]|[[Celestial Mason Jar]]|Mixin ([[Mixins]])|+3|
|[[Booster Cookie]]|[[Booster Cookie]]|[[Booster Cookie]]|Consumable|+15|
|[[Extremely Real Shuriken]]|[[Extremely Real Shuriken]]|[[Extremely Real Shuriken]]|Consumable|+5% to tagged mob|
|Icon|Item|Type|Magic Find|
|-|-|-|-|
|[[Dragon Horn]]|[[Dragon Horn]] (Renowned)|Reforge Stone ([[Reforge Stones]])|+1%|
|[[Entropy Suppressor]]|[[Entropy Suppressor]] (Coldfused)|Reforge Stone ([[Reforge Stones]])|+2 applicable only to the 6 Blaze Slayer ([[Inferno Demonlord]])-specific Daggers ([[Sword Types]])|
|[[Divine Gift]]|[[Divine Gift]]|Enchantment ([[Enchantments]])|+2➡6|
|[[Chimera]]|[[Chimera]]|Enchantment ([[Enchantments]])|Copies 20%➡100% of your active pet stats, including Magic Find|
|[[Legion]]|[[Legion]]|Enchantment ([[Enchantments]])|+0.07➡0.35% for each player within 30 blocks, up to +1.4➡7% on a single piece and up to +5.6➡28% on a full armor set|
|[[Habanero Tactics]]|[[Habanero Tactics]]|Enchantment ([[Enchantments]])|+10➡15 on slayer weapons while Smoldering Polarization ([[Re-heated Gummy Polar Bear]]) is active on a single piece and +40➡60 on a full armor set|
|[[Bobbin' Time]]|[[Bobbin' Time]]|Enchantment ([[Enchantments]])|+0.6➡1% for each fishing bobber within 30 blocks up to +3➡5% on a single piece and up to +12➡20% on a full armor set|
|[[Enrichments]]|Magic Find Enrichment ([[Enrichments]])|[[Enrichments]]|+0.5 per each enriched Accessory ([[Accessories]]) Can only be applied to all LEGENDARY ([[Rarity]]), MYTHIC ([[Rarity]]), SPECIAL ([[Rarity]]) and VERY SPECIAL ([[Rarity]]) accessories (except [[Hocus-Pocus Cipher]]), totalling at 65 accessories, granting a total of 32.5 Magic Find [Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
#### Attributes
Certain [[Attributes]] can be syphoned to grant Magic Find.
|Slot|Name|Rarity||
|-|-|-|-|
|[[Drowned Shard]]|[[Drowned Shard]] Undead Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against Undead ([[Undead (Mob Type)]]) mobs|
|[[Wild Hog Shard]]|[[Wild Hog Shard]] Animal Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Animal]] mobs|
|[[Hewver Shard]]|[[Hewver Shard]] Critter Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against Critter ([[Critters]]) mobs|
|[[Lava Flame Shard]]|[[Lava Flame Shard]] Magmatic Fortune ([[Attributes]])|RARE ([[Rarity]])|+1-10 against [[Magmatic]] mobs|
|[[Wiki Tiki Shard]]|[[Wiki Tiki Shard]] Construct Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Construct]] mobs|
|[[Minotaur Shard]]|[[Minotaur Shard]] Mythological Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Mythological]] mobs|
|[[Hivethief Shard]]|[[Hivethief Shard]] Cubic Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against Cubic ([[Cubic (Mob Type)]]) mobs|
|[[Parakeet Shard]]|[[Parakeet Shard]] Flying Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Airborne]] mobs|
|[[Hideyho Shard]]|[[Hideyho Shard]] Elusive Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Elusive]] mobs|
|[[Chuckwalla Shard]]|[[Chuckwalla Shard]] Subterranean Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Subterranean]] mobs|
|[[Hideonfloor Shard]]|[[Hideonfloor Shard]] Woodland Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Woodland]] mobs|
|[[Billygoat Shard]]|[[Billygoat Shard]] Frozen Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against Frozen ([[Frozen (Mob Type)]]) mobs|
|[[Hideonwall Shard]]|[[Hideonwall Shard]] Arcane Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Arcane]] mobs|
|[[Black Widow Shard]]|[[Black Widow Shard]] Arthropod Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Arthropod]] mobs|
|[[Giant Water Bug Shard]]|[[Giant Water Bug Shard]] Aquatic Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 against [[Aquatic]] mobs|
|[[Silkbreeze Shard]]|[[Silkbreeze Shard]] Forager's Fortune ([[Attributes]])|EPIC ([[Rarity]])|+0.5-5 while on Foraging Islands ([[Locations]])|
|[[Giant Isopod Shard]]|[[Giant Isopod Shard]] Fisher's Fortune ([[Attributes]])|EPIC ([[Rarity]])|+0.5-5 while on Fishing Islands ([[Ship]])|
|[[Cinderbat Shard]]|[[Cinderbat Shard]] Magic Find ([[Attributes]])|LEGENDARY ([[Rarity]])|+0.5-5|
|Icon|Source|Type|Magic Find|
|-|-|-|-|
|Pet Score Rewards|Pet Score ([[Pets]])||+1➡13 depending on your Pet Score ([[Pets]])|
|Magic Find V|Magic Find Account Upgrade ([[Account & Profile Upgrades]])|Profile Upgrade|+1➡5|
|[[Century Cakes]]|Century Cake of the Next Dungeon Floor ([[Century Cakes]])|[[Furniture]]|+1 when consumed|
|[[Beacon]]|[[Beacon]]|Buff|+1➡5 (Can be increased by 20% using [[Scorched Power Crystal]])|
|Bestiary|[[Bestiary]] Leveling Rewards ([[Bestiary]])|Profile Upgrade|Grants 10/25/45/70/100 (per max level) depending on the mob and your Bestiary Progress ([[Bestiary]]) with that mob. Note that this is not awarded as an actual stat and thus doesnt get buffed by any multipliers, with the exception of the [[Grandma Wolf Pet]] kill combo|
||Mayor Jerry ([[Candidate Jerry]])|Mayor ([[Mayor Election]])|+10%|
||Mayor Aatrox ([[Aatrox]])|Mayor ([[Mayor Election]])|+20% and +20 against [[Slayer]] bosses when elected with his Pathfinder perk|
|[[Necron's Ladder]]|[[Necron's Ladder]]|Profile Upgrade|+1|
|[[Diana's Bookshelf]]|[[Diana's Bookshelf]]|Profile Upgrade|+1|
|[[Doug]]|Diana's Favor ([[Doug]])|Carnival Shop|Grants +1-3 on [[Mythological]] mobs.|
|[[Alcina]]|Witches Stew ([[Year of the Witch]])|Year of the Witch|Gain +1 on [any Mob Type ([[Mob Types]]) except [[Mythological]], Pest ([[Pest (Mob Type)]]), and [[Spooky]]] mobs.|
|Heart of the Mountain|Miner's Blessing ([[Heart of the Mountain]])|Heart of the Mountain Perk|+30 while on [[Mining Islands]]|
### Bingo Exclusive Magic Find Sources
||Bingo Buff ([[Bingo]])|All [[Bingo]] players receive +20 Magic Find by default.|
|[[Bingo Pet]]; [[Bingo Pet]]; [[Bingo Pet]]|[[Bingo Pet]]|A RARE ([[Rarity]]) or higher [[Bingo Pet]] increases the base stats of the active pet by 10.3% + 0.3 per level, up to +40%. Example: If you have a level 90 [[Griffin Pet]] equipped while also owning a level 49 Bingo Pet, the Griffin will have a base +9 Magic Find, which gets increased by the Bingo Pet by 25% for a final value of 11.25 Magic Find|
[(only on Extreme Bingo (Bingo))]
|[[Bingolibur]]|Grants +1 Magic Find for every SkyBlock Level ([[SkyBlock Levels]]), up to 50|
### No Longer Available
|Source|Type|Magic Find|
|-|-|-|
|[[Candidate Barry]]'s Astral Negotiator secret bonus|Mayor ([[Mayor Election]])|Used to increase Magic Find by 1 for every year he had not been elected, with a cap of 20|
|[[Candidate Aura]]'s Work Better|Mayor ([[Mayor Election]])|+50 Magic Find|
|Aura's Miniter's Public Surveillance|[[Minister Election]]|Check in with any of the [[Surveillance Goon]] on the map every 30 minutes or suffer a 10% stat debuff.|
|[[Judicial Goon]]|[[Minister Election]]|+5 Magic Find for 2hr if voted against freeing prisoners|
## Maximum Magic Find
This article needs to be reworked as its content is outdated. You can help the wiki by editing this page and reworking it.
This article was last edited by WitherTaco (contribs|logs|block) on 2:34, October 25 2026 (46 hours ago)
To obtain the theoretical maximum Magic Find player must obtain all of the following:
- Accessories: +38
  - [[Crab Hat of Celebration]]/ [[Sloth Hat of Celebration]]/ [[5th Anniversary Balloon Hat|Balloon Hat (disambiguation)]] - +1
  - [[Rarity|LEGENDARY]] [[Pulse Ring]] - +1
  - [[Anguish Artifact]] - +3
  - [[Enrichments|Magic Find Enrichment]] on 66 Accessories total - +33
- Temporary Effects: +137 & +14%
  - [[Booster Cookie]] - +15
  - [[God Potion]] consisting of:
    - [[Magic Find Potion|Magic Find IV Potion]] - +75
    - [[Jerry Candy]] - +3
    - [[Critical Potion]] with [[Slayer© Energy Drink]] - +10
    - [[Wolf Fur Mixin]] with 1 hit kill - +7
    - [[Celestial Mason Jar]] - +3
  - [[Rat Pet|Lv100 Rat Pet]]'s Rat's Blessing from another player - +7
  - [[Tarantula Pet|Lv100 Tarantula Pet]]'s Web Battlefield with 10 kills from another player - +10
  - [[Century Cakes|Century Cake of the Next Dungeon Floor]] - +1
  - [[Beacon|Beacon V]] with [[Scorched Power Crystal]] - +6
  - [[Rarity|LEGENDARY]] [[Grandma Wolf Pet]] with a [[Grandma's Knitting Needle]] and a Kill Combo of 50+ combo - +14%
- 500+ [[Pets|Pet Score]] - +13
- [[Account & Profile Upgrades|Magic Find Account Upgrade]] - +5
- [[Necron's Ladder]] completed - +1
- [[Diana's Bookshelf]] completed - +1
- [[Golden Dragon Pet|Lv200 Golden Dragon Pet]] - +45
  - Base Stat: +10
  - Shining Scales ability with 9 digits in your gold collection - +20
  - Pet Item: [[Hephaestus Relic]]- +15
- Sword: [[Daedalus Blade]] - +120
  - 230 [[Mythological]] [[Bestiary]] tiers - +69 (on [[Mythological]] Mobs)
  - Enchantments:
    - [[Chimera|Chimera V]] - +45
    - [[Divine Gift|Divine Gift III]] - +6
- Armor: +15 & +37%
  - Helmet: [[Clover Helmet]] - +5%
  - 3/4: [[Mythos Armor]] - +15 (on [[Mythological]] Mobs)
  - Reforge: [[Reforging|Renowned]] ( [[Dragon Horn]]) - +4%
  - Enchantment: [[Legion|Legion V]] with 20 nearby players - +28%
- Attributes: +15
  - [[Attributes|Mythological Fortune X]] - +5 (on [[Mythological]] Mobs)
  - [[Attributes|Magic Find X]] - +5
  - [[Attributes|Elusive Fortune X]] - +5 (on [[Elusive]] Mobs)
- Equipment: +13
  - Necklace: [[Rift Necklace]] with all 8 available [[Rift Timecharms]] - +8
  - Cloak: [[Golden Fleece]] - +5
- [[Extremely Real Shuriken]] - +5%
- 5 nearby people with [[Nutcracker Armor]] - +5
- [[Candidate Jerry]] - +10%
- [[Doug|Diana's Favor]] - +3 (on [[Mythological]] Mobs)
- [[Alcina|Witches Stews]] - +2 ( [[Year of the Witch|Hopefully-not-human Hodgepodge]] and [[Year of the Witch|Effervescent Bouillon]] for a [[Minos Inquisitor]].)
- Maxed [[Bestiary]] for [[Minos Inquisitor]] - 70 for [[Minos Inquisitor]]
[Confirm] Combining all that results in a base stat of 414 Magic Find with a multiplier of 66%. [[Daedalus Blade]]'s ability is not affected by the multiplier and it adds 69 Magic Find totalling +756.24 Magic Find against a [[Minos Inquisitor]] while on a normal profile. While on a [[Bingo]] profile, the theoretical maximum is +783.31 Magic Find against a [[Minos Inquisitor]]. Achieving this amount of Magic Find on a Bingo profile is unlikely to happen.
## Maximum Magic Find (Rift)
To obtain the maximum possible Magic Find in the [[Rift Dimension]], the player must obtain all of the following:
- Magic Find V [[Account & Profile Upgrades|Account Upgrade]] (+5 )
- [[Booster Cookie]] (+15 )
- [[Beacon|Beacon V]] + [[Scorched Power Crystal]] (+6 )
- [[Century Cakes|Century Cake of the Next Dungeon Floor]] (+1 )
- [[Necron's Ladder]] completed (+1 )
- [[Diana's Bookshelf]] completed (+1 )
- [[Extremely Real Shuriken]] (+5% and an additional +5 against [[Slayer]] Bosses)
This results in a total of 35.45 Magic Find against [[Riftstalker Bloodfiend]] (which is the only mob with Magic Find drops in the Rift).
## Trivia
- [[Speed]], [[Attack Speed]], [[Ferocity]], [[Swing Range]], [[Mining Spread]], [[Gemstone Spread]], [[Timber]], [[Fishing Speed]], [[Trophy Chance]], [[Treasure Chance]], Magic Find and [[Charm Chance]] are the only stats with a cap.
- Before Magic Find cap was listed in stats, it was achieved by u/ChayUwU on Reddit by using a bug where drill engines would give a lot of stats, which included Magic Find. (for more info regarding the bug visit the [[Drills|Drills page]])
## History
[[SkyBlock Prototype]]:
|Oct 24, 2019|0.7.3|Added Magic Find ([[Magic Find Potion]]).|
|May 5, 2020|0.7.8|Magic Find is now a stat.|
|Oct 19, 2020|Fixed high Magic Find reducing the drop chance of pets.|
|Dec 15, 2023|Magic Find no longer affects Loot Share drops that the mob owner does not roll Magic Find for.|
|Dec 15, 2023|Fixed Magic Find displaying the killer's Magic Find in chat instead of your own Magic Find.|
|Jul 8, 2026|0.26|Updated Magic Find Icon|
Linked from: [[5th Anniversary Balloon Hat]], [[6th Anniversary Balloon Hat]], [[7th Anniversary Cake Hat]], [[Aatrox]], [[Ability Damage]], [[Abyssal Miner]], [[Accessories/Misc Crafts]], [[Accessories/Other]], [[Account & Profile Upgrades]], [[Agarimoo]], [[Airborne]], [[Alligator]], [[Angry Archaeologist]], [[Anguish Artifact]], [[Anguish Ring]], [[Anguish Talisman]], [[Animal]], [[Annihilation Cloak]], [[Aquatic]], [[Arachne]], [[Arachne's Brood]], [[Arachne's Keeper]], [[Arcane]], [[Arenjey God]], [[Armor]], [[Armor/Helmets]], [[Armor/Sets]], [[Arthropod]], [[Ashfang]], [[Atoll Croaker]], [[Attack Speed]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Combat]], [[Attributes/List/Epic]], [[Attributes/List/Fishing]], [[Attributes/List/Global]], [[Attributes/List/Legendary]], [[Attributes/List/Rare]], [[Attributes/Search]] (+508 more)

# Magic Find/Table
Categories: Confirmations needed
### Pets
Certain [[Pets]] grant [[Magic Find]]. The [[Pets|Pet]] must be equipped in order to take effect.
|Icon|Item|Rarity|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Golden Dragon Pet]]|[[Golden Dragon Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|+5.05➡10 [[Magic Find]] Shining Scales: Grants +2.2 [[Magic Find]] for each digit in [[Gold Ingot]] collection. (up to +20 [[Magic Find]] )|
|[[Ender Dragon Pet]]|[[Ender Dragon Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Superior: Increases [[Magic Find]] by +0.1➡10%.|
|[[Black Cat Pet]]|[[Black Cat Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|Supernatural: Grants +0.15➡15 [[Magic Find]]|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|MYTHIC ([[Rarity]])|Mining Pet ([[Pets]])|Refined Senses: Grants +0.1-10% [[Magic Find]] while on [[Mining Islands]].|
|[[Blaze Pet]]|[[Blaze Pet]]|COMMON ([[Rarity]])-LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Nether Embodiment Increases [[Magic Find]] by +0.05➡10% (based on rarity) while on the [[Crimson Isle]].|
|[[Megalodon Pet]]|[[Megalodon Pet]]|EPIC ([[Rarity]]) and LEGENDARY ([[Rarity]])|Fishing Pet ([[Pets]])|+0.1➡10 [[Magic Find]] Enhancer Scales: Doubles the pet's base stats during the [[Fishing Festival]].|
|[[Griffin Pet]]; [[Griffin Pet]]|[[Griffin Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|King of Kings: Grants +0.2➡20 [[Magic Find]] on [[Mythological]] mobs.|
|[[Spider Pet]] [[Tarantula Pet]]|[[Spider Pet]][[Tarantula Pet]]|MYTHIC ([[Rarity]])|Combat Pet ([[Pets]])|Web Battlefield: Killing mobs grants +0.01➡1 [[Magic Find]] for 40s to all players staying within 20 blocks of where they died. (stacks up to 10 times)|
|[[Grandma Wolf Pet]]|[[Grandma Wolf Pet]]|COMMON ([[Rarity]]) to LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|+0.1➡9% [[Magic Find]] depending on the [[Rarity]] and kill combo This buff is unique since it's the only multiplier that also affects Bestiary Magic Find ([[Bestiary]])|
|[[Rat Pet]]|[[Rat Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Combat Morph ([[Pets]])|Rat's Blessing: Has a chance to grant a random player (other than yourself) +2.05➡7 [[Magic Find]] for 20.4➡60 seconds after finding a yummy piece of Cheese!|
|[[Goblin Pet]]|[[Goblin Pet]]|LEGENDARY ([[Rarity]])|Mining Pet ([[Pets]])|+0.07➡7 [[Magic Find]]|
|[[Mole Pet]]|[[Mole Pet]]|LEGENDARY ([[Rarity]])|Mining Pet ([[Pets]])|+0.05➡5 [[Magic Find]]|
|[[Mammoth Pet]]|[[Mammoth Pet]]|LEGENDARY ([[Rarity]])|Combat Pet ([[Pets]])|Tusk Luck: Gain +0.005➡0.5 [[Magic Find]] for every 100 [[Mining Fortune]], doubled in the [[Glacite Tunnels]] and [[Glacite Mineshafts]]|
|[[Baby Yeti Pet]]; [[Baby Yeti Pet]]|[[Baby Yeti Pet]]|LEGENDARY ([[Rarity]]) and MYTHIC ([[Rarity]])|Fishing Pet ([[Pets]])|Frosty Familiarity: Grants +0.1➡10 [[Magic Find]] against Winter Sea Creatures.|
|[[Jade Dragon Pet]]|[[Jade Dragon Pet]]|LEGENDARY ([[Rarity]])|Foraging Pet ([[Pets]])|+5.05➡10 [[Magic Find]]|
### Pet Items
Certain [[Pet Items]] grant [[Magic Find]]. The [[Pet Items|Pet Item]] must be equipped on the player's active [[Pets|Pet]] to take effect.
|Slot|Name|Rarity|[[Magic Find]]|Source|
|-|-|-|-|-|
|[[Minos Relic]]|[[Minos Relic]]|EPIC ([[Rarity]])|Increases all pet stats by 33.3%.|Drop from [[Minos Champion]] (requires LEGENDARY ([[Rarity]]) [[Griffin Pet]])|
|[[Hephaestus Relic]]|[[Hephaestus Relic]]|LEGENDARY ([[Rarity]])|Increases all pet stats by 50%.|Recipe: [[Minos Relic]] ×3 + [[Hephaestus Anvil]] → [[Hephaestus Relic]]|
|[[Four-Eyed Fish]]|[[Four-Eyed Fish]]|EPIC ([[Rarity]])|+13 [[Magic Find]] to [[Griffin Pet]]|Recipe: [[Enchanted Spider Eye]] x64 ×6 + [[Lucky Clover]] + [[Pre-Digestion Fish]] + [[Reinforced Scales]] → [[Four-Eyed Fish]]|
|[[Lucky Clover]]|[[Lucky Clover]]|EPIC ([[Rarity]])|+7 [[Magic Find]]|Recipe: [[Enchanted Emerald]] x32 ×8 + [[Lucky Clover Core]] → [[Lucky Clover]]|
|[[Poignant Lucky Clover]]|[[Poignant Lucky Clover]]|LEGENDARY ([[Rarity]])|+13 [[Magic Find]]|[[Carrot King Avatar]]|
|[[Grandma's Knitting Needle]]|[[Grandma's Knitting Needle]]|RARE ([[Rarity]])|+5% [[Magic Find]] at 50+ combo to [[Grandma Wolf Pet]]|[[Oruo The Almighty]]: 50 [[Sun Gecko Essence]]|
|Icon|Item|Rarity|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Sword of Revelations]]|[[Sword of Revelations]]|EPIC ([[Rarity]])|Weapon ([[Weapons]])|Grants +5 [[Magic Find]] on [[Mythological]] mobs.|
|[[Daedalus Blade]]|[[Daedalus Blade]]|LEGENDARY ([[Rarity]])|Weapon ([[Weapons]])|Grants +0.2 [[Magic Find]] (+0.3 [[Magic Find]] when upgraded) on [[Mythological]] mobs per [[Bestiary]] tier you have across all of them. (max +69 [[Magic Find]] )|
|Icon|Item|Rarity|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Superior Dragon Armor]]; [[Superior Dragon Armor]]; [[Superior Dragon Armor]]; [[Superior Dragon Armor]]|[[Superior Dragon Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5% [[Magic Find]] set bonus|
|[[Sorrow Armor]]; [[Sorrow Armor]]; [[Sorrow Armor]]; [[Sorrow Armor]]|[[Sorrow Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5 [[Magic Find]] per piece (Max is +20 [[Magic Find]] )|
|[[Nutcracker Armor]]; [[Nutcracker Armor]]; [[Nutcracker Armor]]; [[Nutcracker Armor]]|[[Nutcracker Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|Full Set Bonus: Battalion:; +1 [[Magic Find]] to everyone within 30 blocks (stacks up to 5 times)|
|[[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Armor]]; [[Magma Lord Necklace]]|[[Magma Lord Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+20 (4 Pieces)➜30 (5 Pieces) [[Magic Find]] on [[Magmatic]] mobs.|
|[[Mythos Armor]]; [[Mythos Armor]]; [[Mythos Armor]]; [[Mythos Armor]]|[[Mythos Armor]]|LEGENDARY ([[Rarity]])|[[Armor]]|+10 (2 Pieces)➜15 (3 Pieces)➜20 [[Magic Find]] on [[Mythological]] mobs.|
|[[Crown of Greed]]|[[Crown of Greed]]|LEGENDARY ([[Rarity]])|[[Armor]]|+10 [[Magic Find]] on [[Mythological]] mobs|
|[[Crown of Avarice]]|[[Crown of Avarice]]|LEGENDARY ([[Rarity]])|[[Armor]]|+2.5 to 25 [[Magic Find]] against [[Mythological]] mobs|
|[[Clover Helmet]]|[[Clover Helmet]]|LEGENDARY ([[Rarity]])|[[Armor]]|+5% [[Magic Find]]|
|[[Crab Hat of Celebration]]; [[Sloth Hat of Celebration]]; [[5th Anniversary Balloon Hat]]/[[6th Anniversary Balloon Hat]]; [[7th Anniversary Cake Hat]]|[[Crab Hat of Celebration]]; or; [[Sloth Hat of Celebration]]; or; Anniversary Balloon Hat ([[5th Anniversary Balloon Hat]]); or; [[7th Anniversary Cake Hat]]|SPECIAL ([[Rarity]])|Hatcessory ([[Hatcessories]])|+1 [[Magic Find]]|
|Icon|Item|Rarity|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Delirium Necklace]]|[[Delirium Necklace]]|EPIC ([[Rarity]])|Necklace ([[Necklaces]])|+1 [[Magic Find]] , up to +1.2 [[Magic Find]] when starred ([[Star Upgrades]]).|
|[[Shriveled Bracelet]]|[[Shriveled Bracelet]]|EPIC ([[Rarity]])|Glove ([[Gloves]])|Grants +10 [[Magic Find]] on [[Arthropod]] mobs.|
|[[Rift Necklace]]|[[Rift Necklace]]|LEGENDARY ([[Rarity]])|Necklace ([[Necklaces]])|+1 [[Magic Find]] to +8 [[Magic Find]] , depending on the number of [[Rift Timecharms]].|
|[[Destruction Cloak]]|[[Destruction Cloak]]|EPIC ([[Rarity]])|Cloak ([[Cloaks]])|+1 [[Magic Find]]|
|[[Annihilation Cloak]]|[[Annihilation Cloak]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+2 [[Magic Find]]|
|[[David's Cloak]]|[[David's Cloak]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+2 [[Magic Find]]|
|[[Golden Fleece]]|[[Golden Fleece]]|LEGENDARY ([[Rarity]])|Cloak ([[Cloaks]])|+5 [[Magic Find]] on [[Mythological]] mobs.|
|Icon|Item|Rarity|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Pulse Ring]]|[[Pulse Ring]]|UNCOMMON ([[Rarity]]) to LEGENDARY ([[Rarity]])|Accessory ([[Accessories]])|+0.25 [[Magic Find]] +0.5 [[Magic Find]] +0.75 [[Magic Find]] +1 [[Magic Find]]|
|[[Crab Hat of Celebration]]; [[Sloth Hat of Celebration]]; [[5th Anniversary Balloon Hat]]/[[6th Anniversary Balloon Hat]]; [[7th Anniversary Cake Hat]]|[[Crab Hat of Celebration]]; or; [[Sloth Hat of Celebration]]; or; Anniversary Balloon Hat ([[5th Anniversary Balloon Hat]]); or; [[7th Anniversary Cake Hat]]|SPECIAL ([[Rarity]])|Hatcessory ([[Hatcessories]])|+1 , only one Hatcessory ([[Hatcessories]]) gives [[Magic Find]] while in accessory bag.|
|[[Anguish Talisman]]|[[Anguish Talisman]]|RARE ([[Rarity]])|Accessory ([[Accessories]])|+1 [[Magic Find]]|
|[[Anguish Ring]]|[[Anguish Ring]]|EPIC ([[Rarity]])|Accessory ([[Accessories]])|+2 [[Magic Find]]|
|[[Anguish Artifact]]|[[Anguish Artifact]]|LEGENDARY ([[Rarity]])|Accessory ([[Accessories]])|+3 [[Magic Find]]|
|Icon|Item|Tier|Type|[[Magic Find]]|
|-|-|-|-|-|
|[[Magic Find Potion]]|[[Magic Find Potion]]|I|Potion ([[Potions]])|+10 [[Magic Find]]|
|[[Magic Find Potion]]|[[Magic Find Potion]]|II|Potion ([[Potions]])|+25 [[Magic Find]]|
|[[Magic Find Potion]]|[[Magic Find Potion]]|III|Potion ([[Potions]])|+50 [[Magic Find]]|
|[[Magic Find Potion]]|[[Magic Find Potion]]|IV|Potion ([[Potions]])|+75 [[Magic Find]]|
|[[Slayer© Energy Drink]]|[[Slayer© Energy Drink]]|[[Slayer© Energy Drink]]|Brew ([[Brews]])|+10 [[Magic Find]] to Critical Potions ([[Critical Potion]]) brewed with this|
|[[Jerry Candy]]|[[Jerry Candy]]|[[Jerry Candy]]|Consumable|+3 [[Magic Find]]|
|[[God Potion]]|[[God Potion]]|[[God Potion]]|Consumable|+88 [[Magic Find]] from [[Magic Find Potion]], [[Critical Potion]] with [[Slayer© Energy Drink]] and from [[Jerry Candy]]|
|[[Wolf Fur Mixin]]|[[Wolf Fur Mixin]]|[[Wolf Fur Mixin]]|Mixin ([[Mixins]])|+7 [[Magic Find]] when a mob is killed in one hit|
|[[Celestial Mason Jar]]|[[Celestial Mason Jar]]|[[Celestial Mason Jar]]|Mixin ([[Mixins]])|+3 [[Magic Find]]|
|[[Booster Cookie]]|[[Booster Cookie]]|[[Booster Cookie]]|Consumable|+15 [[Magic Find]]|
|[[Extremely Real Shuriken]]|[[Extremely Real Shuriken]]|[[Extremely Real Shuriken]]|Consumable|+5% [[Magic Find]] to tagged mob|
|Icon|Item|Type|[[Magic Find]]|
|-|-|-|-|
|[[Dragon Horn]]|[[Dragon Horn]] (Renowned)|Reforge Stone ([[Reforge Stones]])|+1% [[Magic Find]]|
|[[Entropy Suppressor]]|[[Entropy Suppressor]] (Coldfused)|Reforge Stone ([[Reforge Stones]])|+2 [[Magic Find]] applicable only to the 6 Blaze Slayer ([[Inferno Demonlord]])-specific Daggers ([[Sword Types]])|
|[[Divine Gift]]|[[Divine Gift]]|Enchantment ([[Enchantments]])|+2➡6 [[Magic Find]]|
|[[Chimera]]|[[Chimera]]|Enchantment ([[Enchantments]])|Copies 20%➡100% of your active pet stats, including [[Magic Find]]|
|[[Legion]]|[[Legion]]|Enchantment ([[Enchantments]])|+0.07➡0.35% [[Magic Find]] for each player within 30 blocks, up to +1.4➡7% [[Magic Find]] on a single piece and up to +5.6➡28% [[Magic Find]] on a full armor set|
|[[Habanero Tactics]]|[[Habanero Tactics]]|Enchantment ([[Enchantments]])|+10➡15 [[Magic Find]] on slayer weapons while Smoldering Polarization ([[Re-heated Gummy Polar Bear]]) is active on a single piece and +40➡60 [[Magic Find]] on a full armor set|
|[[Bobbin' Time]]|[[Bobbin' Time]]|Enchantment ([[Enchantments]])|+0.6➡1% [[Magic Find]] for each fishing bobber within 30 blocks up to +3➡5% [[Magic Find]] on a single piece and up to +12➡20% [[Magic Find]] on a full armor set|
|[[Enrichments]]|Magic Find Enrichment ([[Enrichments]])|[[Enrichments]]|+0.5 per each enriched Accessory ([[Accessories]]) Can only be applied to all LEGENDARY ([[Rarity]]), MYTHIC ([[Rarity]]), SPECIAL ([[Rarity]]) and VERY SPECIAL ([[Rarity]]) accessories (except [[Hocus-Pocus Cipher]]), totalling at 65 accessories, granting a total of 32.5 [[Magic Find]] [Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
#### Attributes
Certain [[Attributes]] can be syphoned to grant [[Magic Find]].
|Slot|Name|Rarity|[[Magic Find]]|
|-|-|-|-|
|[[Drowned Shard]]|[[Drowned Shard]] Undead Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against Undead ([[Undead (Mob Type)]]) mobs|
|[[Wild Hog Shard]]|[[Wild Hog Shard]] Animal Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Animal]] mobs|
|[[Hewver Shard]]|[[Hewver Shard]] Critter Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against Critter ([[Critters]]) mobs|
|[[Lava Flame Shard]]|[[Lava Flame Shard]] Magmatic Fortune ([[Attributes]])|RARE ([[Rarity]])|+1-10 [[Magic Find]] against [[Magmatic]] mobs|
|[[Wiki Tiki Shard]]|[[Wiki Tiki Shard]] Construct Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Construct]] mobs|
|[[Minotaur Shard]]|[[Minotaur Shard]] Mythological Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Mythological]] mobs|
|[[Hivethief Shard]]|[[Hivethief Shard]] Cubic Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against Cubic ([[Cubic (Mob Type)]]) mobs|
|[[Parakeet Shard]]|[[Parakeet Shard]] Flying Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Airborne]] mobs|
|[[Hideyho Shard]]|[[Hideyho Shard]] Elusive Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Elusive]] mobs|
|[[Chuckwalla Shard]]|[[Chuckwalla Shard]] Subterranean Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Subterranean]] mobs|
|[[Hideonfloor Shard]]|[[Hideonfloor Shard]] Woodland Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Woodland]] mobs|
|[[Billygoat Shard]]|[[Billygoat Shard]] Frozen Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against Frozen ([[Frozen (Mob Type)]]) mobs|
|[[Hideonwall Shard]]|[[Hideonwall Shard]] Arcane Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Arcane]] mobs|
|[[Black Widow Shard]]|[[Black Widow Shard]] Arthropod Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Arthropod]] mobs|
|[[Giant Water Bug Shard]]|[[Giant Water Bug Shard]] Aquatic Fortune ([[Attributes]])|RARE ([[Rarity]])|+0.5-5 [[Magic Find]] against [[Aquatic]] mobs|
|[[Silkbreeze Shard]]|[[Silkbreeze Shard]] Forager's Fortune ([[Attributes]])|EPIC ([[Rarity]])|+0.5-5 [[Magic Find]] while on Foraging Islands ([[Locations]])|
|[[Giant Isopod Shard]]|[[Giant Isopod Shard]] Fisher's Fortune ([[Attributes]])|EPIC ([[Rarity]])|+0.5-5 [[Magic Find]] while on Fishing Islands ([[Ship]])|
|[[Cinderbat Shard]]|[[Cinderbat Shard]] Magic Find ([[Attributes]])|LEGENDARY ([[Rarity]])|+0.5-5 [[Magic Find]]|
|Icon|Source|Type|[[Magic Find]]|
|-|-|-|-|
|Pet Score Rewards|Pet Score ([[Pets]])||+1➡13 [[Magic Find]] depending on your Pet Score ([[Pets]])|
|Magic Find V|Magic Find Account Upgrade ([[Account & Profile Upgrades]])|Profile Upgrade|+1➡5 [[Magic Find]]|
|[[Century Cakes]]|Century Cake of the Next Dungeon Floor ([[Century Cakes]])|[[Furniture]]|+1 [[Magic Find]] when consumed|
|[[Beacon]]|[[Beacon]]|Buff|+1➡5 [[Magic Find]] (Can be increased by 20% using [[Scorched Power Crystal]])|
|Bestiary|[[Bestiary]] Leveling Rewards ([[Bestiary]])|Profile Upgrade|Grants 10/25/45/70/100 [[Magic Find]] (per max level) depending on the mob and your Bestiary Progress ([[Bestiary]]) with that mob. Note that this is not awarded as an actual stat and thus doesnt get buffed by any multipliers, with the exception of the [[Grandma Wolf Pet]] kill combo|
||Mayor Jerry ([[Candidate Jerry]])|Mayor ([[Mayor Election]])|+10% [[Magic Find]]|
||Mayor Aatrox ([[Aatrox]])|Mayor ([[Mayor Election]])|+20% [[Magic Find]] and +20 [[Magic Find]] against [[Slayer]] bosses when elected with his Pathfinder perk|
|[[Necron's Ladder]]|[[Necron's Ladder]]|Profile Upgrade|+1 [[Magic Find]]|
|[[Diana's Bookshelf]]|[[Diana's Bookshelf]]|Profile Upgrade|+1 [[Magic Find]]|
|[[Doug]]|Diana's Favor ([[Doug]])|Carnival Shop|Grants +1-3 [[Magic Find]] on [[Mythological]] mobs.|
|[[Alcina]]|Witches Stew ([[Year of the Witch]])|Year of the Witch|Gain +1 [[Magic Find]] on [any Mob Type ([[Mob Types]]) except [[Mythological]], Pest ([[Pest (Mob Type)]]), and [[Spooky]]] mobs.|
|Heart of the Mountain|Miner's Blessing ([[Heart of the Mountain]])|Heart of the Mountain Perk|+30 [[Magic Find]] while on [[Mining Islands]]|

# Mining Speed
Aliases: Miningspeed
Categories: Confirmations needed, More info needed, Player Statistics, Mining
[Mining Speed]
Type: Stat
Uses: Increases the speed at which one breaks blocks.
Increasing: [[Heart of the Mountain]], [[Pickaxes]], [[Drills]], [[Armor]], Reforges ([[Reforging]]), Amber ([[Gemstone]]), and more
[Values]
Base Value: 0
Max Value: N/A
[Symbol]
Unicode Code Point: U+E015
Icon (The icon displayed in the Equipment Menu interface.): Diamond Pickaxe ()
Mining Speed is one of the player statistics. It is a measure of the block-breaking time.
## Mechanics
- Any item that increases Mining Speed by a base value can be thought of as a decrease of the base breaking time.
- Mining Speed does not affect [[Private Island]], [[The Garden]], [[The Park]], [[Hub Island|Hub]], [[The Farming Islands (disambiguation)|The Farming Islands]], or the [[Rift Dimension]]. These places use the Vanilla Mining Speed.
- There is no known cap for Mining Speed, however the Softcap limits the breaking of a block to at least 4 ticks (1 tick equals 0.05 seconds).
- Ping may affect the actual time time it takes to break a block.
### Calculation
- The time taken to break a block can be calculated using the following formula :
  - Mining Timein ticks=⌊Block Strength×30Mining Speed⌉
  - Mining Timein seconds=⌊Block Strength×30Mining Speed⌉×120
### Softcap
The softcap limits how fast a block can be mined to at least 4 ticks (or 0.2 seconds). To determine the Mining Speed needed to reach it for a given block, use the following formula:
- Mining Speed needed to reach Softcap=⌈20×Block Strength3⌉
- The softcap can be bypassed by breaking a block instantly.
### Instant Mining
- The softcap can be bypassed if the block is mined within a single Minecraft tick (0.05 seconds). In this case, the block will break instantly.
- To instantly break a [[Blocks|Block]] (except [[Obsidian]]), Mining Speed needs to be >30x higher than a its Block Strength, or >60x if it's a block of [[Obsidian]], an [[Ores|Ore]], a [[Gemstone|Gemstone Block]] or a [[Dwarven Metals|Dwarven Metal Block]].
Show/Hide Block Strengths
|[[Ores]]|Breaking Strength|min⁡ Mining Speed for instamining|
|-|-|-|
|Coal Ore ([[Ores]])|30|1800|
|Iron Ore ([[Ores]])|30|1800|
|Gold Ore ([[Ores]])|30|1800|
|Lapis Lazuli Ore ([[Ores]])|30|1800|
|Redstone Ore ([[Ores]])|30|1800|
|Emerald Ore ([[Ores]])|30|1800|
|Diamond Ore ([[Ores]])|30|1800|
|Nether Quartz Ore ([[Ores]])|30|1800|
|Sulphur Ore ([[Ores]])|500|30000|
|Pure Coal ([[Ores]])|600|36000|
|Pure Iron ([[Ores]])|600|36000|
|Pure Gold ([[Gold Ingot]])|600|36000|
|Pure Lapis Lazuli ([[Ores]])|600|36000|
|Pure Redstone ([[Ores]])|600|36000|
|Pure Emerald ([[Ores]])|600|36000|
|Pure Diamond ([[Ores]])|600|36000|
|Pure Nether Quartz ([[Ores]])|600|36000|
|Blocks|Theorized Vanilla Block Hardness|min⁡ Gear for instamining|
|-|-|-|
|[[Ice]]|0,5|[[Golden Pickaxe]] with Haste II ([[Haste Potion]]) or enchanted with Efficiency II ([[Efficiency]]).|
|[[Sand]]|0,5|[[Golden Shovel]] with Haste II ([[Haste Potion]]) or enchanted with Efficiency II ([[Efficiency]]).|
|[[Red Sand]]|0,5|(same as above)|
|[[Gravel]]|0,6|[[Golden Shovel]] with Haste III ([[Haste Potion]]) or enchanted with Efficiency III ([[Efficiency]]).|
|[[Mycelium]]|0,6|(same as above)|
|[[Glowstone]]|0,3|Unreachable.; Can be broken in 5 ticks under the effect of Haste IV ([[Haste Potion]])|
|Blocks|Breaking Strength|min⁡ Mining Speed for instamining|
|-|-|-|
|[[Netherrack]]|8|241|
|[[Stone]]|15|451|
|[[Cobblestone]]|20|601|
|[[End Stone]]|30|901|
|[[Hard Stone]]|50|1501|
|Hard Stone (terracotta variant) ([[Hard Stone]])|100|3001|
|[[Obsidian]]|500|30001|
|Dwarven Metals|Breaking Strength|min⁡ Mining Speed for instamining|
|-|-|-|
|Mithril (Cyan Terracotta) ([[Mithril]])|500|30001|
|Mithril (Gray Wool) ([[Mithril]])|500|30001|
|Mithril (Prismarine) ([[Mithril]])|800|48001|
|Mithril (Light Blue Wool) ([[Mithril]])|1500|90001|
|[[Titanium]]|2000|120001[Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
|Umber (Smooth Red Sandstone) ([[Umber]])|5600|336001[Confirm]|
|Umber (Terracotta) ([[Umber]])|5600|336001[Confirm]|
|Umber (Brown Terracotta) ([[Umber]])|5600|336001[Confirm]|
|Tungsten (Clay) ([[Tungsten]])|5600|336001[Confirm]|
|Tungsten (Cobblestone) ([[Tungsten]])|5600|336001[Confirm]|
|[[Glacite]]|6000|360001[Confirm]|
|Gemstones|Breaking Strength|min⁡ Mining Speed for instamining|
|-|-|-|
|Ruby ([[Gemstone]])|2300|138001[Confirm]|
|Amber ([[Gemstone]])|3000|180001[Confirm]|
|Amethyst ([[Gemstone]])|3000|180001[Confirm]|
|Jade ([[Gemstone]])|3000|180001[Confirm]|
|Opal ([[Gemstone]])|3000|180001[Confirm]|
|Sapphire ([[Gemstone]])|3000|180001[Confirm]|
|Topaz ([[Gemstone]])|3800|228001[Confirm]|
|Jasper ([[Gemstone]])|4800|288001[Confirm]|
|Aquamarine ([[Gemstone]])|5200|312001[Confirm]|
|Citrine ([[Gemstone]])|5200|312001[Confirm]|
|Onyx ([[Onyx (disambiguation)]])|5200|312001[Confirm]|
|Peridot ([[Gemstone]])|5200|312001[Confirm]|
Show/Hide Tick Thresholds
|Mining Time (in Ticks)|Mining Speed while mining… Coal Ore ([[Ores]]) Iron Ore ([[Ores]]) Gold Ore ([[Ores]]) Lapis Lazuli Ore ([[Ores]]) Redstone Ore ([[Ores]]) Emerald Ore ([[Ores]]) Diamond Ore ([[Ores]]) Nether Quartz Ore ([[Ores]])|Mining Speed while mining… Sulphur Ore ([[Ores]])|Mining Speed while mining… Pure Coal ([[Ores]]) Pure Iron ([[Ores]]) Pure Gold ([[Gold Ingot]]) Pure Lapis Lazuli ([[Ores]]) Pure Redstone ([[Ores]]) Pure Emerald ([[Ores]]) Pure Diamond ([[Ores]]) Pure Nether Quartz ([[Ores]])|
|-|-|-|-|
|60|15|248|298|
|50|18|298|357|
|40||371|445|
|30|30|492|591|
|29|31|509|611|
|28|32|527|632|
|27|33|546|655|
|26|34|567|679|
|25|36|589|706|
|24|37|611|735|
|23|39|639|766|
|22|41|667|801|
|21|42|697|837|
|20 (1 second)|44|732|878|
|19|47|770|923|
|18|49|811|973|
|17|52|857|1029|
|16|55|910|1091|
|15|59|968|1162|
|14|63|1035|1242|
|13|67|1112|1334|
|12|73|1201|1441|
|11|79|1305|1566|
|10|84|1429|1715|
|9|95|1579|1895|
|8|106|1765|2118|
|7|121|2001|2401|
|6|139|2308|2770|
|5|164|2728|3273|
|4 (Softcap)|201|3334|4001|
|3||||
|2||||
|1 (Instamine)|1800|30000|36000|
|Mining Time (in Ticks)|Necessary and sufficient conditions while mining… [[Ice]]|Necessary and sufficient conditions while mining… [[Sand]] [[Red Sand]]|Necessary and sufficient conditions while mining… [[Gravel]] [[Mycelium]]|Necessary and sufficient conditions while mining… [[Glowstone]]|
|-|-|-|-|-|
|15|Default|Default|Haste I ([[Haste Potion]])||
|14|[More Info Needed] (More infomation needed; When this info is added, remove this.)|[More Info Needed]|[More Info Needed]||
|13|Haste I ([[Haste Potion]])|Haste I ([[Haste Potion]])|Haste II ([[Haste Potion]])||
|12|[More Info Needed]|[More Info Needed]|Haste III ([[Haste Potion]])||
|11|Haste II ([[Haste Potion]])|Haste II ([[Haste Potion]])|[More Info Needed]||
|10|Haste III ([[Haste Potion]])|Haste III ([[Haste Potion]])|Haste IV ([[Haste Potion]])||
|9|Haste IV ([[Haste Potion]])|Haste IV ([[Haste Potion]])|[[Wooden Shovel]]|Default|
|8|[[Wooden Pickaxe]]|[[Wooden Shovel]]|[[Wooden Shovel]]; Haste I ([[Haste Potion]])|Haste I ([[Haste Potion]])|
|7|[[Wooden Pickaxe]]; Haste I ([[Haste Potion]])|[[Wooden Shovel]]; Haste I ([[Haste Potion]])|[[Wooden Shovel]]; Haste II ([[Haste Potion]])|Haste II ([[Haste Potion]])|
|6|[[Wooden Pickaxe]]; Haste II ([[Haste Potion]])|[[Wooden Shovel]]; Haste II ([[Haste Potion]])|[[Wooden Shovel]]; Haste III ([[Haste Potion]])|Haste III ([[Haste Potion]])|
|5|[[Golden Pickaxe]]; Haste II ([[Haste Potion]]); 1 M. Penalty|[[Golden Shovel]]; Haste II ([[Haste Potion]]); 1 M. Penalty|[[Golden Shovel]]; Haste IV ([[Haste Potion]]); 1 M. Penalty|Haste IV ([[Haste Potion]])|
|4 (Softcap)|[[Golden Pickaxe]]; Haste IV ([[Haste Potion]]); 1 M. Penalty|[[Golden Shovel]]; Haste IV ([[Haste Potion]]); 1 M. Penalty|Efficiency I ([[Efficiency]]) [[Golden Shovel]]; Haste IV ([[Haste Potion]]); 1 M. Penalty||
|3|[[Iron Pickaxe]]|[[Iron Shovel]]|[[Iron Shovel]]||
|2|[[Golden Pickaxe]]|[[Golden Shovel]]|[[Golden Shovel]]||
|1 (Instamine)|Efficiency II ([[Efficiency]]) [[Golden Pickaxe]]|Efficiency II ([[Efficiency]]) [[Golden Shovel]]|Efficiency III ([[Efficiency]]) [[Golden Shovel]]||
|1 (Instamine)|[[Golden Pickaxe]]; Haste II ([[Haste Potion]])|[[Golden Shovel]]; Haste II ([[Haste Potion]])|[[Golden Shovel]]; Haste III ([[Haste Potion]])||
|Mining Time (in Ticks)|Mining Speed while mining… [[Netherrack]]|Mining Speed while mining… [[Stone]]|Mining Speed while mining… [[Cobblestone]]|Mining Speed while mining… [[End Stone]]|Mining Speed while mining… [[Hard Stone]]|Mining Speed while mining… Hard Stone (terracotta variants) ([[Hard Stone]])|Mining Speed while mining… [[Obsidian]]|
|-|-|-|-|-|-|-|-|
|60|4||10|15|25|50|248|
|50||9|12|18|30|60|298|
|40|6||15|||75|372|
|30|8|15|20|30|50|99|492|
|29|||21|31|51|102|509|
|28||16||32|53|106|527|
|27|9||22|33|55|110|546|
|26||17|23|34|57|114|567|
|25||18|24|36|59|118|589|
|24|10|19|25|37|62|123|613|
|23|||26|39|64|128|639|
|22|11||27|41|67|134|667|
|21||21|28|42|70|140|698|
|20 (1 second)|12|22|30|44|74|147|732|
|19||24|31|47|77|154|770|
|18|13|25|33|49|82|163|811|
|17|14|26|35|52|86|172|858|
|16|15|28|37|55|91|182|910|
|15|16|30|39|59|97|194|968|
|14|17|32|42|63|104|207|1035|
|13|18|34|45|67|112|223|1112|
|12|20|37|49|73|121|241|1201|
|11|21|40|53|79|131|261|1305|
|10|23|43|58|86|143|286|1429|
|9|26|48|64|95|158|316|1579|
|8|29|53|71|106|177|353|1765|
|7|33|61|81|121|201|401|2001|
|6|37|70|93|139|231|462|2308|
|5|44|82|110|164|273|546|2728|
|4 (Softcap)|54|101|134|201|334|667|3334|
|3||||||||
|2||||||||
|1 (Instamine)|241|451|601|901|1501|3001|30001|
|Mining Time (in Ticks)|Mining Speed while mining… [[Mithril]]|Mining Speed while mining… [[Titanium]]|Mining Speed while mining… [[Umber]] [[Tungsten]]|Mining Speed while mining… [[Glacite]]|
|-|-|-|-|-|
|60|248 397 744|992|2777|2976|
|50|298 476 892|1189|3327|3565|
|40|371 593 1112|1482|4149|4445|
|30|492 788 1476|1968|5509|5902|
|29|509 814 1526|2034|5695|6102|
|28|527 843 1579|2106|5895|6316|
|27|546 873 1637|2182|6110|6546|
|26|567 906 1699|2265|6340|6793|
|25|589 942 1765|2353|6589|7059|
|24|613 980 1837|2449|6858|7347|
|23|639 1022 1915|2554|7149|7660|
|22|667 1067 2001|2667|7467|8001|
|21|698 1117 2094|2791|7814|8373|
|20 (1 second)|732 1171 2196|2927|8196|8781|
|19|770 1231 2308|3077|8616|9231|
|18|811 1298 2433|3244|9082|9730|
|17|858 1372 2572|3429|9601|10286|
|16|910 1455 2728|3637|10182|10910|
|15|968 1549 2904|3871|10839|11613|
|14|1035 1656 3105|4138|11587|12414|
|13|1112 1778 3334|4445|12445|13334|
|12|1201 1921 3601|4801|13441|14401|
|11|1305 2087 3914|5218|14609|15653|
|10|1429 2286 4286|5715|16001|17143|
|9|1579 2527 4737|6316|17685|18948|
|8|1765 2824 5295|7060|19765|21177|
|7|2001 3201 6001|8001|22401|24001|
|6|2308 3693 6924|9231|25847|27693|
|5|2728 4364 8182|10910|30546|32728|
|4 (Softcap)|3334 5334 10001|13334|37334|40001|
|3|||||
|2|||||
|1 (Instamine)|30001 48001 90001|120001[Confirm]|336001[Confirm]|360001[Confirm]|
|Mining Time (in Ticks)|Mining Speed while mining… Ruby ([[Gemstone]])|Mining Speed while mining… Amber ([[Gemstone]]) Amethyst ([[Gemstone]]) Jade ([[Gemstone]]) Opal ([[Gemstone]]) Sapphire ([[Gemstone]])|Mining Speed while mining… Topaz ([[Gemstone]])|Mining Speed while mining… Jasper ([[Gemstone]])|Mining Speed while mining… Aquamarine ([[Gemstone]]) Citrine ([[Gemstone]]) Onyx ([[Onyx (disambiguation)]]) Peridot ([[Gemstone]])|
|-|-|-|-|-|-|
|60|1141|1488|1885|2381|2579|
|50|1367|1783|2258|2852|3090|
|40|1704|2223|2815|3556|3852|
|30|2263|2951|3738|4722|5115|
|29|2339|3051|3865|4882|5289|
|28|2422|3158|4001|5053|5474|
|27|2510|3273|4146|5237|5673|
|26|2604|3397|4302|5434|5887|
|25|2706|3530|4471|5648|6118|
|24|2817|3674|4654|5878|6368|
|23|2937|3830|4852|6128|6639|
|22|3067|4001|5067|6401|6934|
|21|3210|4187|5303|6698|7256|
|20 (1 second)|3366|4391|5561|7025|7610|
|19|3539|4616|5847|7385|8001|
|18|3730|4865|6163|7784|8433|
|17|3943|5143|6515|8229|8915|
|16|4182|5455|6910|8728|9455|
|15|4452|5807|7355|9291|10065|
|14|4759|6207|7863|9932|10759|
|13|5112|6667|8445|10667|11556|
|12|5520|7201|9121|11520|12481|
|11|6601|7827|9914|12522|13566|
|10|6572|8572|10858|13715|14858|
|9|7264|9474|12001|15158|16422|
|8|8118|10589|13412|16942|18353|
|7|9201|12001|15201|19201|20801|
|6|10616|13847|17539|22154|24000|
|5|12546|16364|20728|26182|28364|
|4 (Softcap)|15334|20001|25334|32001|34667|
|3||||||
|2||||||
|1 (Instamine)|138001[Confirm]|180001[Confirm]|228001[Confirm]|288001[Confirm]|312001[Confirm]|
Mining Time (in Ticks): Mining Speed while mining…
Mining Time (in Ticks): Anthill ([[Ant's Cave]])
60: 1736
50: 2080
40: 2593
30: 3443
29: 3560
28: 3685
27: 3819
26: 3963
25: 4118
24: 4286
23: 4469
22: 4667
21: 4884
20 (1 second): 5122
19: 5385
18: 5676
17: 6001
16: 6364
15: 6775
14: 7242
13: 7778
12: 8401
11: 9131
10: 10001
9: 11053
8: 12354
7: 14001
6: 16154
5: 19091
4 (Softcap): 23334
3
2
1 (Instamine): 105001[Confirm]
### Mining Fatigue Effect
Players are given the Mining Fatigue Effect on all islands excepted [[Private Island]], [[The Garden]], [[The Park]], [[Hub Island|Hub]], [[The Farming Islands (disambiguation)|The Farming Islands]], [[Catacombs|The Catacombs]] or the [[Rift Dimension]]. These places use the Vanilla Mining Speed to remove the vanilla mining behavior (client-side mining animations) and let the server handle the animations itself. It does not slow down or remove Mining Speed, but is in fact necessary its implementation.
It also provides additional aesthetic benefits:
- No breaking/mining animation (except for the swinging) for blocks that cannot be broken;
- No ghost blocks due to mining blocks;
- No block rollbacks;
- Mining animation synced up with the server's speed (server's TPS). This can also be a nuisance with poor server performance;
- Blocks don't turn into air before getting replaced by bedrock (or another block).
### Interactions
- Block-specific Mining Speed increases (e.g. [[Mithril Golem Pet]] and [[Mithril Pickaxe]]) are not affected by [[Heart of the Mountain|Mining Speed Boost]].
## Increasing Base Mining Speed
Players have 0 Mining Speed by default.
## Increasing Bonus Mining Speed
|Slot|Item|Type|Rarity|Source|Mining Speed|Condition|
|-|-|-|-|-|-|-|
|[[Gemstone Gauntlet]]|[[Gemstone Gauntlet]]|[[Gauntlet]]|LEGENDARY ([[Rarity]])|Item Stats|+800|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Gemstone Gauntlet]]|[[Gemstone Gauntlet]]|[[Gauntlet]]|LEGENDARY ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|Slot|Item|Type|Rarity|Source|Mining Speed|Condition|
|-|-|-|-|-|-|-|
|[[Wooden Pickaxe]]|[[Wooden Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+70||
|[[Stone Pickaxe]]|[[Stone Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+110||
|[[Iron Pickaxe]]|[[Iron Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+160||
|[[Golden Pickaxe]]|[[Golden Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+250||
|[[Diamond Pickaxe]]|[[Diamond Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+160||
|[[Rookie Pickaxe]]|[[Rookie Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+150||
|[[Zombie Pickaxe]]|[[Zombie Pickaxe]]|Pickaxe ([[Pickaxes]])|COMMON ([[Rarity]])|Item Stats|+190||
|[[Promising Pickaxe]]|[[Promising Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+50||
|[[Promising Pickaxe]]|[[Promising Pickaxe]]'s Stored Potential|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Ability|+0 → +250||
|[[Jungle Pickaxe]]|[[Jungle Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+330|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Fractured Mithril Pickaxe]]|[[Fractured Mithril Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+225||
|[[Bandaged Mithril Pickaxe]]|[[Bandaged Mithril Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+250|Heart of the Mountain Tier 2 ([[Heart of the Mountain]])|
|[[Mithril Pickaxe]]|[[Mithril Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+300|Heart of the Mountain Tier 2 ([[Heart of the Mountain]])|
|[[Refined Mithril Pickaxe]]|[[Refined Mithril Pickaxe]]|Pickaxe ([[Pickaxes]])|RARE ([[Rarity]])|Item Stats|+350|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|[[Rusty Titanium Pickaxe]]|[[Rusty Titanium Pickaxe]]|Pickaxe ([[Pickaxes]])|UNCOMMON ([[Rarity]])|Item Stats|+100||
|[[Titanium Pickaxe]]|[[Titanium Pickaxe]]|Pickaxe ([[Pickaxes]])|RARE ([[Rarity]])|Item Stats|+140|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|[[Polished Titanium Pickaxe]]|[[Polished Titanium Pickaxe]]|Pickaxe ([[Pickaxes]])|RARE ([[Rarity]])|Item Stats|+200|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Stonk]]|[[Stonk]]|Pickaxe ([[Pickaxes]])|EPIC ([[Rarity]])|Item Stats|+380||
|[[Pickonimbus 2000]]|[[Pickonimbus 2000]]|Pickaxe ([[Pickaxes]])|EPIC ([[Rarity]])|Item Stats|+750|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Bingonimbus 2000]]|[[Bingonimbus 2000]]|Pickaxe ([[Pickaxes]])|EPIC ([[Rarity]])|Item Stats|+1500||
|[[Pioneer Pickaxe]]|[[Pioneer Pickaxe]]|Pickaxe ([[Pickaxes]])|SPECIAL ([[Rarity]])|Item Stats|+1||
|[[Elle's Pickaxe]]|[[Elle's Pickaxe]]|Pickaxe ([[Pickaxes]])|SPECIAL ([[Rarity]])|Item Stats|+250||
|[[Mithril Drill SX-R226]]|[[Mithril Drill SX-R226]]|Drill ([[Drills]])|RARE ([[Rarity]])|Item Stats|+450|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|[[Mithril Drill SX-R326]]|[[Mithril Drill SX-R326]]|Drill ([[Drills]])|RARE ([[Rarity]])|Item Stats|+600|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Ruby Drill TX-15]]|[[Ruby Drill TX-15]]|Drill ([[Drills]])|RARE ([[Rarity]])|Item Stats|+150|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Gemstone Drill LT-522]]|[[Gemstone Drill LT-522]]|Drill ([[Drills]])|RARE ([[Rarity]])|Item Stats|+300|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Topaz Drill KGR-12]]|[[Topaz Drill KGR-12]]|Drill ([[Drills]])|EPIC ([[Rarity]])|Item Stats|+450|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Jasper Drill X]]|[[Jasper Drill X]]|Drill ([[Drills]])|EPIC ([[Rarity]])|Item Stats|+600|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X355]]|[[Titanium Drill DR-X355]]|Drill ([[Drills]])|EPIC ([[Rarity]])|Item Stats|+700|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X455]]|[[Titanium Drill DR-X455]]|Drill ([[Drills]])|EPIC ([[Rarity]])|Item Stats|+900|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X555]]|[[Titanium Drill DR-X555]]|Drill ([[Drills]])|EPIC ([[Rarity]])|Item Stats|+1200|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X655]]|[[Titanium Drill DR-X655]]|Drill ([[Drills]])|LEGENDARY ([[Rarity]])|Item Stats|+1600|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Divan's Drill]]|[[Divan's Drill]]|Drill ([[Drills]])|MYTHIC ([[Rarity]])|Item Stats|+1800|Heart of the Mountain Tier 7 ([[Heart of the Mountain]])|
|[[Ruby Drill TX-15]]|[[Ruby Drill TX-15]]|Drill ([[Drills]])|RARE ([[Rarity]])||+800|Heart of the Mountain Tier 4 ([[Heart of the Mountain]]); On Gemstones ([[Gemstone]])|
|[[Gemstone Drill LT-522]]|[[Gemstone Drill LT-522]]|Drill ([[Drills]])|RARE ([[Rarity]])||+800|Heart of the Mountain Tier 4 ([[Heart of the Mountain]]); On Gemstones ([[Gemstone]])|
|[[Topaz Drill KGR-12]]|[[Topaz Drill KGR-12]]|Drill ([[Drills]])|EPIC ([[Rarity]])||+800|Heart of the Mountain Tier 5 ([[Heart of the Mountain]]); On Gemstones ([[Gemstone]])|
|[[Jasper Drill X]]|[[Jasper Drill X]]|Drill ([[Drills]])|EPIC ([[Rarity]])||+800|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); On Gemstones ([[Gemstone]])|
|[[Ruby Drill TX-15]]|[[Ruby Drill TX-15]]|Drill ([[Drills]])|RARE ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Gemstone Drill LT-522]]|[[Gemstone Drill LT-522]]|Drill ([[Drills]])|RARE ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Topaz Drill KGR-12]]|[[Topaz Drill KGR-12]]|Drill ([[Drills]])|EPIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Jasper Drill X]]|[[Jasper Drill X]]|Drill ([[Drills]])|EPIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X455]]|[[Titanium Drill DR-X455]]|Drill ([[Drills]])|EPIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X555]]|[[Titanium Drill DR-X555]]|Drill ([[Drills]])|EPIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Titanium Drill DR-X655]]|[[Titanium Drill DR-X655]]|Drill ([[Drills]])|LEGENDARY ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Divan's Drill]]|[[Divan's Drill]]|Drill ([[Drills]])|MYTHIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 7 ([[Heart of the Mountain]])|
|[[Divan's Drill]]|[[Divan's Drill]]|Drill ([[Drills]])|MYTHIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 7 ([[Heart of the Mountain]])|
|[[Divan's Drill]]|[[Divan's Drill]]|Drill ([[Drills]])|MYTHIC ([[Rarity]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 7 ([[Heart of the Mountain]]); 1 Flawless Jade ([[Gemstone]]), 1 Flawless Amber ([[Gemstone]]) and 1 Flawless Topaz Gemstones ([[Gemstone]]), 250,000 [[Coins]]|
|Slot|Item|Type|Source|Mining Speed|Condition|
|-|-|-|-|-|-|
|[[Bingo Pet]]|[[Bingo Pet]]|All Skills RARE ([[Rarity]])+|Chimera perk|+0.4% → 40% Pet Stats|Base Stats of the active Pet.|
|[[Mole Pet]]|[[Mole Pet]]|Mining LEGENDARY ([[Rarity]])|Pet Stats|+1 → 150||
|[[Scatha Pet]]|[[Scatha Pet]]|Mining RARE ([[Rarity]])+|Pet Stats|+1 → 100||
|[[Glacite Golem Pet]]|[[Glacite Golem Pet]]|Mining COMMON ([[Rarity]])+|Pet Stats|+1 → 125||
|[[Goblin Pet]]|[[Goblin Pet]]|Mining LEGENDARY ([[Rarity]])|Grunt Work perk|+2.5 → 250|[[Ores]], including Pure Ores ([[Ores]])|
|[[Goblin Pet]]|[[Goblin Pet]]|Mining LEGENDARY ([[Rarity]])||+1250|[[Ores]], excluding Pure Ores ([[Ores]])|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|Mining COMMON ([[Rarity]])|Mithril Affinity perk|+1 → 100|[[Mithril]]|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|Mining UNCOMMON ([[Rarity]]) → RARE ([[Rarity]])|Mithril Affinity perk|+1.5 → 150|[[Mithril]]|
|[[Mithril Golem Pet]]|[[Mithril Golem Pet]]|Mining EPIC ([[Rarity]])+|Mithril Affinity perk|+2 → 200|[[Mithril]]|
|[[Silverfish Pet]]|[[Silverfish Pet]]|Mining LEGENDARY ([[Rarity]])|Dexterity perk|+1.5 → 150||
|[[Silverfish Pet]]|[[Silverfish Pet]]|Mining LEGENDARY ([[Rarity]])|Dexterity perk|+50 → 150|On islands using the "Skyblock Mining System ([[Block Strength]])" and without a higher Haste ([[Haste Potion]]) effect active through other means|
|[[Bejeweled Collar]]|[[Bejeweled Collar]]|Pet Item ([[Pet Items]]) RARE ([[Rarity]])|Pet Stats|+25||
|[[Quick Claw]]|[[Quick Claw]]|Pet Item ([[Pet Items]]) EPIC ([[Rarity]])|Pet Stats|+1 / 2 Pet Levels|Pet Level|
|[[Minos Relic]]|[[Minos Relic]]|Pet Item ([[Pet Items]]) EPIC ([[Rarity]])|Pet Stats|+33% Pet Stats||
|[[Hephaestus Relic]]|[[Hephaestus Relic]]|Pet Item ([[Pet Items]]) LEGENDARY ([[Rarity]])|Pet Stats|+50% Pet Stats||
|Slot|Item|Rarity|Type|Source|Mining Speed|Requirement|
|-|-|-|-|-|-|-|
|[[Ember Ash Armor]]|[[Ember Ash Armor]]|UNCOMMON ([[Rarity]])|[[Armor]] Set|Item Stats|+60||
|[[Lapis Armor]]|[[Lapis Armor]]|UNCOMMON ([[Rarity]])|[[Armor]] Set|Item Stats|+80|Mining V (5) ([[Mining]])|
|[[Prospecting Armor]]|[[Prospecting Armor]]|UNCOMMON ([[Rarity]])|[[Armor]] Set|Item Stats|+60||
|[[Prospecting Armor]]|[[Prospecting Armor]]|UNCOMMON ([[Rarity]])|[[Armor]] Set|Full Set Bonus: Beginner's Boost|+40||
|[[Miner Armor]]|[[Miner Armor]]|RARE ([[Rarity]])|[[Armor]] Set|Item Stats|+40||
|[[Goblin Armor]]|[[Goblin Armor]]|RARE ([[Rarity]])|[[Armor]] Set|Item Stats|+40||
|[[Goblin Armor]]|[[Goblin Armor]]|RARE ([[Rarity]])|[[Armor]] Set|Full Set Bonus: Smart Miner|+1 / 15 [[Intelligence]] removed||
|[[Glacite Armor]]|[[Glacite Armor]]|EPIC ([[Rarity]])|[[Armor]] Set|Item Stats|+40||
|[[Glacite Armor]]|[[Glacite Armor]]|EPIC ([[Rarity]])|[[Armor]] Set|Full Set Bonus: Expert Miner|+2 / [[Mining]] level||
|[[Heat Armor]]|[[Heat Armor]]|RARE ([[Rarity]])|[[Armor]] Set|Item Stats|+60|Hard Stone II (2) ([[Hard Stone]])|
|[[Flamebreaker Armor]]|[[Flamebreaker Armor]]|EPIC ([[Rarity]])|[[Armor]] Set|Item Stats|+100|Hard Stone V (5) ([[Hard Stone]])|
|[[Yog Armor]]|[[Yog Armor]]|EPIC ([[Rarity]])|[[Armor]] Set|Item Stats|+100|Hard Stone V (5) ([[Hard Stone]])|
|[[Yog Armor]]|[[Yog Armor]]|EPIC ([[Rarity]])|[[Armor]] Set|Full Set Bonus: Absorb|+1 → 500|Hard Stone V (5) ([[Hard Stone]])|
|[[Sorrow Armor]]|[[Sorrow Armor]]|LEGENDARY ([[Rarity]])|[[Armor]] Set|Item Stats|+200|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Armor of Divan]]|[[Armor of Divan]]|LEGENDARY ([[Rarity]])|[[Armor]] Set|Item Stats|+320|Heart of the Mountain Tier 6 ([[Heart of the Mountain]])|
|[[Goblin Armor]]|Goblin Helmet ([[Goblin Armor]])|RARE ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|5,000 [[Coins]]|
|[[Goblin Armor]]|Goblin Chestplate ([[Goblin Armor]])|RARE ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|5,000 [[Coins]]|
|[[Goblin Armor]]|Goblin Leggings ([[Goblin Armor]])|RARE ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|5,000 [[Coins]]|
|[[Goblin Armor]]|Goblin Boots ([[Goblin Armor]])|RARE ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|5,000 [[Coins]]|
|[[Glacite Armor]]|Glacite Helmet ([[Glacite Armor]])|EPIC ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x||
|[[Glacite Armor]]|Glacite Chestplate ([[Glacite Armor]])|EPIC ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x||
|[[Glacite Armor]]|Glacite Leggings ([[Glacite Armor]])|EPIC ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x||
|[[Glacite Armor]]|Glacite Boots ([[Glacite Armor]])|EPIC ([[Rarity]])|Boots|[[Gemstone Slot]]|+x||
|[[Flamebreaker Armor]]|Flamebreaker Helmet ([[Flamebreaker Armor]])|EPIC ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Flamebreaker Armor]]|Flamebreaker Chestplate ([[Flamebreaker Armor]])|EPIC ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Flamebreaker Armor]]|Flamebreaker Leggings ([[Flamebreaker Armor]])|EPIC ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Flamebreaker Armor]]|Flamebreaker Boots ([[Flamebreaker Armor]])|EPIC ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Yog Armor]]|Yog Helmet ([[Yog Armor]])|EPIC ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Yog Armor]]|Yog Chestplate ([[Yog Armor]])|EPIC ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Yog Armor]]|Yog Leggings ([[Yog Armor]])|EPIC ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Yog Armor]]|Yog Boots ([[Yog Armor]])|EPIC ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]]); 1 Fine Amber Gemstone ([[Gemstone]]), 5,000 [[Coins]]|
|[[Yog Armor]]|Yog Helmet ([[Yog Armor]])|EPIC ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]])|
|[[Yog Armor]]|Yog Chestplate ([[Yog Armor]])|EPIC ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]])|
|[[Yog Armor]]|Yog Leggings ([[Yog Armor]])|EPIC ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]])|
|[[Yog Armor]]|Yog Boots ([[Yog Armor]])|EPIC ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Hard Stone V (5) ([[Hard Stone]])|
|[[Sorrow Armor]]|Sorrow Helmet ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Sorrow Armor]]|Sorrow Chestplate ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Sorrow Armor]]|Sorrow Leggings ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Sorrow Armor]]|Sorrow Boots ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Sorrow Armor]]|Sorrow Helmet ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]]); 20 Fine Jade ([[Gemstone]]), 20 Fine Amber ([[Gemstone]]), 20 Fine Topaz ([[Gemstone]]), 20 Fine Ruby ([[Gemstone]]), 20 Fine Amethyst ([[Gemstone]]), 20 Fine Sapphire ([[Gemstone]]) and 20 Fine Jasper Gemstones ([[Gemstone]]), 100,000 [[Coins]]|
|[[Sorrow Armor]]|Sorrow Chestplate ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]]); 20 Fine Jade ([[Gemstone]]), 20 Fine Amber ([[Gemstone]]), 20 Fine Topaz ([[Gemstone]]), 20 Fine Ruby ([[Gemstone]]), 20 Fine Amethyst ([[Gemstone]]), 20 Fine Sapphire ([[Gemstone]]) and 20 Fine Jasper Gemstones ([[Gemstone]]), 100,000 [[Coins]]|
|[[Sorrow Armor]]|Sorrow Leggings ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]]); 20 Fine Jade ([[Gemstone]]), 20 Fine Amber ([[Gemstone]]), 20 Fine Topaz ([[Gemstone]]), 20 Fine Ruby ([[Gemstone]]), 20 Fine Amethyst ([[Gemstone]]), 20 Fine Sapphire ([[Gemstone]]) and 20 Fine Jasper Gemstones ([[Gemstone]]), 100,000 [[Coins]]|
|[[Sorrow Armor]]|Sorrow Boots ([[Sorrow Armor]])|LEGENDARY ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 5 ([[Heart of the Mountain]]); 20 Fine Jade ([[Gemstone]]), 20 Fine Amber ([[Gemstone]]), 20 Fine Topaz ([[Gemstone]]), 20 Fine Ruby ([[Gemstone]]), 20 Fine Amethyst ([[Gemstone]]), 20 Fine Sapphire ([[Gemstone]]) and 20 Fine Jasper Gemstones ([[Gemstone]]), 100,000 [[Coins]]|
|[[Armor of Divan]]|Helmet of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Helmet of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Helmet|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Chestplate of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Chestplate of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Chestplate|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Leggings of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Leggings of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Leggings|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Boots of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|[[Armor of Divan]]|Boots of Divan ([[Armor of Divan]])|LEGENDARY ([[Rarity]])|Boots|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 6 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|Slot|Item|Rarity|Type|Source|Mining Speed|Condition|
|-|-|-|-|-|-|-|
|[[Mithril Necklace]]/[[Mithril Cloak]]/[[Mithril Belt]]/[[Mithril Gauntlet]]|[[Mithril Equipment]]|UNCOMMON ([[Rarity]])|[[Equipment]] Set|Item Stats|+80|Heart of the Mountain Tier 2 ([[Heart of the Mountain]])|
|(same as above)|[[Mithril Equipment]]|UNCOMMON ([[Rarity]])|[[Equipment]] Set|Dwarf Wannabe Full Set Bonus|+30|Heart of the Mountain Tier 2 ([[Heart of the Mountain]]); [[Dwarven Mines]]. Does not include the [[Glacite Tunnels]].|
|[[Titanium Necklace]]/[[Titanium Cloak]]/[[Titanium Belt]]/[[Titanium Gauntlet]]|[[Titanium Equipment]]|RARE ([[Rarity]])|[[Equipment]] Set|Item Stats|+120|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|(same as above)|[[Titanium Equipment]]|RARE ([[Rarity]])|[[Equipment]] Set|True Dwarf Full Set Bonus|+50|Heart of the Mountain Tier 3 ([[Heart of the Mountain]]); [[Dwarven Mines]]. Does not include the [[Glacite Tunnels]].|
|[[Amber Necklace]]/[[Sapphire Cloak]]/[[Jade Belt]]/[[Amethyst Gauntlet]]|[[Gemstone Equipment]]|EPIC ([[Rarity]])|[[Equipment]] Set|Item Stats|+120|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Dwarven Handwarmers]]|[[Dwarven Handwarmers]]|EPIC ([[Rarity]])|[[Gloves]]|Item Stats|+45|Heart of the Mountain Tier 8 ([[Heart of the Mountain]])|
|[[Pendant of Divan]]|[[Pendant of Divan]]|LEGENDARY ([[Rarity]])|Necklace ([[Necklaces]])|Item Stats|+100|Heart of the Mountain Tier 10 ([[Heart of the Mountain]])|
|[[Pendant of Divan]]|[[Pendant of Divan]]|LEGENDARY ([[Rarity]])|Necklace ([[Necklaces]])|[[Gemstone Slot]]|+x|Heart of the Mountain Tier 10 ([[Heart of the Mountain]]); 1 [[Gemstone Chamber]]|
|Slot|Item|Rarity|Source|Mining Speed|Condition|
|-|-|-|-|-|-|
|[[Haste Ring]]|[[Haste Ring]]|RARE ([[Rarity]])|Item Stats|+10||
|[[Haste Ring]]|[[Haste Ring]]|RARE ([[Rarity]])||+100|On islands using the "Skyblock Mining System ([[Block Strength]])" and without a higher Haste ([[Haste Potion]]) effect active through other means|
|[[Haste Artifact]]|[[Haste Artifact]]|EPIC ([[Rarity]])|Item Stats|+25||
|[[Haste Artifact]]|[[Haste Artifact]]|EPIC ([[Rarity]])||+150|On islands using the "Skyblock Mining System ([[Block Strength]])" and without a higher Haste ([[Haste Potion]]) effect active through other means|
|[[Titanium Talisman]]|[[Titanium Talisman]]|UNCOMMON ([[Rarity]])|Item Stats|+15|Heart of the Mountain Tier 2 ([[Heart of the Mountain]])|
|[[Titanium Ring]]|[[Titanium Ring]]|RARE ([[Rarity]])|Item Stats|+30|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|[[Titanium Artifact]]|[[Titanium Artifact]]|EPIC ([[Rarity]])|Item Stats|+45|Heart of the Mountain Tier 4 ([[Heart of the Mountain]])|
|[[Titanium Relic]]|[[Titanium Relic]]|LEGENDARY ([[Rarity]])|Item Stats|+60|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Talisman of Power]]|[[Talisman of Power]]|COMMON ([[Rarity]]) → UNCOMMON ([[Rarity]])|Gemstone Slot|+x at 50% efficiency||
|[[Ring of Power]]|[[Ring of Power]]|UNCOMMON ([[Rarity]]) → RARE ([[Rarity]])|Gemstone Slot|+x at 50% efficiency||
|[[Artifact of Power]]|[[Artifact of Power]]|RARE ([[Rarity]]) → EPIC ([[Rarity]])|Gemstone Slot|+x at 50% efficiency||
|[[Relic of Power]]|[[Relic of Power]]|EPIC ([[Rarity]]) → LEGENDARY ([[Rarity]])|Gemstone Slot|+x at 50% efficiency|Heart of the Mountain Tier 10 ([[Heart of the Mountain]])|
|[[Speed Relic]]|[[Speed Relic]]|EPIC ([[Rarity]])|Item Stats|+1||
Drill Parts:
|Slot|Item|Type|Rarity|Source|Target|Mining Speed|Condition|
|-|-|-|-|-|-|-|-|
|[[Starfall Seasoning]]|[[Starfall Seasoning]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+25|Heart of the Mountain Tier 2 ([[Heart of the Mountain]])|
|[[Starfall Seasoning]]|[[Starfall Seasoning]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])||Drill ([[Drills]])|+25|Heart of the Mountain Tier 2 ([[Heart of the Mountain]]); Within 20 blocks of a Fallen Star ([[Fallen Stars]]).|
|[[Mithril-Plated Drill Engine]]|[[Mithril-Plated Drill Engine]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+75|Heart of the Mountain Tier 3 ([[Heart of the Mountain]])|
|[[Titanium-Plated Drill Engine]]|[[Titanium-Plated Drill Engine]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+150|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
|[[Ruby-Polished Drill Engine]]|[[Ruby-Polished Drill Engine]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+250|Heart of the Mountain Tier 7 ([[Heart of the Mountain]])|
|[[Sapphire-Polished Drill Engine]]|[[Sapphire-Polished Drill Engine]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+400|Heart of the Mountain Tier 8 ([[Heart of the Mountain]])|
|[[Amber-Polished Drill Engine]]|[[Amber-Polished Drill Engine]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|+600|Heart of the Mountain Tier 9 ([[Heart of the Mountain]])|
|[[Blue Cheese Goblin Omelette]]|[[Blue Cheese Goblin Omelette]]|Drill Part ([[Drill Parts]])|RARE ([[Rarity]])|Item Stats|Drill ([[Drills]])|See Mining Speed#Perks tab|Heart of the Mountain Tier 5 ([[Heart of the Mountain]])|
[Enchantments]
|Slot|Item|Type|Rarity|Source|Target|Mining Speed|Condition|
||[[Enchanted Book]] (Efficiency I–V ([[Efficiency]]))|Enchantment ([[Enchantments]])|COMMON ([[Rarity]]) → UNCOMMON ([[Rarity]])||Axe ([[Axes]]), Pickaxe ([[Pickaxes]]), Shovel ([[Shovels]]), Drill ([[Drills]]), [[Shears]], [[Gauntlet]]|+30 → 110||
|[[Silex]]|[[Silex]] (Efficiency VI–X ([[Efficiency]]))|Enchantment ([[Enchantments]])|EPIC ([[Rarity]])||Pickaxe ([[Pickaxes]]), Drill ([[Drills]]), [[Gauntlet]]|+110 → 210|[[Efficiency]] n−1 applied.|
||[[Enchanted Book]] (Lapidary I–V ([[Lapidary]]))|Enchantment ([[Enchantments]])|COMMON ([[Rarity]]) → UNCOMMON ([[Rarity]])||Pickaxe ([[Pickaxes]]), Drill ([[Drills]]), [[Gauntlet]]|+20 → 100|Enchanting XXII (22) ([[Enchanting]]); On Gemstones ([[Gemstone]]).|
||[[Enchanted Book]] (Flowstate I–III ([[Flowstate]]))|Enchantment ([[Enchantments]])|COMMON ([[Rarity]]) → UNCOMMON ([[Rarity]])||Pickaxe ([[Pickaxes]]), Drill ([[Drills]]), [[Gauntlet]]|+1 → 600|Enchanting XV (15) ([[Enchanting]]); Last block was mined in the last 10 seconds in the same world.|
||[[Enchanted Book]] (Chimera I–V ([[Chimera]]))|Enchantment ([[Enchantments]])|COMMON ([[Rarity]]) → UNCOMMON ([[Rarity]])||[[Gauntlet]], Longsword ([[Longswords]]), Sword ([[Swords]])|Copies +20% → 100% of the active Pet Stats|Enchanting XXXI (31) ([[Enchanting]])|
[Other]
|Slot|Item|Type|Rarity|Source|Target|Mining Speed|Condition|
|[[Divan's Powder Coating]]|[[Divan's Powder Coating]]|Item Upgrade ([[Item Upgrades]])|LEGENDARY ([[Rarity]])||Drill ([[Drills]])|+500||
|[[Power Scrolls]]|Amber Power Scroll ([[Power Scrolls]])|Power Scroll ([[Power Scrolls]])|EPIC ([[Rarity]])||Any item with a Right-Click ability [Confirm]|+30|For 5 seconds after using a Right-Click ability.|
|[[Polarvoid Book]]|[[Polarvoid Book]]|Item Upgrade ([[Item Upgrades]])|RARE ([[Rarity]])||Drill ([[Drills]])|+10 → 50||
|[[Recombobulator 3000]]|[[Recombobulator 3000]]|Item Upgrade ([[Item Upgrades]])|LEGENDARY ([[Rarity]])||Nearly all items|||
[Gemstones]
|Slot|Item|Type|Rarity|Source|Target|Mining Speed|Condition|
|Slot|Item|Type|Rarity|Source|Target|C ([[Rarity]]), U ([[Rarity]]), R ([[Rarity]]), E ([[Rarity]]), L ([[Rarity]]), M ([[Rarity]]), D ([[Rarity]])|Condition|
|[[Gemstone]]|Rough Amber Gemstone ([[Gemstone]])|Gemstone|||Multiple|04, 08, 12, 16, 20, 24, 28||
|[[Gemstone]]|Flawed Amber Gemstone ([[Gemstone]])|Gemstone|||Multiple|06, 10, 14, 18, 24, 30, 36||
|[[Gemstone]]|Fine Amber Gemstone ([[Gemstone]])|Gemstone|||Multiple|10, 14, 20, 28, 36, 45, 54||
|[[Gemstone]]|Flawless Amber Gemstone ([[Gemstone]])|Gemstone|||Multiple|14, 20, 30, 44, 58, 75, 92||
|[[Gemstone]]|Perfect Amber Gemstone ([[Gemstone]])|Gemstone|||Multiple|020, 028, 040, 060, 080, 100, 120||
[Reforges]
|Slot|Item|Type|Rarity|Source|Target|Mining Speed|Condition|
|Slot|Item|Type|Rarity|Source|Target|C ([[Rarity]]), U ([[Rarity]]), R ([[Rarity]]), E ([[Rarity]]), L ([[Rarity]]), M ([[Rarity]]), D ([[Rarity]])|Condition|
||Prospector's ([[Reforging]])|Basic Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|0, ?||
||Unyielding ([[Reforging]])|Basic Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|0, ?||
||Fortunate ([[Reforging]])|Basic Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|01, 02, 03, 04, 06, 08, 10||
||Sturdy ([[Reforging]])|Basic Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|03, 06, 09, 12, 15, 20, 25||
||Excellent ([[Reforging]])|Basic Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|04, 08, 12, 16, 20, 25, ??||
|[[Andesite Whetstone]]|[[Andesite Whetstone]] (Refined ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|[0]|Mining XXV (25) ([[Mining]])|
|[[Frigid Husk]]|[[Frigid Husk]] (Glacial ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|[0]|Mining XXX (30) ([[Mining]])|
|[[Pocket Iceberg]]|[[Pocket Iceberg]] (Scraped ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|[0]|Mining XXV (25) ([[Mining]])|
|[[Pure Mithril]]|[[Pure Mithril]] (Mithraic ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|[0]|Mining XVIII (18) ([[Mining]])|
|[[Black Diamond]]|[[Black Diamond]] (Fruitful ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|05, 10, 15, 25, 40, 55, 70|Mining II (2) ([[Mining]])|
|[[Petrified Starfall]]|[[Petrified Starfall]] (Stellar ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|05, 10, 15, 25, 40, 55, 70|Mining XXVI (26) ([[Mining]])|
|[[Scorched Topaz]]|[[Scorched Topaz]] (Heated ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|05, 10, 15, 25, 40, 55, 70||
|[[Scorched Topaz]]|[[Scorched Topaz]] (Heated ([[Reforging]]))|Unique Reforge ([[Reforging]])||Reforge Bonus|Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|[+x / +1 Heat]; 1.0, 1.4, 1.8, 2.2, 2.8, 3.4, 4.0||
|[[Gleaming Crystal]]|[[Gleaming Crystal]] (Lustrous ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|10, 20, 30, 40, 50, 60, 75|Mining XXIV (24) ([[Mining]])|
|[[Diamonite]]|[[Diamonite]] (Fleet ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|010, 020, 030, 040, 050, 075, 100|Mining XV (15) ([[Mining]])|
|[[Dwarven Geode]]|[[Dwarven Geode]] (Auspicious ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|010, 020, 030, 040, 050, 075, 100|Mining XXI (21) ([[Mining]])|
|[[Lapis Crystal]]|[[Lapis Crystal]] (Magnetic ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|010, 020, 030, 040, 050, 075, 100|Mining V (5) ([[Mining]])|
|[[Amber Material]]|[[Amber Material]] (Ambered ([[Reforging]]))|Unique Reforge ([[Reforging]])|||Pickaxe ([[Pickaxes]]), Drill ([[Drills]])|025, 035, 050, 075, 100, 150, 200|Mining XXX (30) ([[Mining]])|
|[[Titanium Tesseract]]|[[Titanium Tesseract]] (Dimensional ([[Reforging]]))|Unique Reforge ([[Reforging]])|||[[Armor]]|10, 15, 20, 30, 40, 50|Mining XX (20) ([[Mining]])|
|[[Jaderald]]|[[Jaderald]] (Jaded ([[Reforging]]))|Unique Reforge ([[Reforging]])|||[[Armor]]|05, 12, 20, 30, 45, 60, ??|Mining XXX (30) ([[Mining]])|
|[[Blazen Sphere]]|[[Blazen Sphere]] (Blazing ([[Reforging]]))|Unique Reforge ([[Reforging]])|||[[Equipment]]|00, ??|Mining XXVII (27) ([[Mining]])|
|[[Dwarven Treasure]]|[[Dwarven Treasure]] (Royal ([[Reforging]]))|Unique Reforge ([[Reforging]])|||[[Equipment]]|04, 06, 08, 10, 14, 18, ??|Mining XIV (14) ([[Mining]])|
|Slot|Shard|Attribute|Rarity|Mining Speed|Condition|
|-|-|-|-|-|-|
|[[Miner Zombie Shard]]|[[Miner Zombie Shard]]|Rotten Pickaxe ([[Attributes]])|COMMON ([[Rarity]])|+3 → 30||
|[[Quartzfang Shard]]|[[Quartzfang Shard]]|Quartz Speed ([[Attributes]]),|RARE ([[Rarity]])|+10 → 100|During [[Weather]], on [[Mining Islands]]|
|[[Nilbog Shard]]|[[Nilbog Shard]]|Royal Riches ([[Attributes]])|EPIC ([[Rarity]])|+5 → 50|[[Mines of Divan]]|
|Perk|Type|Mining Speed|Condition|
|-|-|-|-|
|Mining Speed|[[Heart of the Mountain]] perk|+20 → +1000||
|Mining Speed|[[Heart of the Mountain]] perk|+40 → +1020|[[Blue Cheese Goblin Omelette]]|
|Pickaxe Ability: Mining Speed Boost|[[Heart of the Mountain]] perk|+200% for 10 seconds||
|Pickaxe Ability: Mining Speed Boost|[[Heart of the Mountain]] perk|+250% for 15 seconds|[[Blue Cheese Goblin Omelette]] or Center of the Mountain Tier 2 or above.|
|Pickaxe Ability: Mining Speed Boost|[[Heart of the Mountain]] perk|+300% for 20 seconds|[[Blue Cheese Goblin Omelette]] and Center of the Mountain Tier 2 or above.|
|Precision Mining|[[Heart of the Mountain]] perk|+30%|Aiming at a critical particle while mining [[Ores]], Pure Ores ([[Ores]]) or [[Dwarven Metals]]|
|Sky Mall|[[Heart of the Mountain]] perk|+100|[[Mining Islands]]|
|Professional|[[Heart of the Mountain]] perk|+55 → +750|Gemstones ([[Gemstone]])|
|Professional|[[Heart of the Mountain]] perk|+60 → +755|Gemstones ([[Gemstone]]); [[Blue Cheese Goblin Omelette]]|
|Front Loaded|[[Heart of the Mountain]] perk|+250|First 2,500 Gemstones ([[Gemstone]]) mined each day. Resets at 12:00:00 am UTC.|
|Speedy Mineman|[[Heart of the Mountain]] perk|+40 → +2000||
|Speedy Mineman|[[Heart of the Mountain]] perk|+80 → +2040|[[Blue Cheese Goblin Omelette]]|
|Strong Arm|[[Heart of the Mountain]] perk|+5 → +500|[[Dwarven Metals]]|
|Strong Arm|[[Heart of the Mountain]] perk|+10 → +505|[[Dwarven Metals]]; [[Blue Cheese Goblin Omelette]]|
|Mineshaft Mayhem|[[Heart of the Mountain]] perk|+200|[[Glacite Mineshafts]]|
|Eager Adventurer|[[Heart of the Mountain]] perk|+4 → +400|[[Glacite Mineshafts]]|
|Eager Adventurer|[[Heart of the Mountain]] perk|+8 → +404|[[Glacite Mineshafts]]; [[Blue Cheese Goblin Omelette]]|
|Eager Miner|Essence Shop ([[Essence Shops]]) perk|+10 → +100|Mining Islands|
|Slot|Item|Type|Mining Speed|Condition|
|-|-|-|-|-|
|[[Dwarven Lantern]]|[[Dwarven Lantern]]|Deployable ([[Deployables]])|+20 for 5 minutes||
|[[Mithril Lantern]]|[[Mithril Lantern]]|Deployable ([[Deployables]])|+40 for 5 minutes||
|[[Titanium Lantern]]|[[Titanium Lantern]]|Deployable ([[Deployables]])|+60 for 5 minutes||
|[[Glacite Lantern]]|[[Glacite Lantern]]|Deployable ([[Deployables]])|+80 for 5 minutes||
|[[Will-o'-wisp]]|[[Will-o'-wisp]]|Deployable ([[Deployables]])|+100 for 5 minutes||
|[[Haste Potion]]|Haste 1-4 ([[Haste Potion]])|Potion Effect ([[Potions]])|+50 → 200|On islands using the "Skyblock Mining System ([[Block Strength]])" and without a higher Haste ([[Haste Potion]]) effect active through other means|
|Item|Type|Mining Speed|Condition|
|-|-|-|-|
|[[Better Together]]|Mining Event ([[Dwarven Mines]])|+0 → 1250|1 → 5 or more other players in the same Zone ([[Locations]]).|
|Breeze ([[Weather]])|[[Weather]]|+100|[[Dwarven Mines]]; [[Crystal Hollows]]; [[Glacite Tunnels]]|
|Mist ([[Weather]])|[[Weather]]|+250|[[Dwarven Mines]]|
|Rockfall ([[Weather]])|[[Weather]]|+250|[[Crystal Hollows]]|
|Snowstorm ([[Weather]])|[[Weather]]|+250|[[Glacite Tunnels]]|
## Theoretical maximum Mining Speed
The following setup produces the highest known displayed Mining Speed. Block specific variants are listed separately because they are added only when mining their respective target and are not affected by Mining Speed multipliers.
### Raw Mining Speed
Maximum Raw Mining Speed as of 0.27.1:
|Mining Speed|Type of source|Source|
|-|-|-|
|1,000|HotM ([[Heart of the Mountain]]) perk|Mining Speed at level 50|
|2,000|HotM ([[Heart of the Mountain]]) perk|Speedy Mineman at level 50|
|30|Attribute ([[Attributes]])|Rotten Pickaxe 10 ([[Attributes]]) ( [[Miner Zombie Shard]])|
|100|[[Equipment]]|[[Pendant of Divan]]|
|100|[[Gemstone]]|1 Perfect Amber Gemstone ([[Gemstone]]) applied on a MYTHIC ([[Rarity]]) [[Pendant of Divan]] ( [[Recombobulator 3000]]).|
|30|[[Equipment]]|[[Sapphire Cloak]]|
|30|[[Equipment]]|[[Jade Belt]]|
|45|[[Equipment]]|[[Dwarven Handwarmers]]|
|60|Accessory ([[Accessories]])|[[Titanium Relic]]|
|25|Accessory ([[Accessories]])|[[Haste Artifact]]|
|1|Accessory ([[Accessories]])|[[Speed Relic]]|
|50|Accessory ([[Accessories]])|MYTHIC ([[Rarity]]) [[Relic of Power]] with all its gemstone slots filled with Perfect Gemstones, including 1 Perfect Amber Gemstone ([[Gemstone]]) ( [[Recombobulator 3000]]).|
|1,800|Drill ([[Drills]])|[[Divan's Drill]]|
|600|Drill Part ([[Drill Parts]])|[[Amber-Polished Drill Engine]]|
|210|Enchantment ([[Enchantments]])|Efficiency X ([[Efficiency]])|
|240|[[Gemstone]]|2 Perfect Amber Gemstones ([[Gemstone]]) applied on the 2 Amber gemstone slots of a DIVINE ([[Rarity]]) [[Divan's Drill]] ( [[Recombobulator 3000]]).|
|50|Item Upgrade ([[Item Upgrades]])|5 Polarvoid Books ([[Polarvoid Book]])|
|500|Item Upgrade ([[Item Upgrades]])|1 [[Divan's Powder Coating]] applied on a Drill ([[Drills]]).|
[Σpermanent and unconditional and optimal=6,871]
|60|Drill Part ([[Drill Parts]])|[[Blue Cheese Goblin Omelette]] cascading onto the Mining Speed and Speedy Mineman perks from HotM ([[Heart of the Mountain]]).|
|120|[[Gemstone]]|1 Perfect Amber Gemstone ([[Gemstone]]) applied on the 1 Mining gemstone slot of a DIVINE ([[Rarity]]) [[Divan's Drill]] ( [[Recombobulator 3000]]).|
|200|Reforge ([[Reforging]])|1 [[Amber Material]] applied on a DIVINE ([[Rarity]]) [[Divan's Drill]] ( [[Recombobulator 3000]]).|
|100|[[Armor]]|[[Yog Armor]]|
|500|[[Armor]]|[[Yog Armor]]'s Full Set Bonus: Absorb and at least 2,500 Yogs ([[Yog]]) killed.|
|640|[[Gemstone]]|8 Perfect Amber Gemstones ([[Gemstone]]) applied on LEGENDARY ([[Rarity]]) Armor ([[Yog Armor]]) ( [[Recombobulator 3000]]).|
|180|Reforge ([[Reforging]])|4 Jaderalds ([[Jaderald]]) applied on LEGENDARY ([[Rarity]]) [[Yog Armor]] ( [[Recombobulator 3000]]).|
|18|Reforge ([[Reforging]])|1 [[Dwarven Treasure]] applied on a MYTHIC ([[Rarity]]) [[Pendant of Divan]] ( [[Recombobulator 3000]]).|
|42|Reforge ([[Reforging]])|3 Dwarven Treasures ([[Dwarven Treasure]]) applied on LEGENDARY ([[Rarity]]) [[Sapphire Cloak]], [[Jade Belt]], [[Dwarven Handwarmers]] ( [[Recombobulator 3000]]).|
|150|Pet ([[Pets]])|[Lv100] LEGENDARY ([[Rarity]]) [[Mole Pet]]|
|75|Pet Item ([[Pet Items]])|[[Hephaestus Relic]] applied on a [Lv100] LEGENDARY ([[Rarity]]) [[Mole Pet]].|
[Σpermanent and unconditional and unoptimal=2,085]
|150|Accessory ([[Accessories]])|[[Haste Artifact]]'s Haste III ([[Haste Potion]]) effect while not mining [[Ice]], [[Sand]], [[Red Sand]], [[Gravel]], [[Mycelium]] or [[Glowstone]], and not on [[Private Island]], [[The Garden]], [[The Park]], the Farming Islands ([[The Farming Islands (disambiguation)]]), Hub ([[Hub Island]]) and the [[Rift Dimension]].|
|100|Shop Perk ([[Shop Perk (disambiguation)]])|Eager Miner ([[Marigold]]) at level 10, on [[Mining Islands]].|
[Σpermanent and conditional=250]
|+300%|HotM ([[Heart of the Mountain]]) perk|Mining Speed Boost ([[Heart of the Mountain]]) for 20 seconds, with a Drill ([[Drills]]) equipped with a [[Blue Cheese Goblin Omelette]].|
|600|Enchantment ([[Enchantments]])|Flowstate III ([[Flowstate]]), after mining 200 blocks in the same world, for 10 seconds, refreshed upon mining another block.|
|100|Deployable ([[Deployables]])|[[Will-o'-wisp]]|
|30|[[Power Scrolls]]|Amber Power Scroll ([[Power Scrolls]]) for 5 seconds after using a Right-Click ability.|
[Σnon permanent and unconditional=730]
|404|HotM ([[Heart of the Mountain]]) perk|Eager Adventurer, in [[Glacite Mineshafts]], with a [[Blue Cheese Goblin Omelette]].|
|100|HotM ([[Heart of the Mountain]]) perk|Sky Mall on the 100 buff, on [[Mining Islands]].|
|200|HotM ([[Heart of the Mountain]]) perk|Mineshaft Mayhem on the 200 buff, in [[Glacite Mineshafts]].|
|50|Potion effect ([[Potions]])|Haste IV ([[Haste Potion]]) gain over Haste III ([[Haste Potion]]) while not mining [[Ice]], [[Sand]], [[Red Sand]], [[Gravel]], [[Mycelium]] or [[Glowstone]], and not on [[Private Island]], [[The Garden]], [[The Park]], the Farming Islands ([[The Farming Islands (disambiguation)]]), Hub ([[Hub Island]]) and the [[Rift Dimension]].|
|+750|Event ([[Dwarven Mines]])|[[Better Together]] mining event, with 3 other players in the same [[Glacite Mineshafts]].|
[Σnon permanent and conditional=1504]
[Σflat increases max=11,440 Mining Speed]
[∑max=45,760 Mining Speed]
### Additional Mining Speed "variants"
The same setup grants the following additional sub-Mining Speeds:
Maximum additional Mining Speed "variants":
|"Variant" of Mining Speed|Type of source|Source|
|-|-|-|
|+30%|HotM ([[Heart of the Mountain]]) perk|Precision Mining ([[Heart of the Mountain]]), while aiming at a critical particle while mining [[Ores]], Pure Ores ([[Ores]]) or [[Dwarven Metals]].|
|+755|HotM ([[Heart of the Mountain]]) perk|Professional ([[Heart of the Mountain]]), on Gemstones ([[Gemstone]]).|
|+250|HotM ([[Heart of the Mountain]]) perk|Front Loaded ([[Heart of the Mountain]]), for the first 2,500 Gemstones ([[Gemstone]]) mined each day. Resets at [More Info Needed].|
|+505|HotM ([[Heart of the Mountain]]) perk|Strong Arm ([[Heart of the Mountain]]), on [[Dwarven Metals]].|
|+500|HotM ([[Heart of the Mountain]]) perk|Strong Arm ([[Heart of the Mountain]]), on Pure Ores ([[Ores]]). This is a hidden buff. Does not scale beyond Level 100.|
|+2,500|HotM ([[Heart of the Mountain]]) perk|Strong Arm ([[Heart of the Mountain]]), on [[Hard Stone]] if the player is not on ground. This is a hidden buff. Does not scale beyond Level 100.|
|+100|Enchantment ([[Enchantments]])|Lapidary V ([[Lapidary]]), on Gemstones ([[Gemstone]]).|
## History
[[Alpha Hypixel Network]]:
|Sep 30, 2026|Fixed Mining Speed Boost ability not updating when switching to another tool.|
[SkyBlock Prototype]
|Jan 15, 2021|0.11|Added Mining Speed.|
|Jul 8, 2026|0.26|Updated Mining Speed Icon|
|Oct 6, 2026|0.27.2|Fixed Mining Speed Boost ability not updating when switching to another tool.|
Linked from: [[Abiphones]], [[Accessories/Misc Crafts]], [[Accessories/Obtained From Collections or Recipes]], [[Accessories/Other]], [[Accessories/September 27 2021 Stacking Fixes]], [[Amber Material]], [[Amber Necklace]], [[Amber-Polished Drill Engine]], [[Amethyst Gauntlet]], [[Ant's Cave]], [[Apprentice Loggers Belt]], [[Armor]], [[Armor of Divan]], [[Armor/Sets]], [[Attack Speed]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Common]], [[Attributes/List/Epic]], [[Attributes/List/Mining]], [[Attributes/List/Rare]], [[Attributes/Search]], [[Bandaged Mithril Pickaxe]], [[Bejeweled Collar]], [[Belts]], [[Better Together]], [[Bingonimbus 2000]], [[Black Diamond]], [[Block Strength]], [[Blocks]], [[Breakable Blocks]], [[Catacombs]], [[Changelog]], [[Changelog/2021/January 15]], [[Changelog/2021/January 20]], [[Changelog/2021/January 27]], [[Changelog/2021/July 14]], [[Cloaks]], [[Cold]], [[Cold Resistance]] (+173 more)

# Mithril Powder
Categories: Confirmations needed, More info needed, Currencies, Mob Drops
[Mithril Powder]
Type: [[Currency]]
᠅ Mithril Powder is a [[Currency]] used in the [[Heart of the Mountain]].
## Obtaining
Mithril Powder can be obtained from various sources, as listed below:
- Mining [[Mithril]].
- Participating in [[Dwarven Mines]] events.
- Claiming [[Dwarven Mines]] [[Commissions]].
- Killing [[Mithril Grubber|Mithril Grubbers]], [[Golden Goblin|Golden Goblins]], or [[Diamond Goblin|Diamond Goblins]].
- Damaging [[Powder Ghast|Powder Ghasts]].
- Finding [[Dark Monolith|Dark Monoliths]].
- Giving [[Fetchur]] the item they ask for.
- Completing the [[Puzzler]]'s puzzle.
- Completing [[Crystal Nucleus]] runs after reaching [[Heart of the Mountain|Heart of the Mountain X (10)]].
- Accepting offers from [[Emissaries]] on [[The Garden]].
### Blocks
|[[Mithril]] Variant|᠅ Mithril Powder Given|
|-|-|
|[[Hardened Clay]] [[Wool]]|1 ᠅ Mithril Powder|
|[[Prismarine]] [[Prismarine Bricks]] [[Dark Prismarine]]|2 ᠅ Mithril Powder|
|[[Wool]]|5 ᠅ Mithril Powder|
### Mobs
|Mob|᠅ Mithril Powder Given|
|-|-|
|[[Golden Goblin]]|500 ᠅ Mithril Powder|
|[[Diamond Goblin]]|1,000 ᠅ Mithril Powder|
|Small Mithril Grubber ([[Mithril Grubber]])|250 ᠅ Mithril Powder|
|Medium Mithril Grubber ([[Mithril Grubber]])|500 ᠅ Mithril Powder|
|Large Mithril Grubber ([[Mithril Grubber]])|1,000 ᠅ Mithril Powder|
|Bloated Mithril Grubber ([[Mithril Grubber]])|5,000 ᠅ Mithril Powder|
|[[Powder Ghast]]|100-250 ᠅ Mithril Powder per hit [Confirm (Confirmation needed; When this info is confirmed, remove this.)]|
## Usage
- ᠅ Mithril Powder is used to unlock [[Heart of the Mountain|Core of the Mountain]] Levels 2 to 3 and upgrade perks in [[Heart of the Mountain]] Tiers 1 to 3.
- Per 2,400 ᠅ Mithril Powder until 600,000 ᠅ Mithril Powder: [[SkyBlock Levels|+1 XP]] (Earn an exponentially decreasing amount of XP for powder above the cap until 12,500,000 ᠅ Mithril Powder)
## Increasing Mithril Powder Gain
### Heart of the Mountain
- [[Heart of the Mountain|Core of the Mountain]] Level 4 : Grants +1 ᠅ Mithril Powder per [[Mithril]] mined.
- [[Heart of the Mountain|Sky Mall]]: Grants a chance to gain +15% Powder while mining for a [[Time Systems|SkyBlock Day]].
- [[Heart of the Mountain|Daily Grind]]: Grants +500 ᠅ Mithril Powder per [[Heart of the Mountain]] Tier for the first daily commission completed in the [[Dwarven Mines]].
- [[Heart of the Mountain|Daily Powder]]: Grants +500 ᠅ Mithril Powder per Heart of the Mountain level for the first [[Mithril]] Metal mined per real-life day.
- [[Heart of the Mountain|Powder Buff]]: Increases Powder gain from all sources by +1%–50% (+51% with [[Blue Cheese Goblin Omelette]]).
### Accessories
- [[Powder of One]]: Grants +2.5% ᠅ Mithril Powder
- [[Powder of the Few]]: Grants +5% ᠅ Mithril Powder
- [[Powder of the Many]]: Grants +7.5% ᠅ Mithril Powder
- [[Powder of the People]]: Grants +10% ᠅ Mithril Powder
### Drills
- [[Mithril Drill SX-R226]]: Grants +20% ᠅ Mithril Powder while held.
- [[Mithril Drill SX-R326]]: Grants +40% ᠅ Mithril Powder while held.
### Drill Parts
- [[Blue Cheese Goblin Omelette]]: Grants +1 level to unlocked Heart of the Mountain perks (+1% to Powder Buff).
- [[Spicy Goblin Omelette]]: Grants +20% Powder while a [[Drills|Drill]] with the part equipped is held.
### Reforges
#### Mining Tool Reforges
- [[Reforging|Stellar]] ( [[Petrified Starfall]]): Grants +8-20% ᠅ Mithril Powder while mining near a [[Fallen Stars|Fallen Star]].
#### Armor Reforges
- [[Reforging|Dimensional]]: Grants 10 ᠅ Mithril Powder per [[Titanium]] mined.
  - The effect stacks with multiple pieces, granting up to 40 ᠅ Mithril Powder per [[Titanium]] mined with 4 pieces.
#### Equipment Reforges
- [[Reforging|Royal]] ( [[Dwarven Treasure]]): Grants +15% ᠅ Mithril Powder from [[Dwarven Mines|Mining Events]] in the [[Dwarven Mines]].
### Pets
- [[Rarity|LEGENDARY]] or [[Rarity|MYTHIC]] [[Mithril Golem Pet]]: Grants +0.2-20% ᠅ Mithril Powder while equipped.
### Attributes
- [[Attributes|Atomized Mithril]] ( [[Star Sentry Shard]]): Grants 1.01-1.1x ᠅ Mithril Powder.
- [[Attributes|Echo of Atomized]] ( [[Komodo Dragon Shard]]): Buffs the effect of [[Attributes|Atomized Mithril]] by 2-20%.
- [[Attributes|Echo of Echoes]] ( [[Tiamat Shard]]): Buffs the effect of [[Attributes|Echo of Atomized]] by 5-50%.
### Consumables
- [[Powder Pie]]: Grants +15% ᠅ Mithril Powder for 1 hour.
### Events
- [[2x Powder]]: Doubles all Powder gain for the duration of the event.
- [[Fallen Stars|Fallen Star]]: Grants +2 ᠅ Mithril Powder per [[Mithril]] mined.
- +10% ᠅ Mithril Powder while [[Weather|Mist]] is active.
### Others
- [[Doug]]'s Powder Hoarder Perk: Gain +2-6% ᠅ Mithril Powder during the [[Mining Fiesta]].
## Extents of Powder Buffs Effects
᠅ Mithril Powder Sources and Effects:
|Source|Type of Source|Effect [[Mithril]]|Effect [[Commissions]]|Effect [[Raffle]] Mining Events ([[Dwarven Mines]])|Effect Golden ([[Golden Goblin]]) and Diamond Goblins ([[Diamond Goblin]]),; Mithril Grubbers ([[Mithril Grubber]])|Effect [[Powder Ghast]]|Effect [[Titanium Tesseract]] Dimensional ([[Reforging]]); Reforge Bonus|Effect [[Crystal Nucleus]]|Effect [[Fetchur]]|Effect [[Puzzler]]|
|-|-|-|-|-|-|-|-|-|-|-|
|[[Powder of the People]] and its downgrades|Accessory ([[Accessories]])|✔|✔|✔|✔|[More Info Needed] (More infomation needed; This is very hard to test considering the range of powder it may drop per hit. Needs admin confirmation pls; When this info is added, remove this.)|✔|✔|[More Info Needed] (More infomation needed; I'll add this once the table is mostly complete.; When this info is added, remove this.)|[More Info Needed]|
|[[Powder Pie]]|Consumable ([[Consumables]])|✔|✔|✔|✔|(same as above)|✔|✔|(same as above)|[More Info Needed]|
|[[Mithril Drill SX-R326]] and its downgrade|Drill ([[Drills]])|✔|✔|✔|✔|(same as above)|✔|✔|(same as above)|[More Info Needed]|
|[[2x Powder]]|Event ([[Dwarven Mines]]) (Mining)|✔|✔||✔|(same as above)|✔|✔|(same as above)|[More Info Needed]|
|Powder Buff ([[Heart of the Mountain]])|HotM ([[Heart of the Mountain]]) perk|✔|✔|✔|✔|(same as above)|✔|✔|(same as above)|[More Info Needed]|
|Royal ([[Reforging]]) ( [[Dwarven Treasure]])|Reforge ([[Reforging]])|||✔||(same as above)|||(same as above)|[More Info Needed]|
|Dimensional ([[Reforging]]) ( [[Titanium Tesseract]])|Reforge ([[Reforging]])|✕ [Confirm]|✕|✕|✕|(same as above)|✔|[More Info Needed] (More infomation needed; When this info is added, remove this.)|(same as above)|[More Info Needed]|
|Stellar ([[Reforging]]) ( [[Petrified Starfall]])|Reforge ([[Reforging]])|✔|✕|✕|✕|(same as above)|✕||(same as above)|[More Info Needed]|
|Atomized Mithril ([[Attributes]]) ( [[Star Sentry Shard]])|Attribute ([[Attributes]])|✔|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|[[Blue Cheese Goblin Omelette]]|Drill Part ([[Drill Parts]])|✕|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|[[Spicy Goblin Omelette]]|Drill Part ([[Drill Parts]])|✔|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|Powder Hoarder ([[Doug]])|Events Shop ([[Doug]]) perk|✔|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|Sky Mall ([[Heart of the Mountain]])|HotM ([[Heart of the Mountain]]) perk|✔|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|LEGENDARY ([[Rarity]])+ [[Mithril Golem Pet]]'s The Smell Of Powder|Pet ([[Pets]]) perk|✔|✕|✕|✕|(same as above)|✕|✕|(same as above)|[More Info Needed]|
|Mist ([[Weather]])|[[Weather]]|✔|✕|✕|✕|(same as above)|✕||(same as above)|[More Info Needed]|
## Trivia
- All sources of ᠅ Mithril Powder buffs are additive, except for the [[2x Powder]] event.
- The maximum amount of ᠅ Mithril Powder a player may have is 2 billion.
- [[Golden Goblin|Golden Goblins]] and [[Diamond Goblin|Diamond Goblins]] used to not be affected by sources that increase ᠅ Mithril Powder gain, with the exception of the [[2x Powder]] event.
- The [[Reforging|Royal]] reforge grants +14.4% ᠅ Mithril Powder.
## History
[[Alpha Hypixel Network]]:
|Sep 30, 2026|Fixed Powder multipliers not applying to Mithril Grubbers ([[Mithril Grubber]]), Golden Goblins ([[Golden Goblin]]) or Diamond Goblins ([[Diamond Goblin]]).|
|Sep 30, 2026|Fixed incorrect rounding when calculating how much Powder to drop based on the Powder multiplier percentage.|
[SkyBlock Prototype]
|Jan 15, 2021|0.11|Added ᠅ Mithril Powder.|
|Oct 15, 2026|Fixed Powder resetting and temporarily being negative when reaching the 2 billion cap.|
Linked from: [[2x Powder]], [[Abandoned Quarry]], [[Accessories/Other]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Mining]], [[Attributes/List/Rare]], [[Attributes/Search]], [[Bednom]], [[Brynmor]], [[Centauri]], [[Changelog/2021/January 15]], [[Changelog/2021/January 20]], [[Changelog/2021/March 30]], [[Changelog/2021/September 13]], [[Commissions]], [[Consumables]], [[Crystal Hollows]], [[Crystal Nucleus]], [[Currency]], [[Dark Monolith]], [[Dark Prismarine]], [[Diamond Goblin]], [[Doug]], [[Drill Parts]], [[Drill Parts/List]], [[Drills]], [[Dwarven Mines]], [[Dwarven Treasure]], [[Fallen Stars]], [[Fetchur]], [[Garden Visitors]], [[Garden Visitors/List]], [[Goblin Raid]], [[Golden Goblin]], [[Grand Library]], [[Heart of the Mountain]], [[Locations]], [[Locations/Dwarven Mines]], [[Metal Detector]] (+37 more)

# Moonglade Beacon
Categories: Confirmations needed, Pages with UIs, Galatea
[Moonglade Beacon]
The Moonglade Beacon is a beacon in the [[South Reaches]] that, once tuned properly, grants increased [[Fig Fortune]] and [[Mangrove Fortune]] depending on how many stacks it has and its signal strength.
## Overview
### Frequency Tuning
To tune the Moonglade Beacon, one must correctly match the Color, Speed, and Pitch of a beat (telegraphed by colored glass panes). Successfully tuning the beacon will grant +1 Stack to all players on the island for 20 minutes. Each Stack grants +5 [[Fig Fortune]] and +5 [[Mangrove Fortune]]. Players by default can only get bonuses from 5 stacks.
There is also a 10% chance to obtain a [[Beaconmite Shard]], which when syphoned, grants the [[Attributes|Beacon Zealot]] attribute.
### Increasing Signal Strength
#### Beacon Zealot
The [[Attributes|Beacon Zealot]] attribute, obtained from the [[Beaconmite Shard]] increases the stats granted by the beacon to the player by 10%->100%. This percentage bonus is applied after the raw stat bonus from Signal Enhancers. Additionally it also grants a 0.1%->1% chance to obtain [[Signal Enhancer|Signal Enhancers]] from [[Tree Gifts]].
#### Signal Enhancers
A [[Signal Enhancer]] can be used to increase the Signal Strength of the Moonglade Beacon. This can be done a maximum of 10 times. Before obtaining the bonus, players must first solve a harder version of the Frequency Tuning minigame. The Signal Enhancer is only consumed after being solved. Each level of Signal Strength grants an additional +0.5 [[Fig Fortune]] and +0.5 [[Mangrove Fortune]] per Stack from the Moonglade Beacon. Every other[Confirm (Confirmation needed; When this info is confirmed, remove this.)] consumed Signal Enhancer also increases the number of stacks players can be affected by by 1 up to a total maximum of 10.
With [[Attributes|Beacon Zealot X]] and 10 consumed [[Signal Enhancer|Signal Enhancers]], players can get up to 200 [[Fig Fortune]] and 200 [[Mangrove Fortune]] from the Moonglade Beacon, compared to the default maximum of 25 of each.
## History
[[Alpha Hypixel Network]]:
|Jun 5, 2025|Added Moonglade Beacon.|
[SkyBlock Prototype]
|Jun 23, 2025|0.23|Added Moonglade Beacon.|
Linked from: [[Achievements]], [[Attributes]], [[Attributes/List]], [[Attributes/List/Foraging]], [[Attributes/List/Rare]], [[Attributes/Search]], [[Beacon (disambiguation)]], [[Beaconmite Shard]], [[Boris]], [[Galatea]], [[Locations]], [[Locations/Moonglade Marsh]], [[Moonglade (disambiguation)]], [[Moonglade Marsh]], [[NPC/List/Moonglade Marsh]], [[Signal Enhancer]], [[SkyBlock Levels]], [[SkyBlock Levels/Tasks]], [[South Reaches]]

# Mythological/List
Categories: Confirmations needed
The types of [[Mythological]] mobs that can be dig up from a [[Griffin Burrows|Griffin Burrow]] varies depending on the rarity of the player's [[Griffin Pet]].
Listed spawn chances are base chances. [[Tracking]] increases the weight of [[Elusive]] mobs. For example, having 15 [[Tracking]] would multiply their weights by 1.15x.
In addition to the stats listed below, all [[Mythological]] mobs have 50% resistance to [[Damage Calculation|Magic Damage]].
[[Gaia Construct|Gaia Constructs]] as well as all mobs that first appear in [[Rarity|EPIC]] tier or above are immune to damage from bows,[Confirm (Confirmation needed; When this info is confirmed, remove this.)] with the exception of [[King Minos]]' hit shield.
### Common
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv15] [[Minos Hunter]]|[[Mythological]] [[Humanoid]]|4,000 [[Health]] 40 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|50%; (1 in 2 mobs)|
|[Lv15] Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|2,500 [[Health]] 30 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|50%; (1 in 2 mobs)|
### Uncommon
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv25] Blessed Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|15,000 [[Health]] 125 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|27.78%; (1 in 3.6 mobs)|
|[Lv25] Blessed Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|12,500 [[Health]] 75 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|27.78%; (1 in 3.6 mobs)|
|[Lv40] Blessed Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|20,000 [[Health]] 100 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|22.22%; (1 in 4.5 mobs)|
|[Lv40] Blessed Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|25,000 [[Health]] 100 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|22.22%; (1 in 4.5 mobs)|
### Rare
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv60] Stalwart Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|100,000 [[Health]] 500 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|20.83%; (1 in 4.8 mobs)|
|[Lv55] Stalwart Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|75,000 [[Health]] 350 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|20.83%; (1 in 4.8 mobs)|
|[Lv70] Stalwart Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|125,000 [[Health]] 250 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|16.67%; (1 in 6 mobs)|
|[Lv70] Stalwart Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|150,000 [[Health]] 400 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|16.67%; (1 in 6 mobs)|
|[Lv85] Stalwart Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|200,000 [[Health]] 750 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|12.50%; (1 in 8 mobs)|
|[Lv85] Stalwart Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|175,000 [[Health]] 600 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|12.50%; (1 in 8 mobs)|
### Epic
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv80] Venerable Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|350,000 [[Health]] 1,250 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.86%; (1 in 5.6 mobs)|
|[Lv85] Venerable Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|250,000 [[Health]] 1,000 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.86%; (1 in 5.6 mobs)|
|[Lv95] Venerable Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|400,000 [[Health]] 750 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|14.29%; (1 in 7 mobs)|
|[Lv95] Venerable Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|500,000 [[Health]] 800 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|14.29%; (1 in 7 mobs)|
|[Lv140] Venerable Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|750,000 [[Health]] 1,500 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.71%; (1 in 9.33 mobs)|
|[Lv140] Venerable Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|650,000 [[Health]] 2,000 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.71%; (1 in 9.33 mobs)|
|[Lv45] Venerable Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|1,500,000 [[Health]] 350 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|7.14%; (1 in 14 mobs)|
|[Lv175] Venerable Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|2,000,000 [[Health]] 1,000 [[Damage]]|[[Minos Relic]]|✕ No|400|7.14%; (1 in 14 mobs)|
### Legendary
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv125] Exalted Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|1,000,000 [[Health]] 2,750 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.39%; (1 in 5.75 mobs)|
|[Lv155] Exalted Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|750,000 [[Health]] 2,250 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.39%; (1 in 5.75 mobs)|
|[Lv150] Exalted Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|1,250,000 [[Health]] 1,750 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|13.91%; (1 in 7.19 mobs)|
|[Lv150] Exalted Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|1,500,000 [[Health]] 2,000 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|13.91%; (1 in 7.19 mobs)|
|[Lv175] Exalted Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|2,000,000 [[Health]] 3,750 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.43%; (1 in 9.58 mobs)|
|[Lv175] Exalted Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|1,500,000 [[Health]] 3,500 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.43%; (1 in 9.58 mobs)|
|[Lv120] Exalted Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|8,000,000 [[Health]] 500 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|6.96%; (1 in 14.38 mobs)|
|[Lv310] Exalted Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|12,500,000 [[Health]] 1,750 [[Damage]]|[[Minos Relic]]|✕ No|400|6.96%; (1 in 14.38 mobs)|
|[Lv750] Exalted Sphinx ([[Sphinx]])|[[Mythological]] [[Humanoid]] [[Elusive]]|40,000,000 [[Health]] 4,000 [[Damage]]|[[Brain Food]]|✔ Yes ([[Sphinx Shard]])|75|1.30%; (1 in 76.67 mobs)|
|[Lv750] Exalted Minos Inquisitor ([[Minos Inquisitor]])|[[Mythological]] [[Humanoid]] [[Elusive]]|50,000,000 [[Health]] 750 [[Damage]]|[[Enchanted Book]] (Chimera I ([[Chimera]]))|✕ No|75|1.30%; (1 in 76.67 mobs)|
### Mythic
|Mob|Mob Types|Stats|Unique Drops|Has Shard ([[Attributes]])|Weight|Chance|
|-|-|-|-|-|-|-|
|[Lv200] Empyrean Minos Hunter ([[Minos Hunter]])|[[Mythological]] [[Humanoid]]|1,750,000 [[Health]] 4,000 [[Damage]]|[[Hilt of Revelations]]|✔ Yes ([[Minos Hunter Shard]])|1,000|17.30%; (1 in 5.78 mobs)|
|[Lv200] Empyrean Siamese Lynx ([[Siamese Lynxes]])|[[Mythological]] [[Animal]]|1,250,000 [[Health]] 3,000 [[Damage]]|[[Crochet Tiger Plushie]]|✕ No|1,000|17.30%; (1 in 5.78 mobs)|
|[Lv250] Empyrean Stranded Nymph ([[Stranded Nymph]])|[[Mythological]] [[Aquatic]] [[Humanoid]]|2,500,000 [[Health]] 2,500 [[Damage]]|[[Washed-up Souvenir]]|✕ No|800|13.84%; (1 in 7.22 mobs)|
|[Lv250] Empyrean Cretan Bull ([[Cretan Bull]])|[[Mythological]] [[Animal]]|3,000,000 [[Health]] 2,750 [[Damage]]|[[Cretan Urn]]|✔ Yes ([[Cretan Bull Shard]])|800|13.84%; (1 in 7.22 mobs)|
|[Lv325] Empyrean Harpy ([[Harpy]])|[[Mythological]] [[Humanoid]] [[Animal]]|3,750,000 [[Health]] 6,500 [[Damage]]|[[Antique Remedies]]|✔ Yes ([[Harpy Shard]])|600|10.38%; (1 in 9.63 mobs)|
|[Lv325] Empyrean Gaia Construct ([[Gaia Construct]])|[[Mythological]] [[Construct]]|3,500,000 [[Health]] 5,000 [[Damage]]|[[Dwarf Turtle Shelmet]]|✕ No|600|10.38%; (1 in 9.63 mobs)|
|[Lv210] Empyrean Minotaur ([[Minotaur]])|[[Mythological]] [[Humanoid]] [[Animal]]|15,500,000 [[Health]] 1,000 [[Damage]]|[[Daedalus Stick]]|✔ Yes ([[Minotaur Shard]])|400|6.92%; (1 in 14.45 mobs)|
|[Lv550] Empyrean Minos Champion ([[Minos Champion]])|[[Mythological]] [[Humanoid]]|25,000,000 [[Health]] 2,500 [[Damage]]|[[Minos Relic]]|✕ No|400|6.92%; (1 in 14.45 mobs)|
|[Lv1,250] Empyrean Sphinx ([[Sphinx]])|[[Mythological]] [[Humanoid]] [[Elusive]]|65,000,000 [[Health]] 7,000 [[Damage]]|[[Brain Food]]|✔ Yes ([[Sphinx Shard]])|75|1.30%; (1 in 77.07 mobs)|
|[Lv1,250] Empyrean Minos Inquisitor ([[Minos Inquisitor]])|[[Mythological]] [[Humanoid]] [[Elusive]]|80,000,000 [[Health]] 1,000 [[Damage]]|[[Enchanted Book]] (Chimera I ([[Chimera]]))|✕ No|75|1.30%; (1 in 77.07 mobs)|
|[Lv1,750] Empyrean Manticore ([[Manticore]])|[[Mythological]] [[Animal]] [[Elusive]]|125,000,000 [[Health]] 8,000 [[Damage]]|[[Fateful Stinger]] [[Manti-core]]|✕ No|15|0.26%; (1 in 385.33 mobs)|
|[Lv1,750] Empyrean King Minos ([[King Minos]])|[[Mythological]] [[Humanoid]] [[Elusive]]|100,000,000 [[Health]] 2,500 [[Damage]]|[[Crown of Greed]] [[Shimmering Wool]]|✔ Yes ([[King Minos Shard]])|15|0.26%; (1 in 385.33 mobs)|

# Pet Upgrades
Categories: Confirmations needed
Pet Upgrades are items that can be used to upgrade certain [[Pets]] to a higher rarity.
## List of Pet Upgrades
|Icon|Name|Pet|Upgrades from|Upgrades to|Source|
|-|-|-|-|-|-|
|[[Frozen Scute]]|[[Frozen Scute]]|[[Armadillo Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from paid [[Frozen Corpses]].|
|[[Pocket-sized Igloo]]|[[Pocket-sized Igloo]]|[[Baby Yeti Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 1x [[Littlefoot Fluff]] 4x [[True Ice]] 64x [[Enchanted Packed Ice]] Recipe: [[True Ice]] ×4 + [[Enchanted Packed Ice]] x16 ×4 + [[Littlefoot Fluff]] → [[Pocket-sized Igloo]]|
|[[Vampire Fang]]|[[Vampire Fang]]|[[Bat Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Grim Reaper]].|
|[[Small Honey Dipper]]|[[Small Honey Dipper]]|[[Bee Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 500 [[Coins]] from [[Bea]].|
|[[Medium Honey Dipper]]|[[Medium Honey Dipper]]|[[Bee Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 5,000 [[Coins]] from [[Bea]].|
|[[Large Honey Dipper]]|[[Large Honey Dipper]]|[[Bee Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 50,000 [[Coins]] from [[Bea]].|
|[[Giant Honey Dipper]]|[[Giant Honey Dipper]]|[[Bee Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 500,000 [[Coins]] from [[Bea]].|
|[[Royal Jelly]]|[[Royal Jelly]]|[[Bee Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 64x [[Floral Gelatin]] 64x [[Jelly]] Recipe: [[Floral Gelatin]] x8 ×8 + [[Jelly]] x64 → [[Royal Jelly]]|
|[[Black Woolen Yarn]]|[[Black Woolen Yarn]]|[[Black Cat Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Donating 200 (3 stacks plus 8) [[Dark Candy]] to [[Vargul the Unearthed]].|
|[[Eerie Treat]]|[[Eerie Treat]]|[[Eerie Pet]]|COMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 10 [[Sewer Fish]] from [[Tyashoi Alchemist]].|
|[[Eerie Toy]]|[[Eerie Toy]]|[[Eerie Pet]]|RARE ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 1 [[Nightmare Nullifier]] from [[Tyashoi Alchemist]].|
|[[Trunk Polish]]|[[Trunk Polish]]|[[Elephant Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 1x [[Glass Bottle]] 4x [[Creambloom]] 128x (2 stacks (128 items total)) [[Melon Juice]] Recipe: [[Melon Juice]] x32 ×4 + [[Creambloom]] ×4 + [[Glass Bottle]] → [[Trunk Polish]]|
|[[Enderman Cortex Rewriter]]|[[Enderman Cortex Rewriter]]|[[Enderman Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Voidling Extremist]].|
|[[Mixed Mite Gel]]|[[Mixed Mite Gel]]|[[Endermite Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 160x (2 stacks plus 32 (160 in total)) [[Mite Gel]] Recipe: [[Mite Gel]] x32 ×7 → [[Mixed Mite Gel]]|
|[[Radioactive Vial]]|[[Radioactive Vial]]|[[Flying Fish Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Lord Jawbus]].|
|[[Small Frog Treat]]|[[Small Frog Treat]]|[[Frog Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 30 [[Agatha's Coupon]] from [[Agatha]].|
|[[Medium Frog Treat]]|[[Medium Frog Treat]]|[[Frog Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 40 [[Agatha's Coupon]] from [[Agatha]].|
|[[Large Frog Treat]]|[[Large Frog Treat]]|[[Frog Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 50 [[Agatha's Coupon]] from [[Agatha]].|
|[[Giant Frog Treat]]|[[Giant Frog Treat]]|[[Frog Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 60 [[Agatha's Coupon]] from [[Agatha]].|
|[[Frogspawn Bucket]]|[[Frogspawn Bucket]]|[[Frog Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 1x [[Lotus Water Orb]] 7x [[Condensed Lily Pad]] Recipe: [[Condensed Lily Pad]] ×7 + [[Lotus Water Orb]] → [[Frogspawn Bucket]]|
|[[Griffin Upgrade Stone]]|Uncommon Griffin Upgrade Stone ([[Griffin Upgrade Stone]])|[[Griffin Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Crafting ingredients: 1x Base Griffin Upgrade Stone ([[Griffin Upgrade Stone]]) 8x [[Griffin Feather]] 32x [[Ancient Claw]] 64x [[Enchanted Gold Ingot]] Recipe: [[Griffin Feather]] x4 ×2 + [[Enchanted Gold Ingot]] x16 ×4 + [[Ancient Claw]] x16 ×2 + [[Griffin Upgrade Stone]] → [[Griffin Upgrade Stone]]|
|[[Griffin Upgrade Stone]]|Rare Griffin Upgrade Stone ([[Griffin Upgrade Stone]])|[[Griffin Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Crafting ingredients: 1x Base Griffin Upgrade Stone ([[Griffin Upgrade Stone]]) 16x [[Griffin Feather]] 64x [[Ancient Claw]] 4x [[Enchanted Gold Block]] Recipe: [[Griffin Feather]] x8 ×2 + [[Enchanted Gold Block]] ×4 + [[Ancient Claw]] x32 ×2 + [[Griffin Upgrade Stone]] → [[Griffin Upgrade Stone]]|
|[[Griffin Upgrade Stone]]|Epic Griffin Upgrade Stone ([[Griffin Upgrade Stone]])|[[Griffin Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Crafting ingredients: 1x Base Griffin Upgrade Stone ([[Griffin Upgrade Stone]]) 64x [[Griffin Feather]] 4x [[Enchanted Ancient Claw]] 12x [[Enchanted Gold Block]] 4x [[Mythos Fragment]] Recipe: [[Griffin Feather]] x32 ×2 + [[Mythos Fragment]] x4 + [[Enchanted Ancient Claw]] x2 ×2 + [[Griffin Upgrade Stone]] + [[Enchanted Gold Block]] x4 ×3 → [[Griffin Upgrade Stone]]|
|[[Griffin Upgrade Stone]]|Legendary Griffin Upgrade Stone ([[Griffin Upgrade Stone]])|[[Griffin Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Crafting ingredients: 1x Base Griffin Upgrade Stone ([[Griffin Upgrade Stone]]) 1x [[Braided Griffin Feather]] 32x [[Enchanted Ancient Claw]] 96x (1 stack plus 32 (96 in total)) [[Enchanted Gold Block]] 16x [[Mythos Fragment]] Recipe: [[Mythos Fragment]] x8 ×2 + [[Braided Griffin Feather]] + [[Enchanted Ancient Claw]] x16 ×2 + [[Griffin Upgrade Stone]] + [[Enchanted Gold Block]] x32 ×3 → [[Griffin Upgrade Stone]]|
|[[Griffin Upgrade Stone]]|Mythic Griffin Upgrade Stone ([[Griffin Upgrade Stone]])|[[Griffin Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Crafting ingredients: 1x Base Griffin Upgrade Stone ([[Griffin Upgrade Stone]]) 2x [[Braided Griffin Feather]] 128x [[Enchanted Ancient Claw]] 192x (3 stacks (192 items total)) [[Enchanted Gold Block]] 48x [[Mythos Fragment]] Recipe: [[Braided Griffin Feather]] ×2 + [[Mythos Fragment]] x48 + [[Enchanted Ancient Claw]] x64 ×2 + [[Griffin Upgrade Stone]] + [[Enchanted Gold Block]] x64 ×3 → [[Griffin Upgrade Stone]]|
|[[Guardian Lucky Block]]|[[Guardian Lucky Block]]|[[Guardian Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Riftstalker Bloodfiend]].|
|[[Scuttler Shell]]|[[Scuttler Shell]]|[[Hermit Crab Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Fiery Scuttler]].|
|[[Jerry 3D Glasses]]|[[Jerry 3D Glasses]]|[[Jerry Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from Jerry Boxes ([[Jerry Box]]).|
|[[Pure Mithril Gem]]|[[Pure Mithril Gem]]|[[Mithril Golem Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Rare drop from [[Diamond Goblin]].|
|[[Small Pig's Ear]]|[[Small Pig's Ear]]|[[Pig Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 32 [[Shiny Token]] and 16 [[Enchanted Raw Porkchop]] from [[Piggy]].|
|[[Medium Pig's Ear]]|[[Medium Pig's Ear]]|[[Pig Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 64 (1 stack) [[Shiny Token]] and 32 [[Enchanted Raw Porkchop]] from [[Piggy]].|
|[[Large Pig's Ear]]|[[Large Pig's Ear]]|[[Pig Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 128 (2 stacks) [[Shiny Token]] and 64 [[Enchanted Raw Porkchop]] from [[Piggy]].|
|[[Giant Pig's Ear]]|[[Giant Pig's Ear]]|[[Pig Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 256 (4 stacks) [[Shiny Token]] and [[Enchanted Cooked Porkchop]] from [[Piggy]].|
|[[Chocolate Syringe]]|[[Chocolate Syringe]]|[[Rabbit Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Sold for 10,000,000,000 [[Chocolate]] from the Chocolate Shop ([[Chocolate Factory]]).|
|[[Rat Jetpack]]|[[Rat Jetpack]]|[[Rat Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Sold for 50,000,000 [[Coins]] in the [[Regalia Room]].|
|[[Small Seal Plushie]]|[[Small Seal Plushie]]|[[Seal Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 64 [[Fishy Treat]] from [[Lukas the Aquarist]].|
|[[Medium Seal Plushie]]|[[Medium Seal Plushie]]|[[Seal Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 128 [[Fishy Treat]] from [[Lukas the Aquarist]].|
|[[Large Seal Plushie]]|[[Large Seal Plushie]]|[[Seal Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 256 [[Fishy Treat]] from [[Lukas the Aquarist]].|
|[[Giant Seal Plushie]]|[[Giant Seal Plushie]]|[[Seal Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 512 (8 stacks) [[Fishy Treat]] from [[Lukas the Aquarist]].|
|[[Small Sloth Claw]]|[[Small Sloth Claw]]|[[Sloth Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 30 [[Miria's Coupon]] from [[Miria]].|
|[[Medium Sloth Claw]]|[[Medium Sloth Claw]]|[[Sloth Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 40 [[Miria's Coupon]] from [[Miria]].|
|[[Large Sloth Claw]]|[[Large Sloth Claw]]|[[Sloth Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 50 [[Miria's Coupon]] from [[Miria]].|
|[[Giant Sloth Claw]]|[[Giant Sloth Claw]]|[[Sloth Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 60 [[Miria's Coupon]] from [[Miria]].|
|[[Magic Top Hat]]|[[Magic Top Hat]]|[[Snowman Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Sold for 10 [[Volcanic Rock]] and 500 [[North Stars]] from [[Einary]].|
|[[Fake Neuroscience Degree]]|[[Fake Neuroscience Degree]]|[[Spider Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|Sold for 5,000 [[Motes]], 10 [[Volt Crux]] and 10 [[Shadow Crux]] from Neuroscientist Kat ([[Kat (Rift)]]).|
|[[Fake Neuroscience Degree]]|[[Fake Neuroscience Degree]]|[[Tarantula Pet]]|LEGENDARY ([[Rarity]])|MYTHIC ([[Rarity]])|(same as above)|
|[[Small Witch Cauldron]]|[[Small Witch Cauldron]]|[[Witch Pet]]|COMMON ([[Rarity]])|UNCOMMON ([[Rarity]])|Sold for 64 Spider Egg ([[Year of the Witch]]) and 64 Funny Bone ([[Year of the Witch]]) from [[Agnes]].|
|[[Medium Witch Cauldron]]|[[Medium Witch Cauldron]]|[[Witch Pet]]|UNCOMMON ([[Rarity]])|RARE ([[Rarity]])|Sold for 64 Waterbourne Lice ([[Year of the Witch]]), 64 Console Panel ([[Year of the Witch]]) and 64 Jawbreaker ([[Year of the Witch]]) from [[Agnes]].|
|[[Large Witch Cauldron]]|[[Large Witch Cauldron]]|[[Witch Pet]]|RARE ([[Rarity]])|EPIC ([[Rarity]])|Sold for 64 Smoldering Embers ([[Year of the Witch]]), 64 Warmed Flakes ([[Year of the Witch]]), 64 Never-Melt Ice ([[Year of the Witch]]) and 64 Glaciated Brains ([[Year of the Witch]]) from [[Agnes]].|
|[[Giant Witch Cauldron]]|[[Giant Witch Cauldron]]|[[Witch Pet]]|EPIC ([[Rarity]])|LEGENDARY ([[Rarity]])|Sold for 64 Shield Dust ([[Year of the Witch]]), 64 Pixie Dust ([[Year of the Witch]]), 64 Ruffled Feather ([[Year of the Witch]]), 64 Brittle Powder ([[Year of the Witch]]) and 64 Dirty Fingernails ([[Year of the Witch]]) from [[Agnes]].|
## Trivia
- Some [[Rarity|EPIC]] pets can be upgraded to [[Rarity|MYTHIC]] rarity using their respective pet upgrade when [[Tier Boost|Tierboosted]] to [[Rarity|LEGENDARY]].[Confirm (Confirmation needed; When this info is confirmed, remove this.)]
- Although [[Eerie Treat]] and [[Eerie Toy]] are considered [[Pet Items]], when given to the [[Eerie Pet]] they do not get equipped or consumed.
- The [[Eerie Pet]] is the only pet to upgrade rarity using [[Pet Items]] (excluding [[Tier Boost]]).
  - Previously, the [[Bat Pet]] and [[Jerry Pet]] used to be upgraded to [[Rarity|MYTHIC]] with their exclusive [[Pet Items]].
## History
[[SkyBlock Prototype]]:
|May 31, 2021|0.11.5|Added Enderman Cortex Rewriter.|
|May 5, 2022|Added Radioactive Vial.|
|Aug 18, 2022|0.14|Added Rat Jetpack.|
|Oct 19, 2022|0.16|Added Mixed Mite Gel.|
|Apr 18, 2023|0.18.3|Changed Jerry 3D Glasses and Vampire Fang from Pet Items to Pet Upgrades.|
|Jun 20, 2023|0.19|Added Fake Neuroscience Degree and Guardian Lucky Block.|
|Oct 24, 2023|0.19.6|Added Pure Mithril Gem, Black Woolen Yarn, Eerie Treat and Eerie Toy.|
|Nov 28, 2023|0.19.8|Added Magic Top Hat.|
