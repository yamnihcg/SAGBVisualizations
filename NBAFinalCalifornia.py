#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:30:23 2018

@author: shriramgharpure
"""
norCalCities = ['Alameda','Antioch','Berkeley', 'Brentwood', 'Chico', 'Citrus Heights', 'Clovis', 'Concord','Cupertino', 'Daly City', 'Davis', 'Elk Grove',	'Fairfield', 'Folsom', 'Fresno', 'Fremont', 'Hanford','Hayward','Livermore','Lodi', 'Madera', 'Manteca', 'Merced', 'Milpitas', 'Modesto', 'Mountain View', 'Napa', 'Novato', 'Oakland', 'Palo Alto', 'Petaluma', 'Pittsburg', 'Pleasanton', 'Porterville', 'Rancho Cordova', 'Redding', 'Redwood City', 'Richmond', 'Rocklin', 'Roseville', 'Sacramento', 'Salinas', 'San Francisco', 'San Jose', 'San Leandro', 'San Mateo', 'San Rafael','San Ramon', 'Santa Clara', 'Santa Cruz', 'Santa Rosa', 'South San Francisco', 'Stockton', 'Sunnyvale', 'Tracy', 'Tulare',  'Turlock', 'Union City', 'Vacaville', 'Vallejo', 'Visalia', 'Walnut Creek','Watsonville', 'Woodland', 'Yuba City']
soCalCities = ['Agoura Hills', 'Alhambra', 'Arcadia', 'Artesia', 'Avalon', 'Azusa', 'Baldwin Park', 'Bell', 'Bell Gardens', 'Bellflower', 'Beverly Hills', 'Bradbury', 'Burbank', 'Calabasas', 'Carson', 'Cerritos', 'Claremont', 'Commerce', 'Compton', 'Covina', 'Cudahy', 'Culver City', 'Diamond Bar', 'Downey', 'Duarte', 'El Monte', 'El Segundo', 'Gardena', 'Glendale', 'Glendora', 'Hawaiian Gardens', 'Hawthorne', 'Hermosa Beach', 'Hidden Hills', 'Huntington Park', 'Industry', 'Inglewood', 'Irwindale', 'La Cañada Flintridge', 'La Habra', 'La Mirada', 'La Puente', 'La Verne', 'Lakewood', 'Lancaster', 'Lawndale', 'Lomita', 'Long Beach', 'Los Angeles', 'Lynwood', 'Malibu', 'Manhattan Beach', 'Maywood', 'Monrovia', 'Montebello', 'Monterey Park', 'Norwalk', 'Palmdale', 'Palos Verdes', 'Paramount', 'Pasadena', 'Pico Rivera', 'Pomona', 'Rancho', 'Redondo Beach', 'Rolling Hills', 'Rosemead', 'San Dimas', 'San Fernando', 'San Gabriel', 'San Marino', 'Santa Clarita','Santa Fe Springs', 'Santa Monica', 'Sierra Madre', 'Signal Hill', 'South El Monte', 'South Gate', 'South Pasadena', 'Temple City', 'Torrance', 'Vernon', 'Walnut', 'West Covina', 'West Hollywood', 'Westlake Village', 'Whittier', 'Aliso Viejo', 'Anaheim', 'Brea', 'Buena Park', 'Costa Mesa', 'Cypress', 'Dana Point', 'Fountain Valley', 'Fullerton', 'Garden Grove', 'Huntington Beach', 'Irvine', 'La Habra', 'La Palma', 'Laguna Beach', 'Laguna Hills', 'Laguna Niguel', 'Laguna Woods', 'Lake Forest', 'Los Alamitos', 'Mission Viejo', 'Newport Beach', 'Orange', 'Placentia', 'Rancho Santa Margarita', 'San Clemente', 'San Juan Capistrano', 'Santa Ana', 'Seal Beach', 'Stanton', 'Tustin', 'Villa Park', 'Westminster', 'Yorba Linda', 'Brawley', 'Calexico', 'Calipatria', 'El Centro', 'Holtville', 'Imperial', 'Westmorland', 'Banning', 'Beaumont', 'Blythe', 'Calimesa', 'Canyon Lake', 'Cathedral City', 'Coachella', 'Corona Desert', 'Hot Springs', 'Eastvale', 'Hemet', 'Indian Wells', 'Indio', 'Jurupa Valley', 'La Quinta', 'Lake Elsinore', 'Menifee', 'Moreno Valley', 'Murrieta', 'Norco', 'Palm Desert', 'Palm Springs', 'Perris', 'Rancho Mirage', 'Riverside', 'San Jacinto', 'Temecula', 'Wildomar', 'Adelanto', 'Apple Valley', 'Barstow', 'Big Bear Lake', 'Chino', 'Chino Hills',     'Colton', 'Fontana', 'Grand Terrace', 'Hesperia', 'Highland', 'Loma Linda', 'Montclair', 'Needles', 'Ontario', 'Rancho Cucamonga', 'Redlands', 'Rialto', 'San Bernardino', 'Twentynine Palms', 'Upland', 'Victorville', 'Yucaipa', 'Yucca Valley', 'Carlsbad', 'Chula Vista', 'Coronado Del Mar', 'El Cajon', 'Encinitas', 'Escondido', 'Imperial Beach', 'La Mesa', 'Lemon Grove', 'National City', 'Oceanside', 'Poway', 'San Diego', 'San Marcos', 'Santee', 'Solana Beach', 'Vista', 'Camarillo', 'Fillmore', 'Moorpark', 'Ojai', 'Oxnard', 'Port Hueneme', 'Santa Paula', 'Simi Valley', 'Thousand Oaks', 'Ventura', 	'Buellton', 'Carpinteria', 'Goleta', 'Guadalupe', 'Lompoc', 'Santa Barbara', 'Santa Maria', 'Solvang']
californiaNBA = pd.read_csv('/Users/shriramgharpure/Downloads/CaliforniaNBANew.csv')
currentYear = californiaNBA['To']
cityCheck = californiaNBA['City']
playerNames = californiaNBA['Player']
#Getting number of players in NorCal and SoCal plus respective indices
indexNorCalArr = [];
indexSoCalArr = [];
nbaNorCal = 0
nbaSoCal = 0 
for i in range(len(californiaNBA)):
    if cityCheck[i] in norCalCities and (currentYear[i] == 2018 or currentYear[i] == 2019):
        indexNorCalArr.append(i)
        nbaNorCal = nbaNorCal + 1
    if cityCheck[i] in soCalCities and (currentYear[i] == 2018 or currentYear[i] == 2019):
        indexSoCalArr.append(i)
        nbaSoCal = nbaSoCal + 1
nCPlayerNames = [];
sCPlayerNames = [];
for elem in indexNorCalArr:
    nCPlayerNames.append(playerNames[elem])
for elem in indexSoCalArr:
    sCPlayerNames.append(playerNames[elem])
allNBAPlayer = pd.read_csv('/Users/shriramgharpure/Downloads/allNBAPlayers.csv')
positionData = allNBAPlayer['Pos']
playerData = allNBAPlayer['Player']
#Cleaning Player Data(Removing the Slashes)
rawPlayerData = []
filteredNCNames = []
filteredSCNames = []
a = 0
b = 0
c = 0
for elem in playerData:
    for i in range(len(elem)):
        if elem[i] == '\\':
            a = i
    rawPlayerData.append(elem[:a])
allNBAPlayer['Player'] = rawPlayerData
for elem in nCPlayerNames:
    for j in range(len(elem)):
        if elem[j] == '\\':
            b = j
    filteredNCNames.append(elem[:b])
for elem in sCPlayerNames:
    for k in range(len(elem)):
        if elem[k] == '\\':
            c = k
    filteredSCNames.append(elem[:c])
#Sourcing Position List for NorCal and SoCal Players
norCalPositions = []
soCalPositions = []
NCIndices = []
SCIndices = []
preference = allNBAPlayer['Player']
positions = allNBAPlayer['Pos']
for i in range(len(allNBAPlayer)):
    for j in range(len(filteredNCNames)):
        if preference[i] == filteredNCNames[j]:
            norCalPositions.append(positions[i])
            NCIndices.append(i)
for i in range(len(allNBAPlayer)):
    for j in range(len(filteredSCNames)):
        if preference[i] == filteredSCNames[j]:
            soCalPositions.append(positions[i])
            SCIndices.append(i)
#Getting the counts at each position
positionList = ['PG', 'SG','SF','PF','C']
nCalCounts = []
sCalCounts = []
tempCount = 0
for pos in positionList:
    for pos2 in norCalPositions:
        if pos == pos2:
            tempCount = tempCount + 1
    nCalCounts.append(tempCount)
    tempCount = 0
for pos in positionList:
    for pos2 in soCalPositions:
        if pos == pos2:
            tempCount = tempCount + 1
    sCalCounts.append(tempCount)
    tempCount = 0
#Stacked Bar Graph - Position Comparison

#indices = np.arange(len(positionList))
#barW = 0.30
#norCalPlot = plt.bar(indices, nCalCounts, barW, label='NorCal')
#soCalPlot = plt.bar(indices+barW, sCalCounts, barW, label='SoCal')
#plt.xticks(indices,positionList)
#plt.xlabel('Position')
#plt.ylabel('Frequency')
#plt.title('NorCal vs. SoCal - Positions in the NBA')
#plt.legend([norCalPlot, soCalPlot],['NorCal','SoCal'])
#plt.savefig('NCvSCNBAPos.png')

#No statistic such as CarAV for NBA available in this dataset = compare NC vs. SC players relative to scoring 

#Better Scorers - NorCal vs. SoCal - Bubble Plot, FG/FGA
#Conclusion - Very similar across players with all experience levels(bubblesize the same)
FGData = californiaNBA['FG']
FGAData = californiaNBA['FGA']
norCalFG = FGData[NCIndices]
soCalFG = FGData[SCIndices]
norCalFGA = FGAData[NCIndices]
soCalFGA = FGAData[SCIndices]
#plt.scatter(norCalFG, norCalFGA, s = norCalFG/norCalFGA * 250, c='#c41010',edgecolors='k')
#plt.xlabel('FG Made')
#plt.ylabel('FG Attempted')
#plt.title('Better Scorers - NorCal')
#plt.savefig('ScoringNCal.png')

#plt.scatter(soCalFG, soCalFGA, s = soCalFG/soCalFGA * 250, c='#1f1bbb',edgecolors='k')
#plt.xlabel('FG Made')
#plt.ylabel('FG Attempted')
#plt.title('Better Scorers - SoCal')
#plt.savefig('ScoringSCal.png')

#Other sides of Offensive Ball, ORB,AST,Games Played
#Trend - More experienced NorCal players have a  higher offensive effect, however, there is no correlation with experience for SoCal Players
ORBData = californiaNBA['ORB']
ASTData = californiaNBA['AST']
Games = californiaNBA['G']
combinedEffectNC = ORBData[NCIndices] + ASTData[NCIndices]
combinedEffectSC = ORBData[SCIndices] + ASTData[SCIndices]
GamesNC = Games[NCIndices]
GamesSC = Games[SCIndices]
#plt.scatter(combinedEffectNC, GamesNC, s = combinedEffectNC/GamesNC * 100, c='#c41010',edgecolors='k')
#plt.xlabel('Offensive Rebounds + Assists')
#plt.ylabel('Games Played')
#plt.title('Offensive Effect - NorCal')
#plt.savefig('OEffectNCal.png')
#plt.scatter(combinedEffectSC, GamesSC, s = combinedEffectSC/GamesSC * 100, c='#1f1bbb',edgecolors='k')
#plt.xlabel('Offensive Rebounds + Assists')
#plt.ylabel('Games Played')
#plt.title('Offensive Effect - SoCal')
#plt.savefig('OEffectSCal.png')

#Defensive Effect - STL(Steals), BLK(Blocks), Games 
#Trend - Defensive Effect is higher w/ experienced players in NorCal
#Trend - Defensive Effect is higher for players w/ similar experience in NorCal
#Trend =  Defensive Effect is not necessarily higher w/ experienced players in SoCal
STLData = californiaNBA['STL']
BLKData = californiaNBA['BLK']
deffectNC = STLData[NCIndices] + BLKData[NCIndices] 
deffectSC = STLData[SCIndices] + BLKData[SCIndices] 
#plt.scatter(deffectNC, GamesNC, s = deffectNC/GamesNC * 100, c='#c41010',edgecolors='k')
#plt.xlabel('Steals + Blocks')
#plt.ylabel('Games Played')
#plt.title('Defensive Effect - NorCal')
#plt.savefig('DEffectNCal.png')
plt.scatter(deffectSC, GamesSC, s = deffectSC/GamesSC * 100, c='#1f1bbb',edgecolors='k')
plt.xlabel('Steals + Blocks')
plt.ylabel('Games Played')
plt.title('Defensive Effect - SoCal')
plt.savefig('DEffectSCal.png')

    