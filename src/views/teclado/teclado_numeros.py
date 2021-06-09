from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from screeninfo import get_monitors


class TecladoNumeros:

    width = get_monitors()[0].width
    height = get_monitors()[0].height


    def BotonesTecladoNumerico(self,widget):
        

        sep_lado = self.width/62
        sep_arriba = self.width/62
        base = self.width/15
        altura = self.width/17
        y_inicia = self.width/3.4
        x_inicia =self.width/3.5

        x=0
        y=0
        self.numero_7 = QToolButton(widget)
        self.numero_7.setText('7')
        self.numero_7.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_7.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_7.clicked.connect(self.fun_numero_7)

        x=1
        y=0
        self.numero_8 = QToolButton(widget)
        self.numero_8.setText('8')
        self.numero_8.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_8.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_8.clicked.connect(self.fun_numero_8)

        x=2
        y=0
        self.numero_9 = QToolButton(widget)
        self.numero_9.setText('9')
        self.numero_9.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_9.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.numero_9.clicked.connect(self.fun_numero_9)

        x=3
        y=0
        self.numero_BORRAR = QToolButton(widget)
        self.numero_BORRAR.setText('Borrar')
        self.numero_BORRAR.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_BORRAR.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base*2+sep_lado, altura)
        self.numero_BORRAR.clicked.connect(self.fun_numero_BORRAR)

        x=0
        y=1
        self.numero_4 = QToolButton(widget)
        self.numero_4.setText('4')
        self.numero_4.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_4.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_4.clicked.connect(self.fun_numero_4)

        x=1
        y=1
        self.numero_5 = QToolButton(widget)
        self.numero_5.setText('5')
        self.numero_5.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_5.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_5.clicked.connect(self.fun_numero_5)

        x=2
        y=1
        self.numero_6 = QToolButton(widget)
        self.numero_6.setText('6')
        self.numero_6.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_6.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_6.clicked.connect(self.fun_numero_6)

        x=3
        y=1
        self.numero_PUNTO = QToolButton(widget)
        self.numero_PUNTO.setText('.')
        self.numero_PUNTO.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_PUNTO.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura)
        self.numero_PUNTO.clicked.connect(self.fun_numero_PUNTO)

        x=4
        y=1
        self.numero_ENTER = QToolButton(widget)
        self.numero_ENTER.setText(chr(16))
        self.numero_ENTER.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_ENTER.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 2*sep_arriba, base, altura*2+sep_arriba)
        self.numero_ENTER.clicked.connect(self.fun_numero_ENTER)

        x=0
        y=2
        self.numero_1 = QToolButton(widget)
        self.numero_1.setText('1')
        self.numero_1.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_1.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_1.clicked.connect(self.fun_numero_1)
        
        x=1
        y=2
        self.numero_2 = QToolButton(widget)
        self.numero_2.setText('2')
        self.numero_2.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_2.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_2.clicked.connect(self.fun_numero_2)

        x=2
        y=2
        self.numero_3 = QToolButton(widget)
        self.numero_3.setText('3')
        self.numero_3.setObjectName("buttonTeclado") #nombre de enlace a css
        self.numero_3.setGeometry(x_inicia+(base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + 3*sep_arriba, base, altura)
        self.numero_3.clicked.connect(self.fun_numero_3)

        x=3
        y=2
        self.numero_0 = QToolButton(widget)
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
        self.Eliminar_guardar_teclado()
        self.Capacidad_guardar_teclado()
        self.Cambiar_guardar_teclado()
        self.Agregar_guardar_teclado()

    def fun_numero_BORRAR(self):
        if self.campo == 'ingresar-cedula':
            var_texto=self.ingresar_cedula.text()
        elif self.campo == 'ingresar-temp':
            var_texto=self.ingresar_temp.text()
        elif self.campo == 'retirar-cedula':
            var_texto=self.salida_cedula.text()
        elif self.campo == 'AdConf-Pass':
            var_texto=self.avanzada_pass.text()
        elif self.campo == 'Agregar-Pass':
            var_texto=self.agregar_pass.text()
        elif self.campo == 'Cambiar-Pass':
            var_texto=self.cambiar_pass.text()
        elif self.campo == 'Cambiar-Pass0':
            var_texto=self.pass_new_0.text()
        elif self.campo == 'Cambiar-Pass1':
            var_texto=self.pass_new_1.text()
        elif self.campo == 'New-Capacidad':
            var_texto=self.capacidad_newcapacidad.text()
        elif self.campo == 'Eliminar-Pass':
            var_texto=self.eliminar_pass.text()
        

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
            self.salida_cedula.setText(texto)
        elif self.campo == 'AdConf-Pass':
            self.avanzada_pass.setText(texto)
        elif self.campo == 'Agregar-Pass':
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            self.eliminar_pass.setText(texto)

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
            texto = self.salida_cedula.text() + '1'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '1'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '1'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '1'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '1'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '1'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '1'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '1'
            self.eliminar_pass.setText(texto)

    def fun_numero_2(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '2'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '2'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '2'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '2'
            self.avanzada_pass.setText(texto)


        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '2'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() +'2'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '2'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '2'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '2'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '2'
            self.eliminar_pass.setText(texto)


    def fun_numero_3(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '3'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '3'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '3'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '3'
            self.avanzada_pass.setText(texto)


        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '3'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '3'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '3'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() +'3'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '3'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '3'
            self.eliminar_pass.setText(texto)


    def fun_numero_4(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '4'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '4'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '4'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '4'
            self.avanzada_pass.setText(texto)


        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '4'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '4'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '4'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '4'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '4'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '4'
            self.eliminar_pass.setText(texto)


    def fun_numero_5(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '5'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '5'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '5'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '5'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '5'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '5'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '5'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '5'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '5'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '5'
            self.eliminar_pass.setText(texto)


    def fun_numero_6(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '6'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '6'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '6'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '6'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '6'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '6'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '6'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '6'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '6'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '6'
            self.eliminar_pass.setText(texto)


    def fun_numero_7(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '7'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '7'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '7'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '7'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() +'7'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() +'7'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() +'7'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '7'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() +'7'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() +'7'
            self.eliminar_pass.setText(texto)


    def fun_numero_8(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '8'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '8'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '8'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '8'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '8'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '8'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '8'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '8'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '8'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '8'
            self.eliminar_pass.setText(texto)


    def fun_numero_9(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '9'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '9'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '9'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '9'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '9'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '9'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '9'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '9'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '9'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() + '9'
            self.eliminar_pass.setText(texto)


    def fun_numero_0(self):
        if self.campo == 'ingresar-cedula':
            texto = self.ingresar_cedula.text() + '0'
            self.ingresar_cedula.setText(texto)

        elif self.campo == 'ingresar-temp':
            
            texto = self.ingresar_temp.text() + '0'
            self.ingresar_temp.setText(texto)

        elif self.campo == 'retirar-cedula':
            texto = self.salida_cedula.text() + '0'
            self.salida_cedula.setText(texto)

        elif self.campo == 'AdConf-Pass':
            texto = self.avanzada_pass.text() + '0'
            self.avanzada_pass.setText(texto)

        elif self.campo == 'Agregar-Pass':
            texto = self.agregar_pass.text() + '0'
            self.agregar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass':
            texto = self.cambiar_pass.text() + '0'
            self.cambiar_pass.setText(texto)
        elif self.campo == 'Cambiar-Pass0':
            texto = self.pass_new_0.text() + '0'
            self.pass_new_0.setText(texto)
        elif self.campo == 'Cambiar-Pass1':
            texto = self.pass_new_1.text() + '0'
            self.pass_new_1.setText(texto)
        elif self.campo == 'New-Capacidad':
            texto = self.capacidad_newcapacidad.text() + '0'
            self.capacidad_newcapacidad.setText(texto)
        elif self.campo == 'Eliminar-Pass':
            texto = self.eliminar_pass.text() +'0'
            self.eliminar_pass.setText(texto)




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
