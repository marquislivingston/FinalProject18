import random
import time

class artist:
	"""artist class"""

	def __init__(self, name, location, kind, catchiness, lyrics, flow, fans, chart, ability, abilitydescription, abilityuse, phrase, songs, projects, rating, attack, defense, health):
		"""constructor for artist class"""
		self.name = name
		self.location = location
		self.kind = kind
		self.catchiness = catchiness
		self.lyrics = lyrics
		self.flow = flow
		self.fans = fans
		self.chart = chart
		self.ability = ability
		self.abilitydescription = abilitydescription
		self.abilityuse = abilityuse
		self.phrase = phrase
		self.songs = songs
		self.projects = projects
		self.rating = rating
		self.attack = attack
		self.defense = defense
		self.health = health

























	def listinfo(opponent):
		"""lists all the info of a given artist"""
		catchinessdisplay = round(opponent.catchiness*100*2)
		lyricsdisplay = round(opponent.lyrics*100)
		defensedisplay = round((1-opponent.defense)*2*100)
		print (f"NAME: {opponent.name}")
		print (f"RATING: {opponent.rating}")
		print (f"CITY: {opponent.location}")
		print (f"GENRE: {opponent.kind}")
		print (f"CATCHINESS: {catchinessdisplay}")
		print (f"LYRICS: {lyricsdisplay}")
		print (f"ATTACK: {opponent.attack}")
		print (f"DEFENSE: {defensedisplay}")
		print (f"FANS: {opponent.fans}00")
		print (f"HIGHEST CHART SPOT: {opponent.chart}")
		print (f"ABILITY: {opponent.ability}")
		print (f"""	DESCRIPTION: {opponent.abilitydescription}
	USES PER FIGHT: {opponent.abilityuse}""")
		print (f"NOTABLE SONG: {opponent.songs}")
		print (f"NOTABLE PROJECT: {opponent.projects}")
		print("")
		print("")



























	def fight(opponent):
		"""creates fight between opponent and player"""
		global playerwin
		playerwin = False
		asapmobactive = False
		slaughtergangactive = False
		slimefamilyactive = False
		asapmobactive2 = False

		### I WROTE THESE ABILITIES IN AT THE BEGINNING (SLAUGHTER GANG AND SLIME FAMILY) AND I DIDNT WANT THEM BUT IM TOO SCARED TO DELETE THEM FOR SOME REASON BUT THEY'RE NOT BEING USED SO I THOUGHT IT WAS HARMLESS TO KEEP THEM ###
		slaughtergangactive2 = False
		slimefamilyactive2 = False
		opponentattack = False

		### converts attributes into displayable stats ###
		catchinessdisplay = round(player.catchiness*100*2)
		lyricsdisplay = round(player.lyrics*100)
		defensedisplay = round((1-player.defense)*2*100)
		catchinessdisplay2 = round(opponent.catchiness*100*2)
		lyricsdisplay2 = round(opponent.lyrics*100)
		defensedisplay2 = round((1-opponent.defense)*2*100)

		### if both of the players healths are greater than 0, asks user what to do next ###
		while player.health > 0 and opponent.health > 0:
			print("\033[H\033[J")
			print(f"""{player.name.upper()}		{opponent.name}
ATTACK: {player.attack}		ATTACK: {opponent.attack}
DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
HEALTH: {player.health}		HEALTH: {opponent.health}
""")
			action = input("""WHAT WOULD YOU LIKE TO DO?
ATTACK
CHECK STATS
SPECIAL ABILITY

""")
			while action != "ATTACK" and action != "CHECK STATS" and action != "SPECIAL ABILITY":
				action = input("""WHAT WOULD YOU LIKE TO DO?
ATTACK
CHECK STATS
SPECIAL ABILITY

""")




			### if user inputs check stats, displays info for both fighters ###
			if action == "CHECK STATS":
				print("\033[H\033[J")
				time.sleep(2)
				artist.listinfo(opponent)
				print("")
				time.sleep(1)
				artist.listinfo(player)
				print("")
				time.sleep(2)
				input("PRESS ENTER WHEN DONE")







			### if user inputs attack ###
			if action == "ATTACK":

				### 50% chance of either player going first ###
				chance = random.randint(0, 9)
				if chance >= 5:
					playerspeed = 1
					opponentspeed = 0
				elif chance < 5:
					opponentspeed = 1
					playerspeed = 0
				if playerspeed > opponentspeed:
					print("")
					print(f"YOU ARE FASTER!")
					time.sleep(2)

					### generates random number from 1-100 for use in lyrics stat ###
					randomlyrics = random.randint(0, 100)

					### calculates damage to opponent ###
					playerdamage = player.attack*opponent.defense

					### if random number is greater than chance of crit (lyrics stat), crit is not achieved ###
					if randomlyrics >= lyricsdisplay:
						playerdamage = playerdamage * 1.5
						impacthit = True
					else:
						impacthit = False

					### if random number is greater than opponent's chance of evasion (catchiness stat), evasion is not achieved ###
					randomcatchiness = random.randint(0, 1000)
					if randomcatchiness <= catchinessdisplay2:
						playerdamage = 0
						miss = True
					else:
						miss = False

					### if asap mob ability is in use, adds 60 damage to next attack ###
					if asapmobactive is True:
						playerdamage = playerdamage + 60

					### deleted abilities ###
					if slaughtergangactive is True:
						playerdamage = playerdamage + 20
					if slimefamilyactive is True:
						playerdamage = (babygunna.attack+youngthug.attack)*opponent.defense
					opponent.health = opponent.health - playerdamage
					if slimefamilyactive is True:
						slimefamilyactive = False
						player.abilityuse = 0
					if slaughtergangactive is True:
						slaughtergangactive = False
						player.abilityuse = 0
					if asapmobactive is True:
						asapmobactive = False
						player.abilityuse = 0

					### if opponent did not evade, and critical hit was achieved, prints out the following and how much damage was done ###
					if miss is False:
						if impacthit is True:
							print("")
							print("THIS SONG IS A HIT! 1.5x DAMAGE!")
							time.sleep(2)
						print("")
						print(f"YOU ATTACKED {opponent.name} FOR {playerdamage} HEALTH!")
						time.sleep(2)

					### if opponent did evade, prints out the following ###
					elif miss is True:
						print("")
						print(f"YOU MISSED YOUR ATTACK!")
						time.sleep(2)


					### if opponent is dead after attack, reprints both players stats (with opponent health at 0), says they've been defeated, resets both health stats to 100, and sets playerwin to true ###
					if opponent.health <= 0:
						print("\033[H\033[J")
						print(f"""{player.name.upper()}	    {opponent.name}
ATTACK: {player.attack}		ATTACK: {opponent.attack}
DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
HEALTH: {player.health}		HEALTH: 0
""")
						time.sleep(2)
						print("")
						print(f"CONGRATULATIONS! {opponent.name} HAS BEEN DEFEATED!")
						time.sleep(2)
						player.health = 100
						opponent.health = 100
						playerwin = True
						break

					### if player is dead after attack, reprints both players stats (with player health at 0), says you've been defeated, resets both health stats to 100, and sets playerwin to false ###
					elif player.health <= 0:
						print("\033[H\033[J")
						print(f"""{player.name.upper()}	    {opponent.name}
ATTACK: {player.attack}		ATTACK: {opponent.attack}
DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
HEALTH: 0		HEALTH: {opponent.health}
""")
						print("")
						print("OH NO! YOU'VE BEEN DEFEATED!")
						time.sleep(2)
						player.health = 100
						opponent.health = 100
						playerwin = False
						break


					### if both players are still alive, now it is opponents turn to attack, using the same lyrics and catchiness procedures as for the player with one addition being the 50% chance to activate their special ability ###
					print("")
					print(f"{opponent.name}'S TURN!")
					randomchoice = random.randint(0,100)
					if randomchoice >= 50 and opponent.abilityuse != 0:
						opponentspecialability = True
						opponentattack = False
					elif randomchoice < 50:
						opponentattack = True
					else:
						opponentattack = True

					if opponentattack is True:
						time.sleep(2)
						randomlyrics = random.randint(0, 100)
						opponentdamage = opponent.attack*player.defense
						if randomlyrics >= lyricsdisplay2:
							opponentdamage = opponentdamage * 1.5
							impacthit = True
						else:
							impacthit = False
						randomcatchiness = random.randint(0, 1000)
						if randomcatchiness <= catchinessdisplay:
							opponentdamage = 0
							miss = True
						else:
							miss = False
						if asapmobactive2 is True:
							opponentdamage = opponentdamage + 60
						if slaughtergangactive2 is True:
							opponentdamage = opponentdamage + 20
						if slimefamilyactive2 is True:
							opponentdamage = (babygunna.attack+youngthug.attack)*player.defense
						player.health = player.health - opponentdamage
						if slimefamilyactive2 is True:
							slimefamilyactive2 = False
							opponent.abilityuse = 0
						if slaughtergangactive2 is True:
							slaughtergangactive2 = False
							opponent.abilityuse = 0
						if asapmobactive2 is True:
							asapmobactive2 = False
							opponent.abilityuse = 0
						if miss is False:
							if impacthit is True:
								print("")
								print("THIS SONG IS A HIT! 1.5x DAMAGE!")
							print("")
							print(f"{opponent.name.upper()} ATTACKED YOU FOR {opponentdamage} HEALTH!")
							time.sleep(2)
						elif miss is True:
							print("")
							print(f"HE MISSED HIS ATTACK!")
							time.sleep(2)

					### if 50% chance to activate special ability is true, then series of if/elif statements about what to do if certain abilities are active and what stats to change, always lowering abilityuse by 1 so it can only be used once, and then going through the attack protocol after ###
					elif opponentspecialability is True:
						if opponent.ability == "DISAPPEAR":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "QUICK SPEED":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "BLOOD GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "THIEF":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.ability = player.ability
							player.ability = "???"
							opponent.abilityuse = opponent.abilityuse - 1
						elif opponent.ability == "BABY VOICE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "PRODUCER TAG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						elif opponent.ability == "SLIME FAMILY":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							slimefamilyactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "SLAUGHTER GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							slaughtergangactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "LEAN":
							if opponent.health < 70:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.catchiness = opponent.catchiness*3
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 70
								opponent.abilityuse = 0
						elif opponent.ability == "BLACK AND BLONDE X":
							if opponent.health < 150:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 150
								opponent.abilityuse = 0
						elif opponent.ability == "SAMPLE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*3
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						elif opponent.ability == "GO TO JAIL":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "GLO GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*2
							opponent.abilityuse = 0
						elif opponent.ability == "HEARTBREAK":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "ADAPT":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*3
							opponent.abilityuse = 0
						elif opponent.ability == "HYPE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							player.health = player.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "ASAP MOB":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							asapmobactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "TR3YWAY":
							if opponent.health < 70:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 70
								opponent.abilityuse = 0
						elif opponent.ability == "RAGE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "BEAT BY JEFF":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*3
							opponent.abilityuse = 0
						elif opponent.ability == "THE RACE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						if opponent.ability == "???":
							print("")
							print("HE HAS NO ABILITY!")
						randomlyrics = random.randint(0, 100)
						opponentdamage = opponent.attack*player.defense
						opponent.abilityuse = 0
						if randomlyrics >= lyricsdisplay2:
							opponentdamage = opponentdamage * 1.5
							impacthit = True
						else:
							impacthit = False
						randomcatchiness = random.randint(0, 1000)
						if randomcatchiness <= catchinessdisplay:
							opponentdamage = 0
							miss = True
						else:
							miss = False
						if asapmobactive2 is True:
							opponentdamage = opponentdamage + 60
						if slaughtergangactive2 is True:
							opponentdamage = opponentdamage + 20
						if slimefamilyactive2 is True:
							opponentdamage = (babygunna.attack+youngthug.attack)*player.defense
						player.health = player.health - opponentdamage
						if slimefamilyactive2 is True:
							slimefamilyactive2 = False
							opponent.abilityuse = 0
						if slaughtergangactive2 is True:
							slaughtergangactive2 = False
							opponent.abilityuse = 0
						if asapmobactive2 is True:
							asapmobactive2 = False
							opponent.abilityuse = 0
						if miss is False:
							if impacthit is True:
								print("")
								print("THIS SONG IS A HIT! 1.5x DAMAGE!")
								time.sleep(2)
							print("")
							print(f"{opponent.name.upper()} ATTACKED YOU FOR {opponentdamage} HEALTH!")
							time.sleep(2)
						elif miss is True:
							print("")
							print(f"HE MISSED HIS ATTACK!")
							time.sleep(2)

						if opponent.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: {player.health}		HEALTH: 0
    """)
							time.sleep(2)
							print("")
							print(f"CONGRATULATIONS! {opponent.name} HAS BEEN DEFEATED!")
							time.sleep(2)
							player.health = 100
							opponent.health = 100
							playerwin = True
							break
						elif player.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: 0		HEALTH: {opponent.health}
    """)
							print("")
							print("OH NO! YOU'VE BEEN DEFEATED!")
							player.health = 100
							opponent.health = 100
							time.sleep(2)
							playerwin = False
							break




				### this basically is the attacking if the opponent goes first, so its the same exact code, just in reverse order ###
				else:
					print("")
					print(f"{opponent.name} IS FASTER!")
					time.sleep(2)
					randomchoice = random.randint(0,100)
					if randomchoice >= 50 and opponent.abilityuse != 0:
						opponentspecialability = True
						opponentattack = False
					elif randomchoice < 50:
						opponentattack = True
					else:
						opponentattack = True

					if opponentattack is True:
						time.sleep(2)
						randomlyrics = random.randint(0, 100)
						opponentdamage = opponent.attack*player.defense
						if randomlyrics >= lyricsdisplay2:
							opponentdamage = opponentdamage * 1.5
							impacthit = True
						else:
							impacthit = False
						randomcatchiness = random.randint(0, 1000)
						if randomcatchiness <= catchinessdisplay:
							opponentdamage = 0
							miss = True
						else:
							miss = False
						if asapmobactive2 is True:
							opponentdamage = opponentdamage + 60
						if slaughtergangactive2 is True:
							opponentdamage = opponentdamage + 20
						if slimefamilyactive2 is True:
							opponentdamage = (babygunna.attack+youngthug.attack)*player.defense
						player.health = player.health - opponentdamage
						if slimefamilyactive2 is True:
							slimefamilyactive2 = False
							opponent.abilityuse = 0
						if slaughtergangactive2 is True:
							slaughtergangactive2 = False
							opponent.abilityuse = 0
						if asapmobactive2 is True:
							asapmobactive2 = False
							opponent.abilityuse = 0
						if miss is False:
							if impacthit is True:
								print("")
								print("THIS SONG IS A HIT! 1.5x DAMAGE!")
							print("")
							print(f"{opponent.name.upper()} ATTACKED YOU FOR {opponentdamage} HEALTH!")
							time.sleep(2)
						elif miss is True:
							print("")
							print(f"HE MISSED HIS ATTACK!")
							time.sleep(2)

						if opponent.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: {player.health}		HEALTH: 0
    """)
							time.sleep(2)
							print("")
							print(f"CONGRATULATIONS! {opponent.name} HAS BEEN DEFEATED!")
							time.sleep(2)
							player.health = 100
							opponent.health = 100
							playerwin = True
							break
						elif player.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: 0		HEALTH: {opponent.health}
    """)
							print("")
							print("OH NO! YOU'VE BEEN DEFEATED!")
							player.health = 100
							opponent.health = 100
							time.sleep(2)
							playerwin = False
							break

					elif opponentspecialability is True:
						if opponent.ability == "DISAPPEAR":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "QUICK SPEED":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "BLOOD GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*2
							opponent.lyrics = opponent.lyrics*2
							opponent.abilityuse = 0
						elif opponent.ability == "THIEF":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.ability = player.ability
							player.ability = "???"
							opponent.abilityuse = opponent.abilityuse - 1
						elif opponent.ability == "BABY VOICE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "PRODUCER TAG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						elif opponent.ability == "SLIME FAMILY":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							slimefamilyactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "SLAUGHTER GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							slaughtergangactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "LEAN":
							if opponent.health < 70:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.catchiness = opponent.catchiness*3
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 70
								opponent.abilityuse = 0
						elif opponent.ability == "BLACK AND BLONDE X":
							if opponent.health < 150:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 150
								opponent.abilityuse = 0
						elif opponent.ability == "SAMPLE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*3
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						elif opponent.ability == "GO TO JAIL":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "GLO GANG":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*2
							opponent.abilityuse = 0
						elif opponent.ability == "HEARTBREAK":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.catchiness = opponent.catchiness*2
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "ADAPT":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.health = opponent.health*3
							opponent.abilityuse = 0
						elif opponent.ability == "HYPE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							player.health = player.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "ASAP MOB":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							asapmobactive2 = True
							opponent.abilityuse = 0
						elif opponent.ability == "TR3YWAY":
							if opponent.health < 70:
								print("")
								print("NOT ENOUGH HEALTH!")
								time.sleep(2)
							else:
								print("")
								print(f"{opponent.abilitydescription}")
								time.sleep(2)
								opponent.attack = opponent.attack*3
								opponent.health = opponent.health - 70
								opponent.abilityuse = 0
						elif opponent.ability == "RAGE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*3
							opponent.health = opponent.health/2
							opponent.abilityuse = 0
						elif opponent.ability == "BEAT BY JEFF":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.attack = opponent.attack*2
							opponent.lyrics = opponent.lyrics*3
							opponent.abilityuse = 0
						elif opponent.ability == "THE RACE":
							print("")
							print(f"{opponent.abilitydescription}")
							time.sleep(2)
							opponent.catchiness = opponent.catchiness*2
							opponent.attack = opponent.attack*2
							opponent.abilityuse = 0
						if opponent.ability == "???":
							print("")
							print("HE HAS NO ABILITY!")
							opponent.abilityuse = 0
						randomlyrics = random.randint(0, 100)
						opponentdamage = opponent.attack*player.defense
						if randomlyrics >= lyricsdisplay2:
							opponentdamage = opponentdamage * 1.5
							impacthit = True
						else:
							impacthit = False
						randomcatchiness = random.randint(0, 1000)
						if randomcatchiness <= catchinessdisplay:
							opponentdamage = 0
							miss = True
						else:
							miss = False
						if asapmobactive2 is True:
							opponentdamage = opponentdamage + 60
						if slaughtergangactive2 is True:
							opponentdamage = opponentdamage + 20
						if slimefamilyactive2 is True:
							opponentdamage = (babygunna.attack+youngthug.attack)*player.defense
						player.health = player.health - opponentdamage
						if slimefamilyactive2 is True:
							slimefamilyactive2 = False
							opponent.abilityuse = 0
						if slaughtergangactive2 is True:
							slaughtergangactive2 = False
							opponent.abilityuse = 0
						if asapmobactive2 is True:
							asapmobactive2 = False
							opponent.abilityuse = 0
						if miss is False:
							if impacthit is True:
								print("")
								print("THIS SONG IS A HIT! 1.5x DAMAGE!")
								time.sleep(2)
							print("")
							print(f"{opponent.name.upper()} ATTACKED YOU FOR {opponentdamage} HEALTH!")
							time.sleep(2)
						elif miss is True:
							print("")
							print(f"HE MISSED HIS ATTACK!")
							time.sleep(2)

						if opponent.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: {player.health}		HEALTH: 0
    """)
							time.sleep(2)
							print("")
							print(f"CONGRATULATIONS! {opponent.name} HAS BEEN DEFEATED!")
							time.sleep(2)
							player.health = 100
							opponent.health = 100
							playerwin = True
							break
						elif player.health <= 0:
							print("\033[H\033[J")
							print(f"""{player.name.upper()}	    {opponent.name}
    ATTACK: {player.attack}		ATTACK: {opponent.attack}
    DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
    HEALTH: 0		HEALTH: {opponent.health}
    """)
							print("")
							print("OH NO! YOU'VE BEEN DEFEATED!")
							player.health = 100
							opponent.health = 100
							time.sleep(2)
							playerwin = False
							break


					print("")
					print(f"YOUR TURN!")
					time.sleep(2)
					randomlyrics = random.randint(0, 100)
					playerdamage = player.attack*opponent.defense
					if randomlyrics >= lyricsdisplay:
						playerdamage = playerdamage * 1.5
						impacthit = True
					else:
						impacthit = False
					randomcatchiness = random.randint(0, 1000)
					if randomcatchiness <= catchinessdisplay2:
						playerdamage = 0
						miss = True
					else:
						miss = False
					if asapmobactive is True:
						playerdamage = playerdamage + 60
					if slaughtergangactive is True:
						playerdamage = playerdamage + 20
					if slimefamilyactive is True:
						playerdamage = (babygunna.attack+youngthug.attack)*opponent.defense
					opponent.health = opponent.health - playerdamage
					if slimefamilyactive is True:
						slimefamilyactive = False
						player.abilityuse = 0
					if slaughtergangactive is True:
						slaughtergangactive = False
						player.abilityuse = 0
					if asapmobactive is True:
						asapmobactive = False
						player.abilityuse = 0
					if miss is False:
						if impacthit is True:
							print("")
							print("THIS SONG IS A HIT! 1.5x DAMAGE!")
							time.sleep(2)
						print("")
						print(f"YOU ATTACKED {opponent.name} FOR {playerdamage} HEALTH!")
						time.sleep(2)
					elif miss is True:
						print("")
						print(f"YOU MISSED YOUR ATTACK!")
						time.sleep(2)


				if opponent.health <= 0:
					print("\033[H\033[J")
					print(f"""{player.name.upper()} 	{opponent.name}
