import serial
arduino = serial.Serial('COM5', 9600)

while True:
      line = arduino.readline()
      for lines in line:
            linea = str(line)
            line_find=linea.find("Card UID: ")
            if not line_find == -1:
                  print(line)
                  break
arduino.close() #Finalizamos la comunicacion