import pandas as pd
from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *

class Funciones:
    def HomeWindow(self):
        #imagen central
        self.label_img_central.setVisible(False)

        #inicio
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(True)
        self.estadisticas.setVisible(True)
        self.detener_alarma.setVisible(True)
        self.salida_manual.setVisible(True)
        self.configuracion.setVisible(True)
        self.informacion.setVisible(True)

        #ingresar
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_ingresar.setVisible(False)

        #salida
        self.salida_nombre.setVisible(False)
        self.salida_cedula.setVisible(False)
        self.salida_salida.setVisible(False)

        #configuraciones        
        self.configuraciones_ajustes.setVisible(False)
        self.configuraciones_apagar.setVisible(False)
        self.configuraciones_datos.setVisible(False)
        self.configuraciones_avanzada.setVisible(False)

        #avanzada
        self.avanzada_user.setVisible(False)
        self.avanzada_pass.setVisible(False)
        self.avanzada_ingresar.setVisible(False)

        #inside
        self.inside_agregar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_eliminar.setVisible(False)

        #agregar
        self.agregar_username.setVisible(False)
        self.agregar_pass.setVisible(False)
        self.agregar_agregar.setVisible(False)

        #eliminar
        self.eliminar_username.setVisible(False)
        self.eliminar_pass.setVisible(False)
        self.eliminar_eliminar.setVisible(False)

        #capacidad
        self.capacidad_newcapacidad.setVisible(False)
        self.capacidad_setnew.setVisible(False)

        
        
        
        self.info_ocupacion_actual.setVisible(False)

        self.img_esquina_2.setVisible(False)
        self.qr_manual.setVisible(False)
        self.bar_chart.setVisible(False)
        self.pie_chart.setVisible(False)
        

        TecladoLetras.NotTeclado(self)
        TecladoNumeros.NotTecladoNumerico(self)
    
    
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


        self.salida_nombre.setVisible(False)
        self.salida_cedula.setVisible(False)
        self.salida_salida.setVisible(False)
        self.Ingresar_guardar_teclado()


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

        df = pd.read_csv('src/models/data/DB.csv')
        Lista = df['IsIn']
        print(Lista)
        self.ocupacion_actual =0
        for i in Lista:
            if i == True:
                self.ocupacion_actual +=1
        print('Ocupacion Actual: '+str(self.ocupacion_actual))
        self.info_ocupacion_actual.setText('Ocupación Actual: ' + str(self.ocupacion_actual))

        self.bar_chart.setVisible(True)
        #self.pie_chart.setVisible(True) #tambien esta configurado como torta
        #ACÁ CREA LA GRAFICA PERO POR EL MOMENTO LO HACE EN UNA VENTANA NUEVA
        ######
        '''
        self.create_bar()
        
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

        #xdict = dict(enumerate(x))
        '''

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

        self.salida_nombre.setVisible(True)
        self.salida_nombre.clear()

        self.salida_cedula.setVisible(True)
        self.salida_cedula.clear()

        self.salida_salida.setVisible(True)
        
        self.ingresar_ingresar.setVisible(False)
        self.Retirar_guardar_teclado()

    def Configuracion(self):        
        self.configuraciones_ajustes.setVisible(True)
        self.configuraciones_apagar.setVisible(True)
        self.configuraciones_avanzada.setVisible(True)
        self.configuraciones_datos.setVisible(True)

        self.label_img_central.setVisible(False)  
        self.label_img_esquina.setVisible(True)  
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)