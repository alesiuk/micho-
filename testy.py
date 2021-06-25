import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sqlite3
from scipy import signal
import matplotlib.pyplot as plt

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
        if ((self.P1_Input.currentIndex() == 0)):
            if ((self.P1_Filtro.currentIndex() == 0)):
                P1_Continuar = P1_Senoide_PB_Screen()
            if ((self.P1_Filtro.currentIndex() == 1)):
                P1_Continuar = P1_Senoide_PA_Screen()
            else:
                P1_Continuar = P1_Senoide_PT_Screen()
        else:
            if ((self.P1_Filtro.currentIndex() == 0)):
                P1_Continuar = P1_Pulso_PB_Screen()
            if ((self.P2_Filtro.currentIndex() == 1)):
                P1_Continuar = P1_Pulso_PA_Screen()
            else:
                P1_Continuar = P1_Pulso_PA_Screen()
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
        if ((self.P2_Input.currentIndex() == 0)):
            if ((self.P2_Filtro.currentIndex() == 0)):
                P2_Continuar = P2_Senoide_PB_Screen()
            if ((self.P2_Filtro.currentIndex() == 1)):
                P2_Continuar = P2_Senoide_PA_Screen()
            if ((self.P2_Filtro.currentIndex() == 2)):
                P2_Continuar = P2_Senoide_PT_Screen()
            if ((self.P2_Filtro.currentIndex() == 3)):
                P2_Continuar = P2_Senoide_PS_Screen()
            else:
                P2_Continuar = P2_Senoide_NT_Screen()

        else:
            if ((self.P2_Filtro.currentIndex() == 0)):
                P2_Continuar = P2_Pulso_PB_Screen()
            if ((self.P2_Filtro.currentIndex() == 1)):
                P2_Continuar = P2_Pulso_PA_Screen()
            if ((self.P2_Filtro.currentIndex() == 2)):
                P2_Continuar = P2_Pulso_PT_Screen()
            if ((self.P2_Filtro.currentIndex() == 3)):
                P2_Continuar = P2_Pulso_PS_Screen()
            else:
                P2_Continuar = P2_Pulso_NT_Screen()

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
############################################################################################



