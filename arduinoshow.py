import serial
arduinoData = serial.Serial('com4',9600)
while True:
        myData = (arduinoData.readline().strip())
        print (myData.decode('utf-8'))

