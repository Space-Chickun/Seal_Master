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

#class attribute():
#	# Attribute list to make choices more compact
#	def __init__(self, attribute):
#		self.attribute = attribute

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
	seal("11. Myotismon",		"Attack",			{11:[0,25,50,100,150,200,250]},		"Myotismon"),
	seal("12. Azulongmon",		"Attack",			{12:[0,30,60,120,180,240,300]}, 	"Azulongmon"),
	seal("13. Examon",			"Attack",			{13:[0,30,60,120,180,240,300]}, 	"Examon"),
	seal("14. Omegamon",		"Attack",			{14:[0,30,60,120,180,240,300]},		"Omegamon"),
	seal("15. Dexmon",			"Attack",			{15:[0,30,60,120,180,240,300]}, 	"Dexmon"),
	seal("16. Koromon",			"Critical",			{16:[0,.1,.2,.4,.6,.8,1]},			"Koromon"),
	seal("17. Kunemon",			"Critical",			{17:[0,.15,.3,.6,.9,1.2,1.5]},		"Kunemon"),
	seal("18. Sharmamon",		"Critical",			{18:[0,.15,.3,.6,.9,1.2,1.5]},		"Sharmamon"),
	seal("19. Kyubimon",		"Critical",			{19:[0,.2,.4,.8,1.2,1.6,2]},		"Kyubimon"),
	seal("20. Togemon",			"Critical",			{20:[0,.2,.4,.8,1.2,1.6,2]},		"Togemon"),
	seal("21. Datamon",			"Critical",			{21:[0,.25,.5,1,1.5,2,2.5]},		"Datamon"),
	seal("22. Volcamon",		"Critical",			{22:[0,.25,.5,1,1.5,2,2.5]},		"Volcamon"),
	seal("23. SaberLeomon",		"Critical",			{23:[0,.3,.6,1.2,1.8,2.4,3]},		"SaberLeomon"),
	seal("24. Drimogemon",		"Hit",				{24:[0,10,20,40,60,80,100]},		"Drimogemon"),
	seal("25. FanBeemon",		"Hit",				{25:[0,10,20,40,60,80,100]},		"FanBeemon"),
	seal("26. Gabumon",			"Hit",				{26:[0,10,20,40,60,80,100]},		"Gabumon"),
	seal("27. Coredramon(Blue)","Hit",				{27:[0,20,40,80,120,160,200]},		"Coredramon(Blue)"),
	seal("28. Dorugamon",		"Hit",				{28:[0,20,40,80,120,160,200]},		"Dorugamon"),
	seal("29. DarkTyrannomon",	"Hit",				{29:[0,20,40,80,120,160,200]},		"DarkTyrannomon"),
	seal("30. Garudamon",		"Hit",				{30:[0,30,60,120,180,240,300]},		"Garudamon"),
	seal("31. Knightmon",		"Hit",				{31:[0,30,60,120,180,240,300]},		"Knightmon"),
	seal("32. Parasimon",		"Hit",				{32:[0,40,80,160,240,320,400]},		"Parasimon"),
	seal("33. LordKnightmon",	"Hit",				{33:[0,40,80,160,240,320,400]},		"LordKnightmon"),
	seal("34. Baihumon",		"Hit",				{34:[0,50,100,200,300,400,500]},	"Baihumon"),
	seal("35. Craniamon",		"Hit",				{35:[0,50,100,200,300,400,500]},	"Craniamon"),
	seal("36. Gazimon",			"HP",				{36:[0,15,30,60,90,120,150]},		"Gazimon"),
	seal("37. Keramon",			"HP",				{37:[0,15,30,60,90,120,150]},		"Keramon"),
	seal("38. Tsunomon",		"HP",				{38:[0,15,30,60,90,120,150]},		"Tsunomon"),
	seal("39. Veemon",			"HP",				{39:[0,15,30,60,90,120,150]},		"Veemon"),
	seal("40. Guardromon",		"HP",				{40:[0,20,40,80,120,160,200]},		"Guardromon"),
	seal("41. Kentarumon",		"HP",				{41:[0,20,40,80,120,160,200]},		"Kentarumon"),
	seal("42. Soulmon",			"HP",				{42:[0,20,40,80,120,160,200]},		"Soulmon"),
	seal("43. ReptileDramon",	"HP",				{43:[0,20,40,80,120,160,200]},		"Reptiledramon"),
	seal("94. Raremon",			"HP",				{44:[0,20,40,80,120,160,200]},		"Raremon"),
	seal("45. Sinduramon",		"HP",				{45:[0,25,50,100,150,200,250]},		"Sinduramon"),
	seal("46. SoulSatamon",		"HP",				{46:[0,25,50,100,150,200,250]},		"SoulSatamon"),
	seal("47. DexDoruGreymon",	"HP",				{47:[0,30,60,120,180,240,300]},		"DexDoruGreymon"),
	seal("48. Ebonwumon",		"HP",				{48:[0,50,100,200,300,400,500]},	"Ebonwumon"),
	seal("49. UlForceVeedramon","HP",				{49:[0,50,100,200,300,400,500]},	"UlForceVeedramon"),
	seal("50. DemiMeramon",		"Digisoul",			{50:[0,10,20,40,60,80,100]},		"DemiMeramon"),
	seal("51. Agumon",			"Digisoul",			{51:[0,20,40,80,120,160,200]},		"Agumon"),
	seal("52. Candlemon",		"Digisoul",			{52:[0,20,40,80,120,160,200]},		"Candlemon"),
	seal("53. ToyAgumon",		"Digisoul",			{53:[0,20,40,80,120,160,200]},		"ToyAgumon"),
	seal("54. Dorumon",			"Digisoul",			{54:[0,20,40,80,120,160,200]},		"Dorumon"),
	seal("55. Coredramon(Green)","Digisoul",		{55:[0,30,60,120,180,240,300]},		"Coredramon(Green)"),
	seal("56. Woodmon",			"Digisoul",			{56:[0,30,60,120,180,240,300]},		"Woodmon"),
	seal("57. Asuramon",		"Digisoul",			{57:[0,40,80,160,240,320,400]},		"Asuramon"),
	seal("58, SkullGreymon",	"Digisoul",			{58:[0,40,80,160,240,320,400]},		"SkullGreymon"),
	seal("59. WereGarurumon",	"Digisoul",			{59:[0,40,80,160,240,320,400]},		"WereGarurumon"),
	seal("60. Diablomon",		"Digisoul",			{60:[0,50,100,200,300,400,500]},	"Diablomon"),
	seal("61. Zhuqiaomon",		"Digisoul",			{61:[0,60,120,240,360,480,600]},	"Zhuqiaomon"),
	seal("62. Upamon",			"Defense",			{62:[0,8,16,32,48,64,80]},			"Upamon"),
	seal("63. Elecmon",			"Defense",			{63:[0,10,20,40,60,80,100]},		"Elecmon"),
	seal("64. Goblimon",		"Defense",			{64:[0,10,20,40,60,80,100]},		"Goblimon"),
	seal("65. Renamon",			"Defense",			{65:[0,10,20,40,60,80,100]},		"Renamon"),
	seal("66. Flymon",			"Defense",			{66:[0,15,30,60,90,120,150]},		"Flymon"),
	seal("67. Leomon",			"Defense",			{67:[0,15,30,60,90,120,150]},		"Leomon"),
	seal("68. Meramon",			"Defense",			{68:[0,15,30,60,90,120,150]},		"Meramon"),
	seal("69. Rockmon",			"Defense",			{69:[0,15,30,60,90,120,150]},		"Rockmon"),
	seal("70. Monochromon",		"Defense",			{70:[0,15,30,60,90,120,150]},		"Monochromon"),
	seal("71. Meteormon",		"Defense",			{71:[0,20,40,80,120,160,200]},		"Meteormon"),
	seal("72. WaruMonzaemon",	"Defense",			{72:[0,20,40,80,120,160,200]},		"WaruMonzaemon"),
	seal("73. Kimeramon",		"Defense",			{73:[0,25,50,100,150,200,250]},		"Kimeramon"),
	seal("74. Kentaurosmon",	"Defense",			{74:[0,25,50,100,150,200,250]},		"Kentaurosmon"),
	seal("75. Dracmon",			"Block",			{75:[0,.1,.2,.4,.6,.8,1]},			"Dracmon"),
	seal("76. Tentomon",		"Block",			{76:[0,.1,.2,.4,.6,.8,1]},			"Tentomon"),
	seal("77. Sangloupmon",		"Block",			{77:[0,.15,.3,.6,.9,1.2,1.5]},		"Sangloupmon"),
	seal("78. Waspmon",			"Block",			{78:[0,.15,.3,.6,.9,1.2,1.5]},		"Waspmon"),
	seal("79. Etemon",			"Block",			{79:[0,.2,.4,.8,1.2,1.6,2]},		"Etemon"),
	seal("80. MegaSeadramon",	"Block",			{80:[0,.2,.4,.8,1.2,1.6,2]},		"MegaSeadramon"),
	seal("81. Vikaralamon",		"Block",			{81:[0,.2,.4,.8,1.2,1.6,2]},		"Vikaralamon"),
	seal("82. Armadillomon",	"Evade",			{82:[0,.2,.2,.4,.6,.8,1]},			"Armadillomon"),
	seal("83. Impmon",			"Evade",			{83:[0,.2,.2,.4,.6,.8,1]},			"Impmon"),
	seal("84. Digmon",			"Evade",			{84:[0,.2,.4,.8,1.2,1.6,2]},		"Digmon"),
	seal("85. Veedramon",		"Evade",			{85:[0,.2,.4,.8,1.2,1.6,2]},		"Veedramon"),
	seal("86. Gatomon",			"Evade",			{86:[0,.2,.4,.8,1.2,1.6,2]},		"Gatomon"),
	seal("87. Allomon",			"Evade",			{87:[0,.2,.4,.8,1.2,1.6,2]},		"Allomon"),
	seal("88. Lillymon",		"Evade",			{88:[0,.3,.6,1.2,1.8,2.4,3]},		"Lillymon"),
	seal("89. Mystimon",		"Evade",			{89:[0,.3,.6,1.2,1.8,2.4,3]},		"Mystimon"),
	seal("90. NeoDevimon",		"Evade",			{90:[0,.3,.6,1.2,1.8,2.4,3]},		"NeoDevimon"),
	seal("91. Dynasmon",		"Evade",			{91:[0,.35,.7,1.4,2.1,2.8,3.5]},	"Dynasmon"),
	seal("92. DexDorugoramon",	"Evade",			{92:[0,.35,.7,1.4,2.1,2.8,3.5]},	"DexDorugoramon")
	]

