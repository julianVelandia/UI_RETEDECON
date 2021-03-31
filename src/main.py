from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from QLineClick import QLineEditClick
from datetime import datetime
import pandas as pd

class MainWindow(QMainWindow): #Ventana principal
    def __init__(self, parent=None, *args):
        super(MainWindow,self).__init__(parent = parent)
        with open("static/styles.css") as f:
            self.setStyleSheet(f.read())

        self.df = pd.read_csv('../DB.csv')
        #self.df_as_dataframe = pd.DataFrame(self.df)
        #self.df_as_dataframe = pd.DataFrame(self.df,columns=['Nombre','Cedula','Carnet','Temp','Fecha','HoraIn','HoraOut','Delta','Numingresos','IsIn'])
        self.cedula_cache = ''
        self.carnet = ''

        try:
            ocupacion_doc = open("Lista.txt", "r")
            self.ocupacion = ocupacion_doc.read()
            ocupacion_doc.close()
        except:
            print("ERROR")

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
        self.ingresar_nombre_out.setGeometry(164.2, 237, 290, 70)
        self.ingresar_nombre_out.setMaxLength(40)

        'cuadros de texto out 2'
        self.ingresar_cedula_out = QLineEditClick(self.centralWidget)
        self.ingresar_cedula_out.setPlaceholderText("CEDULA")
        self.ingresar_cedula_out.setObjectName("input")  # nombre de enlace a css
        self.ingresar_cedula_out.setClearButtonEnabled(True)
        self.ingresar_cedula_out.setGeometry(164.2, 341, 290, 70)
        self.ingresar_cedula_out.setMaxLength(15)

        self.campo ='null'

        #Botones Ingresar
        self.BotonesIngresar()
        # Botones Salida Manual
        self.BotonesSalidaManual()
        #botones teclado
        self.BotonesTeclado()
        self.BotonesTecladoNumerico()
        #AccionClcikIngresarNombre
        self.ingresar_nombre.clicked.connect(self.Ingresar_desplegar_teclado)
        #AccionClcikIngresarCedula
        self.ingresar_cedula.clicked.connect(self.Ingresar_desplegar_teclado_numerico_cedula)
        # AccionClcikIngresarNombreOut
        self.ingresar_temp.clicked.connect(self.Ingresar_desplegar_teclado_numerico_temp)

        self.ingresar_nombre_out.clicked.connect(self.Retirar_desplegar_teclado)
        # AccionClcikIngresarCedulaOut
        self.ingresar_cedula_out.clicked.connect(self.Retirar_desplegar_teclado_numerico_cedula)

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
    '''
    Tambiàn eliminar usuarios
    '''
    def Leer(self):

        self.df.replace("CASA", "HOLA")
        print(self.df)

        # definimos la fecha y hora
        nombre = str(self.ingresar_nombre_out.text())
        cedula = str(self.ingresar_cedula_out.text())
        self.carnet = '*'

        self.HoraOut = datetime.today().strftime('%H:%M')
        Lista = self.df['Cedula']
        #self.df.drop([0],axis=0)

        '''
        if str(self.df['Cedula'][0]) == str(self.ingresar_cedula_out.text()) and str(self.df['IsIn'][0]) == 'True':
            #self.df['HoraOut'][0] = datetime.today().strftime('%H:%M')
        else:
            print('MARICA')
        
        for ced in range(len(Lista) - 1, 0, -1):
            if str(self.df['Cedula'][ced]) == str(self.ingresar_cedula_out.text()) and str(self.df['IsIn'][0]) == 'True':
                pass
            else:
                print('MARICA')
        '''

        if self.ingresar_nombre_out.text()!="" and self.ingresar_cedula_out.text()!="":  #lógica para leer si los campos están vacíos
            if not self.ingresar_nombre_out.text().isdigit() and not self.ingresar_cedula_out.text().isalpha():  #detecta si numeros o letras donde no deben

                try:
                    archivo_out = open("Lista.txt", "r")
                    contenido = archivo_out.read()
                    print(contenido)
                    if cedula==self.df['Cedula'][0]:
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
        #if not IsIn:
        #definimos la fecha y hora
        cedula= str(self.ingresar_cedula.text())
        carnet = '*' #Entra por arduino
        temp= str(self.ingresar_temp.text())
        self.Fecha = datetime.today().strftime('%d-%m-%Y')
        self.HoraIn = datetime.today().strftime('%H:%M')
        self.HoraOut = '*'
        self.Delta = '*'
        self.Numingresos = 0 #Se inicia en 0
        self.IsIn = 'True'
        cedulaExist=False
        Lista = self.df['Cedula']
        Lista_carnet = self.df['Carnet']
        ocupacion = int(self.ocupacion)
        '''
        Suma ingresos
        '''
        for cont in range(len(Lista)):
            if str(Lista_carnet[cont]) == str(self.carnet) or str(Lista[cont]) == str(self.ingresar_cedula.text()):
                self.Numingresos+=1
        
        self.Numingresos=str(self.Numingresos)
        print(self.Numingresos)

        if self.ingresar_nombre.text()!="" and self.ingresar_cedula.text()!="" and self.ingresar_temp.text()!="":  #lógica para leer si los campos están vacíos
            if not self.ingresar_nombre.text().isdigit() and not self.ingresar_cedula.text().isalpha() and not self.ingresar_temp.text().isalpha():  #detecta si numeros o letras donde no deben
                # mirar si la cédula ya existe
                # Recorrido del arreglo
                try:
                    if str(self.df['Cedula'][0]) == str(self.ingresar_cedula.text()) and str(self.df['IsIn'][0]) == 'True':
                        cedulaExist = True
                    for ced in range(len(Lista) - 1, 0, -1):
                        if str(self.df['Cedula'][ced]) == str(self.ingresar_cedula.text()) and str(self.df['IsIn'][ced]) == 'True':
                            cedulaExist = True
                except:
                    pass
                ########
                if not cedulaExist:
                    try:
                        self.df_as_txt = open ("../DB.csv", "a")
                        #ParaPandas
                        #Enviar vector persona a DB
                        persona = '\n'+self.ingresar_nombre.text()+','+cedula+','+carnet+','+temp+','+self.Fecha+','+self.HoraIn+','+self.HoraOut+','+self.Delta+','+self.Numingresos+','+self.IsIn
                        self.df_as_txt.write(persona)
                        self.df_as_txt.close()
                        #TXT   OCUPACION FALLA PORQUE SOLO ESCRIBE UNA VEZ
                        ocupacion += 1
                        archivo = open("Lista.txt", "w")
                        archivo.write(str(ocupacion))
                        archivo.close()
                        dialogo_exitoso = QMessageBox(self.centralWidget)
                        dialogo_exitoso.setWindowTitle(self.title)
                        dialogo_exitoso.addButton("Aceptar", 0)
                        dialogo_exitoso.setInformativeText("Se ha ingresado correctamente   \n")
                        dialogo_exitoso.show()

                        self.HomeWindow()
                    except:
                        dialogo_error_escritura = QMessageBox(self.centralWidget)
                        dialogo_error_escritura.setWindowTitle(self.title)
                        dialogo_error_escritura.addButton("Aceptar",0)
                        dialogo_error_escritura.setInformativeText("Error, intente nuevamente\n\nSi el error persiste comuniquese con el fabricante")
                        dialogo_error_escritura.show()
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
        self.numero_ENTER.setText(chr(25))
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

    def SPACE(self):
        if self.campo == 'ingresar-nombre':
            
            texto = self.ingresar_nombre.text() + ' '
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            
            texto = self.ingresar_nombre_out.text() + ' '
            self.ingresar_nombre_out.setText(texto)

    def BORRAR(self):
        if self.campo == 'ingresar-nombre':
            var_texto=self.ingresar_nombre.text()
        elif self.campo == 'retirar-nombre':
            var_texto=self.ingresar_nombre_out.text()

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
        self.Ingresar_guardar_teclado_numerico()
        self.Ingresar_guardar_teclado()
        self.Retirar_guardar_teclado()

    def fun_numero_ENTER(self):
        self.Retirar_guardar_teclado()
        self.Ingresar_guardar_teclado_numerico()
        self.Ingresar_guardar_teclado()
        self.Retirar_guardar_teclado()

    def fun_numero_BORRAR(self):
        if self.campo == 'ingresar-cedula':
            var_texto=self.ingresar_cedula.text()
        elif self.campo == 'ingresar-temp':
            var_texto=self.ingresar_temp.text()
        elif self.campo == 'retirar-cedula':
            var_texto=self.ingresar_cedula_out.text()

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