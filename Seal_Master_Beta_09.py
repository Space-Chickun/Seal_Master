import sys
import math
import os


dash = '-' * 165

os.system('cls')

class seal():
	# List of information about the seals
	def __init__(self, Seal, Attribute, Stats, Name):
		self.Seal = Seal
		self.Attribute = Attribute
		self.Stats = Stats
		self.Name = Name

#			Seal				Attribute			Stats								Name
seals_all = [0,																
	seal("1. Tanemon",			"Attack",			{1:[0,10,20,40,60,80,100]}, 		"Tanemon"),
	seal("2. Guilmon",			"Attack",			{2:[0,15,30,60,90,120,150]},		"Guilmon"),
	seal("3. Patamon",			"Attack",			{3:[0,15,30,60,90,120,150]},		"Patamon"),
	seal("4. Mushroomon",		"Attack",			{4:[0,15,30,60,90,120,150]},		"Mushroomon"),
	seal("5. BlackGarurumon",	"Attack",			{5:[0,20,40,80,120,160,200]},		"BlackGarurumon"),
	seal("6. Chrysalimon",		"Attack",			{6:[0,20,40,80,120,160,200]},		"Chrysalimon"),
	seal("7. Devimon",			"Attack",			{7:[0,20,40,80,120,160,200]},		"Devimon"),
	seal("8. Giromon",			"Attack",			{8:[0,25,50,100,150,200,250]},		"Giromon"),
	seal("9. Cherrymon",		"Attack",			{9:[0,25,50,100,150,200,250]},		"Cherrymon"),
	seal("10. MarineDevimon",	"Attack",			{10:[0,25,50,100,150,200,250]}, 	"MarineDevimon"),
	seal("11. Azulongmon",		"Attack",			{11:[0,30,60,120,180,240,300]}, 	"Azulongmon"),
	seal("12. Examon",			"Attack",			{12:[0,30,60,120,180,240,300]}, 	"Examon"),
	seal("13. Omegamon",		"Attack",			{13:[0,30,60,120,180,240,300]},		"Omegamon"),
	seal("14. Dexmon",			"Attack",			{14:[0,30,60,120,180,240,300]}, 	"Dexmon"),
	seal("15. Koromon",			"Critical",			{15:[0,.1,.2,.4,.6,.8,1]},			"Koromon"),
	seal("16. Kunemon",			"Critical",			{16:[0,.15,.3,.6,.9,1.2,1.5]},		"Kunemon"),
	seal("17. Sharmamon",		"Critical",			{17:[0,.15,.3,.6,.9,1.2,1.5]},		"Sharmamon"),
	seal("18. Kyubimon",		"Critical",			{18:[0,.2,.4,.8,1.2,1.6,2]},		"Kyubimon"),
	seal("19. Togemon",			"Critical",			{19:[0,.2,.4,.8,1.2,1.6,2]},		"Togemon"),
	seal("20. Datamon",			"Critical",			{20:[0,.25,.5,1,1.5,2,2.5]},		"Datamon"),
	seal("21. Volcamon",		"Critical",			{21:[0,.25,.5,1,1.5,2,2.5]},		"Volcamon"),
	seal("22. SaberLeomon",		"Critical",			{22:[0,.3,.6,1.2,1.8,2.4,3]},		"SaberLeomon"),
	seal("23. Drimogemon",		"Hit",				{23:[0,10,20,40,60,80,100]},		"Drimogemon"),
	seal("24. FanBeemon",		"Hit",				{24:[0,10,20,40,60,80,100]},		"FanBeemon"),
	seal("25. Gabumon",			"Hit",				{25:[0,10,20,40,60,80,100]},		"Gabumon"),
	seal("26. Coredramon(Blue)","Hit",				{26:[0,20,40,80,120,160,200]},		"Coredramon(Blue)"),
	seal("27. Dorugamon",		"Hit",				{27:[0,20,40,80,120,160,200]},		"Dorugamon"),
	seal("28. DarkTyrannomon",	"Hit",				{28:[0,20,40,80,120,160,200]},		"DarkTyrannomon"),
	seal("29. Garudamon",		"Hit",				{29:[0,30,60,120,180,240,300]},		"Garudamon"),
	seal("30. Knightmon",		"Hit",				{30:[0,30,60,120,180,240,300]},		"Knightmon"),
	seal("31. Parasimon",		"Hit",				{31:[0,40,80,160,240,320,400]},		"Parasimon"),
	seal("32. LordKnightmon",	"Hit",				{32:[0,40,80,160,240,320,400]},		"LordKnightmon"),
	seal("33. Baihumon",		"Hit",				{33:[0,50,100,200,300,400,500]},	"Baihumon"),
	seal("34. Craniamon",		"Hit",				{34:[0,50,100,200,300,400,500]},	"Craniamon"),
	seal("35. Gazimon",			"HP",				{35:[0,15,30,60,90,120,150]},		"Gazimon"),
	seal("36. Keramon",			"HP",				{36:[0,15,30,60,90,120,150]},		"Keramon"),
	seal("37. Tsunomon",		"HP",				{37:[0,15,30,60,90,120,150]},		"Tsunomon"),
	seal("38. Veemon",			"HP",				{38:[0,15,30,60,90,120,150]},		"Veemon"),
	seal("39. Guardromon",		"HP",				{39:[0,20,40,80,120,160,200]},		"Guardromon"),
	seal("40. Kentarumon",		"HP",				{40:[0,20,40,80,120,160,200]},		"Kentarumon"),
	seal("41. Soulmon",			"HP",				{41:[0,20,40,80,120,160,200]},		"Soulmon"),
	seal("42. ReptileDramon",	"HP",				{42:[0,20,40,80,120,160,200]},		"Reptiledramon"),
	seal("43. Sinduramon",		"HP",				{43:[0,25,50,100,150,200,250]},		"Sinduramon"),
	seal("44. SoulSatamon",		"HP",				{44:[0,25,50,100,150,200,250]},		"SoulSatamon"),
	seal("45. DexDoruGreymon",	"HP",				{45:[0,30,60,120,180,240,300]},		"DexDoruGreymon"),
	seal("46. Ebonwumon",		"HP",				{46:[0,50,100,200,300,400,500]},	"Ebonwumon"),
	seal("47. UlForceVeedramon","HP",				{47:[0,50,100,200,300,400,500]},	"UlForceVeedramon"),
	seal("48. DemiMeramon",		"Digisoul",			{48:[0,10,20,40,60,80,100]},		"DemiMeramon"),
	seal("49. Agumon",			"Digisoul",			{49:[0,20,40,80,120,160,200]},		"Agumon"),
	seal("50. Candlemon",		"Digisoul",			{50:[0,20,40,80,120,160,200]},		"Candlemon"),
	seal("51. ToyAgumon",		"Digisoul",			{51:[0,20,40,80,120,160,200]},		"ToyAgumon"),
	seal("52. Dorumon",			"Digisoul",			{52:[0,20,40,80,120,160,200]},		"Dorumon"),
	seal("53. Coredramon(Green)","Digisoul",		{53:[0,30,60,120,180,240,300]},		"Coredramon(Green)"),
	seal("54. Woodmon",			"Digisoul",			{54:[0,30,60,120,180,240,300]},		"Woodmon"),
	seal("55. Asuramon",		"Digisoul",			{55:[0,40,80,160,240,320,400]},		"Asuramon"),
	seal("56, SkullGreymon",	"Digisoul",			{56:[0,40,80,160,240,320,400]},		"SkullGreymon"),
	seal("57. WereGarurumon",	"Digisoul",			{57:[0,40,80,160,240,320,400]},		"WereGarurumon"),
	seal("58. Diablomon",		"Digisoul",			{58:[0,50,100,200,300,400,500]},	"Diablomon"),
	seal("59. Zhuqiaomon",		"Digisoul",			{59:[0,60,120,240,360,480,600]},	"Zhuqiaomon"),
	seal("60. Upamon",			"Defense",			{60:[0,8,16,32,48,64,80]},			"Upamon"),
	seal("61. Elecmon",			"Defense",			{61:[0,10,20,40,60,80,100]},		"Elecmon"),
	seal("62. Goblimon",		"Defense",			{62:[0,10,20,40,60,80,100]},		"Goblimon"),
	seal("63. Renamon",			"Defense",			{63:[0,10,20,40,60,80,100]},		"Renamon"),
	seal("64. Flymon",			"Defense",			{64:[0,15,30,60,90,120,150]},		"Flymon"),
	seal("65. Leomon",			"Defense",			{65:[0,15,30,60,90,120,150]},		"Leomon"),
	seal("66. Meramon",			"Defense",			{66:[0,15,30,60,90,120,150]},		"Meramon"),
	seal("67. Rockmon",			"Defense",			{67:[0,15,30,60,90,120,150]},		"Rockmon"),
	seal("68. Monochromon",		"Defense",			{68:[0,15,30,60,90,120,150]},		"Monochromon"),
	seal("69. Meteormon",		"Defense",			{69:[0,20,40,80,120,160,200]},		"Meteormon"),
	seal("70. WaruMonzaemon",	"Defense",			{70:[0,20,40,80,120,160,200]},		"WaruMonzaemon"),
	seal("71. Kimeramon",		"Defense",			{71:[0,25,50,100,150,200,250]},		"Kimeramon"),
	seal("72. Kentaurosmon",	"Defense",			{72:[0,25,50,100,150,200,250]},		"Kentaurosmon"),
	seal("73. Dracmon",			"Block",			{73:[0,.1,.2,.4,.6,.8,1]},			"Dracmon"),
	seal("74. Tentomon",		"Block",			{74:[0,.1,.2,.4,.6,.8,1]},			"Tentomon"),
	seal("75. Sangloupmon",		"Block",			{75:[0,.15,.3,.6,.9,1.2,1.5]},		"Sangloupmon"),
	seal("76. Waspmon",			"Block",			{76:[0,.15,.3,.6,.9,1.2,1.5]},		"Waspmon"),
	seal("77. Etemon",			"Block",			{77:[0,.2,.4,.8,1.2,1.6,2]},		"Etemon"),
	seal("78. MegaSeadramon",	"Block",			{78:[0,.2,.4,.8,1.2,1.6,2]},		"MegaSeadramon"),
	seal("79. Vikaralamon",		"Block",			{79:[0,.2,.4,.8,1.2,1.6,2]},		"Vikaralamon"),
	seal("80. Armadillomon",	"Evade",			{80:[0,.2,.2,.4,.6,.8,1]},			"Armadillomon"),
	seal("81. Impmon",			"Evade",			{81:[0,.2,.2,.4,.6,.8,1]},			"Impmon"),
	seal("82. Digmon",			"Evade",			{82:[0,.2,.4,.8,1.2,1.6,2]},		"Digmon"),
	seal("83. Veedramon",		"Evade",			{83:[0,.2,.4,.8,1.2,1.6,2]},		"Veedramon"),
	seal("84. Gatomon",			"Evade",			{84:[0,.2,.4,.8,1.2,1.6,2]},		"Gatomon"),
	seal("85. Allomon",			"Evade",			{85:[0,.2,.4,.8,1.2,1.6,2]},		"Allomon"),
	seal("86. Lillymon",		"Evade",			{86:[0,.3,.6,1.2,1.8,2.4,3]},		"Lillymon"),
	seal("87. Mystimon",		"Evade",			{87:[0,.3,.6,1.2,1.8,2.4,3]},		"Mystimon"),
	seal("88. NeoDevimon",		"Evade",			{88:[0,.3,.6,1.2,1.8,2.4,3]},		"NeoDevimon"),
	seal("89. Dynasmon",		"Evade",			{89:[0,.35,.7,1.4,2.1,2.8,3.5]},	"Dynasmon"),
	seal("90. DexDorugoramon",	"Evade",			{90:[0,.35,.7,1.4,2.1,2.8,3.5]},	"DexDorugoramon")
	]