#attributes_all = [0,
#	attribute("Attack"),
#	attribute("Critical"),
#	attribute("Hitk"),
#	attribute("HP"),
#	attribute("Digisoul"),
#	attribute("Defense"),
#	attribute("Block"),
#	attribute("Evade"),
#	]

final_comparrison_array = [['Name', 'Cost per Card', 'Cards Needed', 'Total Card Cost', 'Openers Needed', 'Openers Cost', 'Bonus Gained', 'Total Cost', 'Cost per Point']]

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
			cards_needed = 1
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
	
def seal_comparrison_all():
	
	openers_cost = float(input("What is the cost, in Tera, of Seal Openers on your server?\t"))
	
	for i in seal_comparison_array:
		comparrison_array = []
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
			bonus = seals_all[i].Stats[i][6]
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
		
#		elif i > j:
#			print_completed_array()
#			str(input("Press Enter when complete!"))
#			break
	
while True:
	seals_select = seals_all['Seal' 'Attribute' 'Stats' 'Name']
	seal_comparison_array = []
	if selection_1 == 1:
		if selection_2 == 1:
			seal_attribute = "Attack"
			break
		elif selection_2 == 2:
			seal_attribute = "Critical"
			break
		elif selection_2 == 3:
			seal_attribute = "Hit"
			break
		elif selection_2 == 4:
			seal_attribute = "HP"
			break
		elif selection_2 == 5:
			seal_attribute = "Digisoul"
			break
		elif selection_2 == 6:
			seal_attribute = "Defense"
			break
		elif selection_2 == 7:
			seal_attribute = "Block"
			break
		elif selection_2 == 8:
			seal_attribute = "Evade"
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
	for Attribute in seals_select[self.Seal, self.Attribute, self.Stats, self.Name]:
		if seal_attribute == self.Attribute:
			seal_comparison_array.append(seals_all.Seal)
			print(seal_comparison_array)
		
seals_to_be_compared = []