ATTACK: {player.attack}		ATTACK: {opponent.attack}
DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
HEALTH: {player.health}		HEALTH: 0
""")
					time.sleep(2)
					print("")
					print(f"CONGRATULATIONS! {opponent.name} HAS BEEN DEFEATED!")
					player.health = 100
					opponent.health = 100
					time.sleep(2)
					playerwin = True
					break
				elif player.health <= 0:
					print("\033[H\033[J")
					print(f"""{player.name.upper()}	    {opponent.name}
ATTACK: {player.attack}		ATTACK: {opponent.attack}
DEFENSE: {defensedisplay}		DEFENSE: {defensedisplay2}
HEALTH: 0		HEALTH: {opponent.health}
""")
					print("")
					print("OH NO! YOU'VE BEEN DEFEATED!")
					player.health = 100
					opponent.health = 100
					time.sleep(2)
					playerwin = False
					break





			### if user inputs special ability, goes through a series of if/elif statements that change certain stats depedning on what ability the user has ###
			if action == "SPECIAL ABILITY":
				time.sleep(2)
				if player.abilityuse == 0:
					print("")
					print("YOU USED UP YOUR SPECIAL MOVE!")

				if player.abilityuse > 0:
					if player.ability == "DISAPPEAR":
						print("")
						print("YOU DISAPPEAR FOR 2 YEARS, DOUBLING ATTACK AND LYRICS")
						time.sleep(2)
						player.attack = player.attack * 2
						player.lyrics = player.lyrics * 2
						player.abilityuse = 0
					elif player.ability == "QUICK SPEED":
						print("")
						print("YOU RAP AT FULL SPEED, DOUBLING ATTACK AND LYRICS")
						time.sleep(2)
						player.attack = player.attack * 2
						player.lyrics = player.lyrics * 2
						player.abilityuse = 0
					elif player.ability == "BLOOD GANG":
						print("")
						print("YOU GO BACK TO YOUR HOOD AND ROLL WITH YOUR GANG, DOUBLING LYRICS AND HEALTH")
						time.sleep(2)
						player.health = player.health * 2
						player.lyrics = player.lyrics * 2
						player.abilityuse = 0
					elif player.ability == "THIEF":
						print("")
						print("YOU STEAL YOUR OPPONENT'S FLOW, TAKING AWAY THEIR ABILITY AND GIVING IT TO YOURSELF")
						time.sleep(2)
						player.ability = opponent.ability
						opponent.ability = "???"
						player.abilityuse = 1
					elif player.ability == "BABY VOICE":
						print("")
						print("YOU CHANGE YOUR VOICE, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF")
						time.sleep(2)
						player.attack = player.attack * 3
						player.catchiness = player.catchiness * 2
						player.health = player.health / 2
						player.abilityuse = 0
					elif player.ability == "PRODUCER TAG":
						print("")
						print("YOU PRODUCE A HIT BEAT, DOUBLING CATCHINESS AND ATTACK")
						time.sleep(2)
						player.catchiness = player.catchiness * 2
						player.attack = player.attack * 2
						player.abilityuse = 0
					elif player.ability == "SLIME FAMILY":
						slimefamilyactive = True
						player.abilityuse = 0
					elif player.ability == "SLAUGHTER GANG":
						slaughtergangactive = True
						player.abilityuse = 0
					elif player.ability == "LEAN":
						if player.health < 70:
							print("")
							print("NOT ENOUGH HEALTH!")
							time.sleep(2)
						else:
							print("")
							print("YOU DRINK LEAN, TRIPLING CATCHINESS AND ATTACK BUT DECREASING HEALTH BY 70")
							time.sleep(2)
							player.catchiness = player.catchiness*3
							player.attack = player.attack * 3
							player.health = player.health - 70
							player.abilityuse = 0
					elif player.ability == "BLACK AND BLONDE X":
						if player.health < 150:
							print("")
							print("NOT ENOUGH HEALTH!")
							time.sleep(2)
						else:
							print("")
							print("YOU REVERT BACK TO YOUR OLD SELF, TRIPLING ATTACK BUT DECREASING HEALTH BY 150")
							time.sleep(2)
							player.attack = player.attack * 3
							player.health = player.health - 150
							player.abilityuse = 0
					elif player.ability == "SAMPLE":
						print("")
						print("YOU SAMPLE A CARTOON, TRIPLING CATCHINESS AND DOUBLING ATTACK")
						time.sleep(2)
						player.catchiness = player.catchiness * 3
						player.attack = player.attack * 2
						player.abilityuse = 0
					elif player.ability == "GO TO JAIL":
						print("")
						print("YOU GO TO JAIL, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF")
						time.sleep(2)
						player.attack = player.attack * 3
						player.catchiness = player.catchiness*2
						player.health = player.health / 2
						player.abilityuse = 0
					elif player.ability == "GLO GANG":
						print("")
						print("YOU CALL YOUR GANG, DOUBLING HEALTH")
						time.sleep(2)
						player.health = player.health * 2
						player.abilityuse = 0
					elif player.ability == "HEARTBREAK":
						print("")
						print("YOU GET YOUR HEART BROKEN, DOUBLING ATTACK AND DOUBLING CATCHINESS BUT DECREASING HEALTH BY HALF")
						time.sleep(2)
						player.attack = player.attack * 2
						player.catchiness = player.catchiness * 2
						player.health = player.health / 2
						player.abilityuse = 0
					elif player.ability == "ADAPT":
						print("")
						print("YOU PUSH THE GENRE FORWARD, TRIPLING HEALTH")
						time.sleep(2)
						player.health = player.health * 3
						player.abilityuse = 0
					elif player.ability == "HYPE":
						print("")
						print(f"YOU PERFORM {player.songs}, DOUBLING CATCHINESS AND CUTTING OPPONENT'S HEALTH IN HALF")
						time.sleep(2)
						player.catchiness = player.catchiness * 2
						opponent.health = opponent.health / 2
						player.abilityuse = 0
					elif player.ability == "ASAP MOB":
						print("")
						print("YOU CALL THE ASAP MOB TO DEAL AN EXTRA 60 DAMAGE TO OPPONENT")
						time.sleep(2)
						asapmobactive = True
						player.abilityuse = 0
					elif player.ability == "TR3WAY":
						if player.health < 70:
							print("")
							print("NOT ENOUGH HEALTH!")
						else:
							print("")
							print("YOU YELL 'TR3YWAY', TRIPLING ATTACK AND DOUBLING DEFENSE BUT DECREASING HEALTH BY 70")
							time.sleep(2)
							player.attack = player.attack * 3
							player.health = player.health - 70
							player.abilityuse = 0
					elif player.ability == "RAGE":
						print("")
						print("YOU PERFORM AT A CONCERT, TRIPLING ATTACK BUT DECREASING DEFENSE BY HALF")
						time.sleep(2)
						player.attack = player.attack * 3
						player.health = player.health / 2
						player.abilityuse = 0
					elif player.ability == "BEAT BY JEFF":
						print("")
						print("YOU RAP ON A BEAT BY JEFF, DOUBLING ATTACK AND TRIPLING LYRICS")
						time.sleep(2)
						player.attack = player.attack * 2
						player.lyrics = player.lyrics * 3
						player.abilityuse = 0
					elif player.ability == "THE RACE":
						print("")
						print("YOU RUN FROM THE POLICE, DOUBLING CATCHINESS AND ATTACK")
						time.sleep(2)
						player.catchiness = player.catchiness * 2
						player.attack = player.attack*2
						player.abilityuse = 0
					if player.ability == "???":
						print("")
						print("YOU HAVE NO ABILITY!")





















### list of all of the artists and their stats ###
frankocean = artist("FRANK OCEAN", "L.A.", "PURE RNB", 0.4, 0.8, "FRANK'S", 65, 25, "DISAPPEAR", "FRANK DISAPPEARS FOR 2 YEARS, DOUBLING ATTACK AND LYRICS", 1, "I WON'T DROP THE ALBUM", "NIGHTS", "BLONDE", 7, 50, 0.4, 200)

kendricklamar = artist("KENDRICK LAMAR", "L.A.", "PURE RAP", 0.35, 0.9, "KENDRICK'S", 75, 1, "QUICK SPEED", "KENDRICK RAPS AT FULL SPEED, DOUBLING ATTACK AND LYRICS", 1,"KUNG-FU KENNY!", "POETIC JUSTICE", "TO PIMP A BUTTERFLY", 9, 70, 0.5, 300)

yg = artist("Y.G.", "L.A.", "PURE RAP", 0.35, 0.8, "YG'S", 70, 1, "BLOOD GANG", "YG GOES BACK TO HIS HOOD AND ROLLS WITH HIS GANG, DOUBLING LYRICS AND HEALTH", 1,"SUUWOOP!", "BIG BANK", "STILL BRAZY", 5, 40, 0.7, 100)

drake = artist("DRAKE", "TORONTO", "MIXED RNB", 0.5, 0.5, "WHOEVER IS HOT RIGHT NOW'S", 100, 1, "THIEF", "DRAKE STEALS OPPONENT'S FLOW, TAKING AWAY THEIR ABILITY AND GIVING IT TO HIMSELF", 1, "YEAH.", "MARVINS ROOM", "TAKE CARE", 10, 100, 0.5, 400)

playboicarti = artist("PLAYBOI CARTI", "ATLANTA", "PURE MELODIC", 0.5, 0.2, "CARTI'S", 35, 29, "BABY VOICE", "CARTI CHANGES HIS VOICE, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF", 1, "*_SLATT*+_", "FLATBED FREESTYLE", "DIE LIT", 8, 70, 0.8, 300)

pierrebourne = artist("PIERRE BOURNE", "ATLANTA", "PURE MELODIC", 0.25, 0.4, "PIERRE'S", 15, 8, "PRODUCER TAG", "PIERRE PRODUCES A HIT BEAT, DOUBLING CATCHINESS AND ATTACK", 1, "YO PIERRE, YOU WANNA COME OUT HERE?", "CIVIL RIGHTS", "THE LIFE OF PIERRE 4", 5, 30, 0.8, 100)

future = artist("FUTURE", "ATLANTA", "PURE MELODIC", 0.35, 0.5, "FUTURE'S", 70, 5, "LEAN", "FUTURE DRINKS LEAN, TRIPLING CATCHINESS AND ATTACK BUT DECREASING HEALTH BY 70", 1, "IF YOUNG METRO DON'T TRUST YOU I'M GONNA SHOOT YOU", "CODEINE CRAZY", "BEAST MODE 2", 6, 60, 0.9, 200)

xxxtentacion = artist("XXXTENTACION", "FLORIDA", "ROCK RAP", 0.35, 0.9, "X'S", 70, 1, "BLACK AND BLONDE X", "X REVERTS BACK TO HIS OLD SELF, TRIPLING ATTACK BUT DECREASING HEALTH BY 150", 1, "AYEEE!", "YUNG BRATZ", "?", 8, 80, 0.6, 300)

skimask = artist("SKI MASK THE SLUMP GOD", "FLORIDA", "PURE RAP", 0.35, 0.8, "SKI'S", 30, 63, "SAMPLE", "SKI SAMPLES A CARTOON, TRIPLING CATCHINESS AND DOUBLING ATTACK", 1, "WATER!", "CATCH ME OUTSIDE", "STOKELEY", 4, 50, 0.7, 100)

kodakblack = artist("KODAK BLACK", "FLORIDA", "MIXED MELODIC", 0.3, 0.5, "KODAK'S", 60, 2, "GO TO JAIL", "KODAK GOES TO JAIL, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF", 1, "IM A SUBURBAN DUDE", "TUNNEL VISION", "DYING TO LIVE", 7, 70, 0.7, 200)

chiefkeef = artist("CHIEF KEEF", "CHICAGO", "DRILL RAP", 0.35, 0.6, "KEEF'S", 60, 56, "GLO GANG", "KEEF CALLS HIS GANG, DOUBLING HEALTH", 1, "O BLOCK 3 HUNNA", "FANETO", "FINALLY RICH", 7, 70, 0.8, 200)

juicewrld = artist("JUICE WRLD", "CHICAGO", "MIXED MELODIC", 0.35, 0.6, "JUICE'S", 50, 2, "HEARTBREAK", "JUICE GETS HIS HEART BROKEN, DOUBLING ATTACK AND DOUBLING CATCHINESS BUT DECREASING HEALTH BY HALF", 1, "999", "LUCID DREAMS", "GOODBYE & GOOD RIDDANCE", 5, 40, 0.7, 100)

kanyewest = artist("KANYE WEST", "CHICAGO", "PURE RAP", 0.3, 0.8, "KANYE'S", 80, 1, "ADAPT", "KANYE PUSHES THE GENRE FORWARD, TRIPLING HEALTH", 1, "I AM A GOD", "RUNAWAY", "MY BEAUTIFUL DARK TWISTED FANTASY", 10, 80, 0.5, 300)

sheckwes = artist("SHECK WES", "NEW YORK", "MIXED MELODIC", 0.5, 0, "SHECK'S", 30, 6, "HYPE", "SHECK PERFORMS MO BAMBA, DOUBLING CATCHINESS AND CUTTING OPPONENT'S HEALTH IN HALF", 1, "BIH!", "MO BAMBA", "MUDBOY", 4, 30, 1.0, 100)

asaprocky = artist("ASAP ROCKY", "NEW YORK", "PURE RAP", 0.3, 0.7, "ROCKY'S", 60, 8, "ASAP MOB", "ROCKY CALLS THE ASAP MOB TO DEAL AN EXTRA 60 DAMAGE TO OPPONENT", 2, "ITS NOT A PURSE, ITS A SATCHEL", "LORD PRETTY FLACKO JODYE", "AT LONG LAST ASAP", 8, 80, 0.7, 300)

tekashi = artist("TEKASHI", "NEW YORK", "SCREAMO RAP", 0.35, 0.6, "TEKASHI'S", 30, 38, "TR3YWAY", "TEKASHI YELLS 'TR3YWAY', TRIPLING ATTACK BUT DECREASING HEALTH BY 70", 1, "YOU KNOW THE VIBES", "GUMMO", "DUMMY BOY", 6, 60, 0.8, 200)

travisscott = artist("TRAVIS SCOTT", "TEXAS", "MIXED MELODIC", 0.35, 0.5, "TRAV'S", 60, 1, "RAGE", "TRAVIS PERFORMS AT A CONCERT, TRIPLING ATTACK BUT DECREASING HEALTH BY HALF", 1, "STRAIGHT UP!", "90210", "RODEO", 8, 60, 0.7, 300)

splurge = artist("SPLURGE", "TEXAS", "PURE RAP", 0.25, 0.7, "SPLURGE'S", 10, 99, "BEAT BY JEFF", "SPLURGE RAPS ON A BEAT BY JEFF, DOUBLING ATTACK AND TRIPLING LYRICS", 1, "AYE LEMME HEAR THAT JEFF", "INTRO PT. 2", "GLENBABY", 4, 40, 1.0, 200)

tayk = artist("TAY-K", "TEXAS", "PURE RAP", 0.3, 0.6, "TAY-K'S", 30, 44, "THE RACE", "TAY-K RUNS FROM THE POLICE, DOUBLING CATCHINESS AND ATTACK", 1, "SCHOOL WAS VERY HARD", "THE RACE", "#SANTANAWORLD", 6, 80, 1.2, 200)

player = artist("name", "location", "genre", 0, 0, "???", 0, "???", "???", "???", 1, "???", "???", "???", 2, 0, 0.9, 100)






















### i actually dont think i use this, but again im too scared to delete it just in case, but this was supposed to display stats ###
def displaystats():
	catchinessdisplay = round(player.catchiness*100*2)
	lyricsdisplay = round(player.lyrics*100)
	defensedisplay = round((1-player.defense)*2*100)
	print(f"""
