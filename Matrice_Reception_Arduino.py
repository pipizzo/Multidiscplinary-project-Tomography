import numpy as np
import serial                                   #interface avec arduino

arduinoData = serial.Serial('com6',9600)        #donnés du serial envoyé par l'arduino

myData = (arduinoData.readline().strip())       #donnés du serial haché

projections = []                                #liste qui va contenir l'ensemble des projections pour les differents angles
c = 0                                           #compteur de tour de la boucle

while c < 50 :                                 #nbre degrés balayé
    projection = []                             #liste qui va contenir une projection pour un angle donne
    for i in range(450) :                        #nbre de mesure prise pour un angle
        myData = (arduinoData.readline().strip())       #donnés du serial haché
        a = int(myData)
        projection.append(a)
    if (c % 2 != 0):
        projection.reverse()
    projections.append(projection)
    c +=1

#print(projections)

b = np.array(projections)
#np.mat(b)
print(b)

#print('')
#c = np.mat(b)
#print(c)
