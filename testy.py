import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3
from scipy import signal
import matplotlib.pyplot as plt

from sympy import (
    init_printing, symbols, arg, I, plot, pi,
    lambdify, Heaviside, exp
)
init_printing()


class Menu_Screen (QDialog):
    def __init__(self):
        super(Menu_Screen, self).__init__()
        loadUi("Menu.ui", self)
        self.P1.clicked.connect(self.gotoPrimer_Orden)
        self.P2.clicked.connect(self.gotoSegundo_Orden)
        self.RLC.clicked.connect(self.gotoRLC)

    def gotoPrimer_Orden(self):
        Primer_Orden = P1_Screen()
        widget1.addWidget(Primer_Orden)
        widget1.setCurrentIndex(widget1.currentIndex()+1)

    def gotoSegundo_Orden(self):
        Segundo_Orden = P2_Screen()
        widget1.addWidget(Segundo_Orden)
        widget1.setCurrentIndex(widget1.currentIndex()+1)

    def gotoRLC(self):
        RLC = RLC_Screen()
        widget1.addWidget(RLC)
        widget1.setCurrentIndex(widget1.currentIndex()+1)

###################################################################################################

class P1_Screen(QDialog):
    def __init__(self):
        super(P1_Screen, self).__init__()
        loadUi("P1.ui", self)
        self.Back_P1.clicked.connect(self.gotoBack_P1)
        self.P1_Continuar.clicked.connect(self.gotoP1_Continuar)


    def gotoBack_P1(self):
        Back_P1 = Menu_Screen()
        widget1.addWidget(Back_P1)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP1_Continuar(self):
        if((self.P1_Input.currentIndex() == 0)):
            P1_Continuar = P1_Senoide_Screen()
        else:
            P1_Continuar = P1_Pulso_Screen()
        widget1.addWidget(P1_Continuar)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)


############################################################################################

class P2_Screen(QDialog):
    def __init__(self):
        super(P2_Screen, self).__init__()
        loadUi("P2.ui", self)
        self.Back_P2.clicked.connect(self.gotoBack_P2)
        self.P2_Continuar.clicked.connect(self.gotoP2_Continuar)

    def gotoBack_P2(self):
        Back_P2 = Menu_Screen()
        widget1.addWidget(Back_P2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar(self):
        if((self.P2_Input.currentIndex() == 0)):
            P2_Continuar = P2_Senoide_Screen()
        else:
            P2_Continuar = P2_Pulso_Screen()
        widget1.addWidget(P2_Continuar)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)



############################################################################################


class RLC_Screen(QDialog):
    def __init__(self):
        super(RLC_Screen, self).__init__()
        loadUi("Circuito_RLC_serie.ui", self)
        self.Back_RLC.clicked.connect(self.gotoBack_RLC)

    def gotoBack_RLC (self):
        Back_RLC = Menu_Screen()
        widget1.addWidget(Back_RLC)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)



############################################################################################


class P1_Senoide_Screen(QDialog):
    def __init__(self):
        super(P1_Senoide_Screen, self).__init__()
        loadUi("P1_Senoide.ui", self)
        self.Back_P1_Senoide.clicked.connect(self.gotoBack_P1_Senoide)
        self.P1_Continuar_Senoide.clicked.connect(self.gotoP1_Continuar_Senoide)

    def gotoBack_P1_Senoide(self):
        Back_P1_Senoide = P1_Screen()
        widget1.addWidget(Back_P1_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP1_Continuar_Senoide(self):
        P1senoideP = float(self.P1_P_Senoide.text())
        #P1senoideF = float(self.P1_F_Senoide.text())
        #P1senoideA = float(self.P1_A_Senoide.text())
        #P1senoideC = float(self.P1_C_Senoide.text())
        P1senoideG = float(self.P1_G_Senoide.text())

        sys = signal.TransferFunction([P1senoideG], [1/P1senoideP, 1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()



class P1_Pulso_Screen(QDialog):
    def __init__(self):
        super(P1_Pulso_Screen, self).__init__()
        loadUi("P1_Pulso.ui", self)
        self.Back_P1_Pulso.clicked.connect(self.gotoBack_P1_Pulso)
        self.P1_Continuar_Pulso.clicked.connect(self.gotoP1_Continuar_Pulso)

    def gotoBack_P1_Pulso(self):
        Back_P1_Pulso = P1_Screen()
        widget1.addWidget(Back_P1_Pulso)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP1_Continuar_Pulso(self):
        P1pulsoA = float(self.P1_A_Pulso.text())
        P1pulsoP = float(self.P1_P_Pulso.text())
        P1pulsoC = float(self.P1_C_Pulso.text())
        P1pulsoG = float(self.P1_G_Pulso.text())

class P2_Senoide_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        P2senoideF = float(self.P1_F_Senoide.text())
        P2senoideA = float(self.P1_A_Senoide.text())
        P2senoideP = float(self.P1_P_Senoide.text())
        P2senoideC = float(self.P1_C_Senoide.text())
        P2senoideG = float(self.P1_G_Senoide.text())
        P2senoideW0 = float(self.P1_W0_Senoide.text())
        P2senoidePHI = float(self.P1_PHI_Senoide.text())

class P2_Pulso_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_Screen, self).__init__()
        loadUi("P2_Pulso.ui", self)
        self.Back_P2_Pulso.clicked.connect(self.gotoBack_P2_Pulso)
        self.P2_Continuar_Pulso.clicked.connect(self.gotoP2_Continuar_Pulso)

    def gotoBack_P2_Pulso(self):
        Back_P2_Pulso = P2_Screen()
        widget1.addWidget(Back_P2_Pulso)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Pulso(self):
        P2pulsoA = float(self.P1_A_Pulso.text())
        P2pulsoP = float(self.P1_P_Pulso.text())
        P2pulsoC = float(self.P1_C_Pulso.text())
        P2pulsoG = float(self.P1_G_Pulso.text())
        P2pulsoW0 = float(self.P1_W0_Pulso.text())
        P2pulsoPHI = float(self.P1_PHI_Pulso.text())


############################################################################################






#main

app = QApplication(sys.argv)
menu = Menu_Screen()
widget1 = QtWidgets.QStackedWidget()
widget1.addWidget(menu)
widget1.setFixedHeight(700)
widget1.setFixedWidth(900)

widget1.show()

try:
    sys.exit(app.exec_())
except:
    print("Closing...")