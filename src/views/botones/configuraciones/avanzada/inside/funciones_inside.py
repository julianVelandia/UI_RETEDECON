from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# locals
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *
# from .agregar.boton_agregar import Boton_agregar

# smtp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# libreria de tiempo
from datetime import datetime


class Funcion_inside:  # (Boton_agregar):

    def InsideAgregar(self):
        self.pantalla = 'agregar'
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.agregar_username.setVisible(True)
        self.agregar_pass.setVisible(True)
        self.agregar_agregar.setVisible(True)

    def InsideEliminar(self):
        self.pantalla = 'eliminar'
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.eliminar_username.setVisible(True)
        self.eliminar_pass.setVisible(True)
        self.eliminar_eliminar.setVisible(True)

    def InsideEnviar(self):

        try:
            # Hora actual
            now = datetime.now()
            # Iniciar parámetros
            remitente = 'retedeconunal@gmail.com'
            destinatarios = ['retedeconunal@gmail.com']
            asunto = 'Datos obtenidos hasta el día ' + str(now.date())
            cuerpo = ''
            ruta_adjunto = 'src/models/data/DB.csv'
            nombre_adjunto = 'DB.csv'

            # Crear objeto mensaje
            mensaje = MIMEMultipart()

            # Establecer atributos del mensaje
            mensaje['From'] = remitente
            mensaje['To'] = ", ".join(destinatarios)
            mensaje['Subject'] = asunto

            # Agregar el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(cuerpo, 'plain'))

            # Abrir el archivo a adjuntar
            archivo_adjunto = open(ruta_adjunto, 'rb')

            # Crear un objeto MIME base
            adjunto_MIME = MIMEBase('application', 'octet-stream')
            # cargar el archivo adjunto
            adjunto_MIME.set_payload((archivo_adjunto).read())
            # Codificar el objeto en BASE64
            encoders.encode_base64(adjunto_MIME)
            # Agregar una cabecera al objeto
            adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
            # agregarlo al mensaje
            mensaje.attach(adjunto_MIME)

            # Crear la conexión con el servidor
            sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

            # Cifrar la conexión
            sesion_smtp.starttls()

            # Iniciar sesión en el servidor
            sesion_smtp.login('retedeconunal@gmail.com', 'Rete..1234')

            # Convertir el objeto mensaje a texto
            texto = mensaje.as_string()

            # Enviar el mensaje
            sesion_smtp.sendmail(remitente, destinatarios, texto)

            # Cerrar la conexión
            sesion_smtp.quit()

            ####
            self.dialogo_mensaje = "Se han enviado los datos al servidor"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()
        except ValueError:
            print(ValueError)
            self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
            self.dialogo.setInformativeText(self.dialogo_mensaje)
            self.dialogo.show()

    def InsideCapacidad(self):
        self.pantalla = 'capacidad'
        self.inside_agregar.setVisible(False)
        self.inside_eliminar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.capacidad_newcapacidad.setVisible(True)
        self.capacidad_setnew.setVisible(True)

    def InsideCambiar(self):
        self.pantalla = 'cambiar'
        print(self.pantalla)
