#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:25:51 2018

@author: shriramgharpure
"""
norCalCities = ['Alameda','Antioch','Berkeley', 'Brentwood', 'Chico', 'Citrus Heights', 'Clovis', 'Concord','Cupertino', 'Daly City', 'Davis', 'Elk Grove',	'Fairfield', 'Folsom', 'Fresno', 'Fremont', 'Hanford','Hayward','Livermore','Lodi', 'Madera', 'Manteca', 'Merced', 'Milpitas', 'Modesto', 'Mountain View', 'Napa', 'Novato', 'Oakland', 'Palo Alto', 'Petaluma', 'Pittsburg', 'Pleasanton', 'Porterville', 'Rancho Cordova', 'Redding', 'Redwood City', 'Richmond', 'Rocklin', 'Roseville', 'Sacramento', 'Salinas', 'San Francisco', 'San Jose', 'San Leandro', 'San Mateo', 'San Rafael','San Ramon', 'Santa Clara', 'Santa Cruz', 'Santa Rosa', 'South San Francisco', 'Stockton', 'Sunnyvale', 'Tracy', 'Tulare',  'Turlock', 'Union City', 'Vacaville', 'Vallejo', 'Visalia', 'Walnut Creek','Watsonville', 'Woodland', 'Yuba City']
soCalCities = ['Agoura Hills', 'Alhambra', 'Arcadia', 'Artesia', 'Avalon', 'Azusa', 'Baldwin Park', 'Bell', 'Bell Gardens', 'Bellflower', 'Beverly Hills', 'Bradbury', 'Burbank', 'Calabasas', 'Carson', 'Cerritos', 'Claremont', 'Commerce', 'Compton', 'Covina', 'Cudahy', 'Culver City', 'Diamond Bar', 'Downey', 'Duarte', 'El Monte', 'El Segundo', 'Gardena', 'Glendale', 'Glendora', 'Hawaiian Gardens', 'Hawthorne', 'Hermosa Beach', 'Hidden Hills', 'Huntington Park', 'Industry', 'Inglewood', 'Irwindale', 'La Cañada Flintridge', 'La Habra', 'La Mirada', 'La Puente', 'La Verne', 'Lakewood', 'Lancaster', 'Lawndale', 'Lomita', 'Long Beach', 'Los Angeles', 'Lynwood', 'Malibu', 'Manhattan Beach', 'Maywood', 'Monrovia', 'Montebello', 'Monterey Park', 'Norwalk', 'Palmdale', 'Palos Verdes', 'Paramount', 'Pasadena', 'Pico Rivera', 'Pomona', 'Rancho', 'Redondo Beach', 'Rolling Hills', 'Rosemead', 'San Dimas', 'San Fernando', 'San Gabriel', 'San Marino', 'Santa Clarita','Santa Fe Springs', 'Santa Monica', 'Sierra Madre', 'Signal Hill', 'South El Monte', 'South Gate', 'South Pasadena', 'Temple City', 'Torrance', 'Vernon', 'Walnut', 'West Covina', 'West Hollywood', 'Westlake Village', 'Whittier', 'Aliso Viejo', 'Anaheim', 'Brea', 'Buena Park', 'Costa Mesa', 'Cypress', 'Dana Point', 'Fountain Valley', 'Fullerton', 'Garden Grove', 'Huntington Beach', 'Irvine', 'La Habra', 'La Palma', 'Laguna Beach', 'Laguna Hills', 'Laguna Niguel', 'Laguna Woods', 'Lake Forest', 'Los Alamitos', 'Mission Viejo', 'Newport Beach', 'Orange', 'Placentia', 'Rancho Santa Margarita', 'San Clemente', 'San Juan Capistrano', 'Santa Ana', 'Seal Beach', 'Stanton', 'Tustin', 'Villa Park', 'Westminster', 'Yorba Linda', 'Brawley', 'Calexico', 'Calipatria', 'El Centro', 'Holtville', 'Imperial', 'Westmorland', 'Banning', 'Beaumont', 'Blythe', 'Calimesa', 'Canyon Lake', 'Cathedral City', 'Coachella', 'Corona Desert', 'Hot Springs', 'Eastvale', 'Hemet', 'Indian Wells', 'Indio', 'Jurupa Valley', 'La Quinta', 'Lake Elsinore', 'Menifee', 'Moreno Valley', 'Murrieta', 'Norco', 'Palm Desert', 'Palm Springs', 'Perris', 'Rancho Mirage', 'Riverside', 'San Jacinto', 'Temecula', 'Wildomar', 'Adelanto', 'Apple Valley', 'Barstow', 'Big Bear Lake', 'Chino', 'Chino Hills',     'Colton', 'Fontana', 'Grand Terrace', 'Hesperia', 'Highland', 'Loma Linda', 'Montclair', 'Needles', 'Ontario', 'Rancho Cucamonga', 'Redlands', 'Rialto', 'San Bernardino', 'Twentynine Palms', 'Upland', 'Victorville', 'Yucaipa', 'Yucca Valley', 'Carlsbad', 'Chula Vista', 'Coronado Del Mar', 'El Cajon', 'Encinitas', 'Escondido', 'Imperial Beach', 'La Mesa', 'Lemon Grove', 'National City', 'Oceanside', 'Poway', 'San Diego', 'San Marcos', 'Santee', 'Solana Beach', 'Vista', 'Camarillo', 'Fillmore', 'Moorpark', 'Ojai', 'Oxnard', 'Port Hueneme', 'Santa Paula', 'Simi Valley', 'Thousand Oaks', 'Ventura', 	'Buellton', 'Carpinteria', 'Goleta', 'Guadalupe', 'Lompoc', 'Santa Barbara', 'Santa Maria', 'Solvang']	
nflNorCalCount = 0 
nflSoCalCount = 0 
indexNorCalArr = []
indexSoCalArr = []
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
CaliforniaNFL = pd.read_csv('/Users/shriramgharpure/Downloads/CaliforniaNFL.csv')
cityCheck = CaliforniaNFL['City']
positionCheck = CaliforniaNFL['Pos']
proBowlCheck = CaliforniaNFL['PB']
careerValueCheck = CaliforniaNFL['CarAV']
gamesPlayedCheck = CaliforniaNFL['G']
# Establish NorCal and SoCal indexes and count number of players in NorCal and Socal
for i in range(len(CaliforniaNFL)):
    if cityCheck[i] in norCalCities:
        nflNorCalCount =  nflNorCalCount + 1;
        indexNorCalArr.append(i)
    if cityCheck[i] in soCalCities:
        nflSoCalCount = nflSoCalCount + 1;
        indexSoCalArr.append(i)
#Count NorCal Players by Position(Fixed Position Data, Not for Players w/ Multiple Positions)
norCal = [];
listPos = ['T', 'G', 'C','QB','RB','FB','WR','TE','DE','DT','OLB','ILB','DB', 'CB','FS','SS','KR','PR']
#First 8 Corr. to Offense, Middle 9 Corr. to Defense, Last 2 Special Teams
tempCount = 0
norCalPos = positionCheck[indexNorCalArr]
for spec in listPos:
    for position in norCalPos:
        if spec == position:
            tempCount = tempCount + 1
    norCal.append(tempCount)
    tempCount = 0
#Count SoCal Players by Position(Fixed Position Data, Not for Players w/ Multiple Positions)
soCal = [];
soCalPos = positionCheck[indexSoCalArr]
for spec in listPos:
    for position in soCalPos:
        if spec == position:
            tempCount = tempCount + 1
    soCal.append(tempCount)
    tempCount = 0
#Stacked Bar Graph - NorCal and SoCal NFL Player Positions
#N = len(listPos)
#indices = np.arange(N)
#barW = 0.30
#norCalPlot = plt.bar(indices, norCal, barW, label='NorCal')
#soCalPlot = plt.bar(indices+barW, soCal, barW, label='SoCal')
#plt.xticks(indices,listPos)
#plt.xlabel('Position')
#plt.ylabel('Frequency')
#plt.title('NorCal vs. SoCal - Positions in the NFL')
#plt.legend([norCalPlot, soCalPlot],['NorCal','SoCal'])
#plt.savefig('NCvSCNFLPos.png')

#CumulativeProBowlSelections 
nCalSelections = 0
cumPBnCal = 0 
indexesSupStarNC = []
indexesSupStarSC = []
norCalPBowl = proBowlCheck[indexNorCalArr]
for elem in norCalPBowl:
    if elem > 0:
        nCalSelections = nCalSelections + 1;
        cumPBnCal = cumPBnCal + elem

sCalSelections = 0 
cumPBsCal = 0
soCalPBowl = proBowlCheck[indexSoCalArr]
for elemTwo in soCalPBowl:
    if elemTwo > 0:
        sCalSelections = sCalSelections + 1;
        cumPBsCal = cumPBsCal + elemTwo
#Metric - Career Strength(Bubble Plot)
#Size of the bubbles is represented by the ratio of CarAV to G - more accurate measurement of player performance
norCalAV = careerValueCheck[indexNorCalArr]
norCalG = gamesPlayedCheck[indexNorCalArr]
soCalAV = careerValueCheck[indexSoCalArr]
soCalG = gamesPlayedCheck[indexSoCalArr]
#NorCalBubblePlot
#plt.scatter(norCalAV, norCalG, s = norCalAV/norCalG * 250, c='#c41010',edgecolors='k')
#plt.xlabel('Career Average Value')
#plt.ylabel('Games Played')
#plt.title('Career Average Value vs. Games Played - NorCal NFL')
#plt.savefig('BubblePlotnCal.png')
#SoCalBubblePlot 
plt.scatter(soCalAV, soCalG, s = soCalAV/soCalG * 250, c='#1f1bbb', edgecolors='k')
plt.xlabel('Career Average Value')
plt.ylabel('Games Played')
plt.title('Career Average Value vs. Games Played - SoCal NFL')
plt.savefig('BubblePlotsCal.png')