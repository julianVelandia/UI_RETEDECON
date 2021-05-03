import serial
arduino = serial.Serial('COM5', 9600)

while True:
    line = arduino.readline()
    for lines in line:
        linea = str(line)
        uid_find=linea.find("Card UID: ")
        IRstatus = linea.find("IR ")
        status = linea[IRstatus+3]
        if status == '1':
            isIn = True
            print(isIn)
            break
        if not uid_find == -1 and isIn:
            #print(line)
            IDstr = ""
            for i in range(11):
                IDstr += linea[uid_find+(i+10)]
            print(IDstr)
            break
arduino.close() #Finalizamos la comunicacion