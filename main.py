from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from configparser import ConfigParser
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
        
        #Mensajes
        self.dialogo_mensaje = 'Error404'
        self.dialogo = QMessageBox(self.centralWidget)
        self.dialogo.setWindowTitle('RETEDECON')
        self.dialogo.addButton("Aceptar", 0)
        self.dialogo.setInformativeText(self.dialogo_mensaje)

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

        #teclados
        self.BotonesTeclado(self.centralWidget)
        self.BotonesTecladoNumerico(self.centralWidget)

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

        #Botones configuracion
        self.boton_configuraciones_ajustes(self.centralWidget)
        self.boton_configuraciones_avanzada(self.centralWidget)
        self.boton_configuraciones_apagar(self.centralWidget)
        self.boton_configuraciones_datos(self.centralWidget)

        #Botones configuracion avanzada
        self.texto_avanzada_user(self.centralWidget)
        self.texto_avanzada_pass(self.centralWidget)
        self.boton_avanzada_ingresar(self.centralWidget)

        #Botones configuracion avanzada inside
        self.boton_inside_agregar(self.centralWidget)
        self.boton_inside_cambiar(self.centralWidget)
        self.boton_inside_capacidad(self.centralWidget)
        self.boton_inside_eliminar(self.centralWidget)
        self.boton_inside_enviar(self.centralWidget)

        #Botones configuracion avanzada inside agregar
        self.boton_agregar_username(self.centralWidget)
        self.boton_agregar_pass(self.centralWidget)
        self.boton_agregar_agregar(self.centralWidget)

        #Botones configuracion avanzada inside agregar
        self.boton_eliminar_username(self.centralWidget)
        self.boton_eliminar_pass(self.centralWidget)
        self.boton_eliminar_eliminar(self.centralWidget)
        
        #Botones configuracion avanzada inside capacidad
        self.boton_capacidad_setnew(self.centralWidget)
        self.text_capacidad_newcapacidad(self.centralWidget)


        
        

        

        self.campo ='null'

        
        
        

        

        

        # Botones Informacion
        self.BotonesInformacion()
        # Label infos
        self.LabelsInformacion()
        # Labels y Botones Estadisticas
        self.LabelsBotonesEstadisticas()

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