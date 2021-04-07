from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QLineClick import QLineEditClick
from datetime import datetime
from configparser import ConfigParser
import sys
import pandas as pd
import pyqtgraph as pg
import hashlib

class MainWindow(QMainWindow): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("static/styles.css") as f:
            self.setStyleSheet(f.read())

        #First Instances
        #self.df = pd.read_csv('../DB.csv') ESTO TOCABA HACERLO CADA VEZ PORQUE SI NO SOLO LEE UNA VEZ
        self.cedula_cache = ''
        self.carnet = ''
        self.config = ConfigParser()

        'Constants'
        self.title = 'RETEDECON'
        self.width = 1024
        self.height = 600

        self.setMinimumSize(self.width,self.height)    #tamaño mínimo
        self.setMaximumSize(self.width,self.height)  #tamaño máximo
        self.setWindowTitle(self.title)   #titulo
        self.setWindowIcon(QIcon("static/icons/favicon3.png"))   #Favicon

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window") #nombre que enlaza en css
        '''
        Imagen central 
        '''
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(289,-10,1024,600)
        self.pixmap = QPixmap('static/icons/Logo_central.png')   #Imagen central
        self.label_img_central.setPixmap(self.pixmap)
        '''
        Botones de home y logo esquina
        '''
        self.label_img_esquina = QToolButton(self.centralWidget)
        self.label_img_esquina.setGeometry(30,5,250,60)        
        self.label_img_esquina.setObjectName("button_home") #nombre de enlace a css
        #self.label_img_esquina.setIcon(QIcon('static/icons/logo_lateral.png')) #icono
        #self.label_img_esquina.setIconSize(QSize(200,60))
        self.label_img_esquina.clicked.connect(self.HomeWindow)

        #Botones
        self.ingresar = QToolButton(self.centralWidget)
        self.ingresar.setText('INGRESO MANUAL')
        self.ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar.setIcon(QIcon('static/icons/icono_entrar')) #icono
        self.ingresar.setIconSize(QSize(60,60))
        self.ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar.clicked.connect(self.Ingresar)

        self.estadisticas = QToolButton(self.centralWidget)
        self.estadisticas.setText('ESTADISTICAS')
        self.estadisticas.setObjectName("button")
        self.estadisticas.setIcon(QIcon('static/icons/icono_estadisticas'))
        self.estadisticas.setIconSize(QSize(60,60))
        self.estadisticas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.estadisticas.clicked.connect(self.Estadisticas)

        self.detener_alarma = QToolButton(self.centralWidget)
        self.detener_alarma.setText('DETENER ALARMA')
        self.detener_alarma.setObjectName("button")
        self.detener_alarma.setIcon(QIcon('static/icons/icono_campana'))
        self.detener_alarma.setIconSize(QSize(60,60))
        self.detener_alarma.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.detener_alarma.clicked.connect(self.DetenerAlarma)

        self.salida_manual = QToolButton(self.centralWidget)
        self.salida_manual.setText('SALIDA MANUAL')
        self.salida_manual.setObjectName("button")
        self.salida_manual.setIcon(QIcon('static/icons/icono_salir'))
        self.salida_manual.setIconSize(QSize(60,60))
        self.salida_manual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.salida_manual.clicked.connect(self.Salida_manual)

        self.configuracion = QToolButton(self.centralWidget)
        self.configuracion.setText('CONFIGURACIÓN')
        self.configuracion.setObjectName("button")
        self.configuracion.setIcon(QIcon('static/icons/icono_configuraciones'))
        self.configuracion.setIconSize(QSize(70,70))
        self.configuracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion.clicked.connect(self.Configuracion)

        self.informacion = QToolButton(self.centralWidget)
        self.informacion.setText('INFORMACIÓN')
        self.informacion.setObjectName("button")
        self.informacion.setIcon(QIcon('static/icons/icono_info'))
        self.informacion.setIconSize(QSize(50,50))
        self.informacion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion.clicked.connect(self.Informacion)

        'geometrías botones'
        self.ingresar.setGeometry(44.7, 112.5, 290, 180)
        self.estadisticas.setGeometry(367, 112.5, 290, 180)
        self.detener_alarma.setGeometry(689.3, 112.5, 290, 180)
        self.salida_manual.setGeometry(44.7, 348.9, 290, 180)
        self.configuracion.setGeometry(367, 348.9, 290, 180)
        self.informacion.setGeometry(689.3, 348.9, 290, 180)

        'Visibilidad inicial'
        self.label_img_central.setVisible(True)
        self.label_img_esquina.setVisible(False)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

        'timer'
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.HomeWindow) #función a ejecutar pasados los 3 seg

        'cuadros de texto'
        self.ingresar_nombre = QLineEditClick(self.centralWidget)
        self.ingresar_nombre.setPlaceholderText("NOMBRE")
        self.ingresar_nombre.setObjectName("input")  # nombre de enlace a css
        self.ingresar_nombre.setClearButtonEnabled(True)
        self.ingresar_nombre.setGeometry(164, 230, 290, 65)
        self.ingresar_nombre.setMaxLength(40)

        'cuadros de texto 2'
        self.ingresar_cedula = QLineEditClick(self.centralWidget)
        self.ingresar_cedula.setPlaceholderText("CEDULA")
        self.ingresar_cedula.setObjectName("input") #nombre de enlace a css
        self.ingresar_cedula.setClearButtonEnabled(True)
        self.ingresar_cedula.setGeometry(164,313,290,65)
        self.ingresar_cedula.setMaxLength(15)

        'Temperatura'
        self.ingresar_temp = QLineEditClick(self.centralWidget)
        self.ingresar_temp.setPlaceholderText("TEMP")
        self.ingresar_temp.setObjectName("input") #nombre de enlace a css
        self.ingresar_temp.setClearButtonEnabled(True)
        self.ingresar_temp.setGeometry(164,396,290,65)
        self.ingresar_temp.setMaxLength(5)

        'cuadros de texto out'
        self.ingresar_nombre_out = QLineEditClick(self.centralWidget)
        self.ingresar_nombre_out.setPlaceholderText("NOMBRE")
        self.ingresar_nombre_out.setObjectName("input")  # nombre de enlace a css
        self.ingresar_nombre_out.setClearButtonEnabled(True)
        self.ingresar_nombre_out.setGeometry(164, 237, 290, 70)
        self.ingresar_nombre_out.setMaxLength(40)

        'cuadros de texto out 2'
        self.ingresar_cedula_out = QLineEditClick(self.centralWidget)
        self.ingresar_cedula_out.setPlaceholderText("CEDULA")
        self.ingresar_cedula_out.setObjectName("input")  # nombre de enlace a css
        self.ingresar_cedula_out.setClearButtonEnabled(True)
        self.ingresar_cedula_out.setGeometry(164, 341, 290, 70)
        self.ingresar_cedula_out.setMaxLength(15)

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

        #Botones Ingresar
        self.BotonesIngresar()
        # Botones Salida Manual
        self.BotonesSalidaManual()
        #botones teclados
        self.BotonesTeclado()
        self.BotonesTecladoNumerico()
        #AccionClcikIngresarNombre
        self.ingresar_nombre.clicked.connect(self.Ingresar_desplegar_teclado)
        #AccionClcikIngresarCedula
        self.ingresar_cedula.clicked.connect(self.Ingresar_desplegar_teclado_numerico_cedula)
        #AccionIngresarTemperatura
        self.ingresar_temp.clicked.connect(self.Ingresar_desplegar_teclado_numerico_temp)
        #AccionClcikIngresarNombreOut
        self.ingresar_nombre_out.clicked.connect(self.Retirar_desplegar_teclado)
        #AccionClcikIngresarCedulaOut
        self.ingresar_cedula_out.clicked.connect(self.Retirar_desplegar_teclado_numerico_cedula)
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


        

    def HomeWindow(self):
        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(True)
        self.estadisticas.setVisible(True)
        self.detener_alarma.setVisible(True)
        self.salida_manual.setVisible(True)
        self.configuracion.setVisible(True)
        self.informacion.setVisible(True)
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.ingresar_ingresar.setVisible(False)
        self.retirar.setVisible(False)
        self.configuracion_apagar.setVisible(False)
        self.configuracion_pantalla.setVisible(False)
        self.configuracion_datos.setVisible(False)
        self.configuracion_capacidad_text.setVisible(False)
        self.configuracion_avanzada_user.setVisible(False)
        self.configuracion_avanzada_pass.setVisible(False)
        self.configuracion_avanzada.setVisible(False)
        self.ingresar_Ad_Conf.setVisible(False)
        self.configuracion_capacidad.setVisible(False)
        self.new_admin_username.setVisible(False)
        self.new_admin_password.setVisible(False)
        self.new_admin.setVisible(False)
        self.quitar_admin.setVisible(False)
        self.manual_de_usuario.setVisible(False)
        self.informacion_fabricante.setVisible(False)
        self.label_texto_info_fab.setVisible(False)
        self.img_esquina_2.setVisible(False)
        self.ingresar_capacidad.setVisible(False)
        self.agregar_eliminar_admin_boton.setVisible(False)
        self.cambiar_password_admin_boton.setVisible(False)
        self.enviar_datos_servidor.setVisible(False)
        self.info_ocupacion_actual.setVisible(False)
        self.qr_manual.setVisible(False)
        self.NotTeclado()
        self.NotTecladoNumerico()

    def Ingresar(self):
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.ingresar_nombre.setVisible(True)
        self.ingresar_nombre.clear()
        self.ingresar_cedula.setVisible(True)
        self.ingresar_cedula.clear()
        self.ingresar_temp.setVisible(True)
        self.ingresar_temp.clear()
        self.ingresar_ingresar.setVisible(True)
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.retirar.setVisible(False)
        self.Ingresar_guardar_teclado()

    def BotonesConfig(self):
        self.configuracion_avanzada = QToolButton(self.centralWidget)
        self.configuracion_avanzada.setText('Configuración Avanzada\n(Administrador)')
        self.configuracion_avanzada.setObjectName("button") #nombre de enlace a css
        self.configuracion_avanzada.setIcon(QIcon('static/icons/icono_config_avanzada')) #icono
        self.configuracion_avanzada.setIconSize(QSize(65,65))
        self.configuracion_avanzada.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_avanzada.setGeometry(534, 120, 290, 180)
        self.configuracion_avanzada.clicked.connect(self.ConfiguracionAvanzada)
        self.configuracion_avanzada.setVisible(False)

        self.configuracion_apagar = QToolButton(self.centralWidget)
        self.configuracion_apagar.setText('Apagar')
        self.configuracion_apagar.setObjectName("button") #nombre de enlace a css
        self.configuracion_apagar.setIcon(QIcon('static/icons/icono_apagar')) #icono
        self.configuracion_apagar.setIconSize(QSize(60,60))
        self.configuracion_apagar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_apagar.clicked.connect(self.Apagar)
        self.configuracion_apagar.setGeometry(534, 340, 290, 180)
        self.configuracion_apagar.setVisible(False)

        self.configuracion_pantalla = QToolButton(self.centralWidget)
        self.configuracion_pantalla.setText('Ajustes de Pantallas')
        self.configuracion_pantalla.setObjectName("button")  # nombre de enlace a css
        self.configuracion_pantalla.setIcon(QIcon('static/icons/icono_config_pantalla'))  # icono
        self.configuracion_pantalla.setIconSize(QSize(60, 60))
        self.configuracion_pantalla.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_pantalla.clicked.connect(self.HomeWindow)
        self.configuracion_pantalla.setGeometry(200, 120, 290, 180)
        self.configuracion_pantalla.setVisible(False)

        self.configuracion_datos = QToolButton(self.centralWidget)
        self.configuracion_datos.setText('Cambiar Estilo De Gráfica\nDe Datos')
        self.configuracion_datos.setObjectName("button")  # nombre de enlace a css
        self.configuracion_datos.setIcon(QIcon('static/icons/icono_estadisticas'))  # icono
        self.configuracion_datos.setIconSize(QSize(70, 70))
        self.configuracion_datos.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_datos.clicked.connect(self.HomeWindow)
        self.configuracion_datos.setGeometry(200, 340, 290, 180)
        self.configuracion_datos.setVisible(False)

    def BotonesIngresar(self):
        self.ingresar_ingresar = QToolButton(self.centralWidget)
        self.ingresar_ingresar.setText('INGRESAR')
        self.ingresar_ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar_ingresar.setIcon(QIcon('static/icons/icono_entrar')) #icono
        self.ingresar_ingresar.setIconSize(QSize(60,60))
        self.ingresar_ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar_ingresar.clicked.connect(self.Escribir)
        self.ingresar_ingresar.setGeometry(570, 230, 290, 231)
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.ingresar_ingresar.setVisible(False)

    def BotonesSalidaManual(self):
        self.retirar = QToolButton(self.centralWidget)
        self.retirar.setText('RETIRAR')
        self.retirar.setObjectName("button") #nombre de enlace a css
        self.retirar.setIcon(QIcon('static/icons/icono_salir')) #icono
        self.retirar.setIconSize(QSize(60,60))
        self.retirar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.retirar.clicked.connect(self.Leer)
        self.retirar.setGeometry(570, 237, 290, 176.3)
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.retirar.setVisible(False)

    def BotonesNewAdmin(self):
        'crear new admin'
        self.new_admin = QToolButton(self.centralWidget)
        self.new_admin.setText('REGISTRAR')
        self.new_admin.setObjectName("button") #nombre de enlace a css
        self.new_admin.setIcon(QIcon('static/icons/icono_entrar')) #icono
        self.new_admin.setIconSize(QSize(60,60))
        self.new_admin.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.new_admin.setGeometry(570, 150, 290, 180)
        self.new_admin.clicked.connect(self.NewAdmin)
        self.new_admin.setVisible(False)

        self.quitar_admin = QToolButton(self.centralWidget)
        self.quitar_admin.setText('ELIMINAR')
        self.quitar_admin.setObjectName("button")  # nombre de enlace a css
        self.quitar_admin.setIcon(QIcon('static/icons/icono_salir'))  # icono
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
        self.ingresar_capacidad.setIcon(QIcon('static/icons/icono_capacidad'))  # icono
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
        self.ingresar_Ad_Conf.setIcon(QIcon('static/icons/icono_entrar'))  # icono
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
        self.configuracion_capacidad.setIcon(QIcon('static/icons/icono_capacidad'))  # icono
        self.configuracion_capacidad.setIconSize(QSize(60, 60))
        self.configuracion_capacidad.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion_capacidad.clicked.connect(self.Capacidad)
        self.configuracion_capacidad.setGeometry(534, 340, 290, 180)
        self.configuracion_capacidad.setVisible(False)
        
        self.agregar_eliminar_admin_boton = QToolButton(self.centralWidget)
        self.agregar_eliminar_admin_boton.setText('Agregar o Eliminar\nAdministrador')
        self.agregar_eliminar_admin_boton.setObjectName("button")  # nombre de enlace a css
        self.agregar_eliminar_admin_boton.setIcon(QIcon('static/icons/icono_add_delete_admin'))  # icono
        self.agregar_eliminar_admin_boton.setIconSize(QSize(60, 60))
        self.agregar_eliminar_admin_boton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.agregar_eliminar_admin_boton.clicked.connect(self.AgregarAdmin)
        self.agregar_eliminar_admin_boton.setGeometry(200, 120, 290, 180)
        self.agregar_eliminar_admin_boton.setVisible(False)

        self.cambiar_password_admin_boton = QToolButton(self.centralWidget)
        self.cambiar_password_admin_boton.setText('Cambiar contraseña')
        self.cambiar_password_admin_boton.setObjectName("button")  # nombre de enlace a css
        self.cambiar_password_admin_boton.setIcon(QIcon('static/icons/icono_capacidad'))  # icono
        self.cambiar_password_admin_boton.setIconSize(QSize(60, 60))
        self.cambiar_password_admin_boton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.cambiar_password_admin_boton.clicked.connect(self.HomeWindow)
        self.cambiar_password_admin_boton.setGeometry(200, 340, 290, 180)
        self.cambiar_password_admin_boton.setVisible(False)

        self.enviar_datos_servidor = QToolButton(self.centralWidget)
        self.enviar_datos_servidor.setText('Enviar Datos Al Servidor')
        self.enviar_datos_servidor.setObjectName("button")  # nombre de enlace a css
        self.enviar_datos_servidor.setIcon(QIcon('static/icons/icono_config_datos'))  # icono
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

    def restar_deltas(self,HoraOut,HoraIn):
        '''
        Devuelve la diferencia en minutos
        '''
        #Ojo, si las fechas son distintas pueden haber problemas
        Fecha_Hoy = datetime.today().strftime('%d-%m-%Y')
        #Fecha = Fecha.split(':')
        HoraOut= HoraOut.split(':')
        HoraIn= HoraIn.split(':')

        #Tiempo total en minutos
        if not Fecha_Hoy=="aaa":
            NumOut=int(HoraOut[0])*60+int(HoraOut[1])
            NumIn=int(HoraIn[0])*60+int(HoraIn[1])

            delta = NumOut-NumIn
            return str(delta)
        else:
            dialogo_error_fecha = QMessageBox(self.centralWidget)
            dialogo_error_fecha.setWindowTitle(self.title)
            dialogo_error_fecha.addButton("Aceptar", 0)
            dialogo_error_fecha.setInformativeText("Ha ocurrido un error al verifcar    \nlas fechas, si persiste comuniquese   \n  con el fabricante \n    ")
            dialogo_error_fecha.show()
    '''
    Acá leemos la base de datos para procesar y o modificar la informacion
    '''
    def Leer(self):
        try:
            df = pd.read_csv('../DB.csv')
            Lista = df['Cedula']
            self.carnet = '*'
            self.HoraOut = datetime.today().strftime('%H:%M')
            if self.ingresar_nombre_out.text()!="" and self.ingresar_cedula_out.text()!="":  #lógica para leer si los campos están vacíos
                if not self.ingresar_nombre_out.text().isdigit() and not self.ingresar_cedula_out.text().isalpha():  #detecta si numeros o letras donde no deben
                    flag = True
                    if str(df['Cedula'][0]) == str(self.ingresar_cedula_out.text()) and str(df['IsIn'][0]) == 'True':
                        flag = False
                        self.df_as_txt = open ("../DB.csv", "r")
                        lineas = self.df_as_txt.readlines()
                        self.df_as_txt.close()
                        lineas[1] = lineas[1].replace('HO*',self.HoraOut).replace('D*',self.restar_deltas(self.HoraOut,df['HoraIn'][0])).replace('True','False')
                        print(lineas[1])
                        self.df_as_txt = open("../DB.csv", "w")
                        for l in lineas:
                            self.df_as_txt.write(l)
                        self.df_as_txt.close()
                        #Confirmacion
                        dialogo_exitoso = QMessageBox(self.centralWidget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha retirado correctamente\n    ")
                        dialogo_exitoso.show()
                        self.HomeWindow()

                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == str(self.ingresar_cedula_out.text()) and str(df['IsIn'][ced]) == 'True':
                            flag =False
                            self.df_as_txt = open ("../DB.csv", "r")
                            lineas = self.df_as_txt.readlines()
                            self.df_as_txt.close()
                            lineas[ced+1] = lineas[ced+1].replace('HO*',self.HoraOut).replace('D*',self.restar_deltas(self.HoraOut,df['HoraIn'][ced])).replace('True','False')
                            self.df_as_txt = open("../DB.csv", "w")
                            for l in lineas:
                                self.df_as_txt.write(l)
                            self.df_as_txt.close()
                            #Confirmacion
                            dialogo_exitoso = QMessageBox(self.centralWidget)
                            dialogo_exitoso.setWindowTitle(self.title)
                            dialogo_exitoso.addButton("Aceptar", 0)
                            dialogo_exitoso.setInformativeText("Se ha retirado correctamente\n    ")
                            dialogo_exitoso.show()
                            self.HomeWindow()
                    if flag:
                        dialogo_error_busqueda = QMessageBox(self.centralWidget)
                        dialogo_error_busqueda.setWindowTitle(self.title)
                        dialogo_error_busqueda.addButton("Aceptar", 0)
                        dialogo_error_busqueda.setInformativeText("Error, no se encontró a ese usuario\n    ")
                        dialogo_error_busqueda.show()
                else:
                    dialogo_error_typ_out = QMessageBox(self.centralWidget)
                    dialogo_error_typ_out.setWindowTitle(self.title)
                    dialogo_error_typ_out.addButton("Aceptar", 0)
                    dialogo_error_typ_out.setInformativeText("Error, verifique los datos ingresados\n   ")
                    dialogo_error_typ_out.show()
            else:
                dialogo_error_incompleto_out = QMessageBox(self.centralWidget)
                dialogo_error_incompleto_out.setWindowTitle(self.title)
                dialogo_error_incompleto_out.addButton("Aceptar", 0)
                dialogo_error_incompleto_out.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto_out.show()
        except:
            dialogo_error_lectura = QMessageBox(self.centralWidget)
            dialogo_error_lectura.setWindowTitle(self.title)
            dialogo_error_lectura.addButton("Aceptar", 0)
            dialogo_error_lectura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error_lectura.show()

    def Escribir(self):
        #if not IsIn:
        #definimos la fecha y hora
        cedula= str(self.ingresar_cedula.text())
        carnet = '*' #Entra por arduino
        temp= str(self.ingresar_temp.text())
        self.Fecha = datetime.today().strftime('%d-%m-%Y')
        self.HoraIn = datetime.today().strftime('%H:%M')
        self.HoraOut = 'HO*'
        self.Delta = 'D*'
        self.Numingresos = 0 #Se inicia en 0
        self.IsIn = 'True'
        cedulaExist=False
        try:
            df = pd.read_csv('../DB.csv')
            Lista = df['Cedula']
            Lista_carnet = df['Carnet']
            '''
            Suma ingresos    MOVER DE ACÁ AL LUGAR CORRECTO!
            '''
            for cont in range(len(Lista)):
                if (str(Lista_carnet[cont]) == str(self.carnet) and not str(self.carnet) == '*') or str(Lista[cont]) == str(self.ingresar_cedula.text()):
                    self.Numingresos+=1
            self.Numingresos=str(self.Numingresos)
            print(self.Numingresos)

            if self.ingresar_nombre.text()!="" and self.ingresar_cedula.text()!="" and self.ingresar_temp.text()!="":  #lógica para leer si los campos están vacíos
                if not self.ingresar_nombre.text().isdigit() and not self.ingresar_cedula.text().isalpha() and not self.ingresar_temp.text().isalpha():  #detecta si numeros o letras donde no deben
                    # mirar si la cédula ya existe
                    # Recorrido del arreglo
                    if str(df['Cedula'][0]) == str(self.ingresar_cedula.text()) and str(df['IsIn'][0]) == 'True':
                        cedulaExist = True
                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(df['Cedula'][ced]) == str(self.ingresar_cedula.text()) and str(df['IsIn'][ced]) == 'True':
                            cedulaExist = True

                    if not cedulaExist:
                        self.df_as_txt = open ("../DB.csv", "a")
                        #ParaPandas
                        #Enviar vector persona a DB
                        persona = '\n'+self.ingresar_nombre.text()+','+cedula+','+carnet+','+temp+','+self.Fecha+','+self.HoraIn+','+self.HoraOut+','+self.Delta+','+self.Numingresos+','+self.IsIn
                        self.df_as_txt.write(persona)
                        self.df_as_txt.close()
                        dialogo_exitoso = QMessageBox(self.centralWidget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha ingresado correctamente   \n")
                        dialogo_exitoso.show()
                        self.HomeWindow()
                    else:
                        dialogo_error_cedulaExistente = QMessageBox(self.centralWidget)
                        dialogo_error_cedulaExistente.setWindowTitle(self.title)
                        dialogo_error_cedulaExistente.addButton("Aceptar", 0)
                        dialogo_error_cedulaExistente.setInformativeText("El usuario ya está adentro    \n")
                        dialogo_error_cedulaExistente.show()
                else:
                    dialogo_error_typ = QMessageBox(self.centralWidget)
                    dialogo_error_typ.setWindowTitle(self.title)
                    dialogo_error_typ.addButton("Aceptar", 0)
                    dialogo_error_typ.setInformativeText("Error, verifique los datos ingresados\n   ")
                    dialogo_error_typ.show()
            else:
                dialogo_error_incompleto = QMessageBox(self.centralWidget)
                dialogo_error_incompleto.setWindowTitle(self.title)
                dialogo_error_incompleto.addButton("Aceptar", 0)
                dialogo_error_incompleto.setInformativeText("Debe llenar todos los campos\nantes de continuar")
                dialogo_error_incompleto.show()
        except:
            dialogo_error_escritura = QMessageBox(self.centralWidget)
            dialogo_error_escritura.setWindowTitle(self.title)
            dialogo_error_escritura.addButton("Aceptar", 0)
            dialogo_error_escritura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
            dialogo_error_escritura.show()

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
        self.ingresar_nombre_out.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula_out.setGeometry(164.2,341+MOV,290,70)
        self.retirar.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()
        self.NotTecladoNumerico()
        self.campo = 'retirar-nombre'

    def Retirar_guardar_teclado(self):
        MOV = 0
        #movimiento botones
        self.ingresar_nombre_out.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula_out.setGeometry(164.2,341+MOV,290,70)
        self.retirar.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()

    def Retirar_desplegar_teclado_numerico_cedula(self):
        MOV = -100
        #movimiento botones
        self.ingresar_nombre_out.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula_out.setGeometry(164.2,341+MOV,290,70)
        self.retirar.setGeometry(570, 237+MOV, 290, 176.3)
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
        self.info_ocupacion_actual.setIcon(QIcon('static/icons/icono_capacidad'))  # icono
        self.info_ocupacion_actual.setIconSize(QSize(60, 60))
        self.info_ocupacion_actual.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.info_ocupacion_actual.setGeometry(120, 120, 290, 140)
        self.info_ocupacion_actual.setVisible(False)

    def Estadisticas(self):
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.info_ocupacion_actual.setVisible(True)
        df = pd.read_csv('../DB.csv')
        Lista = df['IsIn']
        print(Lista)
        self.ocupacion_actual =0
        for i in Lista:
            if i == True:
                self.ocupacion_actual +=1
        print('Ocupacion Actual: '+str(self.ocupacion_actual))


        self.info_ocupacion_actual.setText('Ocupación Actual: ' + str(self.ocupacion_actual))
        #ACÁ CREA LA GRAFICA PERO POR EL MOMENTO LO HACE EN UNA VENTANA NUEVA
        
        '''
        self.win = pg.plot()
        #win.setWindowTitle('pyqtgraph BarGraphItem')
        # create list of floats
        y1 = np.array([0.10,0.20,0.10])
        print(type(y1))
        # create horizontal list
        x1 = np.arange(10)
        pre_x = []
        fechas_unicas = set(df['Fecha'])
        for i in fechas_unicas:
            fecha_normalizada = i.replace('-','').replace('2021','')
            pre_x.append(float(fecha_normalizada))
        x = np.array(pre_x)
        print(type(x))
        print(x)
        x = np.arange(3)
        

        '''
        x = []
        y = []
        fechas_unicas = set(df['Fecha'])
        for i in fechas_unicas:
            x.append(i)
        x.sort()

        cont_fecha = 0
        for unica in x:
            for fecha in range(len(Lista)):
                if unica == df['Fecha'][fecha]:
                    
                    cont_fecha +=1
            y.append(cont_fecha)
            cont_fecha = 0
        
        print(x)
        print(y)

        xdict = dict(enumerate(x))


        

        self.win = pg.GraphicsWindow()
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        plot = self.win.addPlot(axisItems={'bottom': stringaxis})
        curve = plot.plot(list(xdict.keys()),y)
        bg1 = pg.BarGraphItem(x=plot, height=y, width=0.6, brush='r')

        self.win.addItem(curve)


        # create bar chart
        #bg1 = pg.BarGraphItem(x=x, height=y1, width=0.6, brush='r')
        #self.win.addItem(bg1)
        ##

    def DetenerAlarma(self):
        self.stop = 1
        print(self.stop)
        self.HomeWindow()

    def Salida_manual(self):
        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.ingresar_nombre_out.setVisible(True)
        self.ingresar_nombre_out.clear()
        self.ingresar_cedula_out.setVisible(True)
        self.ingresar_cedula_out.clear()
        self.retirar.setVisible(True)
        self.ingresar_ingresar.setVisible(False)
        self.Retirar_guardar_teclado()

    def Configuracion(self):
        self.configuracion_apagar.setVisible(True)
        self.configuracion_pantalla.setVisible(True)
        self.configuracion_datos.setVisible(True)
        self.configuracion_avanzada.setVisible(True)
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

    def BotonesInformacion(self):
        self.manual_de_usuario = QToolButton(self.centralWidget)
        self.manual_de_usuario.setText('Manual de Usuario')
        self.manual_de_usuario.setObjectName("button")  # nombre de enlace a css
        self.manual_de_usuario.setIcon(QIcon('static/icons/icono_manual_usuario'))  # icono
        self.manual_de_usuario.setIconSize(QSize(65, 65))
        self.manual_de_usuario.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.manual_de_usuario.setGeometry(200, 210, 290, 180)
        self.manual_de_usuario.clicked.connect(self.ManualDeUsuario)
        self.manual_de_usuario.setVisible(False)

        self.informacion_fabricante = QToolButton(self.centralWidget)
        self.informacion_fabricante.setText('Información del\nFabricante')
        self.informacion_fabricante.setObjectName("button")  # nombre de enlace a css
        self.informacion_fabricante.setIcon(QIcon('static/icons/favicon3'))  # icono
        self.informacion_fabricante.setIconSize(QSize(60, 60))
        self.informacion_fabricante.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.informacion_fabricante.clicked.connect(self.InformacionFabricante)
        self.informacion_fabricante.setGeometry(534, 210, 290, 180)
        self.informacion_fabricante.setVisible(False)

        self.qr_manual = QToolButton(self.centralWidget)
        self.qr_manual.setObjectName("button_trasnparente")  # nombre de enlace a css
        self.qr_manual.setIcon(QIcon('static/icons/QRDRIVE.png'))  # icono
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

    def BotonesTecladoNumerico(self):
        sep_lado = 12
        sep_arriba = 12
        base = 73
        altura = 65
        y_inicia = 350
        x_inicia =300

        x=0
        y=0
        self.numero_7 = QToolButton(self.centralWidget)
        self.numero_7.setText('7')
        self.numero_7.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_7.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_7.clicked.connect(self.fun_numero_7)

        x=1
        y=0
        self.numero_8 = QToolButton(self.centralWidget)
        self.numero_8.setText('8')
        self.numero_8.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_8.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_8.clicked.connect(self.fun_numero_8)

        x=2
        y=0
        self.numero_9 = QToolButton(self.centralWidget)
        self.numero_9.setText('9')
        self.numero_9.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_9.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_9.clicked.connect(self.fun_numero_9)

        x=3
        y=0
        self.numero_BORRAR = QToolButton(self.centralWidget)
        self.numero_BORRAR.setText('Borrar')
        self.numero_BORRAR.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_BORRAR.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base*2+sep_lado, altura)
        self.numero_BORRAR.clicked.connect(self.fun_numero_BORRAR)

        x=0
        y=1
        self.numero_4 = QToolButton(self.centralWidget)
        self.numero_4.setText('4')
        self.numero_4.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_4.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_4.clicked.connect(self.fun_numero_4)

        x=1
        y=1
        self.numero_5 = QToolButton(self.centralWidget)
        self.numero_5.setText('5')
        self.numero_5.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_5.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_5.clicked.connect(self.fun_numero_5)

        x=2
        y=1
        self.numero_6 = QToolButton(self.centralWidget)
        self.numero_6.setText('6')
        self.numero_6.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_6.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_6.clicked.connect(self.fun_numero_6)

        x=3
        y=1
        self.numero_PUNTO = QToolButton(self.centralWidget)
        self.numero_PUNTO.setText('.')
        self.numero_PUNTO.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_PUNTO.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_PUNTO.clicked.connect(self.fun_numero_PUNTO)

        x=4
        y=1
        self.numero_ENTER = QToolButton(self.centralWidget)
        self.numero_ENTER.setText(chr(16))
        self.numero_ENTER.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_ENTER.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura*2+sep_arriba)
        self.numero_ENTER.clicked.connect(self.fun_numero_ENTER)

        x=0
        y=2
        self.numero_1 = QToolButton(self.centralWidget)
        self.numero_1.setText('1')
        self.numero_1.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_1.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_1.clicked.connect(self.fun_numero_1)
        
        x=1
        y=2
        self.numero_2 = QToolButton(self.centralWidget)
        self.numero_2.setText('2')
        self.numero_2.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_2.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_2.clicked.connect(self.fun_numero_2)

        x=2
        y=2
        self.numero_3 = QToolButton(self.centralWidget)
        self.numero_3.setText('3')
        self.numero_3.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_3.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_3.clicked.connect(self.fun_numero_3)

        x=3
        y=2
        self.numero_0 = QToolButton(self.centralWidget)
        self.numero_0.setText('0')
        self.numero_0.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_0.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_0.clicked.connect(self.fun_numero_0)

        self.NotTecladoNumerico()

    def BotonesTeclado(self):
        sep_lado = 12
        sep_arriba = 12
        base = 73
        altura = 65
        y_inicia = 350
        
        x=0
        y=0
        self.letra_q = QToolButton(self.centralWidget)
        self.letra_q.setText('q')
        self.letra_q.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_q.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_q.clicked.connect(self.q)
        

        x=1
        y=0
        self.letra_w = QToolButton(self.centralWidget)
        self.letra_w.setText('w')
        self.letra_w.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_w.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_w.clicked.connect(self.w)
        

        x=2
        y=0
        self.letra_e = QToolButton(self.centralWidget)
        self.letra_e.setText('e')
        self.letra_e.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_e.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_e.clicked.connect(self.e)
        
        x=3
        y=0
        self.letra_r = QToolButton(self.centralWidget)
        self.letra_r.setText('r')
        self.letra_r.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_r.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_r.clicked.connect(self.r)

        x=4
        y=0
        self.letra_t = QToolButton(self.centralWidget)
        self.letra_t.setText('t')
        self.letra_t.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_t.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_t.clicked.connect(self.t)

        x=5
        y=0
        self.letra_y = QToolButton(self.centralWidget)
        self.letra_y.setText('y')
        self.letra_y.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_y.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_y.clicked.connect(self.y)

        x=6
        y=0
        self.letra_u = QToolButton(self.centralWidget)
        self.letra_u.setText('u')
        self.letra_u.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_u.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_u.clicked.connect(self.u)

        x=7
        y=0
        self.letra_i = QToolButton(self.centralWidget)
        self.letra_i.setText('i')
        self.letra_i.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_i.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_i.clicked.connect(self.i)

        x=8
        y=0
        self.letra_o = QToolButton(self.centralWidget)
        self.letra_o.setText('o')
        self.letra_o.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_o.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_o.clicked.connect(self.o)

        x=9
        y=0
        self.letra_p = QToolButton(self.centralWidget)
        self.letra_p.setText('p')
        self.letra_p.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_p.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_p.clicked.connect(self.p)

        x=10
        y=0
        self.letra_BORRAR = QToolButton(self.centralWidget)
        self.letra_BORRAR.setText('Borrar')
        self.letra_BORRAR.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_BORRAR.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base*2, altura)
        self.letra_BORRAR.clicked.connect(self.BORRAR)

        x=0
        y=1
        self.letra_a = QToolButton(self.centralWidget)
        self.letra_a.setText('a')
        self.letra_a.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_a.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_a.clicked.connect(self.a)

        x=1
        y=1
        self.letra_s = QToolButton(self.centralWidget)
        self.letra_s.setText('s')
        self.letra_s.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_s.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_s.clicked.connect(self.s)

        x=2
        y=1
        self.letra_d = QToolButton(self.centralWidget)
        self.letra_d.setText('d')
        self.letra_d.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_d.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_d.clicked.connect(self.d)

        x=3
        y=1
        self.letra_f = QToolButton(self.centralWidget)
        self.letra_f.setText('f')
        self.letra_f.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_f.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_f.clicked.connect(self.f)

        x=4
        y=1
        self.letra_g = QToolButton(self.centralWidget)
        self.letra_g.setText('g')
        self.letra_g.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_g.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_g.clicked.connect(self.g)

        x=5
        y=1
        self.letra_h = QToolButton(self.centralWidget)
        self.letra_h.setText('h')
        self.letra_h.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_h.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_h.clicked.connect(self.h)

        x=6
        y=1
        self.letra_j = QToolButton(self.centralWidget)
        self.letra_j.setText('j')
        self.letra_j.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_j.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_j.clicked.connect(self.j)

        x=7
        y=1
        self.letra_k = QToolButton(self.centralWidget)
        self.letra_k.setText('k')
        self.letra_k.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_k.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_k.clicked.connect(self.k)

        x=8
        y=1
        self.letra_l = QToolButton(self.centralWidget)
        self.letra_l.setText('l')
        self.letra_l.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_l.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_l.clicked.connect(self.l)

        x=9
        y=1
        self.letra_ene = QToolButton(self.centralWidget)
        self.letra_ene.setText('ñ')
        self.letra_ene.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_ene.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_ene.clicked.connect(self.ene)

        x=10
        y=1
        self.letra_MAYUS = QToolButton(self.centralWidget)
        self.letra_MAYUS.setText('Mayus')
        self.letra_MAYUS.setObjectName("buttonTecladoMAYUS") #nombre de enlace a css
        self.letra_MAYUS.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base*2, altura)
        self.letra_MAYUS.clicked.connect(self.MAYUS)
        self.isMAYUS=False

        x=0
        y=2
        self.letra_z = QToolButton(self.centralWidget)
        self.letra_z.setText('z')
        self.letra_z.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_z.setGeometry((base*x) + (x+1)*sep_lado, y_inicia + (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_z.clicked.connect(self.z)
        

        x=1
        y=2
        self.letra_x = QToolButton(self.centralWidget)
        self.letra_x.setText('x')
        self.letra_x.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_x.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_x.clicked.connect(self.x)
        

        x=2
        y=2
        self.letra_c = QToolButton(self.centralWidget)
        self.letra_c.setText('c')
        self.letra_c.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_c.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_c.clicked.connect(self.c)
        
        x=3
        y=2
        self.letra_v = QToolButton(self.centralWidget)
        self.letra_v.setText('v')
        self.letra_v.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_v.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_v.clicked.connect(self.v)

        x=7
        y=2
        self.letra_SPACE = QToolButton(self.centralWidget)
        self.letra_SPACE.setText('')
        self.letra_SPACE.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_SPACE.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba,2*sep_lado+ 4*base, altura)
        self.letra_SPACE.clicked.connect(self.SPACE)

        x=4
        y=2
        self.letra_b = QToolButton(self.centralWidget)
        self.letra_b.setText('b')
        self.letra_b.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_b.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_b.clicked.connect(self.b)

        x=5
        y=2
        self.letra_n = QToolButton(self.centralWidget)
        self.letra_n.setText('n')
        self.letra_n.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_n.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_n.clicked.connect(self.n)

        x=6
        y=2
        self.letra_m = QToolButton(self.centralWidget)
        self.letra_m.setText('m')
        self.letra_m.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_m.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_m.clicked.connect(self.m)

        x=11
        y=2
        self.letra_ENTER = QToolButton(self.centralWidget)
        self.letra_ENTER.setText(chr(25))
        self.letra_ENTER.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_ENTER.setGeometry((base*x) + (x+1)*sep_lado-sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_ENTER.clicked.connect(self.ENTER)

        self.NotTeclado()

    def q(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'q'
            else:
                texto = self.ingresar_nombre.text() + 'Q'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'q'
            else:
                texto = self.ingresar_nombre_out.text() + 'Q'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'q'
            else:
                texto = self.configuracion_avanzada_user.text() + 'Q'
            self.configuracion_avanzada_user.setText(texto)

    def w(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'w'
            else:
                texto = self.ingresar_nombre.text() + 'W'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'w'
            else:
                texto = self.ingresar_nombre_out.text() + 'W'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'w'
            else:
                texto = self.configuracion_avanzada_user.text() + 'W'
            self.configuracion_avanzada_user.setText(texto)

    def e(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'e'
            else:
                texto = self.ingresar_nombre.text() + 'E'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'e'
            else:
                texto = self.ingresar_nombre_out.text() + 'E'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'e'
            else:
                texto = self.configuracion_avanzada_user.text() + 'E'
            self.configuracion_avanzada_user.setText(texto)

    def r(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'r'
            else:
                texto = self.ingresar_nombre.text() + 'R'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'r'
            else:
                texto = self.ingresar_nombre_out.text() + 'R'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'r'
            else:
                texto = self.configuracion_avanzada_user.text() + 'R'
            self.configuracion_avanzada_user.setText(texto)

    def t(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 't'
            else:
                texto = self.ingresar_nombre.text() + 'T'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 't'
            else:
                texto = self.ingresar_nombre_out.text() + 'T'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 't'
            else:
                texto = self.configuracion_avanzada_user.text() + 'T'
            self.configuracion_avanzada_user.setText(texto)

    def y(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'y'
            else:
                texto = self.ingresar_nombre.text() + 'Y'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'y'
            else:
                texto = self.ingresar_nombre_out.text() + 'Y'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'y'
            else:
                texto = self.configuracion_avanzada_user.text() + 'Y'
            self.configuracion_avanzada_user.setText(texto)
    
    def u(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'u'
            else:
                texto = self.ingresar_nombre.text() + 'U'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'u'
            else:
                texto = self.ingresar_nombre_out.text() + 'U'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'u'
            else:
                texto = self.configuracion_avanzada_user.text() + 'U'
            self.configuracion_avanzada_user.setText(texto)

    def i(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'i'
            else:
                texto = self.ingresar_nombre.text() + 'I'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'i'
            else:
                texto = self.ingresar_nombre_out.text() + 'I'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'i'
            else:
                texto = self.configuracion_avanzada_user.text() + 'I'
            self.configuracion_avanzada_user.setText(texto)

    def o(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'o'
            else:
                texto = self.ingresar_nombre.text() + 'O'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'o'
            else:
                texto = self.ingresar_nombre_out.text() + 'O'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'o'
            else:
                texto = self.configuracion_avanzada_user.text() + 'O'
            self.configuracion_avanzada_user.setText(texto)

    def p(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'p'
            else:
                texto = self.ingresar_nombre.text() + 'P'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'p'
            else:
                texto = self.ingresar_nombre_out.text() + 'P'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'p'
            else:
                texto = self.configuracion_avanzada_user.text() + 'P'
            self.configuracion_avanzada_user.setText(texto)

    def a(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'a'
            else:
                texto = self.ingresar_nombre.text() + 'A'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'a'
            else:
                texto = self.ingresar_nombre_out.text() + 'A'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'a'
            else:
                texto = self.configuracion_avanzada_user.text() + 'A'
            self.configuracion_avanzada_user.setText(texto)

    def s(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 's'
            else:
                texto = self.ingresar_nombre.text() + 'S'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 's'
            else:
                texto = self.ingresar_nombre_out.text() + 'S'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 's'
            else:
                texto = self.configuracion_avanzada_user.text() + 'S'
            self.configuracion_avanzada_user.setText(texto)

    def d(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'd'
            else:
                texto = self.ingresar_nombre.text() + 'D'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'd'
            else:
                texto = self.ingresar_nombre_out.text() + 'D'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'd'
            else:
                texto = self.configuracion_avanzada_user.text() + 'D'
            self.configuracion_avanzada_user.setText(texto)

    def f(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'f'
            else:
                texto = self.ingresar_nombre.text() + 'F'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'f'
            else:
                texto = self.ingresar_nombre_out.text() + 'F'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'f'
            else:
                texto = self.configuracion_avanzada_user.text() + 'F'
            self.configuracion_avanzada_user.setText(texto)

    def g(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'g'
            else:
                texto = self.ingresar_nombre.text() + 'G'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'g'
            else:
                texto = self.ingresar_nombre_out.text() + 'G'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'g'
            else:
                texto = self.configuracion_avanzada_user.text() + 'G'
            self.configuracion_avanzada_user.setText(texto)

    def h(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'h'
            else:
                texto = self.ingresar_nombre.text() + 'H'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'h'
            else:
                texto = self.ingresar_nombre_out.text() + 'H'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'h'
            else:
                texto = self.configuracion_avanzada_user.text() + 'H'
            self.configuracion_avanzada_user.setText(texto)

    def j(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'j'
            else:
                texto = self.ingresar_nombre.text() + 'J'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'j'
            else:
                texto = self.ingresar_nombre_out.text() + 'J'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'j'
            else:
                texto = self.configuracion_avanzada_user.text() + 'J'
            self.configuracion_avanzada_user.setText(texto)

    def k(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'k'
            else:
                texto = self.ingresar_nombre.text() + 'K'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'k'
            else:
                texto = self.ingresar_nombre_out.text() + 'K'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'k'
            else:
                texto = self.configuracion_avanzada_user.text() + 'K'
            self.configuracion_avanzada_user.setText(texto)

    def l(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'l'
            else:
                texto = self.ingresar_nombre.text() + 'L'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'l'
            else:
                texto = self.ingresar_nombre_out.text() + 'L'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'l'
            else:
                texto = self.configuracion_avanzada_user.text() + 'L'
            self.configuracion_avanzada_user.setText(texto)

    def ene(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'ñ'
            else:
                texto = self.ingresar_nombre.text() + 'Ñ'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'ñ'
            else:
                texto = self.ingresar_nombre_out.text() + 'Ñ'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'ñ'
            else:
                texto = self.configuracion_avanzada_user.text() + 'Ñ'
            self.configuracion_avanzada_user.setText(texto)

    def z(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'z'
            else:
                texto = self.ingresar_nombre.text() + 'Z'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'z'
            else:
                texto = self.ingresar_nombre_out.text() + 'Z'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'z'
            else:
                texto = self.configuracion_avanzada_user.text() + 'Z'
            self.configuracion_avanzada_user.setText(texto)

    def x(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'x'
            else:
                texto = self.ingresar_nombre.text() + 'X'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'x'
            else:
                texto = self.ingresar_nombre_out.text() + 'X'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'x'
            else:
                texto = self.configuracion_avanzada_user.text() + 'X'
            self.configuracion_avanzada_user.setText(texto)

    def c(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'c'
            else:
                texto = self.ingresar_nombre.text() + 'C'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'c'
            else:
                texto = self.ingresar_nombre_out.text() + 'C'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'c'
            else:
                texto = self.configuracion_avanzada_user.text() + 'C'
            self.configuracion_avanzada_user.setText(texto)

    def v(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'v'
            else:
                texto = self.ingresar_nombre.text() + 'V'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'v'
            else:
                texto = self.ingresar_nombre_out.text() + 'V'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'v'
            else:
                texto = self.configuracion_avanzada_user.text() + 'V'
            self.configuracion_avanzada_user.setText(texto)

    def b(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'b'
            else:
                texto = self.ingresar_nombre.text() + 'B'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'b'
            else:
                texto = self.ingresar_nombre_out.text() + 'B'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'b'
            else:
                texto = self.configuracion_avanzada_user.text() + 'B'
            self.configuracion_avanzada_user.setText(texto)

    def n(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'n'
            else:
                texto = self.ingresar_nombre.text() + 'N'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'n'
            else:
                texto = self.ingresar_nombre_out.text() + 'N'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'n'
            else:
                texto = self.configuracion_avanzada_user.text() + 'N'
            self.configuracion_avanzada_user.setText(texto)

    def m(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'm'
            else:
                texto = self.ingresar_nombre.text() + 'M'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre_out.text() + 'm'
            else:
                texto = self.ingresar_nombre_out.text() + 'M'
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.configuracion_avanzada_user.text() + 'm'
            else:
                texto = self.configuracion_avanzada_user.text() + 'M'
            self.configuracion_avanzada_user.setText(texto)

    def SPACE(self):
        if self.campo == 'ingresar-nombre':
            
            texto = self.ingresar_nombre.text() + ' '
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            
            texto = self.ingresar_nombre_out.text() + ' '
            self.ingresar_nombre_out.setText(texto)

        elif self.campo == 'AdConf-User':

            texto = self.configuracion_avanzada_user.text() + ' '
            self.configuracion_avanzada_user.setText(texto)

    def BORRAR(self):
        if self.campo == 'ingresar-nombre':
            var_texto=self.ingresar_nombre.text()
        elif self.campo == 'retirar-nombre':
            var_texto=self.ingresar_nombre_out.text()
        elif self.campo == 'AdConf-User':
            var_texto=self.configuracion_avanzada_user.text()

        if len(var_texto)==1 or len(var_texto)==0:
            texto=''
        elif var_texto[-1] != var_texto[-2]:
            texto = var_texto.rstrip(var_texto[-1])
        else:
            raw = var_texto
            t=[]
            for l in range(len(raw)-1):
                
                t.append(raw[l])

            texto="".join(t)

        if self.campo == 'ingresar-nombre':
            self.ingresar_nombre.setText(texto)
        elif self.campo == 'retirar-nombre':
            self.ingresar_nombre_out.setText(texto)
        elif self.campo == 'AdConf-User':
            self.configuracion_avanzada_user.setText(texto)

    def MAYUS(self):
        if not self.isMAYUS:
            self.letra_MAYUS.setStyleSheet("background-color: #ffffff; color: black;")
            self.isMAYUS =True
            self.todas_letras_a_MAYUS()
        else:
            self.letra_MAYUS.setStyleSheet("background-color: none; color: white;")
            self.isMAYUS =False
            self.todas_letras_a_NOT_MAYUS()

    def ENTER(self):
        self.Retirar_guardar_teclado()
        self.Ingresar_guardar_teclado()
        self.Ad_Conf_guardar_teclado()

    def fun_numero_ENTER(self):
        self.Retirar_guardar_teclado()
        self.Ingresar_guardar_teclado_numerico()
        self.Ingresar_guardar_teclado()
        self.Ad_Conf_guardar_teclado()

    def fun_numero_BORRAR(self):
        if self.campo == 'ingresar-cedula':
            var_texto=self.ingresar_cedula.text()
        elif self.campo == 'ingresar-temp':
            var_texto=self.ingresar_temp.text()
        elif self.campo == 'retirar-cedula':
            var_texto=self.ingresar_cedula_out.text()
        elif self.campo == 'AdConf-Pass':
            var_texto=self.configuracion_avanzada_pass.text()

        if len(var_texto)==1 or len(var_texto)==0:
            texto=''
        elif var_texto[-1] != var_texto[-2]:
            texto = var_texto.rstrip(var_texto[-1])
        else:
            raw = var_texto
            t=[]
            for l in range(len(raw)-1):
                
                t.append(raw[l])
            
            texto="".join(t)

        if self.campo == 'ingresar-cedula':
            self.ingresar_cedula.setText(texto)
        elif self.campo == 'ingresar-temp':
            self.ingresar_temp.setText(texto)
        elif self.campo == 'retirar-cedula':
            self.ingresar_cedula_out.setText(texto)
        elif self.campo == 'AdConf-Pass':
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_PUNTO(self):
        if self.campo == 'ingresar-temp':
            texto = self.ingresar_temp.text() + '.'
            self.ingresar_temp.setText(texto)

    def fun_numero_1(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '1'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '1'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '1'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '1'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_2(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '2'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '2'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '2'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '2'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_3(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '3'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '3'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '3'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '3'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_4(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '4'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '4'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '4'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '4'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_5(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '5'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '5'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '5'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '5'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_6(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '6'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '6'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '6'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '6'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_7(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '7'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '7'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '7'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '7'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_8(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '8'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '8'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '8'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '8'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_9(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '9'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '9'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '9'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '9'
            self.configuracion_avanzada_pass.setText(texto)

    def fun_numero_0(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '0'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '0'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.ingresar_cedula_out.text() + '0'
            self.ingresar_cedula_out.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.configuracion_avanzada_pass.text() + '0'
            self.configuracion_avanzada_pass.setText(texto)

    def TecladoNumerico(self):
        self.numero_0.setVisible(True)
        self.numero_1.setVisible(True)
        self.numero_2.setVisible(True)
        self.numero_3.setVisible(True)
        self.numero_4.setVisible(True)
        self.numero_5.setVisible(True)
        self.numero_6.setVisible(True)
        self.numero_7.setVisible(True)
        self.numero_8.setVisible(True)
        self.numero_9.setVisible(True)
        self.numero_ENTER.setVisible(True)
        self.numero_BORRAR.setVisible(True)
        self.numero_PUNTO.setVisible(True)

    def NotTecladoNumerico(self):
        self.numero_0.setVisible(False)
        self.numero_1.setVisible(False)
        self.numero_2.setVisible(False)
        self.numero_3.setVisible(False)
        self.numero_4.setVisible(False)
        self.numero_5.setVisible(False)
        self.numero_6.setVisible(False)
        self.numero_7.setVisible(False)
        self.numero_8.setVisible(False)
        self.numero_9.setVisible(False)
        self.numero_ENTER.setVisible(False)
        self.numero_BORRAR.setVisible(False)
        self.numero_PUNTO.setVisible(False)

    def Teclado(self):
        self.letra_q.setVisible(True)
        self.letra_w.setVisible(True)
        self.letra_e.setVisible(True)
        self.letra_r.setVisible(True)
        self.letra_t.setVisible(True)
        self.letra_y.setVisible(True)
        self.letra_u.setVisible(True)
        self.letra_i.setVisible(True)
        self.letra_o.setVisible(True)
        self.letra_p.setVisible(True)
        self.letra_a.setVisible(True)
        self.letra_s.setVisible(True)
        self.letra_d.setVisible(True)
        self.letra_f.setVisible(True)
        self.letra_g.setVisible(True)
        self.letra_h.setVisible(True)
        self.letra_j.setVisible(True)
        self.letra_k.setVisible(True)
        self.letra_l.setVisible(True)
        self.letra_ene.setVisible(True)
        self.letra_z.setVisible(True)
        self.letra_x.setVisible(True)
        self.letra_c.setVisible(True)
        self.letra_v.setVisible(True)
        self.letra_b.setVisible(True)
        self.letra_n.setVisible(True)
        self.letra_m.setVisible(True)
        self.letra_SPACE.setVisible(True)
        self.letra_MAYUS.setVisible(True)
        self.letra_ENTER.setVisible(True)
        self.letra_BORRAR.setVisible(True)

    def NotTeclado(self):
        self.letra_q.setVisible(False)
        self.letra_w.setVisible(False)
        self.letra_e.setVisible(False)
        self.letra_r.setVisible(False)
        self.letra_t.setVisible(False)
        self.letra_y.setVisible(False)
        self.letra_u.setVisible(False)
        self.letra_i.setVisible(False)
        self.letra_o.setVisible(False)
        self.letra_p.setVisible(False)
        self.letra_a.setVisible(False)
        self.letra_s.setVisible(False)
        self.letra_d.setVisible(False)
        self.letra_f.setVisible(False)
        self.letra_g.setVisible(False)
        self.letra_h.setVisible(False)
        self.letra_j.setVisible(False)
        self.letra_k.setVisible(False)
        self.letra_l.setVisible(False)
        self.letra_ene.setVisible(False)
        self.letra_z.setVisible(False)
        self.letra_x.setVisible(False)
        self.letra_c.setVisible(False)
        self.letra_v.setVisible(False)
        self.letra_b.setVisible(False)
        self.letra_n.setVisible(False)
        self.letra_m.setVisible(False)
        self.letra_SPACE.setVisible(False)
        self.letra_MAYUS.setVisible(False)
        self.letra_ENTER.setVisible(False)
        self.letra_BORRAR.setVisible(False)

    def todas_letras_a_MAYUS(self):
        self.letra_q.setText('Q')
        self.letra_w.setText('W')
        self.letra_e.setText('E')
        self.letra_r.setText('R')
        self.letra_t.setText('T')
        self.letra_y.setText('Y')
        self.letra_u.setText('U')
        self.letra_i.setText('I')
        self.letra_o.setText('O')
        self.letra_p.setText('P')
        self.letra_a.setText('A')
        self.letra_d.setText('D')
        self.letra_s.setText('S')
        self.letra_f.setText('F')
        self.letra_g.setText('G')
        self.letra_h.setText('H')
        self.letra_j.setText('J')
        self.letra_k.setText('K')
        self.letra_l.setText('L')
        self.letra_z.setText('Z')
        self.letra_x.setText('X')
        self.letra_c.setText('C')
        self.letra_v.setText('V')
        self.letra_b.setText('B')
        self.letra_n.setText('N')
        self.letra_m.setText('M')
        self.letra_ene.setText('Ñ')

    def todas_letras_a_NOT_MAYUS(self):
        self.letra_q.setText('q')
        self.letra_w.setText('w')
        self.letra_e.setText('e')
        self.letra_r.setText('r')
        self.letra_t.setText('t')
        self.letra_y.setText('y')
        self.letra_u.setText('u')
        self.letra_i.setText('i')
        self.letra_o.setText('o')
        self.letra_p.setText('p')
        self.letra_a.setText('a')
        self.letra_d.setText('d')
        self.letra_s.setText('s')
        self.letra_f.setText('f')
        self.letra_g.setText('g')
        self.letra_h.setText('h')
        self.letra_j.setText('j')
        self.letra_k.setText('k')
        self.letra_l.setText('l')
        self.letra_z.setText('z')
        self.letra_x.setText('x')
        self.letra_c.setText('c')
        self.letra_v.setText('v')
        self.letra_b.setText('b')
        self.letra_n.setText('n')
        self.letra_m.setText('m')
        self.letra_ene.setText('ñ')

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()