class P1_Senoide_PB_Screen(QDialog):
    def __init__(self):
        super(P1_Senoide_PB_Screen, self).__init__()
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

        if (len(self.P1_G_Senoide.text())== 0):
            P1senoideG=1.0
        else:
            P1senoideG = float(self.P1_G_Senoide.text())
        sys = signal.TransferFunction([P1senoideG], [1/P1senoideP, 1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        #plt.title("Diagrama de Fase")
        #plt.xlabel("Hz")
        #plt.ylabel(["|_H(jw)"])
        plt.show()

class P1_Senoide_PA_Screen(QDialog):
    def __init__(self):
        super(P1_Senoide_PA_Screen, self).__init__()
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

        if (len(self.P1_G_Senoide.text())== 0):
            P1senoideG=1.0
        else:
            P1senoideG = float(self.P1_G_Senoide.text())
        sys = signal.TransferFunction([P1senoideG], [1/P1senoideP, 1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        #plt.title("Diagrama de Fase")
        #plt.xlabel("Hz")
        #plt.ylabel(["|_H(jw)"])
        plt.show()

class P1_Senoide_PT_Screen(QDialog):
    def __init__(self):
        super(P1_Senoide_PT_Screen, self).__init__()
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

        if (len(self.P1_G_Senoide.text())== 0):
            P1senoideG=1.0
        else:
            P1senoideG = float(self.P1_G_Senoide.text())
        sys = signal.TransferFunction([P1senoideG], [1/P1senoideP, 1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        #plt.title("Diagrama de Fase")
        #plt.xlabel("Hz")
        #plt.ylabel(["|_H(jw)"])
        plt.show()


class P1_Pulso_PB_Screen(QDialog):
    def __init__(self):
        super(P1_Pulso_PB_Screen, self).__init__()
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

class P1_Pulso_PA_Screen(QDialog):
    def __init__(self):
        super(P1_Pulso_PB_Screen, self).__init__()
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

class P1_Pulso_PT_Screen(QDialog):
    def __init__(self):
        super(P1_Pulso_PB_Screen, self).__init__()
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



################################################################################
################################################################################

class P2_Senoide_PB_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_PB_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        #P2senoideF = float(self.P2_F_Senoide.text())
        #P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_P_Senoide.text())==0):
            P2senoideP = 1
        else:
            P2senoideP = float(self.P2_P_Senoide.text())
        #if (len(self.P2_C_Senoide.text()) == 0):
            #P2senoideC = 1
        #else:
            #P2senoideC = float(self.P2_C_Senoide.text())
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())

        sys = signal.TransferFunction([P2senoideG], [(1/P2senoideP)**2,2*(P2senoidePHI/P2senoideP), 1])
        w, mag, phase = signal.bode(sys)

        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel("|H(jw)|(dB)")
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel("|_H(jw)(º)")
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

class P2_Senoide_PA_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_PA_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        #P2senoideF = float(self.P2_F_Senoide.text())
        #P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_P_Senoide.text())==0):
            P2senoideP = 1
        else:
            P2senoideP = float(self.P2_P_Senoide.text())
        #if (len(self.P2_C_Senoide.text()) == 0):
            #P2senoideC = 1
        #else:
            #P2senoideC = float(self.P2_C_Senoide.text())
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())

        sys = signal.TransferFunction([P2senoideG], [(1/P2senoideP)**2,2*(P2senoidePHI/P2senoideP), 1])
        w, mag, phase = signal.bode(sys)

        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel("|H(jw)|(dB)")
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel("|_H(jw)(º)")
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

class P2_Senoide_PT_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_PT_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        #P2senoideF = float(self.P2_F_Senoide.text())
        #P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_P_Senoide.text())==0):
            P2senoideP = 1
        else:
            P2senoideP = float(self.P2_P_Senoide.text())
        #if (len(self.P2_C_Senoide.text()) == 0):
            #P2senoideC = 1
        #else:
            #P2senoideC = float(self.P2_C_Senoide.text())
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())

        sys = signal.TransferFunction([P2senoideG], [(1/P2senoideP)**2,2*(P2senoidePHI/P2senoideP), 1])
        w, mag, phase = signal.bode(sys)

        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel("|H(jw)|(dB)")
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel("|_H(jw)(º)")
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

class P2_Senoide_PS_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_PS_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        #P2senoideF = float(self.P2_F_Senoide.text())
        #P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_P_Senoide.text())==0):
            P2senoideP = 1
        else:
            P2senoideP = float(self.P2_P_Senoide.text())
        #if (len(self.P2_C_Senoide.text()) == 0):
            #P2senoideC = 1
        #else:
            #P2senoideC = float(self.P2_C_Senoide.text())
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())

        sys = signal.TransferFunction([P2senoideG], [(1/P2senoideP)**2,2*(P2senoidePHI/P2senoideP), 1])
        w, mag, phase = signal.bode(sys)

        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel("|H(jw)|(dB)")
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel("|_H(jw)(º)")
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()

class P2_Senoide_NT_Screen(QDialog):
    def __init__(self):
        super(P2_Senoide_NT_Screen, self).__init__()
        loadUi("P2_Senoide.ui", self)
        self.Back_P2_Senoide.clicked.connect(self.gotoBack_P2_Senoide)
        self.P2_Continuar_Senoide.clicked.connect(self.gotoP2_Continuar_Senoide)

    def gotoBack_P2_Senoide(self):
        Back_P2_Senoide = P2_Screen()
        widget1.addWidget(Back_P2_Senoide)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoP2_Continuar_Senoide(self):
        #P2senoideF = float(self.P2_F_Senoide.text())
        #P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_P_Senoide.text())==0):
            P2senoideP = 1
        else:
            P2senoideP = float(self.P2_P_Senoide.text())
        #if (len(self.P2_C_Senoide.text()) == 0):
            #P2senoideC = 1
        #else:
            #P2senoideC = float(self.P2_C_Senoide.text())
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())

        sys = signal.TransferFunction([P2senoideG], [(1/P2senoideP)**2,2*(P2senoidePHI/P2senoideP), 1])
        w, mag, phase = signal.bode(sys)

        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel("|H(jw)|(dB)")
        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel("|_H(jw)(º)")
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()


class P2_Pulso_PB_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_PB_Screen, self).__init__()
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

class P2_Pulso_PA_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_PA_Screen, self).__init__()
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

class P2_Pulso_PT_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_PT_Screen, self).__init__()
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

class P2_Pulso_PS_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_PS_Screen, self).__init__()
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

class P2_Pulso_NT_Screen(QDialog):
    def __init__(self):
        super(P2_Pulso_NT_Screen, self).__init__()
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