final_comparrison_array = [['Name', 'Cost per Card', 'Cards Needed', 'Total Card Cost', 'Openers Needed', 'Openers Cost', 'Bonus Gained', 'Total Cost', 'Cost per Point']]
	
	
#selection_1 = int(input(
"""What would you like to do?
1. Compare all cards of a specific attribute.
2. Compare specific cards.
3. Quit
			\n\n\n
Choose a number:\t"""#))

while True:
	selection_1 = int(input(
	"""What would you like to do?
1. Compare all cards of a specific attribute.
2. Compare specific cards.
3. Quit
\n\n\n
Choose a number:\t"""))

	if selection_1 == 3:
		print('Good bye!')
		exit()
	elif selection_1 == 1 or selection_1 == 2:
		selection_2 = int(input(
"""Which stat would you like to compare?
1. Attack (AT)
2. Critical Hit Rate (CT)
3. Hit Rate (HT)
4. Health Points (HP)
5. Digi-Soul Points (DS)
6. Defense (DE)
7. Block Rate (BL)
8. Evade Rate (EV)
\n\n\n
 Choose a number:\t"""))
		break

def print_completed_array():
	for i in range(len(final_comparrison_array)):
		if i == 0:
			print(dash)
			print('{:<15s} {:<15s} {:<15s} {:<18s} {:<15s} {:<15s} {:<15s} {:<15s} {:<15s}'.format(final_comparrison_array[i][0], final_comparrison_array[i][1], final_comparrison_array[i][2], final_comparrison_array[i][3], final_comparrison_array[i][4], final_comparrison_array[i][5], final_comparrison_array[i][6], final_comparrison_array[i][7], final_comparrison_array[i][8]))
			print(dash)
		else:
			print('{:<15s} {:^15d} {:^15d} {:^18d} {:^15d} {:^15s} {:^15d} {:^15d} {:^15d}'.format(final_comparrison_array[i][0], final_comparrison_array[i][1], final_comparrison_array[i][2], final_comparrison_array[i][3], final_comparrison_array[i][4], final_comparrison_array[i][5], final_comparrison_array[i][6], final_comparrison_array[i][7], round(final_comparrison_array[i][8],3)))
 
