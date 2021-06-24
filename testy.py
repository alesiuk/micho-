import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3

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
        #self.P11_Continuar.clicked.connect(self.gotoP1_Continuar1)

    def gotoBack_P1_Senoide(self):
        Back_P1_Senoide = P1_Screen()
        widget1.addWidget(Back_P1_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

class P1_Pulso_Screen(QDialog):
    def __init__(self):
        super(P1_Pulso_Screen, self).__init__()
        loadUi("P1_Pulso.ui", self)
        self.Back_P1_Pulso.clicked.connect(self.gotoBack_P1_Pulso)
        #self.P11_Continuar.clicked.connect(self.gotoP1_Continuar1)

    def gotoBack_P1_Pulso(self):
        Back_P1_Pulso = P1_Screen()
        widget1.addWidget(Back_P1_Pulso)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

class P2_Senoide_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        #self.P11_Continuar.clicked.connect(self.gotoP1_Continuar1)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

class P2_Pulso_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_Screen, self).__init__()
        loadUi("P2_Pulso.ui", self)
        self.Back_P2_Pulso.clicked.connect(self.gotoBack_P2_Pulso)
        #self.P11_Continuar.clicked.connect(self.gotoP1_Continuar1)

    def gotoBack_P2_Pulso(self):
        Back_P2_Pulso = P2_Screen()
        widget1.addWidget(Back_P2_Pulso)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)


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
