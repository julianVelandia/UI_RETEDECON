import serial

class UNO:
    def __init__(self):
        self.arduinoUNO = serial.Serial('COM5', 9600)

    def datain(self):
        while True:
            line = self.arduinoUNO.readline()
            linea = str(line)
            uid_find = linea.find("Card UID: ")
            IRstatus = linea.find("IR ")
            status = linea[IRstatus + 3]
            for lines in line:
                if status == '1':
                    isIn = True
                    print(isIn)
                    break
                if not uid_find == -1 :
                    #print(line)
                    IDstr = ""
                    for i in range(11):
                        IDstr += linea[uid_find+(i+10)]
                    print(IDstr)
                    break
        self.arduinoUNO.close()  # Finalizamos la comunicacion con UNO

class NANO:
    def __init__(self):
        self.arduinoNANO = serial.Serial('COM4', 9600)

    def dataout(self):
        while True:
            line = self.arduinoNANO.readline()
            for lines in line:
                linea = str(line)
                uid_find = linea.find("Card UID: ")
                if not uid_find == -1:
                    # print(line)
                    IDstr = ""
                    for i in range(11):
                        IDstr += linea[uid_find + (i + 10)]
                    print(IDstr)
                    break
        self.arduinoNANO.close() #Finalizamos la comunicacion con NANO

uno = UNO()
uno.datain()
#nano = NANO()
#nano.dataout()