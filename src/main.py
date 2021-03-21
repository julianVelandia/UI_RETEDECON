from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QLineClick import QLineEditClick
from datetime import datetime

class MainWindow(QMainWindow): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("style.css") as f:
            self.setStyleSheet(f.read())
        'constants'
        self.title = 'RETEDECON'
        self.width = 1024
        self.height = 600

        self.setMinimumSize(self.width,self.height)    #tamaño mínimo
        self.setMaximumSize(self.width,self.height)  #tamaño máximo
        self.setWindowTitle(self.title)   #titulo
        self.setWindowIcon(QIcon("static/favicon3.png"))   #Favicon

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("window") #nombre que enlaza en css
        '''
        Imagen central 
        '''
        self.label_img_central = QLabel(self)
        self.label_img_central.setGeometry(289,-10,1024,600)
        self.pixmap = QPixmap('static/Logo_central.png')   #Imagen central
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
        self.configuracion.setIconSize(QSize(60,60))
        self.configuracion.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.configuracion.clicked.connect(self.Configuracion)

        self.informacion = QToolButton(self.centralWidget)
        self.informacion.setText('INFORMACIÓN')
        self.informacion.setObjectName("button")
        self.informacion.setIcon(QIcon('static/icons/icono_campana'))
        self.informacion.setIconSize(QSize(60,60))
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
        self.ingresar_nombre.setGeometry(164.2, 237, 290, 70)
        self.ingresar_nombre.setMaxLength(40)

        'cuadros de texto 2'
        self.ingresar_cedula = QLineEditClick(self.centralWidget)
        self.ingresar_cedula.setPlaceholderText("CEDULA")
        self.ingresar_cedula.setObjectName("input") #nombre de enlace a css
        self.ingresar_cedula.setClearButtonEnabled(True)
        self.ingresar_cedula.setGeometry(164.2,341,290,70)
        self.ingresar_cedula.setMaxLength(15)

        'cuadros de texto out'
        self.ingresar_nombre_out = QLineEditClick(self.centralWidget)
        self.ingresar_nombre_out.setPlaceholderText("NOMBRE")
        self.ingresar_nombre_out.setObjectName("input")  # nombre de enlace a css
        self.ingresar_nombre_out.setClearButtonEnabled(True)
        self.ingresar_nombre_out.setGeometry(164.2, 237, 290, 70)
        self.ingresar_nombre_out.setMaxLength(40)

        'cuadros de texto out 2'
        self.ingresar_cedula_out = QLineEditClick(self.centralWidget)
        self.ingresar_cedula_out.setPlaceholderText("CEDULA")
        self.ingresar_cedula_out.setObjectName("input")  # nombre de enlace a css
        self.ingresar_cedula_out.setClearButtonEnabled(True)
        self.ingresar_cedula_out.setGeometry(164.2, 341, 290, 70)
        self.ingresar_cedula_out.setMaxLength(15)

        #Botones Ingresar
        self.BotonesIngresar()
        # Botones Salida Manual
        self.BotonesSalidaManual()
        #botones teclado
        self.BotonesTeclado()
        #AccionClcikIngresarNombre
        self.ingresar_nombre.clicked.connect(self.Ingresar_desplegar_teclado)
        #AccionClcikIngresarCedula
        self.ingresar_cedula.clicked.connect(self.Ingresar_desplegar_teclado)
        # AccionClcikIngresarNombreOut
        self.ingresar_nombre_out.clicked.connect(self.Retirar_desplegar_teclado)
        # AccionClcikIngresarCedulaOut
        self.ingresar_cedula_out.clicked.connect(self.Retirar_desplegar_teclado)

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
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.ingresar_ingresar.setVisible(False)
        self.retirar.setVisible(False)
        self.NotTeclado()
        
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
        self.ingresar_ingresar.setVisible(True)
        self.ingresar_nombre_out.setVisible(False)
        self.ingresar_cedula_out.setVisible(False)
        self.retirar.setVisible(False)
        self.Ingresar_guardar_teclado()

    def BotonesIngresar(self):
        self.ingresar_ingresar = QToolButton(self.centralWidget)
        self.ingresar_ingresar.setText('INGRESAR')
        self.ingresar_ingresar.setObjectName("button") #nombre de enlace a css
        self.ingresar_ingresar.setIcon(QIcon('static/icons/icono_entrar')) #icono
        self.ingresar_ingresar.setIconSize(QSize(60,60))
        self.ingresar_ingresar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ingresar_ingresar.clicked.connect(self.Escribir)
        self.ingresar_ingresar.setGeometry(570, 237, 290, 176.3)
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
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

    '''Esta función se encarga de escribir lo datos en un archivo .txt y tiene
    programadas ventanas emergentes en caso de errores o notificaciones'''
    def Leer(self):
        # definimos la fecha y hora
        fecha_hora_out = datetime.now().isoformat(timespec='seconds')
        # vector que contiene los datos a leer
        persona_out = ["Nombre: ", self.ingresar_nombre_out.text(), " CC: ", self.ingresar_cedula_out.text(), " Fecha y hora: ", fecha_hora_out, "\n"]
        if persona_out[1] != "" and persona_out[3] != "":  # lógica para leer si los campos están vacíos
            if not persona_out[1].isdigit() and not persona_out[3].isalpha():  # detecta si numeros o letras donde no deben
                try:
                    '''Esta parte aun no funciona correctamente'''
                    '''Aún no se como buscar en todo el documento'''
                    archivo_out = open("Lista.txt", "r")
                    contenido = archivo_out.readline()
                    lista_contenido = contenido.split("-")
                    print(lista_contenido)
                    if lista_contenido[0]==persona_out[1] and lista_contenido[1]==persona_out[3]:
                        archivo_out.close()
                        dialogo_exitoso = QMessageBox(self.centralWidget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha retirado correctamente\n    ")
                        dialogo_exitoso.show()
                        self.HomeWindow()
                    else:
                        dialogo_error_busqueda = QMessageBox(self.centralWidget)
                        dialogo_error_busqueda.setWindowTitle(self.title)
                        dialogo_error_busqueda.addButton("Aceptar", 0)
                        dialogo_error_busqueda.setInformativeText("Error, no se encontró a ese usuario\n    ")
                        dialogo_error_busqueda.show()
                        archivo_out.close()
                except:
                    dialogo_error_lectura = QMessageBox(self.centralWidget)
                    dialogo_error_lectura.setWindowTitle(self.title)
                    dialogo_error_lectura.addButton("Aceptar", 0)
                    dialogo_error_lectura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
                    dialogo_error_lectura.show()
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

    def Escribir(self):
        #definimos la fecha y hora
        fecha_hora= datetime.now().isoformat(timespec='seconds')
        #vector que contiene los datos a escribir
        persona = ["Nombre: ", self.ingresar_nombre.text(), " CC: ", self.ingresar_cedula.text(), " Fecha y hora: ", fecha_hora,"\n"]
        if persona[1]!="" and persona[3]!="":  #lógica para leer si los campos están vacíos
            if not persona[1].isdigit() and not persona[3].isalpha():  #detecta si numeros o letras donde no deben
                try:
                    archivo = open("Lista.txt", "a")
                    archivo.writelines(persona)
                    archivo.close()
                    dialogo_exitoso = QMessageBox(self.centralWidget)
                    dialogo_exitoso.setWindowTitle(self.title)
                    dialogo_exitoso.addButton("Aceptar", 0)
                    dialogo_exitoso.setInformativeText("Se ha ingresado correctamente\n    ")
                    dialogo_exitoso.show()
                    self.HomeWindow()
                except:
                    dialogo_error_escritura = QMessageBox(self.centralWidget)
                    dialogo_error_escritura.setWindowTitle(self.title)
                    dialogo_error_escritura.addButton("Aceptar",0)
                    dialogo_error_escritura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
                    dialogo_error_escritura.show()
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

    def Ingresar_desplegar_teclado(self):
        MOV = -100
        #movimiento botones
        self.ingresar_nombre.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula.setGeometry(164.2,341+MOV,290,70)
        self.ingresar_ingresar.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()

    def Ingresar_guardar_teclado(self):
        MOV = 0
        #movimiento botones
        self.ingresar_nombre.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula.setGeometry(164.2,341+MOV,290,70)
        self.ingresar_ingresar.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()

    def Retirar_desplegar_teclado(self):
        MOV = -100
        #movimiento botones
        self.ingresar_nombre_out.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula_out.setGeometry(164.2,341+MOV,290,70)
        self.retirar.setGeometry(570, 237+MOV, 290, 176.3)
        self.Teclado()

    def Retirar_guardar_teclado(self):
        MOV = 0
        #movimiento botones
        self.ingresar_nombre_out.setGeometry(164.2,237+MOV,290,70)
        self.ingresar_cedula_out.setGeometry(164.2,341+MOV,290,70)
        self.retirar.setGeometry(570, 237+MOV, 290, 176.3)
        self.NotTeclado()

    def Estadisticas(self):
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

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
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

    def Informacion(self):
        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

    def Teclado(self):
        self.teclado_q.setVisible(True)
        self.teclado_w.setVisible(True)

    def BotonesTeclado(self):
        sep_lado = 16
        sep_arriba = 16
        base = 70
        altura = 65
        y_inicia = 380
        self.teclado_q = QToolButton(self.centralWidget)
        self.teclado_q.setText('q')
        self.teclado_q.setObjectName("buttonTeclado") #nombre de enlace a css
        self.teclado_q.setGeometry((base*0) + 1*sep_lado,y_inicia+ (altura*0) + sep_arriba, base, altura)
        self.teclado_q.clicked.connect(self.q)

        self.teclado_w = QToolButton(self.centralWidget)
        self.teclado_w.setText('w')
        self.teclado_w.setObjectName("buttonTeclado") #nombre de enlace a css
        self.teclado_w.setGeometry((base*1) + 2*sep_lado, y_inicia+ (altura*0) + sep_arriba, base, altura)
        self.teclado_w.clicked.connect(self.q)

        self.NotTeclado()

    def NotTeclado(self):
        self.teclado_q.setVisible(False)
        self.teclado_w.setVisible(False)

    def q(self):
        print('q')

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()