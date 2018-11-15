#Refer to 'Reklaim Values'

import random

class World(object):
	def menu(self):
			keepOn = True   
			while keepOn == True:
				#Holds options for methods for user to chooses from. List allows for easy additions
				#One list is actual method, other is string value. Make sure all items are in proper order
				chooseOpt = [self.createRace,self.createNation,self.createReligion,self.zone,self.magicTech,self.createCulture,self.word,self.esc]
				chooseOptSoft = ['Create a Race','Build a Nation',"Find a Religion","Create a Zone",'Create a Magic/Tech School','Create a Culture/Ethnic Group','Generate a Word','Escape']
				#Display options for user to choose
				
				for num in range(len(chooseOptSoft)):
						print str(num) + ") " + chooseOptSoft[num]
				ask =input("Choose one of the following by typing the number beside the option")
				
				#Create Parameters for different methods
				if chooseOptSoft[ask] == 'Generate a Word':
						print chooseOpt[ask]('',True).capitalize()
				elif chooseOptSoft[ask] == 'Create a Race':
						print chooseOpt[ask](random.choice((True,False)),random.choice((True,False)),True)["Description"]
				else:
						print chooseOpt[ask](True)['description']

	def __init__(self):
			#Create list of world items
			self.worldRaces = {}
			self.worldReligions = {}
			self.worldCultures = {}
			self.worldLanguages = {}
			self.worldNations = {}
			
			print "Races"
			for races in range(random.randint(4,12)):
				holdRace = self.createRace("",False,False)
				self.worldRaces[holdRace['Name']] = holdRace
				print self.worldRaces[holdRace['Name']]['Description']
				print ""
			print "Languages of the World:"
			for langs in range(random.randint(3,8)):
				holdLanguage = self.genLanguage(False)
				self.worldLanguages[holdLanguage['name']] = holdLanguage
				print ""
				print "Name: " + self.worldLanguages[holdLanguage['name']]["name"]
				print "Consants:" + ','.join(self.worldLanguages[holdLanguage['name']]["cons"])
				print "Vowels: " + ','.join(self.worldLanguages[holdLanguage['name']]["vowels"])
				print "Writing Script: " + self.worldLanguages[holdLanguage['name']]['writing script']
				print ""
			
			#print self.worldLanguages.keys()
			
			print "Religions"
			for reli in range(random.randint(3,10)):
				holdReligion = self.createReligion(False)
				self.worldReligions[holdReligion['name']] = holdReligion
				print self.worldReligions[holdReligion['name']]["description"]
				print ""
			
			#Cultures
			print "Cultures:"
			for cult in range(random.randint(4,8)):
				holdCult = self.createCulture(False)
				if holdCult['type'] == "religious":
					holdCult['religions'] = random.sample(self.worldReligions.keys(),1)
					holdCult['races'] = random.sample(self.worldRaces.keys(),random.randint(1,len(self.worldRaces)))
					holdCult['languages'] = random.sample(self.worldLanguages.keys(),random.randint(1,2))
				elif holdCult['type'] == "linguistic":
					holdCult['religions'] = random.sample(self.worldReligions.keys(),random.randint(1,len(self.worldReligions)))
					holdCult['races'] = random.sample(self.worldRaces.keys(),random.randint(1,len(self.worldRaces)))
					holdCult['languages'] = random.sample(self.worldLanguages.keys(),1)
				elif holdCult['type'] == "racial":
					holdCult['religions'] = random.sample(self.worldReligions.keys(),random.randint(0,len(self.worldReligions)))
					holdCult['races'] = random.sample(self.worldRaces.keys(),1)
					holdCult['languages'] = random.sample(self.worldLanguages.keys(),random.randint(1,3))
				else: #Nation ethnic
					holdCult['religions'] = random.sample(self.worldReligions.keys(),random.randint(1,len(self.worldReligions)))
					holdCult['races'] = random.sample(self.worldRaces.keys(),random.randint(1,len(self.worldRaces)))
					holdCult['languages'] = random.sample(self.worldLanguages.keys(),random.randint(1,3))
					
				
				
				#Determine name (make if statement if culture has more than one language group)
				if len(holdCult['languages']) == 1:
					holdCult['name'] = self.word(self.worldLanguages[holdCult['languages'][0]],False).capitalize()
				else:
					holdCult['name'] = self.word(self.worldLanguages[holdCult['languages'][random.randint(0,len(holdCult['languages'])-1)]],False).capitalize()
				
				
				
				
				#Name and Attach
				self.worldCultures[holdCult['name']] = holdCult
				#print self.worldCultures[holdCult['name']]['name']
				self.worldCultures[holdCult['name']]['description'] = holdCult['name'] + self.worldCultures[holdCult['name']]['description']
				print self.worldCultures[holdCult['name']]['description']
				if len(self.worldCultures[holdCult['name']]['races']) == 1:
					print "Races that follow:" + "".join(self.worldCultures[holdCult['name']]['races'][0])
				else:
					print "Races that follow:" + ",".join(self.worldCultures[holdCult['name']]['races'])
				if len(self.worldCultures[holdCult['name']]['languages']) == 1:
					print "Languages: " + "".join(self.worldCultures[holdCult['name']]['languages'][0])
				else:
					print "Languages: " + ",".join(self.worldCultures[holdCult['name']]['languages'])

				

				if len(self.worldCultures[holdCult['name']]['religions']) == 1:
					print "Religions followed: " + "".join(self.worldCultures[holdCult['name']]['religions'][0])
				else:
					print "Religions followed: " + ",".join(self.worldCultures[holdCult['name']]['religions'])
				
				
				#Nation for national ethnic
				#Nation ethnics create nations
				if holdCult["type"] == "national":
					newNation = self.createNation(True)
					newNation["cultural majority"] = holdCult['name']
					newNation["offical language"] = self.worldCultures[holdCult["name"]]["languages"][0]
					newNation["offical religion"] = self.worldCultures[holdCult["name"]]["religions"][0]
					print newNation["description"]
					self.worldNations[newNation["name"]] = newNation
				

				print ""
			
				
			
			
			for state in range(random.randint(6,25)):
				holdState = self.createNation(False)
				#Determine nation's culture to take language
				holdState["cultures"] = random.sample(self.worldCultures.keys(),random.randint(1,len(self.worldCultures.keys())))
				holdState['cultural majority'] = holdState["cultures"][0]
				#print holdState["cultures"]
				holdState['offical language'] = self.worldCultures[holdState["cultures"][0]]["languages"][0]
				holdState['name'] = self.word(self.worldLanguages[holdState['offical language']],False).capitalize()
				#Choose offical religion
				ethna = random.randint(0,len(holdState["cultures"])-1) #Holds randomly selected number that holdState has in culture for represenation
				#print ethna
				#print holdState["cultures"][ethna]
				#print len(self.worldCultures[holdState["cultures"][ethna]])
				#print self.worldCultures[holdState["cultures"][ethna]]["religions"]
				#print self.worldCultures[holdState["cultures"][ethna]]
				#print len(self.worldCultures[holdState["cultures"][ethna]]["religions"])
				holdState["offical religion"] = self.worldCultures[holdState["cultures"][ethna]]["religions"][0]
				holdState["description"] = "The " + holdState["prefix"] + " " + holdState["name"] + holdState["description"]
				print holdState['description']
				print "Cultural Majority: " + "".join(holdState["cultural majority"])
				print "Offical Language: " + "".join(holdState["offical language"])
				print "Offical Religion: " + "".join(holdState["offical religion"])
				print ""
				self.worldNations[holdState['name']] = holdState
			
			#Magic schools (tempory)
			for school in range((random.randint(4,8))):
				print self.magicTech(True)["description"]
				print ""
				
				
	def genLanguage(self,isRandom): #Will hold all variables and features in a dictionary including cons, vowels and new letters
		#Original English alphabet
		oldVowels = ['a','e','i','o','u','y']
		oldCons = ['b','c','d','f','g','h','j','k','l','n','m','p','q','r','s','t','v','w','x','z',""]
		#Butcher old alphabet into new alphabet
		newVowels = random.sample(oldVowels,random.randint(2,6))
		newCons = random.sample(oldCons,random.randint(10,20))
		#Determine if new letters are being added
		determineNewLetters = random.choice((True,False))
		if determineNewLetters == True:
			numberAdd = random.randint(1,8)
			for x in range(numberAdd):
				newLetter = "".join(random.sample((oldCons + oldVowels),2))
				newCons.append(newLetter)
		else:
						pass

		#Determine how long words normally are between
		minWordLength = random.randint(2,6)
		maxWordLength = random.randint(6,10)
		#Determine how many cons are allowed before vowel is put in
		maxAllowCons = random.randint(1,3)

		#Gen a name (templete for genWord)
		nameWord = [] #Will contain random cons and vowels
		conCount = 0

		for x in range(random.randint(minWordLength,maxWordLength)):
						nameWord.append(random.choice(newCons + newVowels))

		for y in nameWord:
			if any(y in newCons for y in nameWord):
				conCount += 1
			else:
				conCount = 0
			if conCount == maxAllowCons:
				nameWord.insert(nameWord.index(y),random.choice(newVowels))
		
		nameWord = "".join(nameWord)

		#Determine writing style
		writingType = random.choice(("logographic(Chinese)","Syllable(Japanese)","Alphabetic(Latin)","Abugida(Indian)","Adjad(Arabic)","Featural(Korean)"))


		languageDict = {"name":nameWord.capitalize(),"cons":newCons,"vowels":newVowels,"writing script":writingType,"min word length": minWordLength,"max word length":maxWordLength,"max allowed cons":maxAllowCons}             
		return languageDict 
	
	def word(self,language,isRandom):
		
		if isRandom == True:
						newCons = ['b','c','d','f','g','h','j','k','l','n','m','p','q','r','s','t','v','w','x','z']
						newVowels = ['a','e','i','o','u','y']
						minWordLength = random.randint(2,3)
						maxWordLength = random.randint(4,10)
						maxAllowCons = random.randint(1,3)
		else:
						
						newCons = language['cons']
						newVowels = language['vowels']
						#Determine how long words normally are between
						minWordLength = language['min word length']
						maxWordLength = language['max word length']
						#Determine how many cons are allowed before vowel is put in
						maxAllowCons = language['max allowed cons']
		
		#Gen a name (templete for genWord)
		newWord = [] #Will contain random cons and vowels
		conCount = 0

		for x in range(random.randint(minWordLength,maxWordLength)):
						newWord.append(random.choice(newCons + newVowels))

		for y in newWord:
						if any(y in newCons for y in newWord):
														conCount += 1
						else:
														conCount = 0
						if conCount == maxAllowCons:
														newWord.insert(newWord.index(y),random.choice(newVowels))
		newWord = "".join(newWord)
		
		return newWord
	
	
	def createRace(self,isCustom,isWild,isRandom):#isCustom is either true or false 
		#Set up variables and lists
		self.racePremadeList = ["Human","Elf","Ork","Centaur","Dwarf","Halfling","Goblin","Gnome","Troll","Lizardfolk","Ratfolk","Catfolk","Tengu","Bearfolk","Kitsune"] #Premade races
		animalInspireList = ["Horse","Avian","Archnae","Canine","Feline","Humaniod","Lizard","Octopus"]
		color = ["white","black","grey","red","blue","yellow","green","purple","orange","brown",'olive','transparent']
		abilities = ["Strength","Agility","Toughness","Wisdom","Intelligence","Charisma","Melee",'Ballistic']
		
		
		#Base final result
		finalrace = {'Name':"","Advantages":[],"Disadvantages":[],'Can Carry Tools':True,"is Wild":False,"Skin Tones":[],"is Custom":isCustom}
		if isCustom not in [True,False]:
				isCustom = random.choice((True,False))
		
		if isCustom == False:
				finalrace['is Custom'] = False
				finalrace['Name'] = random.choice(self.racePremadeList)
				if isRandom == False:
												self.racePremadeList.remove(finalrace['Name']) #Prevent repeats
				finalrace["Skin Tones"] = random.sample(color,random.randint(2,5))
				finalrace["Size"] = random.choice(("Large","Medium","Small"))
				finalrace['Form'] = "Humaniod"
				finalrace['Exterior'] = ['Flesh',"Hair"]

		elif isCustom == True:
				finalrace['Name'] = self.word('',True).capitalize()
				finalrace['Form'] = random.choice(('Bi-pedal','Quad-pedal','Serptine'))
				finalrace['Exterior'] = random.sample(["Flesh",'Feather',"Shell","Scales","Bone","Fur","Spikes","Rock","Wool"],random.randint(2,3))
				finalrace['Diet'] = random.choice(('Omnivore',"Herbivore","Carnivore","Parastic","Chemoivore","Scavenger","Liquid"))
				finalrace['Size'] = random.choice(["Huge","Large","Medium Size","Small","Tiny"])
				finalrace['Reproduction'] = random.choice(('Live Birth',"Egg","Asexual","Parastic"))
				finalrace['Parts'] = {'Arm':random.randint(0,10),"Leg":random.randint(0,10),"Head":random.randint(1,10),"Eye":random.choice([2]*10 + range(0,20)),"Tail":random.choice([0]*10 + range(0,10)),"Teeth":random.randint(0,100),"Horn":random.choice([0]*10 + range(0,10)),"Wing":random.choice([0]*10 + range(0,10,2)),"Ear":random.randint(0,10),"Tongue":random.randint(0,10),"Tentacle":random.choice([0]*10 + range(0,20))}
				if finalrace['Form'] == "Bi-pedal":
												finalrace['Parts']['Legs'] = 2
				if finalrace['Parts']["Arm"] > 0 or finalrace["Parts"]["Tail"] > 0:
												finalrace["Can Carry Tools"] = True
				else:
												finalrace["Can Carry Tools"] = False
				finalrace["Skin Tones"] = random.sample(color,random.randint(2,5))
				finalrace["is Wild"] = random.choice((True,False))

		if isWild != "":
				finalrace["is Wild"] = isWild
		else:
				pass
		
		#Build Description
		finalrace["Description"] = "The " + finalrace["Name"] + " is a "+finalrace['Size'] + " " + finalrace["Form"] + " with  " + "/".join(finalrace['Exterior']) + " exterior. "
		if finalrace["is Wild"] == True:
				finalrace["Description"] += " They are mostly wild creatures " + random.choice((",although some are them are domesticated. ",", and others races have a hard time taming them. " ))
		if isCustom == True:
				finalrace["Description"] = finalrace["Description"] + " They have "
				for x in ["Arm","Leg","Head","Tail","Teeth","Eye","Ear","Horn","Wing","Tongue","Tentacle"]:
						#print x
						if finalrace["Parts"][x] == 1:
								finalrace["Description"] = finalrace["Description"] + "a " + x + ". "
						elif finalrace["Parts"][x] > 1:
								finalrace["Description"] = finalrace["Description"] + str(finalrace["Parts"][x]) + " " + x + "s. "
						else:
								pass

				finalrace["Description"] += ". They rely a " + finalrace["Diet"] + " diet. They have a " + finalrace['Reproduction'] + " reproduction system."
		
		return finalrace
	
	def createCulture(self,isRandom):
		type = random.choice(["national","religious","linguistic","racial"])
		name = ""
		enterainment = random.sample(["drugs","individual sports","team sports","games","puzzles","martial arts","theater","fine arts","books"],2)
		coreMindset = random.choice(["expansion","discovery","domination","unity","freedom","honor","piety","enlightment","aesthetic","rationality","productivity","pride","transformation","purity"])
		kinshipList = ["polyandry","polygyny","monogamous","open","incestual","mating only","exogamy","endogamy","arranged child marriage"]
		genderRoles = random.choice(["female led","male led","equal amoung genders"])
		groupings = random.choice(["large close groups"," small bands","large isolated groups","rather isolated"])
		viewWar = random.choice(["avoidant","netural","postive opinion"])
		viewXeno = random.choice(["hate","embrace","assimilate","don't care for"])
		viewReligion = random.choice(["negative","netural","postive","radical"])
		cultureColor = random.choice(['white','black','grey','blue','yellow','red','green','purple','orange','brown'])
		
		
		#Gender roles and core mindsets affect marriages
		if genderRoles == "male led":
				kinshipList.remove("polyandry")
		elif genderRoles == "female led":
				kinshipList.remove("polygyny")
		if coreMindset == "purity":
				kinshipList.remove("exogamy")
		if groupings == "rather isolated":
				kinshipList = ["open","mating only"]
		
		kinship = random.choice(kinshipList)
		
		
		
		if isRandom == True:
			name = self.word('',True)
			description = "The " + name.capitalize()
		else:
			description = "This culture"
		
		#description = "This culture  is a " + culture['type'] + " ethnic group that is led by the idea of " + culture["core mindset"] + ". Their society exist in " + culture['groupings'] +" that are " + culture['gender roles'] + ' and their marriages are ' + culture['kinship']
		description =  " is a " + type + " ethnic group that is led by the idea of " + coreMindset + ". Their society exist in " + groupings + " that are " + genderRoles + " and their marriages are " + kinship 
		description += ". They have a " + viewWar + " on war. They tend to have a " + viewReligion + " towards religion and they " + viewXeno + " outsiders."  
				
		
		#print description
		culture = {'cultural majority':"",'view on war':viewWar,'view on xeno':viewXeno,'view on religions':viewReligion ,"description":"",'races':[],"religions":[],"Enterainment": ",".join(enterainment),"core mindset":coreMindset,"groupings":groupings,"gender roles":genderRoles,"kinship":kinship,"core mindset":coreMindset,"enterainment":enterainment,"type":type,"languages":[],"language chosen":[],"name":name,"description":description}
		#print culture
		
		return culture
	
	def createReligion(self,isRandom):
		name = self.word("",True).capitalize() + "ism"
		type = random.choice(("polytheistic","monotheistic","animistic","dualism","atheistic","agnostic","henotheistic")) #religion type
		form = random.choice(("bug ","humanoid ","unknown ","animal ","strange ","no ","multiple ")) + "form(s)"
		focus = random.choice(("discovering secrets of the universe","enlightenment","spreading religion","building a utopia","gaining power","finding success","redemption from original sin","find spiritual freedom","form a relationship with the spiritual realm","persevere the 'old ways'"))
		#worship = random.sample(("tithe","prayer","sacrifices","singing hymns","performing through arts","confessions","mediation","attendance of services","reading","sex"),random.randint(2,3))
		actions = ["stealing","killing","wasting","giving alms","tolerance","gaining wealth","eating of meat","eating of vegetables","being prideful","engaging in politics","joining communities","marriage","watching certain arts"]
		holyActs = []
		sinActs = []
		passActs = []
		for acts in actions:
				random.choice((holyActs,sinActs,passActs)).append(acts)
																		
		placeWorship = random.choice(["nature","public shrines","private shrines","grand temples","public gathering","holy sites"])
		actsWorship = random.sample(["tithe","prayer","sacrifices","singing hymns","performing through arts","confessions","mediation","attendance of services","reading","prayers","good works","giving up possessions","live sacrifices","praises","crusading","seasonal rituals","ritual sex","mediation","drug usage","building shrines"],random.randint(2,3))
		religionAuthority = random.choice(("prophets","clergy","book(s)","philosophers","oracle","witches","mages","rulers"))
		coreDoctrine = random.choice(("nature","chaos","order","knowledge","protection","strength","love","race","elements","war","peace","glory","conversion","creation","community","creation","fertility","end times","voids","death"))
		
		#Create gods
		domains = ['air','animals','technology','chaos','society','light','darkness','life','death','earth','fire','water','magic','nobility','commonfolk','protection','stars','sex','evil','good','war','peace','mountains','forest','food','industry']
		deities = {}
		deitiesName = []
		if type == 'monotheistic' or type == 'dualism':
			deitiesName.append(self.word("",True))
			deities[deitiesName[0]] = deitiesName[0].capitalize() #+ " is believed to be the only god in existence."
		elif type == "polytheistic" or type == 'animistic':
			for gods in range(random.randint(4,20)):
					deitiesName.append(self.word("",True))
					deities[deitiesName[gods]] = deitiesName[gods].capitalize()  
					if type == "animistic":
						deities[deitiesName[gods]] += " is the spirit of " +  '/'.join(random.sample(domains,random.randint(1,3)))
					else:
						deities[deitiesName[gods]] += " is the " + random.choice(('god','goddess')) + ' of ' + '/'.join(random.sample(domains,random.randint(1,3)))
		elif type == 'henotheistic':
			deitiesName.append(self.word("",True))
			deities[deitiesName[0]] = deitiesName[0].capitalize() #+ " is the main god, however, they may be other gods out there."

		description = name + " is a " + type + ' religion that focus on ' + coreDoctrine + ". "
		if len(deities) == 0:
				description += "They don't acknowledge any deity."
		elif len(deities) == 1:
				description += "They believe in one " + random.choice(("goddess","god"))+" by the name of " + deities[deitiesName[0]] + ", which takes on " + form
		else:
			for x in deitiesName:
				description += '\n' + deities[x] + ". "
			description += " They take on " + form
	
		description += " They worship using " + ",".join(actsWorship) + " while following holy acts such as: " + "/".join(holyActs) + ". However they will forbid themselves from: " + "/".join(sinActs) + ". " + religionAuthority.capitalize() + " can be found at " + placeWorship + " giving lessons and worshiping." 
		
		religionDict = {"description":description,'name':name,'deities':deities,'deities names':deitiesName,"culture origin":"","type":type,"form of deities":form,"focus":focus,"holy acts":holyActs,"sinful acts":sinActs,"place of worship":placeWorship,"acts of worship":actsWorship,"religious authority":religionAuthority,"core doctrine":coreDoctrine}
		
		
		
		return religionDict

	def magicTech(self,isRandom):
		fields = ['mining','small goods crafting','large crafting goods','automation','farming','livestock','hunting','landscaping','melee weapons','range weapons','control strategies','armoring','gathering','investigation','trapping','detection','networking','encryption','messaging','diplomatic manipulation','environmental control','shelter building','utility building','minion','user interface','medicine','surgery','organ/limb replacement','fertility and development']
		sources = ['psychic magic','electronics','elemental','artifact magic','planar magic','mana based magic','ki based magic','bloodline knowledge','alchemy','biological','mechanics']
		devices = ['techniques','gadgets','summons','rituals','abilities']
		instabilities = ['normal', 'low', 'high','very high']
		manningList =  ['demanding','decent', 'effective', 'highly effective']
		
		source = random.choice(sources)
		#Elemental is various
		if source == 'elemental':
				source = random.choice(['fire magic','water magic','earth magic','air magic','shadow magic','light magic'])
		
		device = random.sample(devices,random.randint(2,3))
		instability = random.choice(instabilities)
		manning = random.choice(manningList)
		superior = []
		inferior = []
		#Create superior and inferior fields without copies 
		#Superior
		for x in range(random.randint(2,4)):
				choose = random.choice(fields)
				superior.append(choose)
				fields.remove(choose)
		#Inferior
		for x in range(random.randint(1,2)):
				choose = random.choice(fields)
				inferior.append(choose)
				fields.remove(choose)

		
		description = "The " + self.word("",True).capitalize() + " school uses " + source + " to improve on "    
		if len(superior) == 2:
				description += " and ".join(superior)
		else:
				for x in range(len(superior)):
						if superior[x] == superior[-1]:
								description += " and " + superior[x]
						elif superior[x] == superior[0]:
								description += superior[x]
						else:
								description += "," + superior[x]
						
										
		
		
		description += ", but it tends to do poorly when doing "
		if len(inferior) == 1:
				description += "".join(inferior)
		else:
				description += " and ".join(inferior)
						
		description += ". It uses " + " and ".join(device) + " that is "        + manning + " on manning that has " + instability + " risk."
		
		result = {'manning':manning,'risk':instabilities,'devices':device,"superior fields":superior,'inferior fields':inferior,'source':source,'description':description}
		
		return result

			
	def zone(self,isRandom):
		climate = random.choice(['tropical','temperate','arid','desert','steppe','tundra','artic','scrub'])
		size = size = random.choice(('tiny','small','medium','large'))
		elevation = random.choice(['high','level','low'])
		hasWater = random.choice([True,True,True,False,False])
		water = str(random.randint(1,50))+ " " + random.choice(['sea','rivers','lakes'])
		resourceList = ['ore','oils','preious metals','hunting','industry','trade']
		if climate in ['tropical','temperate','scrub']:
				resourceList.extend(['farming','forestry','pasture'])
		resource = random.sample(resourceList,random.randint(0,3))
		description = "This zone is a " + size +" " + climate + " with a " + elevation + " elevation."
		if hasWater == True:
				description += " It has " + water
		else:
				water = 'no water'
		
		if len(resource) == 0:
				description += " This zone has no resource that are being used"
		elif len(resource) == 1:
				description += " This zone uses " + "".join(resource) + " as a way to make money"
		else:
				description += " This zone uses "
				for x in resource:
						if x == resource[-1]:  
								description += " and " + x 
						else:
								description += "," + x
				description += " as a way to make money"
		
		zone = {'description':description,'climate':climate,'size':size,'elevation':elevation,'water':water,'resources':resource}
		return zone

					
	def createNation(self,isRandom):
		name = ""
		government = random.choice(['tribal','oligarchy','democratic','autocratic','theocratic','monarchy','republic'])
		economy = random.choice(['captialist','socialist','communist','substance','mixed economy','corporate economy','mercantilist'])
		size = random.choice(('tiny','small','medium size','large'))
		issues = random.choice(['economic stagnation',"surging technology","cultural renissance","economic boon","hyper militarism","fear","nationalism","extremism","dangerous factionalism","high corruption","crumbling infrastructure","extreme poverty","cultural revolution","poor security","famine","drought","brain drain",'isolationism',"invasion","hostile environment","pollution","war recovery","disease","political crackdown","succession issues","rampant immigration"])
		prefix = ["Land of ",'State of ',"United States of "]
		if government in ['democratic','republic']:
				prefix.extend(["Republic of ","People's Republic of ","Democratic State of ","People's Land of ","Federal State of ","Confederate States of "])
		elif government == 'monarchy':
				prefix.extend(["Kingdom of ","Principality of  ","Commonwealth of ","Empire of "])
		elif government == 'autocratic':
				prefix.extend(["Empire of ","Grand State of ","Imperium of "])
		elif government == 'theocratic':
				prefix.extend(["Holy Nation of ",'Commune of ',"Sacred State of "])
		else:
				prefix.extend(["Republic of ","People's Republic of ","Democratic State of ","People's Land of ","Confederate States of ","Holy Nation of ",'Commune of ',"Sacred State of ","Guilded Nation of ","Tribes of ","City-States of "])

		preName = random.choice(prefix)
		sectors = []
		if size == 'tiny':
				sectorNumber = 1
		elif size == 'small':
				sectorNumber = random.randint(1,3)
		elif size == 'medium size':
				sectorNumber = random.randint(2,5)
		else:
				sectorNumber = random.randint(5,10)
		sectors = []
		for x in range(sectorNumber):
				sectors.append(self.zone(False))
		
		nationResource = []
		for x in range(len(sectors)):
				for y in sectors[x]['resources']:
						if sectors[x]['resources'] in nationResource:
								pass
						else:
								nationResource.append(y)
		
		
		 
		if isRandom == True:
			name = self.word("",True).capitalize()
			description  = "The " + preName + " " + name
		else:
			description  = ""
		
		description +=  " is a " + size+ " " + government+ " " + economy + " nation that is going through a period of " + issues 
		
		nation = {"issue":issues,"description":description,"nation's resource":nationResource,'prefix':preName,'name':name,'government':government,'economy':economy,'size':size,'factions':[],'offical language':"",'offical religion':"","relgions":[],"cultures":[]}     
		

		return nation
					
	def faction(self,isRandom):
			pass
			
			 
			
	def person(self,isRandom):
		pass
			
			
	def esc(self,blank):
			quit()


world = World()
world.menu()                    