def seal_comparrison_single():
		
	i = 0
		
	for s in seals_all:
		if i == 0:
			i += 1
			continue
		elif s.Attribute == seal_attribute:
			print(s.Seal)
		
	while True:
		seal_select = int(input("Select a seal to compare:\t"))
		seal_number = int(input("How many {} seals do you already have open?\t".format(seals_all[seal_select].Name)))
		if seal_number == 0:
			bonus = round((seals_all[seal_select].Stats[seal_select][1]),2)
			print("Your current level is unopened. Your next bonus for {} is at 1 card and will grant you {} {} .".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][1],seals_all[seal_select].Attribute))
			cards_needed = 50
			print("Recommend opening seals in intervals of 50 to get full use out of openers.")
			break
		elif seal_number == 1:
			bonus = round((seals_all[seal_select].Stats[seal_select][2] - seals_all[seal_select].Stats[seal_select][1]),2)
			print("Your current level is Normal. Your next bonus for {} is at 50 cards and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][2],seals_all[seal_select].Attribute,bonus))
			cards_needed = 49
			break
		elif seal_number >= 2 and seal_number <= 49:
			bonus = round((seals_all[seal_select].Stats[seal_select][2] - seals_all[seal_select].Stats[seal_select][1]),2)
			print("Your next level is Normal. Your next bonus for {} is at 50 seals and will grant you {} {}, an increase of {}".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][2],seals_all[seal_select].Attribute,bonus))
			cards_needed = 50 - seal_number
			break
		elif seal_number == 50:
			bonus = round((seals_all[seal_select].Stats[seal_select][3] - seals_all[seal_select].Stats[seal_select][2]),2)
			print("Your current level is Bronze. Your next bonus for {} is at 200 cards and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][3],seals_all[seal_select].Attribute,bonus))
			cards_needed = 150
			break
		elif seal_number >= 51 and seal_number <= 199:
			bonus = round((seals_all[seal_select].Stats[seal_select][3] - seals_all[seal_select].Stats[seal_select][2]),2)
			print("Your next level is Bronze. Your next bonus for {} is at 200 seals and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][3],seals_all[seal_select].Attribute,bonus))
			cards_needed = 200 - seal_number
			break
		elif seal_number == 200:
			bonus = round((seals_all[seal_select].Stats[seal_select][4] - seals_all[seal_select].Stats[seal_select][3]),2)
			print("Your current level is Silver. Your next bonus for {} is at 500 cards and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][4],seals_all[seal_select].Attribute,bonus))
			cards_needed = 300
			break
		elif seal_number >= 201 and seal_number <= 499:
			bonus = round((seals_all[seal_select].Stats[seal_select][4] - seals_all[seal_select].Stats[seal_select][3]),2)
			print("Your next level is Silver. Your next bonus for {} is at 500 seals and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][4],seals_all[seal_select].Attribute,bonus))
			cards_needed = 500 - seal_number
			break
		elif seal_number == 500:
			bonus = round((seals_all[seal_select].Stats[seal_select][5] - seals_all[seal_select].Stats[seal_select][4]),2)
			print("Your current level is Gold. Your next bonus for {} is at 1000 cards and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][5],seals_all[seal_select].Attribute,bonus))
			cards_needed = 500
			break
		elif seal_number >= 501 and seal_number <= 999:
			bonus = round((seals_all[seal_select].Stats[seal_select][5] - seals_all[seal_select].Stats[seal_select][4]),2)
			print("Your next level is Gold. Your next bonus for {} is at 1000 seals and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][5],seals_all[seal_select].Attribute,bonus))
			cards_needed = 1000 - seal_number
			break
		elif seal_number == 1000:
			bonus = round((seals_all[seal_select].Stats[seal_select][6] - seals_all[seal_select].Stats[seal_select][5]),2)
			print("Your current level is Platinum. Your final bonus for {} is at 3000 cards and will grant you {} {}, an increase of {}.".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][6],seals_all[seal_select].Attribute,bonus))
			cards_needed = 2000
			break
		elif seal_number >= 1001 and seal_number <= 2999:
			bonus = round((seals_all[seal_select].Stats[seal_select][6] - seals_all[seal_select].Stats[seal_select][5]),2)
			print("Your next level is Platinum. Your next bonus for {} is at 3,000 seals and will grant you {} {}, and increase of {}".format(seals_all[seal_select].Name,seals_all[seal_select].Stats[seal_select][6],seals_all[seal_select].Attribute,bonus))
			cards_needed = 3000 - seal_number
			break
		elif seal_number == 3000:
			print("Your current level is Master. Congratulations, you have fully unlocked {}, granting you {} {}.".format(seals_all[seal_select].Name, seals_all[seal_select].Stats[seal_select][6],seals_all[seal_select].Attribute))
			cards_needed = 0
			break

	comparrison_array = []

	while True:
		comparrison_card_cost = int(input("What is the cost, in Mega, of each {} card on your server?\t".format(seals_all[seal_select].Name)))
		openers_cost = float(input("What is the cost, in Tera, of Seal Openers on your server?\t"))
		card_cost = cards_needed * comparrison_card_cost
		openers_needed = math.ceil(cards_needed / 50)
		total_openers_cost_float = openers_cost * 1000 * openers_needed
		total_openers_cost = str(total_openers_cost_float)
		total_cost = int(card_cost + total_openers_cost_float)
		cost_per_point = int(total_cost / bonus)
		comparrison_array.extend((seals_all[seal_select].Name, comparrison_card_cost, cards_needed, card_cost, openers_needed, total_openers_cost, bonus, total_cost, cost_per_point))
		break
	final_comparrison_array.append(comparrison_array)	
	
	should_continue = str(input("Would you like to add another card to compare? (y/n):\t"))
	if should_continue == 'n':
		print_completed_array()
	elif should_continue == 'y':
		seal_comparrison_single()
	
def seal_comparrison_all(*args):
	
	# print(len(args))
	
	if len(args) == 2:
	
		x = 0
		
		for ar in args:
			if x == 0:
				k = ar
				x += 1
			elif x == 1:	
				j = ar
	
	p = 0
	
	for s in seals_all:
		if p == 0:
			p += 1
			continue
		elif s.Attribute == seal_attribute:
			print(s.Seal)

	comparrison_array = []
	
	i = k
	
	openers_cost = float(input("What is the cost, in Tera, of Seal Openers on your server?\t"))
	
	while True:
		if i >= k and i <= j:
			seal_number = int(input("How many {} seals do you already have open?\t".format(seals_all[i].Name)))
			if seal_number == 0:
				bonus = round((seals_all[i].Stats[i][1]),2)
				print("Your current level is unopened. Your next bonus for {} is at 1 card and will grant you {} {} .".format(seals_all[i].Name,seals_all[i].Stats[i][1],seals_all[i].Attribute))
				cards_needed = 50
				print("Recommend opening seals in intervals of 50 to get full use out of openers.")
			elif seal_number == 1:
				bonus = round((seals_all[i].Stats[i][2] - seals_all[i].Stats[i][1]),2)
				print("Your current level is Normal. Your next bonus for {} is at 50 cards and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][2],seals_all[i].Attribute,bonus))
				cards_needed = 49
			elif seal_number >= 2 and seal_number <= 49:
				bonus = round((seals_all[i].Stats[i][2] - seals_all[i].Stats[i][1]),2)
				print("Your next level is Normal. Your next bonus for {} is at 50 seals and will grant you {} {}, an increase of {}".format(seals_all[i].Name,seals_all[i].Stats[i][2],seals_all[i].Attribute,bonus))
				cards_needed = 50 - seal_number
			elif seal_number == 50:
				bonus = round((seals_all[i].Stats[i][3] - seals_all[i].Stats[i][2]),2)
				print("Your current level is Bronze. Your next bonus for {} is at 200 cards and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][3],seals_all[i].Attribute,bonus))
				cards_needed = 150
			elif seal_number >= 51 and seal_number <= 199:
				bonus = round((seals_all[i].Stats[i][3] - seals_all[i].Stats[i][2]),2)
				print("Your next level is Bronze. Your next bonus for {} is at 200 seals and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][3],seals_all[i].Attribute,bonus))
				cards_needed = 200 - seal_number
			elif seal_number == 200:
				bonus = round((seals_all[i].Stats[i][4] - seals_all[i].Stats[i][3]),2)
				print("Your current level is Silver. Your next bonus for {} is at 500 cards and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][4],seals_all[i].Attribute,bonus))
				cards_needed = 300
			elif seal_number >= 201 and seal_number <= 499:
				bonus = round((seals_all[i].Stats[i][4] - seals_all[i].Stats[i][3]),2)
				print("Your next level is Silver. Your next bonus for {} is at 500 seals and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][4],seals_all[i].Attribute,bonus))
				cards_needed = 500 - seal_number
			elif seal_number == 500:
				bonus = round((seals_all[i].Stats[i][5] - seals_all[i].Stats[i][4]),2)
				print("Your current level is Gold. Your next bonus for {} is at 1000 cards and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][5],seals_all[i].Attribute,bonus))
				cards_needed = 500
			elif seal_number >= 501 and seal_number <= 999:
				bonus = round((seals_all[i].Stats[i][5] - seals_all[i].Stats[i][4]),2)
				print("Your next level is Gold. Your next bonus for {} is at 1000 seals and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][5],seals_all[i].Attribute,bonus))
				cards_needed = 1000 - seal_number
			elif seal_number == 1000:
				bonus = round((seals_all[i].Stats[i][6] - seals_all[i].Stats[i][5]),2)
				print("Your current level is Platinum. Your final bonus for {} is at 3000 cards and will grant you {} {}, an increase of {}.".format(seals_all[i].Name,seals_all[i].Stats[i][6],seals_all[i].Attribute,bonus))
				cards_needed = 2000
			elif seal_number >= 1001 and seal_number <= 2999:
				bonus = round((seals_all[i].Stats[i][6] - seals_all[i].Stats[i][5]),2)
				print("Your next level is Platinum. Your next bonus for {} is at 3,000 seals and will grant you {} {}, and increase of {}".format(seals_all[i].Name,seals_all[i].Stats[i][6],seals_all[i].Attribute,bonus))
				cards_needed = 3000 - seal_number
			elif seal_number == 3000:
				print("Your current level is Master. Congratulations, you have fully unlocked {}, granting you {} {}.".format(seals_all[i].Name, seals_all[i].Stats[i][6],seals_all[i].Attribute))
				cards_needed = 0	
			
			comparrison_card_cost = int(input("What is the cost, in Mega, of each {} card on your server?\t".format(seals_all[i].Name)))
			card_cost = cards_needed * comparrison_card_cost
			openers_needed = math.ceil(cards_needed / 50)
			total_openers_cost_float = openers_cost * 1000 * openers_needed
			total_openers_cost = str(total_openers_cost_float)
			total_cost = int(card_cost + total_openers_cost_float)
			cost_per_point = int(total_cost / bonus)
			comparrison_array.extend((seals_all[i].Name, comparrison_card_cost, cards_needed, card_cost, openers_needed, total_openers_cost, bonus, total_cost, cost_per_point))
			final_comparrison_array.append(comparrison_array)
			comparrison_array = []
			i += 1
		
		elif i > j:
			print_completed_array()
			break
	
while True:
	if selection_1 == 1:
		if selection_2 == 1:
			seal_attribute = "Attack"
			i = 1
			t = 14
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 2:
			seal_attribute = "Critical"
			i = 15
			t = 22
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 3:
			seal_attribute = "Hit"
			i = 23
			t = 34
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 4:
			seal_attribute = "HP"
			i = 35
			t = 47
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 5:
			seal_attribute = "Digisoul"
			i = 48
			t = 59
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 6:
			seal_attribute = "Defense"
			i = 60
			t = 72
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 7:
			seal_attribute = "Block"
			i = 73
			t = 79
			seal_comparrison_all(i,t)
			break
		elif selection_2 == 8:
			seal_attribute = "Evade"
			i = 80
			t = 90
			seal_comparrison_all(i,t)
			break
		elif selection_2 >= 9:
			print("Invalid Entry")
			break
	elif selection_1 == 2:
		if selection_2 == 1:
			seal_attribute = "Attack"
			seal_comparrison_single()
			break
		elif selection_2 == 2:
			seal_attribute = "Critical"
			seal_comparrison_single()
			break
		elif selection_2 == 3:
			seal_attribute = "Hit"
			seal_comparrison_single()
			break
		elif selection_2 == 4:
			seal_attribute = "HP"
			seal_comparrison_single()
			break
		elif selection_2 == 5:
			seal_attribute = "Digisoul"
			seal_comparrison_single()
			break
		elif selection_2 == 6:
			seal_attribute = "Defense"
			seal_comparrison_single()
			break
		elif selection_2 == 7:
			seal_attribute = "Block"
			seal_comparrison_single()
			break
		elif selection_2 == 8:
			seal_attribute = "Evade"
			seal_comparrison_single()
			break
		elif selection_2 >= 9:
			print("Invalid Entry")
			break
		
seals_to_be_compared = []
