import serial

class UNO:

    def data_in(self, line):
        if self.sw.state == 0:
            try:
                linea = str(line)
                id_find = linea.find("IN")  # CHECK IF IT COMES FROM IN
                if not id_find == -1:
                    uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
                    uid_str = ""
                    for i in range(11):
                        uid_str += linea[uid_find + (i + 10)]
                    print(uid_str)

                    # cambiar de estado
                    self.sw.saux(uid_str)                
            except:
                self.arduinoUNO.close()  # CLOSE THE SERIAL PORT
        if self.sw.state==3:
            try:
                linea = str(line)
                ir_status = linea.find("IR ")  # SEARCH FOR IR STATUS
                status = linea[ir_status + 3]  # READ IR STATUS
                print(status)
                if status == '1':
                    self.sw.s2()
                    print("si")
            except:
                print("failed")
                self.arduinoUNO.close()  # CLOSE THE SERIAL PORT

    def data_out(self, line):
        try:
            linea = str(line)
            id_find = linea.find("EXIT")  # CHECK IF IT COMES FROM EXIT
            #print(line)
            if not id_find == -1:
                uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
                uid_str = ""
                for i in range(11):
                    uid_str += linea[uid_find + (i + 10)]
                print(uid_str)

                #registrar salida en base de datos
                self.sw.salida(uid_str)
        except:
            self.arduinoUNO.close()  # CLOSE THE SERIAL PORT


class Read(UNO):

    def __init__(self):
        self.arduinoUNO = serial.Serial('/dev/ttyACM0', 9600)

    def execute(self):
        while True:
            line = self.arduinoUNO.readline()
            UNO.data_in(self, line)
            UNO.data_out(self, line)