YOUR STATS:
NAME: {player.name.upper()}
LOCATION: {player.location}
GENRE: {player.kind}
ATTACK: {player.attack}
DEFENSE: {defensedisplay}
CATCHINESS: {catchinessdisplay}
LYRICS: {lyricsdisplay}
HEALTH: {player.health}
FLOW: {player.flow}
HIGHEST CHART SPOT: {player.chart}
ABILITY: {player.ability}
	DESCRIPTION: {player.abilitydescription}
	USES PER FIGHT: {player.abilityuse}
NOTABLE SONG: {player.songs}
NOTABLE PROJECT: {player.projects}
RANKING: {player.rating}
""")




















### text introductions and getting info for name and city etc. ###
print("\033[H\033[J")
print("*TYPE IN ALL CAPS OKAY THANKS*")
time.sleep(2)
print("\033[H\033[J")
print("???: HEY KID ")
time.sleep(2)
print("")
print("???: I HEARD YOU WANNA MAKE MUSIC ")
time.sleep(2)
print("")
print("???: WELL THE FIRST THING YOU NEED IS A STAGE NAME ")
time.sleep(2)
print("")
player.name = input("???: WHAT DO YOU WANT YOUR STAGE NAME TO BE? ")
print("")
print("???: AH!")
time.sleep(1)
print("")
print(f"???: {player.name.upper()}!")
time.sleep(1)
print("")
print("???: FITTING")
time.sleep(2)
print("")
print("""???: IF I'M GOING TO HELP YOU
	I NEED TO KNOW WHERE YOU ARE FROM!""")
time.sleep(1)
print("")
player.location = input("""???: WHAT CITY ARE YOU FROM?
    CHICAGO, TEXAS, L.A., NEW YORK, ATLANTA, OR FLORIDA? """)
while player.location != "CHICAGO" and player.location != "TEXAS" and player.location != "L.A." and player.location != "NEW YORK" and player.location != "ATLANTA" and player.location != "FLORIDA":
	print("")
	player.location = input("""???: WHAT CITY ARE YOU FROM?
	CHICAGO, TEXAS, L.A., NEW YORK, ATLANTA, OR FLORIDA? """)
	time.sleep(1)
time.sleep(1)
print("")
print(f"???: SO YOU'RE {player.name.upper()} FROM {player.location.upper()}!")
time.sleep(1)
print("")
print("???: IT LOOKS LIKE WE'LL GET ALONG JUST FINE KID.")
time.sleep(1)
print("")
print("""???: I'M YOUR MANAGER
	CALL ME BIG SMOKE """)
time.sleep(3)
print("\033[H\033[J")
print("""BIG SMOKE: WHAT KIND OF MUSIC YOU WANNA MAKE?

	PURE MELODIC?

	MIXED MELODIC?

	PURE RAP?

	MIXED RAP?

	DRILL RAP?

	PURE RNB?

	MIXED RNB?
	""")
time.sleep(4)
print("")
player.kind = input("BIG SMOKE: WELL WHICH ONE IS IT KID? ")
while player.kind != "PURE MELODIC" and player.kind != "MIXED MELODIC" and player.kind != "PURE RAP" and player.kind != "MIXED RAP" and player.kind != "DRILL RAP" and player.kind != "PURE RNB" and player.kind != "MIXED RNB":
	player.kind = input("BIG SMOKE: WELL WHICH ONE IS IT KID? ")
	time.sleep(1)
time.sleep(2)
print("")
### giving different stats to different builds that were seelcted previously ###
if player.kind == "PURE MELODIC":
	print("+50 CATCHINESS")
	player.catchiness = 0.25
	time.sleep(0.5)
	print("+10 LYRICS")
	player.lyrics = 0.1
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.85
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "MIXED MELODIC":
	print("+30 CATCHINESS")
	player.catchiness = 0.15
	time.sleep(0.5)
	print("+30 LYRICS")
	player.lyrics = 0.3
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.85
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "PURE RAP":
	print("+10 CATCHINESS")
	player.catchiness = 0.05
	time.sleep(0.5)
	print("+40 LYRICS")
	player.lyrics = 0.4
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.85
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "MIXED RAP":
	print("+30 CATCHINESS")
	player.catchiness = 0.15
	time.sleep(0.5)
	print("+30 LYRICS")
	player.lyrics = 0.3
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.85
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "DRILL RAP":
	print("+20 CATCHINESS")
	player.catchiness = 0.1
	time.sleep(0.5)
	print("+30 LYRICS")
	player.lyrics = 0.3
	time.sleep(0.5)
	print("+40 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.8
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "PURE RNB":
	print("+40 CATCHINESS")
	player.catchiness = 0.2
	time.sleep(0.5)
	print("+30 LYRICS")
	player.lyrics = 0.3
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 20
	time.sleep(0.5)
	print("+40 DEFENSE")
	player.defense = 0.9
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)
elif player.kind == "MIXED RNB":
	print("+30 CATCHINESS")
	player.catchiness = 0.15
	time.sleep(0.5)
	print("+30 LYRICS")
	player.lyrics = 0.3
	time.sleep(0.5)
	print("+30 ATTACK")
	player.attack = 30
	time.sleep(0.5)
	print("+30 DEFENSE")
	player.defense = 0.85
	time.sleep(0.5)
	print("+100 HEALTH")
	time.sleep(0.5)
	print("+4 RANKING")
	time.sleep(2)

### more text info ###
print("\033[H\033[J")
time.sleep(2)
artist.listinfo(player)
print("")
time.sleep(2)
input("PRESS ENTER WHEN DONE")
print("BIG SMOKE: I CAN TELL YOU'RE GONNA BE A STAR KID!")
print("\033[H\033[J")
time.sleep(2)
print("")
print("BIG SMOKE: IT'S TIME FOR YOU TO MAKE YOUR FIRST SONG")
time.sleep(2)
print("")
player.songs = input("BIG SMOKE: WHAT DO YOU WANT IT TO BE CALLED? ")
time.sleep(2)
print("")
print(f"BIG SMOKE: {player.songs}...")
time.sleep(2)
print("")
print("BIG SMOKE: SOUNDS FIRE!")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("")
print("BIG SMOKE: ALL DONE. IT SOUNDS LIKE A HIT! CONGRATULATIONS KID")
time.sleep(2)
print("")
print("BIG SMOKE: IM GONNA GO AND TELL THE LABEL, BUT FIRST...")
time.sleep(2)
print("")
print("BIG SMOKE: YOU NEED TO BE CAREFUL OUT THERE. ARTISTS IN YOUR AREA MIGHT GET JEALOUS")
time.sleep(2)
print("")
print("BIG SMOKE: AND EVEN WANNA FIGHT YOU!")
time.sleep(2)
print("")
print("BIG SMOKE: SO I'LL TEACH YOU HOW TO FIGHT...")
time.sleep(2)
print("")
print("BIG SMOKE: LETS TAKE A LOOK AT YOUR STATS AND WHAT THEY MEAN")
time.sleep(4)
print("\033[H\033[J")
displaystats()
time.sleep(2)
print("")
print("BIG SMOKE: YOUR ATTACK STAT IS HOW MUCH DAMAGE YOU DEAL TO YOUR OPPONENT")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: YOUR DEFENSE STAT IS HOW MUCH YOUR OPPONENTS DAMAGE AGAINST YOU IS REDUCED BY")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: YOUR CATCHINESS STAT IS THE CHANCE OF YOUR OPPONENT'S ATTACK MISSING YOU")
print("")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: YOUR LYRICS STAT IS THE CHANCE OF YOUR DAMAGE BEING MULTIPLIED BY 1.5 TIMES")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: YOUR HEALTH IS PRETTY SELF-EXPLANATORY")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: YOU CAN UNLOCK FLOWS AS YOU DEFEAT OTHERS, GIVING YOU STAT BOOSTS")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: THE MORE POPULAR YOU ARE, THE HIGHER SPOT YOU HAVE ON THE BILLBOARD CHARTS")
time.sleep(4)
print("\033[H\033[J")
displaystats()
print("")
print("BIG SMOKE: SPEAKING OF ABILITIES...")
time.sleep(4)
print("")
print("BIG SMOKE: ITS ABOUT TIME YOU PICK A SPECIAL ABILITY")
time.sleep(2)
print("")
print("BIG SMOKE: YOU HAVE SOME OPTIONS")
time.sleep(2)
print("\033[H\033[J")
print("")
print(f"""BIG SMOKE: YOU CAN PICK EITHER

