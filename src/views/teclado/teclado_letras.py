from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TecladoLetras:

    def BotonesTeclado(self,widget):
        sep_lado = 12
        sep_arriba = 12
        base = 73
        altura = 65
        y_inicia = 350
        
        x=0
        y=0
        self.letra_q = QToolButton(widget)
        self.letra_q.setText('q')
        self.letra_q.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_q.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_q.clicked.connect(self.q)
        

        x=1
        y=0
        self.letra_w = QToolButton(widget)
        self.letra_w.setText('w')
        self.letra_w.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_w.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_w.clicked.connect(self.w)
        

        x=2
        y=0
        self.letra_e = QToolButton(widget)
        self.letra_e.setText('e')
        self.letra_e.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_e.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_e.clicked.connect(self.e)
        
        x=3
        y=0
        self.letra_r = QToolButton(widget)
        self.letra_r.setText('r')
        self.letra_r.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_r.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_r.clicked.connect(self.r)

        x=4
        y=0
        self.letra_t = QToolButton(widget)
        self.letra_t.setText('t')
        self.letra_t.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_t.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_t.clicked.connect(self.t)

        x=5
        y=0
        self.letra_y = QToolButton(widget)
        self.letra_y.setText('y')
        self.letra_y.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_y.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_y.clicked.connect(self.yy)

        x=6
        y=0
        self.letra_u = QToolButton(widget)
        self.letra_u.setText('u')
        self.letra_u.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_u.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_u.clicked.connect(self.u)

        x=7
        y=0
        self.letra_i = QToolButton(widget)
        self.letra_i.setText('i')
        self.letra_i.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_i.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_i.clicked.connect(self.i)

        x=8
        y=0
        self.letra_o = QToolButton(widget)
        self.letra_o.setText('o')
        self.letra_o.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_o.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_o.clicked.connect(self.o)

        x=9
        y=0
        self.letra_p = QToolButton(widget)
        self.letra_p.setText('p')
        self.letra_p.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_p.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_p.clicked.connect(self.p)

        x=10
        y=0
        self.letra_BORRAR = QToolButton(widget)
        self.letra_BORRAR.setText('Borrar')
        self.letra_BORRAR.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_BORRAR.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + sep_arriba, base*2, altura)
        self.letra_BORRAR.clicked.connect(self.BORRAR)

        x=0
        y=1
        self.letra_a = QToolButton(widget)
        self.letra_a.setText('a')
        self.letra_a.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_a.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_a.clicked.connect(self.a)

        x=1
        y=1
        self.letra_s = QToolButton(widget)
        self.letra_s.setText('s')
        self.letra_s.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_s.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_s.clicked.connect(self.s)

        x=2
        y=1
        self.letra_d = QToolButton(widget)
        self.letra_d.setText('d')
        self.letra_d.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_d.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_d.clicked.connect(self.d)

        x=3
        y=1
        self.letra_f = QToolButton(widget)
        self.letra_f.setText('f')
        self.letra_f.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_f.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_f.clicked.connect(self.f)

        x=4
        y=1
        self.letra_g = QToolButton(widget)
        self.letra_g.setText('g')
        self.letra_g.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_g.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_g.clicked.connect(self.g)

        x=5
        y=1
        self.letra_h = QToolButton(widget)
        self.letra_h.setText('h')
        self.letra_h.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_h.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_h.clicked.connect(self.h)

        x=6
        y=1
        self.letra_j = QToolButton(widget)
        self.letra_j.setText('j')
        self.letra_j.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_j.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_j.clicked.connect(self.j)

        x=7
        y=1
        self.letra_k = QToolButton(widget)
        self.letra_k.setText('k')
        self.letra_k.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_k.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_k.clicked.connect(self.k)

        x=8
        y=1
        self.letra_l = QToolButton(widget)
        self.letra_l.setText('l')
        self.letra_l.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_l.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_l.clicked.connect(self.l)

        x=9
        y=1
        self.letra_ene = QToolButton(widget)
        self.letra_ene.setText('ñ')
        self.letra_ene.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_ene.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base, altura)
        self.letra_ene.clicked.connect(self.ene)

        x=10
        y=1
        self.letra_MAYUS = QToolButton(widget)
        self.letra_MAYUS.setText('Mayus')
        self.letra_MAYUS.setObjectName("buttonTecladoMAYUS") #nombre de enlace a css
        self.letra_MAYUS.setGeometry((base*x) + (x+1)*sep_lado,y*sep_arriba+ y_inicia+ (altura*y) + sep_arriba, base*2, altura)
        self.letra_MAYUS.clicked.connect(self.MAYUS)
        self.isMAYUS=False

        x=0
        y=2
        self.letra_z = QToolButton(widget)
        self.letra_z.setText('z')
        self.letra_z.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_z.setGeometry((base*x) + (x+1)*sep_lado, y_inicia + (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_z.clicked.connect(self.z)
        

        x=1
        y=2
        self.letra_x = QToolButton(widget)
        self.letra_x.setText('x')
        self.letra_x.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_x.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_x.clicked.connect(self.xx)
        

        x=2
        y=2
        self.letra_c = QToolButton(widget)
        self.letra_c.setText('c')
        self.letra_c.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_c.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_c.clicked.connect(self.c)
        
        x=3
        y=2
        self.letra_v = QToolButton(widget)
        self.letra_v.setText('v')
        self.letra_v.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_v.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_v.clicked.connect(self.v)

        x=7
        y=2
        self.letra_SPACE = QToolButton(widget)
        self.letra_SPACE.setText('')
        self.letra_SPACE.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_SPACE.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba,2*sep_lado+ 4*base, altura)
        self.letra_SPACE.clicked.connect(self.SPACE)

        x=4
        y=2
        self.letra_b = QToolButton(widget)
        self.letra_b.setText('b')
        self.letra_b.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_b.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_b.clicked.connect(self.b)

        x=5
        y=2
        self.letra_n = QToolButton(widget)
        self.letra_n.setText('n')
        self.letra_n.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_n.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_n.clicked.connect(self.n)

        x=6
        y=2
        self.letra_m = QToolButton(widget)
        self.letra_m.setText('m')
        self.letra_m.setObjectName("buttonTeclado") #nombre de enlace a css
        self.letra_m.setGeometry((base*x) + (x+1)*sep_lado, y_inicia+ (altura*y) + (y+1)*sep_arriba, base, altura)
        self.letra_m.clicked.connect(self.m)

        x=11
        y=2
        self.letra_ENTER = QToolButton(widget)
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
                texto = self.salida_nombre.text() + 'q'
            else:
                texto = self.salida_nombre.text() + 'Q'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'q'
            else:
                texto = self.avanzada_user.text() + 'Q'
            self.avanzada_user.setText(texto)
        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'q'
            else:
                texto = self.avanzada_user.text() + 'Q'
            self.avanzada_user.setText(texto)

    def w(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'w'
            else:
                texto = self.ingresar_nombre.text() + 'W'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'w'
            else:
                texto = self.salida_nombre.text() + 'W'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'w'
            else:
                texto = self.avanzada_user.text() + 'W'
            self.avanzada_user.setText(texto)

    def e(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'e'
            else:
                texto = self.ingresar_nombre.text() + 'E'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'e'
            else:
                texto = self.salida_nombre.text() + 'E'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'e'
            else:
                texto = self.avanzada_user.text() + 'E'
            self.avanzada_user.setText(texto)

    def r(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'r'
            else:
                texto = self.ingresar_nombre.text() + 'R'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'r'
            else:
                texto = self.salida_nombre.text() + 'R'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'r'
            else:
                texto = self.avanzada_user.text() + 'R'
            self.avanzada_user.setText(texto)

    def t(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 't'
            else:
                texto = self.ingresar_nombre.text() + 'T'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 't'
            else:
                texto = self.salida_nombre.text() + 'T'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 't'
            else:
                texto = self.avanzada_user.text() + 'T'
            self.avanzada_user.setText(texto)

    def yy(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'y'
            else:
                texto = self.ingresar_nombre.text() + 'Y'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'y'
            else:
                texto = self.salida_nombre.text() + 'Y'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'y'
            else:
                texto = self.avanzada_user.text() + 'Y'
            self.avanzada_user.setText(texto)
    
    def u(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'u'
            else:
                texto = self.ingresar_nombre.text() + 'U'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'u'
            else:
                texto = self.salida_nombre.text() + 'U'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'u'
            else:
                texto = self.avanzada_user.text() + 'U'
            self.avanzada_user.setText(texto)

    def i(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'i'
            else:
                texto = self.ingresar_nombre.text() + 'I'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'i'
            else:
                texto = self.salida_nombre.text() + 'I'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'i'
            else:
                texto = self.avanzada_user.text() + 'I'
            self.avanzada_user.setText(texto)

    def o(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'o'
            else:
                texto = self.ingresar_nombre.text() + 'O'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'o'
            else:
                texto = self.salida_nombre.text() + 'O'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'o'
            else:
                texto = self.avanzada_user.text() + 'O'
            self.avanzada_user.setText(texto)

    def p(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'p'
            else:
                texto = self.ingresar_nombre.text() + 'P'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'p'
            else:
                texto = self.salida_nombre.text() + 'P'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'p'
            else:
                texto = self.avanzada_user.text() + 'P'
            self.avanzada_user.setText(texto)

    def a(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'a'
            else:
                texto = self.ingresar_nombre.text() + 'A'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'a'
            else:
                texto = self.salida_nombre.text() + 'A'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'a'
            else:
                texto = self.avanzada_user.text() + 'A'
            self.avanzada_user.setText(texto)

    def s(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 's'
            else:
                texto = self.ingresar_nombre.text() + 'S'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 's'
            else:
                texto = self.salida_nombre.text() + 'S'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 's'
            else:
                texto = self.avanzada_user.text() + 'S'
            self.avanzada_user.setText(texto)

    def d(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'd'
            else:
                texto = self.ingresar_nombre.text() + 'D'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'd'
            else:
                texto = self.salida_nombre.text() + 'D'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'd'
            else:
                texto = self.avanzada_user.text() + 'D'
            self.avanzada_user.setText(texto)

    def f(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'f'
            else:
                texto = self.ingresar_nombre.text() + 'F'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'f'
            else:
                texto = self.salida_nombre.text() + 'F'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'f'
            else:
                texto = self.avanzada_user.text() + 'F'
            self.avanzada_user.setText(texto)

    def g(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'g'
            else:
                texto = self.ingresar_nombre.text() + 'G'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'g'
            else:
                texto = self.salida_nombre.text() + 'G'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'g'
            else:
                texto = self.avanzada_user.text() + 'G'
            self.avanzada_user.setText(texto)

    def h(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'h'
            else:
                texto = self.ingresar_nombre.text() + 'H'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'h'
            else:
                texto = self.salida_nombre.text() + 'H'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'h'
            else:
                texto = self.avanzada_user.text() + 'H'
            self.avanzada_user.setText(texto)

    def j(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'j'
            else:
                texto = self.ingresar_nombre.text() + 'J'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'j'
            else:
                texto = self.salida_nombre.text() + 'J'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'j'
            else:
                texto = self.avanzada_user.text() + 'J'
            self.avanzada_user.setText(texto)

    def k(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'k'
            else:
                texto = self.ingresar_nombre.text() + 'K'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'k'
            else:
                texto = self.salida_nombre.text() + 'K'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'k'
            else:
                texto = self.avanzada_user.text() + 'K'
            self.avanzada_user.setText(texto)

    def l(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'l'
            else:
                texto = self.ingresar_nombre.text() + 'L'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'l'
            else:
                texto = self.salida_nombre.text() + 'L'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'l'
            else:
                texto = self.avanzada_user.text() + 'L'
            self.avanzada_user.setText(texto)

    def ene(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'ñ'
            else:
                texto = self.ingresar_nombre.text() + 'Ñ'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'ñ'
            else:
                texto = self.salida_nombre.text() + 'Ñ'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'ñ'
            else:
                texto = self.avanzada_user.text() + 'Ñ'
            self.avanzada_user.setText(texto)

    def z(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'z'
            else:
                texto = self.ingresar_nombre.text() + 'Z'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'z'
            else:
                texto = self.salida_nombre.text() + 'Z'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'z'
            else:
                texto = self.avanzada_user.text() + 'Z'
            self.avanzada_user.setText(texto)

    def xx(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'x'
            else:
                texto = self.ingresar_nombre.text() + 'X'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'x'
            else:
                texto = self.salida_nombre.text() + 'X'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'x'
            else:
                texto = self.avanzada_user.text() + 'X'
            self.avanzada_user.setText(texto)

    def c(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'c'
            else:
                texto = self.ingresar_nombre.text() + 'C'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'c'
            else:
                texto = self.salida_nombre.text() + 'C'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'c'
            else:
                texto = self.avanzada_user.text() + 'C'
            self.avanzada_user.setText(texto)

    def v(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'v'
            else:
                texto = self.ingresar_nombre.text() + 'V'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'v'
            else:
                texto = self.salida_nombre.text() + 'V'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'v'
            else:
                texto = self.avanzada_user.text() + 'V'
            self.avanzada_user.setText(texto)

    def b(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'b'
            else:
                texto = self.ingresar_nombre.text() + 'B'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'b'
            else:
                texto = self.salida_nombre.text() + 'B'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'b'
            else:
                texto = self.avanzada_user.text() + 'B'
            self.avanzada_user.setText(texto)

    def n(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'n'
            else:
                texto = self.ingresar_nombre.text() + 'N'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'n'
            else:
                texto = self.salida_nombre.text() + 'N'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'n'
            else:
                texto = self.avanzada_user.text() + 'N'
            self.avanzada_user.setText(texto)

    def m(self):
        if self.campo == 'ingresar-nombre':
            if not self.isMAYUS:
                texto = self.ingresar_nombre.text() + 'm'
            else:
                texto = self.ingresar_nombre.text() + 'M'
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            if not self.isMAYUS:
                texto = self.salida_nombre.text() + 'm'
            else:
                texto = self.salida_nombre.text() + 'M'
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':
            if not self.isMAYUS:
                texto = self.avanzada_user.text() + 'm'
            else:
                texto = self.avanzada_user.text() + 'M'
            self.avanzada_user.setText(texto)

    def SPACE(self):
        if self.campo == 'ingresar-nombre':
            
            texto = self.ingresar_nombre.text() + ' '
            self.ingresar_nombre.setText(texto)

        elif self.campo == 'retirar-nombre':
            
            texto = self.salida_nombre.text() + ' '
            self.salida_nombre.setText(texto)

        elif self.campo == 'AdConf-User':

            texto = self.avanzada_user.text() + ' '
            self.avanzada_user.setText(texto)

    def BORRAR(self):
        if self.campo == 'ingresar-nombre':
            var_texto=self.ingresar_nombre.text()
        elif self.campo == 'retirar-nombre':
            var_texto=self.salida_nombre.text()
        elif self.campo == 'AdConf-User':
            var_texto=self.avanzada_user.text()

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
            self.salida_nombre.setText(texto)
        elif self.campo == 'AdConf-User':
            self.avanzada_user.setText(texto)

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
        self.Ingresar_guardar_teclado()
        self.Ad_Conf_guardar_teclado()


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