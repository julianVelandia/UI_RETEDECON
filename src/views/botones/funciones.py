



class Funciones:
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
        self.bar_chart.setVisible(False)
        self.pie_chart.setVisible(False)
        self.NotTeclado()
        self.NotTecladoNumerico()