PRODUCER TAG
YOU PRODUCE A HIT BEAT, DOUBLING CATCHINESS, AND ATTACK

BLOOD GANG
YOU GO BACK TO YOUR HOOD AND ROLL WITH YOUR GANG, DOUBLING LYRICS AND HEALTH

SAMPLE
YOU SAMPLE A CARTOON, TRIPLING CATCHINESS AND DOUBLING ATTACK

HEARTBREAK
YOU GET YOUR HEART BROKEN, DOUBLING ATTACK AND DOUBLING CATCHINESS BUT DECREASING HEALTH BY HALF

HYPE
YOU PERFORM {player.songs}, TRIPLING CATCHINESS AND CUTTING OPPONENT'S HEALTH IN HALF

BEAT BY JEFF
YOU RAP ON A BEAT BY JEFF, DOUBLING ATTACK AND TRIPLING LYRICS

    """)
time.sleep(4)
player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
while player.ability != "PRODUCER TAG" and player.ability != "BLOOD GANG" and player.ability != "SAMPLE" and player.ability != "HEARTBREAK" and player.ability != "HYPE" and player.ability != "BEAT BY JEFF":
    time.sleep(2)
    player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
    print("")
print("")
print(f"BIG SMOKE: {player.ability}...")
time.sleep(2)
print("")
print("BIG SMOKE: THAT'S A FINE ABILITY.")
time.sleep(2)
print("")
print("*YOU WALK OUTSIDE*")
time.sleep(2)
print("\033[H\033[J")
time.sleep(2)

### fighting different artists based on what city you chose ###
### every location is the same exact code except for the switching of who you fight, so im only putting comments on the first one, so everything between if player.location == "atlanta" and elif player.location == "florida" is pretty much repeated ###
if player.location == "ATLANTA":
    ### makes variables set to whatever the attribute was before any changes in the actual fight due to special abilities, so i can reset the player's stats after so that it doesnt roll over into future fights ###
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S PIERRE BOURNE KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"PIERRE: {pierrebourne.phrase}")
    time.sleep(2)
    ### makes player fight opponent ###
    artist.fight(pierrebourne)
    ### resetting stats using variables from before ###
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    pierrebourne.health = 100
    player.abilityuse = 1
    pierrebourne.abilityuse = 1
    pierrebourne.attack = 30
    pierrebourne.defense = 0.8
    pierrebourne.catchiness = 0.25
    pierrebourne.lyrics = 0.4
    print("\033[H\033[J")
    ### if the player lost, they keep fighting until they win ###
    while playerwin is False:
        print("PIERRE: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(pierrebourne)
        ### resetting stats using variables from before ###
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        pierrebourne.health = 100
        player.abilityuse = 1
        pierrebourne.abilityuse = 1
        pierrebourne.attack = 30
        pierrebourne.defense = 0.8
        pierrebourne.catchiness = 0.25
        pierrebourne.lyrics = 0.4
        print("\033[H\033[J")
    ### giving stat boosts if you win! ###
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED PIERRE'S FLOW!")
        time.sleep(2)
        player.flow = "PIERRE'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "FLORIDA":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S SKI MASK THE SLUMP GOD KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"SKI: {skimask.phrase}")
    time.sleep(2)
    artist.fight(skimask)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    skimask.health = 100
    player.abilityuse = 1
    skimask.abilityuse = 1
    skimask.attack = 50
    skimask.defense = 0.7
    skimask.catchiness = 0.35
    skimask.lyrics = 0.8
    print("\033[H\033[J")
    while playerwin is False:
        print("SKI: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(skimask)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        skimask.health = 100
        player.abilityuse = 1
        skimask.abilityuse = 1
        skimask.attack = 50
        skimask.defense = 0.7
        skimask.catchiness = 0.35
        skimask.lyrics = 0.8
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.40
        time.sleep(0.5)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED SKI'S FLOW!")
        time.sleep(2)
        player.flow = "SKI'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "NEW YORK":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S SHECK WES KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"SHECK: {sheckwes.phrase}")
    time.sleep(2)
    artist.fight(sheckwes)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    sheckwes.health = 100
    player.abilityuse = 1
    sheckwes.abilityuse = 1
    sheckwes.attack = 30
    sheckwes.defense = 1.0
    sheckwes.catchiness = 0.50
    sheckwes.lyrics = 0
    print("\033[H\033[J")
    while playerwin is False:
        print("SHECK: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(sheckwes)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        sheckwes.health = 100
        player.abilityuse = 1
        sheckwes.abilityuse = 1
        sheckwes.attack = 30
        sheckwes.defense = 1.0
        sheckwes.catchiness = 0.50
        sheckwes.lyrics = 0
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+30 CATCHINESS")
        player.catchiness = player.catchiness + 0.30
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED SHECK'S FLOW!")
        time.sleep(2)
        player.flow = "SHECK'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "CHICAGO":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S JUICE WRLD KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print(f"JUICE: {juicewrld.phrase}")
    time.sleep(2)
    print("")
    artist.fight(juicewrld)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    juicewrld.health = 100
    player.abilityuse = 1
    juicewrld.abilityuse = 1
    juicewrld.attack = 40
    juicewrld.defense = 0.7
    juicewrld.catchiness = 0.35
    juicewrld.lyrics = 0.6
    print("\033[H\033[J")
    while playerwin is False:
        print("JUICE: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(juicewrld)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        juicewrld.health = 100
        player.abilityuse = 1
        juicewrld.abilityuse = 1
        juicewrld.attack = 40
        juicewrld.defense = 0.7
        juicewrld.catchiness = 0.35
        juicewrld.lyrics = 0.6
        print("\033[H\033[J")
    if playerwin is True:
        print("JUICE: YOU GOT LUCKY THIS TIME KID")
        time.sleep(2)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+30 CATCHINESS")
        player.catchiness = player.catchiness + 0.30
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(0.5)
        time.sleep(2)
        print("YOU'VE UNLOCKED JUICE'S FLOW!")
        time.sleep(2)
        player.flow = "JUICE'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "L.A.":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S YG KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"YG: {yg.phrase}")
    time.sleep(2)
    artist.fight(yg)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    yg.health = 100
    player.abilityuse = 1
    yg.abilityuse = 1
    yg.attack = 40
    yg.defense = 0.7
    yg.catchiness = 0.35
    yg.lyrics = 0.8
    print("\033[H\033[J")
    while playerwin is False:
        print("YG: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(yg)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        yg.health = 100
        player.abilityuse = 1
        yg.abilityuse = 1
        yg.attack = 40
        yg.defense = 0.7
        yg.catchiness = 0.35
        yg.lyrics = 0.8
        print("\033[H\033[J")
    if playerwin is True:
        print("YG: YOU GOT LUCKY THIS TIME KID")
        time.sleep(2)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+10 LYRICS")
        player.lyrics = player.lyrics + 0.2
        time.sleep(0.5)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED YG'S FLOW!")
        time.sleep(2)
        player.flow = "YG'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "TEXAS":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: YOU GOT A LOTTA NERVE COMING TO MY CITY AND MAKING MUSIC")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S SPLURGE KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"SPLURGE: {splurge.phrase}")
    time.sleep(2)
    artist.fight(splurge)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 100
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    splurge.health = 200
    player.abilityuse = 1
    splurge.abilityuse = 1
    splurge.attack = 40
    splurge.defense = 1.0
    splurge.catchiness = 0.25
    splurge.lyrics = 0.7
    print("\033[H\033[J")
    while playerwin is False:
        print("SPLURGE: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(splurge)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 100
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        splurge.health = 200
        player.abilityuse = 1
        splurge.abilityuse = 1
        splurge.attack = 40
        splurge.defense = 1.0
        splurge.catchiness = 0.25
        splurge.lyrics = 0.7
        print("\033[H\033[J")
    if playerwin is True:
        print("SPLURGE: YOU GOT LUCKY THIS TIME KID")
        time.sleep(2)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+10 LYRICS")
        player.lyrics = player.lyrics + 0.2
        time.sleep(0.5)
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED SPLURGE'S FLOW!")
        time.sleep(2)
        player.flow = "SPLURGE'S"
        player.abilityuse = 1
        print("\033[H\033[J")

### more text exposition ###
print("BIG SMOKE: WOAH WOAH WOAH! WHAT HAPPENED HERE?")
time.sleep(2)
print("")
print("BIG SMOKE:...")
time.sleep(2)
print("")
print("BIG SMOKE: I SEE!")
time.sleep(2)
print("")
print("BIG SMOKE: I'M GLAD YOU WON!")
time.sleep(2)
print("")
print("BIG SMOKE: YOU'RE PROVING YOURSELF TO BE A GREAT YOUNG ARTIST")
time.sleep(2)
print("")
print("BIG SMOKE: I THINK IT'S TIME FOR YOU TO PUT OUT AN ALBUM TO THE WORLD")
time.sleep(2)
print("")
player.projects = input("BIG SMOKE: WHAT DO YOU WANT IT TO BE CALLED? ")
time.sleep(2)
print("\033[H\033[J")
time.sleep(2)
print("")
print(f"BIG SMOKE: {player.projects}...")
time.sleep(2)
print("")
print("BIG SMOKE: SOUNDS FIRE!")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("")
print("BIG SMOKE: ALL DONE. IT SOUNDS LIKE A HIT! CONGRATULATIONS KID")
time.sleep(2)
print("")
print("BIG SMOKE: IM GONNA GO AND TELL THE LABEL, BUT FIRST...")
time.sleep(2)
print("")
print("BIG SMOKE: YOU CAN PICK ANOTHER ABILITY NOW THAT YOU HAVE A HIGHER RATING")
time.sleep(2)
print("")
print("BIG SMOKE: YOU HAVE SOME MORE OPTIONS")
time.sleep(2)
print("\033[H\033[J")
print("")
print(f"""BIG SMOKE: YOU CAN PICK EITHER

