from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TecladoNumeros:
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
