import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Funcion_enviar:
    def EnviarSetnew(self):
        # try:

            # Iniciar parámetros
            remitente = 'retedeconunal@gmail.com'
            destinatarios = [self.enviar_newenviar.text()]
            asunto = 'Correo de prueba'
            cuerpo = 'Este es el contenido del mensaje'
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
            self.HomeWindow()
        # except ValueError:
        #     print(ValueError)
        #     self.dialogo_mensaje = "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante"
        #     self.dialogo.setInformativeText(self.dialogo_mensaje)
        #     self.dialogo.show()