DISAPPEAR
YOU DISAPPEAR FOR 2 YEARS, DOUBLING ATTACK AND LYRICS

LEAN
YOU DRINK LEAN, TRIPLING CATCHINESS AND ATTACK BUT DECREASING HEALTH BY 70

GO TO JAIL
YOU GO TO JAIL, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF

GLO GANG
YOU CALL YOUR GANG, DOUBLING HEALTH

TR3WAY
YOU YELL 'TR3YWAY', TRIPLING ATTACK BUT DECREASING HEALTH BY 70

THE RACE
YOU RUN FROM THE POLICE, DOUBLING CATCHINESS AND ATTACK

    """)
time.sleep(4)
player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
while player.ability != "DISAPPEAR" and player.ability != "LEAN" and player.ability != "GO TO JAIL" and player.ability != "GLO GANG" and player.ability != "TR3WAY" and player.ability != "THE RACE":
    time.sleep(2)
    player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
    print("")
print("")
print(f"BIG SMOKE: {player.ability}...")
player.abilityuse = 1
time.sleep(2)
print("")
print("BIG SMOKE: THAT'S A FINE ABILITY.")
time.sleep(2)
print("\033[H\033[J")
time.sleep(2)
print("")
print("BIG SMOKE: ALSO...")
time.sleep(2)
print("")
print("BIG SMOKE: I BOOKED A LOCAL CONCERT FOR YOU TONIGHT AT THE DANIELS THEATER ON 4TH STREET")
time.sleep(2)
print("")
print("BIG SMOKE: BE THERE AT 8 TONIGHT...")
time.sleep(2)
print("\033[H\033[J")
time.sleep(2)
print("")
print("8 O'CLOCK TONIGHT")
time.sleep(4)
print("\033[H\033[J")
time.sleep(2)

### more of the exact same stuff as before ###
if player.location == "ATLANTA":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT PIERRE")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S FUTURE KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"FUTURE: {future.phrase}")
    time.sleep(2)
    artist.fight(future)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    future.health = 200
    player.abilityuse = 1
    future.abilityuse = 1
    future.attack = 60
    future.defense = 0.9
    future.catchiness = 0.35
    future.lyrics = 0.5
    print("\033[H\033[J")
    while playerwin is False:
        print("FUTURE: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(future)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        future.health = 200
        player.abilityuse = 1
        future.abilityuse = 1
        future.attack = 60
        future.defense = 0.9
        future.catchiness = 0.35
        future.lyrics = 0.5
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED FUTURE'S FLOW!")
        time.sleep(2)
        player.flow = "FUTURE'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "FLORIDA":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT SKI")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S KODAK BLACK KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"KODAK: {kodakblack.phrase}")
    time.sleep(2)
    artist.fight(kodakblack)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    kodakblack.health = 200
    player.abilityuse = 1
    kodakblack.abilityuse = 1
    kodakblack.attack = 70
    kodakblack.defense = 0.7
    kodakblack.catchiness = 0.3
    kodakblack.lyrics = 0.5
    print("\033[H\033[J")
    while playerwin is False:
        print("KODAK: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(kodakblack)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        kodakblack.health = 200
        player.abilityuse = 1
        kodakblack.abilityuse = 1
        kodakblack.attack = 70
        kodakblack.defense = 0.7
        kodakblack.catchiness = 0.3
        kodakblack.lyrics = 0.5
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED KODAK'S FLOW!")
        time.sleep(2)
        player.flow = "KODAK'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "NEW YORK":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT SHECK WES")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S TEKASHI KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"TEKASHI: {tekashi.phrase}")
    time.sleep(2)
    artist.fight(tekashi)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    tekashi.health = 200
    player.abilityuse = 1
    tekashi.abilityuse = 1
    tekashi.attack = 60
    tekashi.defense = 0.8
    tekashi.catchiness = 0.35
    tekashi.lyrics = 0.6
    print("\033[H\033[J")
    while playerwin is False:
        print("TEKASHI: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(tekashi)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        tekashi.health = 200
        player.abilityuse = 1
        tekashi.abilityuse = 1
        tekashi.attack = 60
        tekashi.defense = 0.8
        tekashi.catchiness = 0.35
        tekashi.lyrics = 0.6
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED TEKASHI'S FLOW!")
        time.sleep(2)
        player.flow = "TEKASHI'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "CHICAGO":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT JUICE WRLD")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S CHIEF KEEF KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"CHIEF KEEF: {chiefkeef.phrase}")
    time.sleep(2)
    artist.fight(chiefkeef)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    chiefkeef.health = 200
    player.abilityuse = 1
    chiefkeef.abilityuse = 1
    chiefkeef.attack = 70
    chiefkeef.defense = 0.8
    chiefkeef.catchiness = 0.35
    chiefkeef.lyrics = 0.6
    print("\033[H\033[J")
    while playerwin is False:
        print("CHIEF KEEF: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(chiefkeef)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        chiefkeef.health = 200
        player.abilityuse = 1
        chiefkeef.abilityuse = 1
        chiefkeef.attack = 70
        chiefkeef.defense = 0.8
        chiefkeef.catchiness = 0.35
        chiefkeef.lyrics = 0.6
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED KEEF'S FLOW!")
        time.sleep(2)
        player.flow = "KEEF'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "L.A.":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT YG")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S FRANK OCEAN KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"FRANK OCEAN: {frankocean.phrase}")
    time.sleep(2)
    artist.fight(frankocean)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    frankocean.health = 200
    player.abilityuse = 1
    frankocean.abilityuse = 1
    frankocean.attack = 50
    frankocean.defense = 0.4
    frankocean.catchiness = 0.4
    frankocean.lyrics = 0.8
    print("\033[H\033[J")
    while playerwin is False:
        print("FRANK OCEAN: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(frankocean)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        frankocean.health = 200
        player.abilityuse = 1
        frankocean.abilityuse = 1
        frankocean.attack = 50
        frankocean.defense = 0.4
        frankocean.catchiness = 0.4
        frankocean.lyrics = 0.8
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED FRANK'S FLOW!")
        time.sleep(2)
        player.flow = "FRANK'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "TEXAS":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE THAT {player.name.upper()} KID RIGHT!")
    time.sleep(2)
    print("")
    print("!!!: SO YOU'RE THE ONE WHO FOUGHT SPLURGE")
    time.sleep(2)
    print("")
    print("!!!: AND NOW YOU'RE DOING A SHOW THE SAME NIGHT I AM?")
    time.sleep(2)
    print("")
    print("!!!: THE NAME'S TAY-K KID, LET'S SEE WHAT YOU GOT")
    time.sleep(2)
    print("")
    print(f"TAY-K: {tayk.phrase}")
    time.sleep(2)
    artist.fight(tayk)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 200
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    tayk.health = 200
    player.abilityuse = 1
    tayk.abilityuse = 1
    tayk.attack = 80
    tayk.defense = 1.2
    tayk.catchiness = 0.3
    tayk.lyrics = 0.6
    print("\033[H\033[J")
    while playerwin is False:
        print("TAY-K: YOU'RE NOT GONNA GET OFF THAT EASILY.")
        time.sleep(2)
        artist.fight(tayk)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 200
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        tayk.health = 200
        player.abilityuse = 1
        tayk.abilityuse = 1
        tayk.attack = 80
        tayk.defense = 1.2
        tayk.catchiness = 0.3
        tayk.lyrics = 0.6
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED TAY-K'S FLOW!")
        time.sleep(2)
        player.flow = "TAY-K'S"
        player.abilityuse = 1
        print("\033[H\033[J")

### more textposition ###
print("")
print("BIG SMOKE: WOAH!")
time.sleep(2)
print("")
print("BIG SMOKE: THE CROWD LOVED IT!")
time.sleep(2)
print("")
print("BIG SMOKE: A CLIP OF YOUR GUYS' FIGHT WENT VIRAL AND GOT REPOSTED ON WORLDSTAR!")
time.sleep(2)
print("")
print("BIG SMOKE: YOU'RE FAMOUS NOW KID!")
time.sleep(2)
print("")
print("BIG SMOKE: BUT NOW YOU HAVE AN EVEN BIGGER TARGET ON YOUR BACK")
time.sleep(2)
print("")
print("BIG SMOKE: SO NATURALLY I BOOKED YOU FOR ROLLING LOUD TO CAPITALIZE OFF OF THIS SUCCESS")
time.sleep(2)
print("")
print("BIG SMOKE: ITS THIS SATURDAY, AND ALL OF THE BIG ACTS LIKE PLAYBOI CARTI, XXXTENTACION, ASAP ROCKY, KANYE WEST, KENDRICK LAMAR, AND TRAVIS SCOTT WILL BE THERE!")
time.sleep(4)
print("")
print("BIG SMOKE: BE PREPARED IN CASE ONE OF THEM TRY TO FIGHT YOU, THEY'RE PRETTY POWERFUL")
time.sleep(2)
print("")
print("BIG SMOKE: JUST IN CASE, YOU SHOULD PICK A NEW ABILITY")
time.sleep(2)
print("")
print("BIG SMOKE: YOU HAVE SOME OPTIONS")
time.sleep(2)
print("\033[H\033[J")
print("")
print(f"""BIG SMOKE: YOU CAN PICK EITHER

