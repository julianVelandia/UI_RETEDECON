import serial
import threading


#class UNO:

 #    def data_in(self):
 #        try:
  #           line = self.arduinoUNO.readline()
#             linea = str(line)
#             id_find = linea.find("IN")  # CHECK IF IT COMES FROM IN
#             ir_status = linea.find("IR ")  # SEARCH FOR IR STATUS
#             status = linea[ir_status + 3]  # READ IR STATUS
#             if status == '1':
#                 crossed = True
#                 print(crossed)
#             if not id_find == -1:
#                 line = self.arduinoUNO.readline()
#                 linea = str(line)
#                 uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
#                 if not uid_find == -1:
#                     uid_str = ""
#                     for i in range(11):
#                         uid_str += linea[uid_find + (i + 10)]
#                     print(uid_str + " IN")
#         except Exception as e:
#             print(e)
#             self.arduinoUNO.close()  # CLOSE THE SERIAL PORT
#
#     def data_out(self):
#         try:
#             line = self.arduinoUNO.readline()
#             linea = str(line)
#             id_find = linea.find("EXIT")  # CHECK IF IT COMES FROM EXIT
#             if not id_find == -1:
#                 line = self.arduinoUNO.readline()
#                 linea = str(line)
#                 uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
#                 if not uid_find == -1:
#                     uid_str = ""
#                     for i in range(11):
#                         uid_str += linea[uid_find + (i + 10)]
#                     uid_str = uid_str + " EXIT"
#                     print(uid_str)
#
#         except Exception as e:
#             print(e)
#             self.arduinoUNO.close()  # CLOSE THE SERIAL PORT
#
#

#
#class Read(UNO):
#
#    def __init__(self):
#        self.arduinoUNO = serial.Serial('COM5', 9600)
#        threading.Thread(target=execute, daemon=True).start()
#    def execute(self):
#        while True:
#            UNO.data_in(self)
#            UNO.data_out(self)
#
# re = Read()


def execute():
    arduinoUNO = serial.Serial('COM5', 9600)
    while arduinoUNO.isOpen():
        try:
            # data in
            line = arduinoUNO.readline()
            linea = str(line)
            id_find = linea.find("IN")  # CHECK IF IT COMES FROM IN
            ir_status = linea.find("IR ")  # SEARCH FOR IR STATUS
            status = linea[ir_status + 3]  # READ IR STATUS
            if status == '1':
                crossed = True
                print(crossed)
            if not id_find == -1:
                line = arduinoUNO.readline()
                linea = str(line)
                uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
                if not uid_find == -1:
                    uid_str = ""
                    for i in range(11):
                        uid_str += linea[uid_find + (i + 10)]
                    print(uid_str + " IN")

            # data out

            line = arduinoUNO.readline()
            linea = str(line)
            id_find = linea.find("EXIT")  # CHECK IF IT COMES FROM EXIT
            if not id_find == -1:
                line = arduinoUNO.readline()
                linea = str(line)
                uid_find = linea.find("Card UID: ")  # SEARCH FOR CARD UID
                if not uid_find == -1:
                    uid_str = ""
                    for i in range(11):
                        uid_str += linea[uid_find + (i + 10)]
                    uid_str = uid_str + " EXIT"
                    print(uid_str)
        except Exception as e:
            print(e)
            arduinoUNO.close()  # CLOSE THE SERIAL PORT


threading.Thread(target=execute).start()
