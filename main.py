from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from configparser import ConfigParser
import sys
import hashlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


#locals
from src.controler.QLineClick import QLineEditClick
from src.views.botones.inicio.boton import Boton
from src.views.teclado.teclado_numeros import TecladoNumeros
from src.views.teclado.teclado_letras import TecladoLetras


class MainWindow(QMainWindow,Boton,TecladoNumeros,TecladoLetras): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("src/views/static/styles.css") as f:
            self.setStyleSheet(f.read())

        #INICIALIZAR EN UN ARCHIVO parameter.ini o algo así PARA NO HACER HARDCODING
        self.cedula_cache = ''
        self.carnet = ''
        self.title = 'RETEDECON'
        self.config = ConfigParser()
        self.width = 1024
        self.height = 600

        self.setMinimumSize(self.width,self.height)    #tamaño mínimo
        self.setMaximumSize(self.width,self.height) #tamaño máximo
        self.setWindowTitle(self.title)   #titulo
        self.setWindowIcon(QIcon("src/views/static/icons/favicon3.png")) #Favicon


        #Widget principal
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window") #nombre que enlaza en css
        
        #Imagen central 
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(289,-10,1024,600)
        self.pixmap = QPixmap('src/views/static/icons/Logo_central.png')   #Imagen central
        self.label_img_central.setPixmap(self.pixmap)        
        self.label_img_central.setVisible(True)

        #Timer animación
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.HomeWindow) #función a ejecutar pasados los 3 seg

        #Botones Inicio
        self.boton_home(self.centralWidget)

        self.boton_inicio_ingresar(self.centralWidget)
        self.boton_inicio_estadisticas(self.centralWidget)
        self.boton_inicio_detener_alarma(self.centralWidget)
        self.boton_inicio_salida_manual(self.centralWidget)
        self.boton_inicio_configuracion(self.centralWidget)
        self.boton_inicio_estadisticas(self.centralWidget)
        self.boton_inicio_informacion(self.centralWidget)

        #Botones ingresar
        self.texto_ingresar_nombre(self.centralWidget)
        self.texto_ingresar_cedula(self.centralWidget)
        self.texto_ingresar_temp(self.centralWidget)
        self.boton_ingresar_ingresar(self.centralWidget)

        #Botones salida
        self.texto_salida_nombre_out(self.centralWidget)
        self.texto_salida_cedula_out(self.centralWidget)
        self.boton_salida_salida(self.centralWidget)

        self.BotonesTeclado(self.centralWidget)
        self.BotonesTecladoNumerico(self.centralWidget)



        #luego lo pongo en alguna clase y lo paso bien
        self.dialogo_mensaje = 'Error404'
        self.dialogo = QMessageBox(self.centralWidget)
        self.dialogo.setWindowTitle('RETEDECON')
        self.dialogo.addButton("Aceptar", 0)
        self.dialogo.setInformativeText(self.dialogo_mensaje)





        #config
        'Capacidad'
        self.configuracion_capacidad_text = QLineEditClick(self.centralWidget)
        self.configuracion_capacidad_text.setPlaceholderText("CAPACIDAD")
        self.configuracion_capacidad_text.setObjectName("input") #nombre de enlace a css
        self.configuracion_capacidad_text.setClearButtonEnabled(True)
        self.configuracion_capacidad_text.setGeometry(164,237,290,70)
        self.configuracion_capacidad_text.setMaxLength(5)
        self.configuracion_capacidad_text.setVisible(False)

        'ADMINISTRADOR_USER'
        self.configuracion_avanzada_user = QLineEditClick(self.centralWidget)
        self.configuracion_avanzada_user.setPlaceholderText("USUARIO")
        self.configuracion_avanzada_user.setObjectName("input") #nombre de enlace a css
        self.configuracion_avanzada_user.setClearButtonEnabled(True)
        self.configuracion_avanzada_user.setGeometry(164,237,290,70)
        self.configuracion_avanzada_user.setMaxLength(40)
        self.configuracion_avanzada_user.setVisible(False)

        'ADMINISTRADOR_PASS'
        self.configuracion_avanzada_pass = QLineEditClick(self.centralWidget)
        self.configuracion_avanzada_pass.setPlaceholderText("CONTRASEÑA")
        self.configuracion_avanzada_pass.setObjectName("input")  # nombre de enlace a css
        self.configuracion_avanzada_pass.setClearButtonEnabled(True)
        self.configuracion_avanzada_pass.setGeometry(164, 341, 290, 70)
        self.configuracion_avanzada_pass.setMaxLength(15)
        self.configuracion_avanzada_pass.setVisible(False)
        self.configuracion_avanzada_pass.setEchoMode(QLineEdit.Password)

        'NewAdmin User'
        self.new_admin_username = QLineEditClick(self.centralWidget)
        self.new_admin_username.setPlaceholderText("USUARIO")
        self.new_admin_username.setObjectName("input")  # nombre de enlace a css
        self.new_admin_username.setClearButtonEnabled(True)
        self.new_admin_username.setGeometry(164, 237, 290, 70)
        self.new_admin_username.setMaxLength(40)
        self.new_admin_username.setVisible(False)

        'NewAdmin password'
        self.new_admin_password = QLineEditClick(self.centralWidget)
        self.new_admin_password.setPlaceholderText("CONTRASEÑA")
        self.new_admin_password.setObjectName("input")  # nombre de enlace a css
        self.new_admin_password.setClearButtonEnabled(True)
        self.new_admin_password.setGeometry(164, 341, 290, 70)
        self.new_admin_password.setMaxLength(15)
        self.new_admin_password.setVisible(False)
        self.new_admin_password.setEchoMode(QLineEdit.Password)

        self.campo ='null'

        
        
        

        #AccionClcikIngresarNombre
        self.ingresar_nombre.clicked.connect(self.Ingresar_desplegar_teclado)
        #AccionClcikIngresarCedula
        self.ingresar_cedula.clicked.connect(self.Ingresar_desplegar_teclado_numerico_cedula)
        #AccionIngresarTemperatura
        self.ingresar_temp.clicked.connect(self.Ingresar_desplegar_teclado_numerico_temp)
        #AccionClcikIngresarNombreOut
        self.salida_nombre.clicked.connect(self.Retirar_desplegar_teclado)
        #AccionClcikIngresarCedulaOut
        self.salida_cedula.clicked.connect(self.Retirar_desplegar_teclado_numerico_cedula)
        #AccionClcikIngresarUser
        self.configuracion_avanzada_user.clicked.connect(self.Ad_Conf_desplegar_teclado)
        #AccionClcikIngresarPass
        self.configuracion_avanzada_pass.clicked.connect(self.Ad_Conf_desplegar_teclado_numerico)
        #Botones de configuraciones
        self.BotonesConfig()
        #Botones Ad Conf
        self.BotonesConfiguracionAvanzada()
        # Botones Ad Conf In
        self.BotonesConfiguracionAvanzadaInside()
        # Botones Ad Conf In
        self.BotonesCapacidad()
        # Botones Informacion
        self.BotonesInformacion()
        # Label infos
        self.LabelsInformacion()
        # Labels y Botones Estadisticas
        self.LabelsBotonesEstadisticas()
        # Botones new admin
        self.BotonesNewAdmin()
        '''
        Valores BD
        '''


        self.fecha = 0
        self.HoraIn =0
        self.HoraOut = 0
        self.Delta=0
        self.Numingresos=0
        self.IsIn = False
        '''
        Graficas
        '''
        #Barras
        self.bar_chart = PlotCanvas(self, width=5, height=4)
        self.bar_chart.move(450, 120)
        self.bar_chart.setVisible(False)
        #Pie
        self.pie_chart = PlotCanvasP(self, width=5, height=4)
        self.pie_chart.move(450, 120)
        self.pie_chart.setVisible(False)



    def BotonesConfig(self):
        self.configuracion_avanzada = QToolButton(self.centralWidget)
        self.configuracion_avanzada.setText('Configuración Avanzada\n(Administrador)')
        self.configuracion_avanzada.setObjectName("button") #nombre de enlace a css
        self.configuracion_avanzada.setIcon(QIcon('src/views/static/icons/icono_config_avanzada')) #icono
        self.configuracion_avanzada.setIconSize(QSize(65,65))
        self.configuracion_avanzada.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_avanzada.setGeometry(534, 120, 290, 180)
        self.configuracion_avanzada.clicked.connect(self.ConfiguracionAvanzada)
        self.configuracion_avanzada.setVisible(False)

        self.configuracion_apagar = QToolButton(self.centralWidget)
        self.configuracion_apagar.setText('Apagar')
        self.configuracion_apagar.setObjectName("button") #nombre de enlace a css
        self.configuracion_apagar.setIcon(QIcon('src/views/static/icons/icono_apagar')) #icono
        self.configuracion_apagar.setIconSize(QSize(60,60))
        self.configuracion_apagar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_apagar.clicked.connect(self.Apagar)
        self.configuracion_apagar.setGeometry(534, 340, 290, 180)
        self.configuracion_apagar.setVisible(False)

        self.configuracion_pantalla = QToolButton(self.centralWidget)
        self.configuracion_pantalla.setText('Ajustes de Pantallas')
        self.configuracion_pantalla.setObjectName("button")  # nombre de enlace a css
        self.configuracion_pantalla.setIcon(QIcon('src/views/static/icons/icono_config_pantalla'))  # icono
        self.configuracion_pantalla.setIconSize(QSize(60, 60))
        self.configuracion_pantalla.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_pantalla.clicked.connect(self.HomeWindow)
        self.configuracion_pantalla.setGeometry(200, 120, 290, 180)
        self.configuracion_pantalla.setVisible(False)

        self.configuracion_datos = QToolButton(self.centralWidget)
        self.configuracion_datos.setText('Cambiar Estilo De Gráfica\nDe Datos')
        self.configuracion_datos.setObjectName("button")  # nombre de enlace a css
        self.configuracion_datos.setIcon(QIcon('src/views/static/icons/icono_estadisticas'))  # icono
        self.configuracion_datos.setIconSize(QSize(70, 70))
        self.configuracion_datos.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_datos.clicked.connect(self.HomeWindow)
        self.configuracion_datos.setGeometry(200, 340, 290, 180)
        self.configuracion_datos.setVisible(False)


    def BotonesNewAdmin(self):
        'crear new admin'
        self.new_admin = QToolButton(self.centralWidget)
        self.new_admin.setText('REGISTRAR')
        self.new_admin.setObjectName("button") #nombre de enlace a css
        self.new_admin.setIcon(QIcon('src/views/static/icons/icono_entrar')) #icono
        self.new_admin.setIconSize(QSize(60,60))
        self.new_admin.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.new_admin.setGeometry(570, 150, 290, 180)
        self.new_admin.clicked.connect(self.NewAdmin)
        self.new_admin.setVisible(False)

        self.quitar_admin = QToolButton(self.centralWidget)
        self.quitar_admin.setText('ELIMINAR')
        self.quitar_admin.setObjectName("button")  # nombre de enlace a css
        self.quitar_admin.setIcon(QIcon('src/views/static/icons/icono_salir'))  # icono
        self.quitar_admin.setIconSize(QSize(60, 60))
        self.quitar_admin.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.quitar_admin.setGeometry(570, 350, 290, 180)
        self.quitar_admin.clicked.connect(self.EliminarAdmin)
        self.quitar_admin.setVisible(False)

    def setCapacidadMaxima(self):
        # Reading the config.ini file
        try:
            self.config.read('../config.ini')
            self.config.set('capacity', 'key1', self.configuracion_capacidad_text.text())
            with open('../config.ini', 'w') as f:
                self.config.write(f)
            print(self.config.getint('capacity','key1'))
            self.ConfiguracionAvanzadaInside()
        except:
            dialogo_error = QMessageBox(self.centralWidget)
            dialogo_error.setWindowTitle(self.title)
            dialogo_error.addButton("Aceptar", 0)
            dialogo_error.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error.show()

    def BotonesCapacidad(self):
        self.ingresar_capacidad = QToolButton(self.centralWidget)
        self.ingresar_capacidad.setText('CAMBIAR CAPACIDAD\nMÁXIMA')
        self.ingresar_capacidad.setObjectName("button")  # nombre de enlace a css
        self.ingresar_capacidad.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.ingresar_capacidad.setIconSize(QSize(60, 60))
        self.ingresar_capacidad.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar_capacidad.clicked.connect(self.setCapacidadMaxima)
        self.ingresar_capacidad.setGeometry(570, 230, 290, 231)
        self.ingresar_capacidad.setVisible(False)

    def Capacidad(self):
        self.configuracion_capacidad_text.setVisible(True)
        self.ingresar_capacidad.setVisible(True)
        self.configuracion_capacidad.setVisible(False)
        self.new_admin_username.setVisible(False)
        self.new_admin_password.setVisible(False)
        self.new_admin.setVisible(False)
        self.agregar_eliminar_admin_boton.setVisible(False)
        self.cambiar_password_admin_boton.setVisible(False)
        self.enviar_datos_servidor.setVisible(False)

    def BotonesConfiguracionAvanzada(self):
        self.ingresar_Ad_Conf = QToolButton(self.centralWidget)
        self.ingresar_Ad_Conf.setText('ACCEDER')
        self.ingresar_Ad_Conf.setObjectName("button")  # nombre de enlace a css
        self.ingresar_Ad_Conf.setIcon(QIcon('src/views/static/icons/icono_entrar'))  # icono
        self.ingresar_Ad_Conf.setIconSize(QSize(60, 60))
        self.ingresar_Ad_Conf.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar_Ad_Conf.clicked.connect(self.AdConfPass)
        self.ingresar_Ad_Conf.setGeometry(570, 230, 290, 180)
        self.ingresar_Ad_Conf.setVisible(False)
        self.configuracion_avanzada_user.setVisible(False)
        self.configuracion_avanzada_pass.setVisible(False)

    def ConfiguracionAvanzada(self):
        self.configuracion_apagar.setVisible(False)
        self.configuracion_pantalla.setVisible(False)
        self.configuracion_datos.setVisible(False)
        self.configuracion_avanzada.setVisible(False)
        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.configuracion_avanzada_user.setVisible(True)
        self.configuracion_avanzada_user.clear()
        self.configuracion_avanzada_pass.setVisible(True)
        self.configuracion_avanzada_pass.clear()
        self.ingresar_Ad_Conf.setVisible(True)
        self.Ad_Conf_guardar_teclado()

    def BotonesConfiguracionAvanzadaInside(self):
        self.configuracion_capacidad = QToolButton(self.centralWidget)
        self.configuracion_capacidad.setText('Capacidad Máxima')
        self.configuracion_capacidad.setObjectName("button")  # nombre de enlace a css
        self.configuracion_capacidad.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.configuracion_capacidad.setIconSize(QSize(60, 60))
        self.configuracion_capacidad.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_capacidad.clicked.connect(self.Capacidad)
        self.configuracion_capacidad.setGeometry(534, 340, 290, 180)
        self.configuracion_capacidad.setVisible(False)
        
        self.agregar_eliminar_admin_boton = QToolButton(self.centralWidget)
        self.agregar_eliminar_admin_boton.setText('Agregar o Eliminar\nAdministrador')
        self.agregar_eliminar_admin_boton.setObjectName("button")  # nombre de enlace a css
        self.agregar_eliminar_admin_boton.setIcon(QIcon('src/views/static/icons/icono_add_delete_admin'))  # icono
        self.agregar_eliminar_admin_boton.setIconSize(QSize(60, 60))
        self.agregar_eliminar_admin_boton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.agregar_eliminar_admin_boton.clicked.connect(self.AgregarAdmin)
        self.agregar_eliminar_admin_boton.setGeometry(200, 120, 290, 180)
        self.agregar_eliminar_admin_boton.setVisible(False)

        self.cambiar_password_admin_boton = QToolButton(self.centralWidget)
        self.cambiar_password_admin_boton.setText('Cambiar contraseña')
        self.cambiar_password_admin_boton.setObjectName("button")  # nombre de enlace a css
        self.cambiar_password_admin_boton.setIcon(QIcon('src/views/static/icons/icono_capacidad'))  # icono
        self.cambiar_password_admin_boton.setIconSize(QSize(60, 60))
        self.cambiar_password_admin_boton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.cambiar_password_admin_boton.clicked.connect(self.HomeWindow)
        self.cambiar_password_admin_boton.setGeometry(200, 340, 290, 180)
        self.cambiar_password_admin_boton.setVisible(False)

        self.enviar_datos_servidor = QToolButton(self.centralWidget)
        self.enviar_datos_servidor.setText('Enviar Datos Al Servidor')
        self.enviar_datos_servidor.setObjectName("button")  # nombre de enlace a css
        self.enviar_datos_servidor.setIcon(QIcon('src/views/views/static/icons/icono_config_datos'))  # icono
        self.enviar_datos_servidor.setIconSize(QSize(60, 60))
        self.enviar_datos_servidor.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.enviar_datos_servidor.clicked.connect(self.HomeWindow)
        self.enviar_datos_servidor.setGeometry(534, 120, 290, 180)
        self.enviar_datos_servidor.setVisible(False)

    def ConfiguracionAvanzadaInside(self):
        self.configuracion_capacidad.setVisible(True)
        self.cambiar_password_admin_boton.setVisible(True)
        self.agregar_eliminar_admin_boton.setVisible(True)
        self.enviar_datos_servidor.setVisible(True)
        self.configuracion_apagar.setVisible(False)
        self.configuracion_pantalla.setVisible(False)
        self.configuracion_datos.setVisible(False)
        self.configuracion_avanzada.setVisible(False)
        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.configuracion_avanzada_user.setVisible(False)
        self.configuracion_avanzada_pass.setVisible(False)
        self.ingresar_Ad_Conf.setVisible(False)
        self.ingresar_capacidad.setVisible(False)
        self.configuracion_capacidad_text.setVisible(False)
        self.Ad_Conf_guardar_teclado()
        self.NotTecladoNumerico()

    def AgregarAdmin(self):
        self.configuracion_capacidad.setVisible(False)
        self.new_admin_username.setVisible(True)
        self.new_admin_password.setVisible(True)
        self.new_admin.setVisible(True)
        self.quitar_admin.setVisible(True)
        self.agregar_eliminar_admin_boton.setVisible(False)
        self.cambiar_password_admin_boton.setVisible(False)
        self.enviar_datos_servidor.setVisible(False)

    def NewAdmin(self):
        try:
            self.config.read('../config.ini')
            users = list(self.config['users'])
            users_values = []
            if self.new_admin_username.text() != "" and self.new_admin_password.text() != "":  # lógica para leer si los campos están vacíos
                if not self.new_admin_username.text().isdigit() and not self.new_admin_password.text().isalpha():  # detecta si numeros o letras donde no deben
                    # Use the cycle to append values to the list from the document
                    for key in users:
                        users_values.append(self.config.get('users', str(key)))
                    # Check if user is in the list
                    if self.new_admin_username.text() in users_values:
                        is_user = True
                    else:
                        is_user = False
                    # Existance verification
                    if not is_user:
                        dialogo_registro_exitoso = QMessageBox(self.centralWidget)
                        dialogo_registro_exitoso.setWindowTitle(self.title)
                        dialogo_registro_exitoso.addButton("Aceptar", 0)
                        dialogo_registro_exitoso.setInformativeText("Se ha registrado correctamente   \n")
                        dialogo_registro_exitoso.show()
                        self.HomeWindow()
                    else:
                        dialogo_error_existencia = QMessageBox(self.centralWidget)
                        dialogo_error_existencia.setWindowTitle(self.title)
                        dialogo_error_existencia.addButton("Aceptar", 0)
                        dialogo_error_existencia.setInformativeText("El usuario ya existe\n ")
                        dialogo_error_existencia.show()
                else:
                    dialogo_error_typ = QMessageBox(self.centralWidget)
                    dialogo_error_typ.setWindowTitle(self.title)
                    dialogo_error_typ.addButton("Aceptar", 0)
                    dialogo_error_typ.setInformativeText("Error, verifique los datos ingresados\n  "
                                                         "La contraseña debe tener solo numeros\n  ")
                    dialogo_error_typ.show()
            else:
                dialogo_error_incompleto = QMessageBox(self.centralWidget)
                dialogo_error_incompleto.setWindowTitle(self.title)
                dialogo_error_incompleto.addButton("Aceptar", 0)
                dialogo_error_incompleto.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto.show()
        except:
            dialogo_error = QMessageBox(self.centralWidget)
            dialogo_error.setWindowTitle(self.title)
            dialogo_error.addButton("Aceptar", 0)
            dialogo_error.setInformativeText(
                "Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error.show()

    def EliminarAdmin(self):
        try:
            self.config.read('../config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []
            if self.new_admin_username.text() != "" and self.new_admin_password.text() != "":  # lógica para leer si los campos están vacíos
                if not self.new_admin_username.text().isdigit() and not self.new_admin_password.text().isalpha():  # detecta si numeros o letras donde no deben
                    # Use the cycle to append values to the list from the document
                    for key in users:
                        users_values.append(self.config.get('users', str(key)))
                    # Check if user is in the list
                    if self.new_admin_username.text() in users_values:
                        correct_user = True
                        indU = users_values.index(self.new_admin_username.text())
                    else:
                        correct_user = False
                    # Use the cycle to append values to the list from the document
                    for key in passwords:
                        p1 = self.config.get('passwords', str(key))
                        passwords_values.append(p1)
                    # Check if password is in the list
                    p = self.new_admin_password.text()
                    h = hashlib.new("sha1", p.encode())
                    # Verifications
                    if str(h.digest()) in passwords_values:
                        correct_password = True
                        indP = passwords_values.index(str(h.digest()))
                    else:
                        correct_password = False
                    # Existance verification
                    if correct_user and correct_password and indP==indU:
                        dialogo_eliminación_exitoso = QMessageBox(self.centralWidget)
                        dialogo_eliminación_exitoso.setWindowTitle(self.title)
                        dialogo_eliminación_exitoso.addButton("Aceptar", 0)
                        dialogo_eliminación_exitoso.setInformativeText("Se ha eliminado correctamente   \n")
                        dialogo_eliminación_exitoso.show()
                        self.HomeWindow()
                    elif correct_user and not correct_password or not indU==indP:
                        dialogo_error_existencia = QMessageBox(self.centralWidget)
                        dialogo_error_existencia.setWindowTitle(self.title)
                        dialogo_error_existencia.addButton("Aceptar", 0)
                        dialogo_error_existencia.setInformativeText("Verifique los datos ingresados\n ")
                        dialogo_error_existencia.show()
                    else:
                        dialogo_error_existencia = QMessageBox(self.centralWidget)
                        dialogo_error_existencia.setWindowTitle(self.title)
                        dialogo_error_existencia.addButton("Aceptar", 0)
                        dialogo_error_existencia.setInformativeText("El usuario no existe\n ")
                        dialogo_error_existencia.show()
                else:
                    dialogo_error_typ = QMessageBox(self.centralWidget)
                    dialogo_error_typ.setWindowTitle(self.title)
                    dialogo_error_typ.addButton("Aceptar", 0)
                    dialogo_error_typ.setInformativeText("Error, verifique los datos ingresados\n  "
                                                         "La contraseña debe tener solo numeros\n  ")
                    dialogo_error_typ.show()
            else:
                dialogo_error_incompleto = QMessageBox(self.centralWidget)
                dialogo_error_incompleto.setWindowTitle(self.title)
                dialogo_error_incompleto.addButton("Aceptar", 0)
                dialogo_error_incompleto.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto.show()
        except:
            dialogo_error = QMessageBox(self.centralWidget)
            dialogo_error.setWindowTitle(self.title)
            dialogo_error.addButton("Aceptar", 0)
            dialogo_error.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error.show()

    def Apagar(self):
        sys.exit()

    def AdConfPass(self):
        try:
            #Reading the config.ini file
            self.config.read('../config.ini')
            users = list(self.config['users'])
            passwords = list(self.config['passwords'])
            users_values = []
            passwords_values = []
            #Use the cycle to append values to the list from the document
            for key in users:
                users_values.append(self.config.get('users', str(key)))
            # Check if user is in the list
            if self.configuracion_avanzada_user.text() in users_values:
                correct_user = True
                indU = users_values.index(self.configuracion_avanzada_user.text())
            else:
                correct_user = False
            # Use the cycle to append values to the list from the document
            for key in passwords:
                p1=self.config.get('passwords', str(key))
                passwords_values.append(p1)
            # Check if password is in the list
            p = self.configuracion_avanzada_pass.text()
            h = hashlib.new("sha1", p.encode())
            # Verifications
            if str(h.digest()) in passwords_values:
                correct_password = True
                indP = passwords_values.index(str(h.digest()))
            else:
                correct_password = False
            # Checking other conditions and connecting functions
            if self.configuracion_avanzada_user.text()!="" and self.configuracion_avanzada_pass.text()!="" :  #lógica para leer si los campos están vacíos
                if not self.configuracion_avanzada_user.text().isdigit() and not self.configuracion_avanzada_pass.text().isalpha():  #detecta si numeros donde no deben
                    if correct_user and correct_password and indU==indP:
                        dialogo_acceso_concedido = QMessageBox(self.centralWidget)
                        dialogo_acceso_concedido.setWindowTitle(self.title)
                        dialogo_acceso_concedido.addButton("Aceptar", 0)
                        dialogo_acceso_concedido.setInformativeText("Bienvenido: "+ self.configuracion_avanzada_user.text()+ "  \n    ")
                        dialogo_acceso_concedido.show()
                        self.ConfiguracionAvanzadaInside()
                    else:
                        dialogo_error_escritura = QMessageBox(self.centralWidget)
                        dialogo_error_escritura.setWindowTitle(self.title)
                        dialogo_error_escritura.addButton("Aceptar", 0)
                        dialogo_error_escritura.setInformativeText("Error, verifique los datos ingresados  \nSi el error persiste comuniquese con el fabricante")
                        dialogo_error_escritura.show()
                else:
                    dialogo_error_typ = QMessageBox(self.centralWidget)
                    dialogo_error_typ.setWindowTitle(self.title)
                    dialogo_error_typ.addButton("Aceptar", 0)
                    dialogo_error_typ.setInformativeText("Error, verifique los datos ingresados     \n")
                    dialogo_error_typ.show()
            else:
                dialogo_error_incompleto = QMessageBox(self.centralWidget)
                dialogo_error_incompleto.setWindowTitle(self.title)
                dialogo_error_incompleto.addButton("Aceptar", 0)
                dialogo_error_incompleto.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto.show()
        except:
            dialogo_error = QMessageBox(self.centralWidget)
            dialogo_error.setWindowTitle(self.title)
            dialogo_error.addButton("Aceptar", 0)
            dialogo_error.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error.show()

    

    

    def Ingresar_desplegar_teclado_numerico_cedula(self):
        self.campo = 'ingresar-cedula'
        self.Ingresar_desplegar_teclado_numerico()

    def Ingresar_desplegar_teclado_numerico_temp(self):
        self.campo = 'ingresar-temp'
        self.Ingresar_desplegar_teclado_numerico()

    def Ingresar_desplegar_teclado_numerico(self):
        MOV = -100
        #movimiento botones
        self.ingresar_nombre.setGeometry(164, 240+MOV, 320, 70)
        self.ingresar_cedula.setGeometry(164,330+MOV,180,70)
        self.ingresar_temp.setGeometry(360,330+MOV,120,70)
        self.ingresar_ingresar.setGeometry(570, 240+MOV, 280, 160)
        self.NotTeclado()
        self.TecladoNumerico()

    def Ingresar_guardar_teclado_numerico(self):
        self.ingresar_nombre.setGeometry(164, 240, 320, 70)
        self.ingresar_cedula.setGeometry(164,330,180,70)
        self.ingresar_temp.setGeometry(360,330,120,70)
        self.ingresar_ingresar.setGeometry(570, 240, 280, 160)
        self.NotTecladoNumerico()

    def Ingresar_desplegar_teclado(self):
        MOV = -100
        #movimiento botones
        self.ingresar_nombre.setGeometry(164, 240+MOV, 320, 70)
        self.ingresar_cedula.setGeometry(164,330+MOV,180,70)
        self.ingresar_temp.setGeometry(360,330+MOV,120,70)
        self.ingresar_ingresar.setGeometry(570, 240+MOV, 280, 160)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'ingresar-nombre'

    def Ingresar_guardar_teclado(self):
        self.ingresar_nombre.setGeometry(164, 240, 320, 70)
        self.ingresar_cedula.setGeometry(164,330,180,70)
        self.ingresar_temp.setGeometry(360,330,120,70)
        self.ingresar_ingresar.setGeometry(570, 240, 280, 160)
        self.NotTeclado()

    def Retirar_desplegar_teclado(self):
        MOV = -100
        #movimiento botones
        self.salida_nombre.setGeometry(164.2,237+MOV,290,70)
        self.salida_cedula.setGeometry(164.2,341+MOV,290,70)
        self.salida_salida.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'retirar-nombre'

    def Retirar_guardar_teclado(self):
        MOV = 0
        #movimiento botones
        self.salida_nombre.setGeometry(164.2,237+MOV,290,70)
        self.salida_cedula.setGeometry(164.2,341+MOV,290,70)
        self.salida_salida.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()

    def Retirar_desplegar_teclado_numerico_cedula(self):
        MOV = -100
        #movimiento botones
        self.salida_nombre.setGeometry(164.2,237+MOV,290,70)
        self.salida_cedula.setGeometry(164.2,341+MOV,290,70)
        self.salida_salida.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'retirar-cedula'

    def Ad_Conf_guardar_teclado(self):
        self.configuracion_avanzada_user.setGeometry(164, 240, 320, 70)
        self.configuracion_avanzada_pass.setGeometry(164,330,320,70)
        self.ingresar_Ad_Conf.setGeometry(570, 240, 280, 160)
        self.NotTeclado()

    def Ad_Conf_desplegar_teclado(self):
        MOV = -100
        #movimiento botones
        self.configuracion_avanzada_user.setGeometry(164.2,237+MOV,290,70)
        self.configuracion_avanzada_pass.setGeometry(164.2,341+MOV,290,70)
        self.ingresar_Ad_Conf.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'AdConf-User'

    def Ad_Conf_desplegar_teclado_numerico(self):
        MOV = -100
        #movimiento botones
        self.configuracion_avanzada_user.setGeometry(164.2,237+MOV,290,70)
        self.configuracion_avanzada_pass.setGeometry(164.2,341+MOV,290,70)
        self.ingresar_Ad_Conf.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()
        self.TecladoNumerico()
        self.campo = 'AdConf-Pass'

    def LabelsBotonesEstadisticas(self):
        self.info_ocupacion_actual = QToolButton(self.centralWidget)
        self.info_ocupacion_actual.setObjectName("button")  # nombre de enlace a css
        self.info_ocupacion_actual.setIcon(QIcon('views/static/icons/icono_capacidad'))  # icono
        self.info_ocupacion_actual.setIconSize(QSize(60, 60))
        self.info_ocupacion_actual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.info_ocupacion_actual.setGeometry(120, 120, 290, 140)
        self.info_ocupacion_actual.setVisible(False)



    def BotonesInformacion(self):
        self.manual_de_usuario = QToolButton(self.centralWidget)
        self.manual_de_usuario.setText('Manual de Usuario')
        self.manual_de_usuario.setObjectName("button")  # nombre de enlace a css
        self.manual_de_usuario.setIcon(QIcon('views/static/icons/icono_manual_usuario'))  # icono
        self.manual_de_usuario.setIconSize(QSize(65, 65))
        self.manual_de_usuario.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.manual_de_usuario.setGeometry(200, 210, 290, 180)
        self.manual_de_usuario.clicked.connect(self.ManualDeUsuario)
        self.manual_de_usuario.setVisible(False)

        self.informacion_fabricante = QToolButton(self.centralWidget)
        self.informacion_fabricante.setText('Información del\nFabricante')
        self.informacion_fabricante.setObjectName("button")  # nombre de enlace a css
        self.informacion_fabricante.setIcon(QIcon('views/static/icons/favicon3'))  # icono
        self.informacion_fabricante.setIconSize(QSize(60, 60))
        self.informacion_fabricante.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion_fabricante.clicked.connect(self.InformacionFabricante)
        self.informacion_fabricante.setGeometry(534, 210, 290, 180)
        self.informacion_fabricante.setVisible(False)

        self.qr_manual = QToolButton(self.centralWidget)
        self.qr_manual.setObjectName("button_trasnparente")  # nombre de enlace a css
        self.qr_manual.setIcon(QIcon('src/views/static/icons/QRDRIVE.png'))  # icono
        self.qr_manual.setIconSize(QSize(300, 300))
        self.qr_manual.setGeometry(self.width/3.5, self.height/5, 400, 400)
        self.qr_manual.setVisible(False)

    def ManualDeUsuario(self):
        self.qr_manual.setVisible(True)

        self.informacion_fabricante.setVisible(False)
        self.manual_de_usuario.setVisible(False)

    def LabelsInformacion(self):
        self.label_texto_info_fab = QLabel(self.centralWidget)
        self.label_texto_info_fab.setObjectName("FabInfo")  # nombre de enlace a css
        self.label_texto_info_fab.setText("                                  GRACIAS POR USAR RETEDECON\n"
                           "\n"
                           "RETEDECON es fabricado por:\n"
                           " - Julián C. Velandia\n"
                           " - Sebastian Cubides\n"
                           " - Jhon B. Muñoz\n"
                           "Con la coolaboración de: \n"
                           " - Diego A. Tibaduiza\n"
                           " - Nestor I. Ospina\n"
                           "Bajo la supervición y sustento de la Unidad De Gestion De La Innovación,\n"
                           "Facultad De Ingeniería (Ingnova), de La Universidad Nacional De Colombia.\n\n"
                           "Si desea contactarse con nosotros puede hacerlo a través de los siguientes medios:\n"
                           " - Celular/Whatsapp: +57 313 8244012\n"
                           " - E-Mail: scubidest@unal.edu.co\n\n"
                           "Versión del Software: 1.0")
        self.label_texto_info_fab.setVisible(False)
        self.img_esquina_2 = QToolButton(self.centralWidget)
        self.img_esquina_2.setGeometry(30, 5, 250, 60)
        self.img_esquina_2.setObjectName("button_home")  # nombre de enlace a css
        self.img_esquina_2.setVisible(False)
        self.img_esquina_2.clicked.connect(self.HomeWindow)

    def InformacionFabricante(self):
        self.informacion_fabricante.setVisible(False)
        self.manual_de_usuario.setVisible(False)
        self.label_texto_info_fab.setVisible(True)
        self.img_esquina_2.setVisible(True)

    def Informacion(self):
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.manual_de_usuario.setVisible(True)
        self.informacion_fabricante.setVisible(True)









#bar
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, facecolor = 'black'):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor=facecolor)#facecolor es el color del fondo del canvas
        #Se instancia FigureCanvas para fig.
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #se llama a la funcion plot()
        self.bar()

    def bar(self):
        #Se agrega un subplot y creo que el 111 define como las dimensiones
        ax = self.figure.add_subplot(111)
        ax.set_xlabel('X-Axis',color ='white')  #Texto de las leyendas y color
        ax.set_ylabel('Y-Axis',color ='white')
        #ax.plot(data, 'r-', color='red') ------> Esto está comentado porque es para añadir una grafica de linea
        #Aca creo los datos de prueba que puse
        a = ['Lunes','Martes','Miercoles','Jueves','Viernes']
        b = [10,10,10,10,5]
        ax.set_facecolor('black') #color fondo de la grafica
        ax.spines['left'].set_color('white')    #pinta la regla de la izquierda
        ax.spines['bottom'].set_color('white')   #pinta la regla de abajo
        ax.tick_params(axis='x', colors='white')    #pinta los valores del eje x
        ax.tick_params(axis='y', colors='white')    #pinta los valores del eje y
        ax.bar(a,b) #Esta funcion crea las barras donde a esta en x y b en y
        self.draw() #Dibuja en el canvas
#pie
class PlotCanvasP(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)  # facecolor es el color del fondo del canvas
        # Se instancia FigureCanvas para fig.
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)#######SUPER IMPORTANTE, ESTE PARÁMETRO CONVIERTE DE VENTANA A OBJETO
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        # se llama a la funcion plot()
        self.pie()
    def pie(self):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        a = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
        b = [10, 10, 10, 10, 5]
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        ax = self.figure.add_subplot(111)
        ax.pie(b, labels=a, autopct='%1.1f%%',shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()