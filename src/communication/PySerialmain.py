import serial
#ESTE ES UN EJEMPLO DE LA CONEXIÓN CON ARDUINO SOBRE EL QUE ESTOY TRABAJANDO
arduino = serial.Serial('/dev/ttyACM0', 9600)

while True:
      comando = input('Introduce un comando: ') #Input
      arduino.write(comando.encode()) #Mandar un comando hacia Arduino
      if comando == 'H':
            print('LED ENCENDIDO')
      elif comando == 'L':
            print('LED APAGADO')

arduino.close() #Finalizamos la comunicacion