QUICK SPEED
YOU RAP AT FULL SPEED, DOUBLING ATTACK AND LYRICS

BABY VOICE
YOU CHANGE YOUR VOICE, TRIPLING ATTACK AND DOUBLING CATCHINESS BUT CUTTING HEALTH IN HALF

BLACK AND BLONDE
YOU REVERT BACK TO YOUR OLD SELF, TRIPLING ATTACK BUT DECREASING HEALTH BY 150

ADAPT
YOU PUSH THE GENRE FORWARD, TRIPLING HEALTH

ASAP MOB
YOU CALL THE ASAP MOB TO DEAL AN EXTRA 60 DAMAGE TO OPPONENT

RAGE
YOU PERFORM AT A CONCERT, TRIPLING ATTACK BUT DECREASING HEALTH BY HALF

    """)
time.sleep(4)
player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
while player.ability != "QUICK SPEED" and player.ability != "BABY VOICE" and player.ability != "BLACK AND BLONDE" and player.ability != "ADAPT" and player.ability != "ASAP MOB" and player.ability != "RAGE":
    time.sleep(2)
    player.ability = input("BIG SMOKE: SO WHICH ONE DO YOU WANT? ")
    print("")
print("")
time.sleep(2)
print("\033[H\033[J")
print("")
print("THIS SATURDAY")
time.sleep(4)
print("\033[H\033[J")
print("")
time.sleep(2)

### you know the drill by now ###
if player.location == "ATLANTA":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE FUTURE LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"CARTI: {playboicarti.phrase}")
    time.sleep(2)
    artist.fight(playboicarti)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    playboicarti.health = 300
    player.abilityuse = 1
    playboicarti.abilityuse = 1
    playboicarti.attack = 70
    playboicarti.defense = 0.8
    playboicarti.catchiness = 0.5
    playboicarti.lyrics = 0.2
    print("\033[H\033[J")
    while playerwin is False:
        print("CARTI: AYE SLATT, RUN ME THAT FADE ONE MORE TIME.")
        time.sleep(2)
        artist.fight(playboicarti)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        playboicarti.health = 300
        player.abilityuse = 1
        playboicarti.abilityuse = 1
        playboicarti.attack = 70
        playboicarti.defense = 0.8
        playboicarti.catchiness = 0.5
        playboicarti.lyrics = 0.2
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED CARTI'S FLOW!")
        time.sleep(2)
        player.flow = "CARTI'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "FLORIDA":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE KODAK LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"X: {xxxtentacion.phrase}")
    time.sleep(2)
    artist.fight(xxxtentacion)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    xxxtentacion.health = 300
    player.abilityuse = 1
    xxxtentacion.abilityuse = 1
    xxxtentacion.attack = 80
    xxxtentacion.defense = 0.6
    xxxtentacion.catchiness = 0.35
    xxxtentacion.lyrics = 0.9
    print("\033[H\033[J")
    while playerwin is False:
        print("X: I LOVE IT WHEN THEY RUN, BUT YOU CAN'T RUN THIS TIME")
        time.sleep(2)
        artist.fight(xxxtentacion)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        xxxtentacion.health = 300
        player.abilityuse = 1
        xxxtentacion.abilityuse = 1
        xxxtentacion.attack = 80
        xxxtentacion.defense = 0.6
        xxxtentacion.catchiness = 0.35
        xxxtentacion.lyrics = 0.9
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED X'S FLOW!")
        time.sleep(2)
        player.flow = "X'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "NEW YORK":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE TEKASHI LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"ROCKY: {asaprocky.phrase}")
    time.sleep(2)
    artist.fight(asaprocky)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    asaprocky.health = 300
    player.abilityuse = 1
    asaprocky.abilityuse = 1
    asaprocky.attack = 80
    asaprocky.defense = 0.7
    asaprocky.catchiness = 0.3
    asaprocky.lyrics = 0.7
    print("\033[H\033[J")
    while playerwin is False:
        print("ROCKY: WE DEADA** GOTTA SHOOT THE FADE AGAIN, B.")
        time.sleep(2)
        artist.fight(asaprocky)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        asaprocky.health = 300
        player.abilityuse = 1
        asaprocky.abilityuse = 1
        asaprocky.attack = 80
        asaprocky.defense = 0.7
        asaprocky.catchiness = 0.3
        asaprocky.lyrics = 0.7
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED ROCKY'S FLOW!")
        time.sleep(2)
        player.flow = "ROCKY'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "CHICAGO":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness

    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE CHIEF KEEF LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"KANYE: {kanyewest.phrase}")
    time.sleep(2)
    artist.fight(kanyewest)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    kanyewest.health = 300
    player.abilityuse = 1
    kanyewest.abilityuse = 1
    kanyewest.attack = 80
    kanyewest.defense = 0.5
    kanyewest.catchiness = 0.3
    kanyewest.lyrics = 0.8
    print("\033[H\033[J")
    while playerwin is False:
        print("KANYE: THE MEDIA THINKS IM CRAZY, BUT WOULD A CRAZY PERSON KEEP FIGHTING YOU EVEN THOUGH YOU'RE CLEARLY OUTMATCHED?")
        time.sleep(2)
        artist.fight(kanyewest)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        kanyewest.health = 300
        player.abilityuse = 1
        kanyewest.abilityuse = 1
        kanyewest.attack = 80
        kanyewest.defense = 0.5
        kanyewest.catchiness = 0.3
        kanyewest.lyrics = 0.8
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED KANYE'S FLOW!")
        time.sleep(2)
        player.flow = "KANYE'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "L.A.":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE FRANK OCEAN LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"KENDRICK: {kendricklamar.phrase}")
    time.sleep(2)
    artist.fight(kendricklamar)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    kendricklamar.health = 300
    player.abilityuse = 1
    kendricklamar.abilityuse = 1
    kendricklamar.attack = 70
    kendricklamar.defense = 0.5
    kendricklamar.catchiness = 0.35
    kendricklamar.lyrics = 0.9
    print("\033[H\033[J")
    while playerwin is False:
        print("KENDRICK: WE NEED TO STOP THIS VIOLENCE WITHIN THE RAP COMMUNITY, BUT RIGHT NOW I HAVE TO FIGHT YOU AGAIN.")
        time.sleep(2)
        artist.fight(kendricklamar)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        kendricklamar.health = 300
        player.abilityuse = 1
        kendricklamar.abilityuse = 1
        kendricklamar.attack = 70
        kendricklamar.defense = 0.5
        kendricklamar.catchiness = 0.35
        kendricklamar.lyrics = 0.9
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED KENDRICK'S FLOW!")
        time.sleep(2)
        player.flow = "KENDRICK'S"
        player.abilityuse = 1
        print("\033[H\033[J")
elif player.location == "TEXAS":
    playerattack = player.attack
    playerdefense = player.defense
    playerhealth = player.health
    playerlyrics = player.lyrics
    playercatchiness = player.catchiness
    print("!!!: HEY!")
    time.sleep(2)
    print("")
    print(f"!!!: YOU'RE {player.name.upper()} RIGHT?")
    time.sleep(2)
    print("")
    print(f"!!!: I HEARD YOUR NEW ALBUM, {player.projects}, AND ITS PRETTY HOT!")
    time.sleep(2)
    print("")
    print("!!!: WE SHOULD GET IN THE STUDIO SOMEDAY...")
    time.sleep(2)
    print("")
    print("!!!: BUT RIGHT NOW I GOTTA FIGHT YOU, BECAUSE YOU DISRESPECTED MY LIL HOMIE TAY-K LIKE THAT.")
    time.sleep(2)
    print("")
    print(f"TRAV: {travisscott.phrase}")
    time.sleep(2)
    artist.fight(travisscott)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 300
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    travisscott.health = 300
    player.abilityuse = 1
    travisscott.abilityuse = 1
    travisscott.attack = 60
    travisscott.defense = 0.7
    travisscott.catchiness = 0.35
    travisscott.lyrics = 0.5
    print("\033[H\033[J")
    while playerwin is False:
        print("TRAV: THIS AINT MY FIRST RODEO, BUT IM GONNA KNOCK YOU ALL THE WAY TO ASTROWORLD")
        time.sleep(2)
        artist.fight(travisscott)
        player.attack = playerattack
        player.defense = playerdefense
        player.health = 300
        player.lyrics = playerlyrics
        player.catchiness = playercatchiness
        travisscott.health = 300
        player.abilityuse = 1
        travisscott.abilityuse = 1
        travisscott.attack = 60
        travisscott.defense = 0.7
        travisscott.catchiness = 0.35
        travisscott.lyrics = 0.5
        print("\033[H\033[J")
    if playerwin is True:
        print("+20 CATCHINESS")
        player.catchiness = player.catchiness + 0.20
        time.sleep(0.5)
        print("+20 LYRICS")
        player.lyrics = player.lyrics + 0.4
        time.sleep(0.5)
        print("+20 ATTACK")
        player.attack = player.attack + 20
        time.sleep(0.5)
        print("+10 DEFENSE")
        player.defense = player.defense -0.05
        time.sleep(0.5)
        print("+100 HEALTH")
        player.health = player.health + 100
        time.sleep(0.5)
        print("+40 CATCHINESS")
        player.catchiness = player.catchiness + 0.40
        time.sleep(0.5)
        print("+2 RANKING")
        player.rating = 6
        time.sleep(2)
        print("YOU'VE UNLOCKED TRAV'S FLOW!")
        time.sleep(2)
        player.flow = "TRAV'S"
        player.abilityuse = 1
        print("\033[H\033[J")
### more texpositional information ###
print("")
print("BIG SMOKE: WOAH!")
time.sleep(2)
print("")
print("BIG SMOKE: I HAD NO IDEA YOU WERE THIS GOOD KID!")
time.sleep(2)
print("")
print("BIG SMOKE: YOU'RE A BONAFIDE STAR!")
time.sleep(2)
print("")
print("BIG SMOKE: I HAVE SOMETHING TO G-")
time.sleep(2)
print("")
print("BIG SMOKE: ...")
time.sleep(2)
print("")
print("BIG SMOKE: ...")
time.sleep(2)
print("")
print("BIG SMOKE: WHAT'S THAT?")
time.sleep(2)
print("")
print("!!!: BAD TING YA KNO...")
time.sleep(2)
print("")
print("!!!: INNA 6 WE NO LIKE YA KIND DAWG EH?")
time.sleep(2)
print("")
print("!!!: ME NAME DRAKE AND ME WANT YA STYLE MON")
time.sleep(2)
### same as the fight stuff from before ###
player.health = 400
playerattack = player.attack
playerdefense = player.defense
playerhealth = player.health
playerlyrics = player.lyrics
playercatchiness = player.catchiness
drake.abilityuse = 2
print("")
print(f"DRAKE: {drake.phrase}")
time.sleep(2)
artist.fight(drake)
player.attack = playerattack
player.defense = playerdefense
player.health = 400
player.lyrics = playerlyrics
player.catchiness = playercatchiness
drake.health = 400
player.abilityuse = 1
drake.abilityuse = 1
drake.attack = 100
drake.defense = 0.5
drake.catchiness = 0.5
drake.lyrics = 0.5
print("\033[H\033[J")
while playerwin is False:
    print("DRAKE: YA NO GET AWAY THAT EASY TING EH?")
    time.sleep(2)
    artist.fight(drake)
    player.attack = playerattack
    player.defense = playerdefense
    player.health = 400
    player.lyrics = playerlyrics
    player.catchiness = playercatchiness
    drake.health = 400
    player.abilityuse = 1
    drake.abilityuse = 1
    drake.attack = 100
    drake.defense = 0.5
    drake.catchiness = 0.5
    drake.lyrics = 0.5
    print("\033[H\033[J")
if playerwin is True:
    ### final dislpaying of texpositional information ###
    print("")
    print(f"BIG SMOKE: {player.name}...")
    time.sleep(2)
    print("")
    print("BIG SMOKE: YOU JUST DEFEATED DRAKE, THE BIGGEST STAR IN THE WORLD")
    time.sleep(2)
    print("")
    print("BIG SMOKE: YOU ARE NOW THE MOST POPULAR ARTIST IN THE WORLD, AND CREATED YOUR OWN WAVE")
    time.sleep(3)
    print("")
    print("BIG SMOKE: I'VE NEVER BEEN MORE PROUD THAN THIS MOMENT RIGHT NOW")
    time.sleep(2)
    print("")
    print("BIG SMOKE: I SAW YOU COME UP FROM THE STREETS, AND NOW YOU'RE ON TOP OF THE WORLD!")
    time.sleep(2)
    print("")
    print("BIG SMOKE: I THINK ITS TIME TO RETIRE AT THE TOP BEFORE YOU BECOME IRRELEVANT AND OLD")
    time.sleep(2)
    print("")
    print("BIG SMOKE: THANK YOU FOR EVERYTHING AND I WISH YOU LUCK FOR THE REST OF YOUR LIFE")
    time.sleep(2)
    print("")
    print("BIG SMOKE: THANK YOU...")
    time.sleep(2)
    print("")
    print("A SINGLE TEAR DROPS FROM HIS FACE")
    time.sleep(4)
    print("")
    print("T H E   E N D")

    time.sleep(4)
    print("")
    print("#LLJ")
    time.sleep(8)
    print("\033[H\033[J")
