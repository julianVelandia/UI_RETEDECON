from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QLineClick import QLineEditClick
from datetime import datetime

import sqlite3


class MainWindow(QMainWindow): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("static/style.css") as f:
            self.setStyleSheet(f.read())

        'conección base de datos'
        self.conn = sqlite3.connect('DB.db')
        self.ccc = self.conn.cursor()

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
        self.ingresar_temp.setPlaceholderText("TEMPERATURA")
        self.ingresar_temp.setObjectName("input") #nombre de enlace a css
        self.ingresar_temp.setClearButtonEnabled(True)
        self.ingresar_temp.setGeometry(164,396,290,65)
        self.ingresar_temp.setMaxLength(3)

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
        self.ingresar_temp.setVisible(False)
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
        self.ingresar_temp.setVisible(True)
        self.ingresar_temp.clear()
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

    '''Esta función se encarga de escribir lo datos en un archivo .txt y tiene
    programadas ventanas emergentes en caso de errores o notificaciones'''
    def Leer(self):
        # definimos la fecha y hora
        fecha_hora_out = datetime.now().isoformat(timespec='seconds')
        # vector que contiene los datos a leer
        persona_out = ["Nombre: ", self.ingresar_nombre_out.text(), " CC: ", self.ingresar_cedula_out.text(), " Fecha y hora: ", fecha_hora_out, "\n"]

        'Para la base de datos'
        nombre_out_bd = self.ingresar_nombre_out.text()
        cedula_out_bd = self.ingresar_cedula_out.text()
        fecha_hora_out_bd = str(fecha_hora_out)

        if persona_out[1] != "" and persona_out[3] != "":  # lógica para leer si los campos están vacíos
            if not persona_out[1].isdigit() and not persona_out[3].isalpha():  # detecta si numeros o letras donde no deben
                try:
                    '''Esta parte aun no funciona correctamente'''
                    '''Aún no se como buscar en todo el documento'''
                    'Para la base de datos'
                    self.ccc.execute('DELETE FROM usuarios (nombre_bd,cedula_bd,fecha_hora_bd) VALUES ("{}","{}","{}")'.format(nombre_out_bd,cedula_out_bd,fecha_hora_out_bd))
                    self.conn.commit() #buscar evitar ataques de SQL injection

                    
                    
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

        'Para la base de datos'
        nombre_bd = self.ingresar_nombre.text()
        cedula_bd = self.ingresar_cedula.text()
        #fecha_hora_bd = str(fecha_hora)
        
        if persona[1]!="" and persona[3]!="":  #lógica para leer si los campos están vacíos
            if not persona[1].isdigit() and not persona[3].isalpha():  #detecta si numeros o letras donde no deben
                try:
                    'Para la base de datos'
                    self.ccc.execute('INSERT INTO usuarios (nombre_bd,cedula_bd) VALUES ("{}","{}")'.format(nombre_bd,cedula_bd))
                    self.conn.commit() #buscar evitar ataques de SQL injection

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
        MOV = -115
        #movimiento botones


        self.ingresar_nombre.setGeometry(164, 230+MOV, 290, 60)
        self.ingresar_cedula.setGeometry(164,305+MOV,290,60)
        self.ingresar_temp.setGeometry(164,380+MOV,290,60)
        self.ingresar_ingresar.setGeometry(570, 255+MOV, 290, 176.3)

        self.Teclado()

    def Ingresar_guardar_teclado(self):

        self.ingresar_nombre.setGeometry(164, 230, 290, 65)
        self.ingresar_cedula.setGeometry(164,305,290,65)
        self.ingresar_temp.setGeometry(164,380,290,65)
        self.ingresar_ingresar.setGeometry(570, 255, 290, 176.3)
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

    

    def BotonesTeclado(self):
        sep_lado = 16
        sep_arriba = 16
        base = 69
        altura = 65
        y_inicia = 340
        
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
        self.letra_a.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_a.clicked.connect(self.a)

        x=1
        y=1
        self.letra_s = QToolButton(self.centralWidget)
        self.letra_s.setText('s')
        self.letra_s.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_s.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_s.clicked.connect(self.s)

        x=2
        y=1
        self.letra_d = QToolButton(self.centralWidget)
        self.letra_d.setText('d')
        self.letra_d.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_d.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_d.clicked.connect(self.d)

        x=3
        y=1
        self.letra_f = QToolButton(self.centralWidget)
        self.letra_f.setText('f')
        self.letra_f.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_f.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_f.clicked.connect(self.f)

        x=4
        y=1
        self.letra_g = QToolButton(self.centralWidget)
        self.letra_g.setText('g')
        self.letra_g.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_g.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_g.clicked.connect(self.g)

        x=5
        y=1
        self.letra_h = QToolButton(self.centralWidget)
        self.letra_h.setText('h')
        self.letra_h.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_h.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_h.clicked.connect(self.h)

        x=6
        y=1
        self.letra_j = QToolButton(self.centralWidget)
        self.letra_j.setText('j')
        self.letra_j.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_j.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_j.clicked.connect(self.j)

        x=7
        y=1
        self.letra_k = QToolButton(self.centralWidget)
        self.letra_k.setText('k')
        self.letra_k.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_k.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_k.clicked.connect(self.k)

        x=8
        y=1
        self.letra_l = QToolButton(self.centralWidget)
        self.letra_l.setText('l')
        self.letra_l.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_l.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_l.clicked.connect(self.l)

        x=9
        y=1
        self.letra_ene = QToolButton(self.centralWidget)
        self.letra_ene.setText('ñ')
        self.letra_ene.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_ene.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_ene.clicked.connect(self.ene)

        x=10
        y=1
        self.letra_MAYUS = QToolButton(self.centralWidget)
        self.letra_MAYUS.setText('mayus')
        self.letra_MAYUS.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_MAYUS.setGeometry((base/2)+(base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base*1.5, altura)
        self.letra_MAYUS.clicked.connect(self.MAYUS)

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

        x=4
        y=2
        self.letra_SPACE = QToolButton(self.centralWidget)
        self.letra_SPACE.setText('')
        self.letra_SPACE.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_SPACE.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba,3*sep_lado+ 4*base, altura)
        self.letra_SPACE.clicked.connect(self.SPACE)

        x=8
        y=2
        self.letra_b = QToolButton(self.centralWidget)
        self.letra_b.setText('b')
        self.letra_b.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_b.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_b.clicked.connect(self.b)

        x=9
        y=2
        self.letra_n = QToolButton(self.centralWidget)
        self.letra_n.setText('n')
        self.letra_n.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_n.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_n.clicked.connect(self.n)

        x=10
        y=2
        self.letra_m = QToolButton(self.centralWidget)
        self.letra_m.setText('m')
        self.letra_m.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_m.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_m.clicked.connect(self.m)

        

        self.NotTeclado()

    def q(self):
        texto = self.ingresar_nombre.text() + 'q'
        self.ingresar_nombre.setText(texto)

    def w(self):
        texto = self.ingresar_nombre.text() + 'w'
        self.ingresar_nombre.setText(texto)

    def e(self):
        texto = self.ingresar_nombre.text() + 'e'
        self.ingresar_nombre.setText(texto)

    def r(self):
        texto = self.ingresar_nombre.text() + 'r'
        self.ingresar_nombre.setText(texto)

    def t(self):
        texto = self.ingresar_nombre.text() + 't'
        self.ingresar_nombre.setText(texto)

    def y(self):
        texto = self.ingresar_nombre.text() + 'y'
        self.ingresar_nombre.setText(texto)
    
    def u(self):
        texto = self.ingresar_nombre.text() + 'u'
        self.ingresar_nombre.setText(texto)

    def i(self):
        texto = self.ingresar_nombre.text() + 'i'
        self.ingresar_nombre.setText(texto)

    def o(self):
        texto = self.ingresar_nombre.text() + 'o'
        self.ingresar_nombre.setText(texto)

    def p(self):
        texto = self.ingresar_nombre.text() + 'p'
        self.ingresar_nombre.setText(texto)

    def a(self):
        texto = self.ingresar_nombre.text() + 'a'
        self.ingresar_nombre.setText(texto)

    def s(self):
        texto = self.ingresar_nombre.text() + 's'
        self.ingresar_nombre.setText(texto)

    def d(self):
        texto = self.ingresar_nombre.text() + 'd'
        self.ingresar_nombre.setText(texto)

    def f(self):
        texto = self.ingresar_nombre.text() + 'f'
        self.ingresar_nombre.setText(texto)

    def g(self):
        texto = self.ingresar_nombre.text() + 'g'
        self.ingresar_nombre.setText(texto)

    def h(self):
        texto = self.ingresar_nombre.text() + 'h'
        self.ingresar_nombre.setText(texto)

    def j(self):
        texto = self.ingresar_nombre.text() + 'j'
        self.ingresar_nombre.setText(texto)

    def k(self):
        texto = self.ingresar_nombre.text() + 'k'
        self.ingresar_nombre.setText(texto)

    def l(self):
        texto = self.ingresar_nombre.text() + 'l'
        self.ingresar_nombre.setText(texto)

    def ene(self):
        texto = self.ingresar_nombre.text() + 'ñ'
        self.ingresar_nombre.setText(texto)

    def z(self):
        texto = self.ingresar_nombre.text() + 'z'
        self.ingresar_nombre.setText(texto)

    def x(self):
        texto = self.ingresar_nombre.text() + 'x'
        self.ingresar_nombre.setText(texto)

    def c(self):
        texto = self.ingresar_nombre.text() + 'c'
        self.ingresar_nombre.setText(texto)

    def v(self):
        texto = self.ingresar_nombre.text() + 'v'
        self.ingresar_nombre.setText(texto)

    def b(self):
        texto = self.ingresar_nombre.text() + 'b'
        self.ingresar_nombre.setText(texto)

    def n(self):
        texto = self.ingresar_nombre.text() + 'n'
        self.ingresar_nombre.setText(texto)

    def m(self):
        texto = self.ingresar_nombre.text() + 'm'
        self.ingresar_nombre.setText(texto)

    def SPACE(self):
        texto = self.ingresar_nombre.text() + ' '
        self.ingresar_nombre.setText(texto)

    def BORRAR(self):
        texto = self.ingresar_nombre.text().split()
        print(texto)
        #self.ingresar_nombre.setText(texto)

    def MAYUS(self):
        texto = self.ingresar_nombre.text().split()
        print(texto)
        #self.ingresar_nombre.setText(texto)

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

    

        

if __name__=='__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()