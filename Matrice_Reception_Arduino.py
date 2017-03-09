import numpy as np
import serial

arduinoData = serial.Serial('com4',9600) #donnés du serial envoyé par l'arduino

myData = (arduinoData.readline().strip()) #donnés du serial haché

projections = []
c = 0

while c < 179 :                               #nbre degrés balayé
    projection = []
    for i in range(64) :                    #nbre de mesure prise pour un angle
        a = int(myData)
        projection.append(a)

    #print(projection)
    projections.append(projection)
    c +=1
    
                                      #ATTENTION à regler le pas

print(projections)

#b = np.array(projections)
#np.mat(b)

#print('')
#c = np.mat(b)
#print(c)
