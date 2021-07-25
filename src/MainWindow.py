from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from configparser import ConfigParser
# locals
from src.views.botones.inicio.boton import Boton
from src.views.teclado.teclado_numeros import TecladoNumeros
from src.views.teclado.teclado_letras import TecladoLetras
from src.communication.PySerialmain import Read
import threading

from screeninfo import get_monitors


class MainWindow(QMainWindow, Boton, TecladoNumeros, TecladoLetras, Read):  # Ventana principal
    def __init__(self, alarm, sw, parent=None, *args):
        super(MainWindow, self).__init__(parent=parent)
        with open("src/views/static/styles.css") as f:
            self.setStyleSheet(f.read())

        # conexion con studentWindow
        self.sw = sw

        self.cedula_cache = ''
        self.carnet = ''
        self.title = 'RETEDECON'
        self.config = ConfigParser()
        self.width = get_monitors()[0].width
        self.height = get_monitors()[0].height


        # alarma
        self.alarm = alarm

        self.setMinimumSize(self.width, self.height)  # tamaño mínimo 
        self.setMaximumSize(self.width, self.height)  # tamaño máximo
        self.setWindowTitle(self.title)  # titulo
        self.setWindowIcon(QIcon("src/views/static/icons/favicon3.png"))  # Favicon
        self.showMaximized()

        # Widget principal
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window")  # nombre que enlaza en css

        # Mensajes
        self.dialogo_mensaje = 'Error404'
        self.dialogo = QMessageBox(self.centralWidget)
        self.dialogo.setWindowTitle('RETEDECON')
        self.dialogo.addButton("Aceptar", 0)
        self.dialogo.setInformativeText(self.dialogo_mensaje)

        # Imagen central
        self.label_img_central = QLabel(self)
        self.pixmap = QPixmap('src/views/static/icons/Logo_central.png')  # Imagen central

        self.label_img_central.setGeometry(self.width / 2 - self.pixmap.width() / 2,
                                           self.height / 2 - self.pixmap.height() / 2, self.pixmap.width(),
                                           self.pixmap.height())        
        self.label_img_central.setPixmap(self.pixmap)
        self.label_img_central.setVisible(True)

        # Timer animación
        self.timer = QTimer()
        self.timer.setInterval(2500)
        self.timer.setSingleShot(True)
        self.timer.start()
        self.timer.timeout.connect(self.HomeWindow)  # función a ejecutar pasados los 3 seg

        # teclados
        self.BotonesTeclado(self.centralWidget)
        self.BotonesTecladoNumerico(self.centralWidget)

        # Botones Inicio
        self.boton_home(self.centralWidget)
        self.boton_inicio_ingresar(self.centralWidget)
        self.boton_inicio_estadisticas(self.centralWidget)
        self.boton_inicio_detener_alarma(self.centralWidget)
        self.boton_inicio_salida_manual(self.centralWidget)
        self.boton_inicio_configuracion(self.centralWidget)
        self.boton_inicio_estadisticas(self.centralWidget)
        self.boton_inicio_informacion(self.centralWidget)

        # Botones ingresar
        self.texto_ingresar_nombre(self.centralWidget)
        self.texto_ingresar_cedula(self.centralWidget)
        self.texto_ingresar_temp(self.centralWidget)
        self.boton_ingresar_ingresar(self.centralWidget)

        # Botones salida
        self.texto_salida_nombre_out(self.centralWidget)
        self.texto_salida_cedula_out(self.centralWidget)
        self.boton_salida_salida(self.centralWidget)

        # Botones configuracion
        self.boton_configuraciones_ajustes(self.centralWidget)
        self.boton_configuraciones_avanzada(self.centralWidget)
        self.boton_configuraciones_apagar(self.centralWidget)
        self.boton_configuraciones_datos(self.centralWidget)

        # Botones Datos
        self.boton_datos_barras(self.centralWidget)
        self.boton_datos_pie(self.centralWidget)

        # Botones informacion
        self.qr_informacion_qr(self.centralWidget)
        self.label_informacion_label(self.centralWidget)
        self.boton_informacion_manual(self.centralWidget)
        self.boton_informacion_fabricante(self.centralWidget)

        # Botones estadisticas
        self.boton_estadisticas_ocupacion(self.centralWidget)
        self.boton_estadisticas_duracion(self.centralWidget)
        self.boton_estadisticas_personasDia(self.centralWidget)
        self.boton_estadisticas_cambiar_semana(self.centralWidget)
        self.boton_barras(self.centralWidget)
        self.boton_torta(self.centralWidget)
        self.graficas_estadisticas()

        # Botones configuracion avanzada
        self.texto_avanzada_user(self.centralWidget)
        self.texto_avanzada_pass(self.centralWidget)
        self.boton_avanzada_ingresar(self.centralWidget)

        # Botones configuracion avanzada inside
        self.boton_inside_agregar(self.centralWidget)
        self.boton_inside_cambiar(self.centralWidget)
        self.boton_inside_capacidad(self.centralWidget)
        self.boton_inside_eliminar(self.centralWidget)
        self.boton_inside_enviar(self.centralWidget)

        # Botones configuracion avanzada inside agregar
        self.boton_agregar_username(self.centralWidget)
        self.boton_agregar_pass(self.centralWidget)
        self.boton_agregar_agregar(self.centralWidget)

        # Botones configuracion avanzada inside agregar
        self.boton_eliminar_username(self.centralWidget)
        self.boton_eliminar_pass(self.centralWidget)
        self.boton_eliminar_eliminar(self.centralWidget)

        # Botones configuracion avanzada inside capacidad
        self.boton_capacidad_setnew(self.centralWidget)
        self.text_capacidad_newcapacidad(self.centralWidget)

        # Botones Configuracion avanzada inside cambiar
        self.text_cambiar_pass(self.centralWidget)
        self.text_pass_new(self.centralWidget)
        self.boton_cambiar_cambiar(self.centralWidget)

        #Limpiar registros
        ### CUADRAR FRANJA HORARIA PARA ACTUALIZACIÓN DE DATOS
        self.sacar_dia_anterior()

        #Read.__init__(self)
        #threading.Thread(target=self.execute, daemon=True).start()
