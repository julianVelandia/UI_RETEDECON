from src.views.teclado.teclado_letras import *
from src.views.teclado.teclado_numeros import *
from PyQt5.QtMultimedia import QSound
# from main import alarm

class Funciones:
    pantalla = 'inicio'

    def HomeWindow(self):
        self.pantalla = 'inicio'

        # imagen central
        self.label_img_central.setVisible(False)
        self.atras.setVisible(False)

        # inicio
        self.label_img_esquina.setVisible(True)
        self.label_img_esquina_2.setVisible(False)

        self.ingresar.setVisible(True)
        self.estadisticas.setVisible(True)
        self.detener_alarma.setVisible(True)
        self.salida_manual.setVisible(True)
        self.configuracion.setVisible(True)
        self.informacion.setVisible(True)

        # ingresar
        self.ingresar_nombre.setVisible(False)
        self.ingresar_cedula.setVisible(False)
        self.ingresar_temp.setVisible(False)
        self.ingresar_ingresar.setVisible(False)

        # salida
        self.salida_nombre.setVisible(False)
        self.salida_cedula.setVisible(False)
        self.salida_salida.setVisible(False)

        # configuraciones
        self.configuraciones_ajustes.setVisible(False)
        self.configuraciones_apagar.setVisible(False)
        self.configuraciones_datos.setVisible(False)
        self.configuraciones_avanzada.setVisible(False)

        # Datos
        self.datos_barras.setVisible(False)
        self.datos_pie.setVisible(False)

        # informacion
        self.informacion_manual.setVisible(False)
        self.informacion_fabricante.setVisible(False)
        self.informacion_qr.setVisible(False)
        self.informacion_label.setVisible(False)

        # estadisticas
        self.estadisticas_ocupacion.setVisible(False)
        self.estadisticas_duracion.setVisible(False)
        self.estadisticas_personasDia.setVisible(False)
        self.estadisticas_cambiar_semana_adelante.setVisible(False)
        self.estadisticas_cambiar_semana_atras.setVisible(False)
        self.estadisticas_barras.setVisible(False)
        self.estadisticas_torta.setVisible(False)
        self.estadisticas_bar_chart.setVisible(False)
        self.estadisticas_pie_chart.setVisible(False)

        # avanzada
        self.avanzada_user.setVisible(False)
        self.avanzada_pass.setVisible(False)
        self.avanzada_ingresar.setVisible(False)

        # inside
        self.inside_agregar.setVisible(False)
        self.inside_enviar.setVisible(False)
        self.inside_cambiar.setVisible(False)
        self.inside_capacidad.setVisible(False)
        self.inside_eliminar.setVisible(False)

        # agregar
        self.agregar_username.setVisible(False)
        self.agregar_pass.setVisible(False)
        self.agregar_agregar.setVisible(False)

        # eliminar
        self.eliminar_username.setVisible(False)
        self.eliminar_pass.setVisible(False)
        self.eliminar_eliminar.setVisible(False)

        # capacidad
        self.capacidad_newcapacidad.setVisible(False)
        self.capacidad_setnew.setVisible(False)

        # cambiar
        self.cambiar_user.setVisible(False)
        self.cambiar_pass.setVisible(False)
        self.pass_new_0.setVisible(False)
        self.pass_new_1.setVisible(False)
        self.cambiar_cambiar.setVisible(False)

        TecladoLetras.NotTeclado(self)
        TecladoNumeros.NotTecladoNumerico(self)

    def Ingresar(self):
        self.pantalla = 'ingresar'

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
        self.pantalla = 'estadisticas'

        self.label_img_central.setVisible(False)
        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)
        self.estadisticas_ocupacion.setVisible(True)
        self.estadisticas_duracion.setVisible(True)
        self.estadisticas_personasDia.setVisible(True)
        self.estadisticas_cambiar_semana_adelante.setVisible(True)
        self.estadisticas_cambiar_semana_atras.setVisible(True)
        self.estadisticas_barras.setVisible(True)
        self.estadisticas_torta.setVisible(True)

        self.EstadisticasOcupacion()
        #
        if self.SiBarrasNoPie:
            self.estadisticas_bar_chart.bara(self.EstadisticasGetInfo(), True)

            self.estadisticas_bar_chart.setVisible(True)
            self.estadisticas_pie_chart.setVisible(False)
        else:
            self.estadisticas_bar_chart.setVisible(False)
            self.estadisticas_pie_chart.setVisible(True)

    def DetenerAlarma(self):
        self.pantalla = 'detener'
        self.alarm.stop()
        self.HomeWindow()

    def Salida_manual(self):
        self.pantalla = 'salida'

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
        self.pantalla = 'configuracion'

        self.configuraciones_ajustes.setVisible(True)
        self.configuraciones_apagar.setVisible(True)
        self.configuraciones_avanzada.setVisible(True)
        self.configuraciones_datos.setVisible(True)
        self.label_img_esquina.setVisible(True)

        self.label_img_central.setVisible(False)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

    def Informacion(self):
        self.pantalla = 'informacion'

        self.informacion_manual.setVisible(True)
        self.informacion_fabricante.setVisible(True)

        self.label_img_esquina.setVisible(True)
        self.ingresar.setVisible(False)
        self.estadisticas.setVisible(False)
        self.detener_alarma.setVisible(False)
        self.salida_manual.setVisible(False)
        self.configuracion.setVisible(False)
        self.informacion.setVisible(False)

        self.label_img_central.setVisible(False)

    def Atras(self):
        if self.pantalla == 'datos' or self.pantalla == 'inside':
            self.pantalla = 'configuracion'
            self.HomeWindow()
            self.Configuracion()

        elif self.pantalla == 'agregar' or self.pantalla == 'eliminar' or self.pantalla == 'capacidad' or self.pantalla == 'cambiar':
            self.pantalla = 'inside'

            # agregar
            self.agregar_username.setVisible(False)
            self.agregar_pass.setVisible(False)
            self.agregar_agregar.setVisible(False)

            # eliminar
            self.eliminar_username.setVisible(False)
            self.eliminar_pass.setVisible(False)
            self.eliminar_eliminar.setVisible(False)

            # capacidad
            self.capacidad_newcapacidad.setVisible(False)
            self.capacidad_setnew.setVisible(False)
            self.AvanzadaInsideInside()

            # cambiar
            self.cambiar_user.setVisible(False)
            self.cambiar_pass.setVisible(False)
            self.pass_new_0.setVisible(False)
            self.pass_new_1.setVisible(False)
            self.cambiar_cambiar.setVisible(False)

        elif self.pantalla == 'manual' or self.pantalla == 'fabricante':
            self.HomeWindow()
            self.Informacion()
            self.pantalla = 'informacion'

    def checkState(self):
        if self.state == 0:
            self.s0()
        elif self.state == 1:
            self.s1()
        elif self.state == 2:
            self.s2()
        elif self.state == 3:
            self.s3()
        elif self.state == 4:
            self.s4()
        elif self.state == 5:
            self.s5()

    def s0(self):
        self.label_img_central.setVisible(False)
        self.movie0 = QMovie('src/views/static/gif/s0.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie0)
        self.giflabel.setVisible(True)
        self.movie0.start()

    def s1(self):
        self.movie1 = QMovie('src/views/static/gif/s1.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie1)
        self.giflabel.setVisible(True)
        self.movie1.start()

    def s2(self):
        self.movie2 = QMovie('src/views/static/gif/s2.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie2)
        self.giflabel.setVisible(True)
        self.movie2.start()

    def s3(self):
        self.movie3 = QMovie('src/views/static/gif/s3.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie3)
        self.giflabel.setVisible(True)
        self.movie3.start()

    def s4(self):
        self.movie4 = QMovie('src/views/static/gif/s4.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie4)
        self.giflabel.setVisible(True)
        self.movie4.start()

    def s5(self):
        self.movie5 = QMovie('src/views/static/gif/s5.gif')  # Gif paso 1
        self.giflabel.setMovie(self.movie5)
        self.giflabel.setVisible(True)
        self.movie5.start()
        self.alarm.play()

    ## botones de prueba

    def botonesPrueba(self, widget):
        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('Si')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.si)
        self.botonPrueba1.setGeometry(534, 210, 60, 60)
        self.botonPrueba1.setVisible(True)

        self.botonPrueba1 = QToolButton(widget)
        self.botonPrueba1.setText('No')
        self.botonPrueba1.setObjectName("small")  # nombre de enlace a css
        self.botonPrueba1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.botonPrueba1.clicked.connect(self.no)
        self.botonPrueba1.setGeometry(634, 210, 60, 60)
        self.botonPrueba1.setVisible(True)

    def si(self):
        self.state = (self.state+1)%5
        self.checkState()

    def no(self):
        self.state = 5
        self.checkState()
