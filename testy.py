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
        if ((self.P2_Input.currentIndex() == 0)):
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
        self.RLC_Continuar.clicked.connect(self.gotoRLC_Continuar)

    def gotoBack_RLC (self):
        Back_RLC = Menu_Screen()
        widget1.addWidget(Back_RLC)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar (self):
        if(((self.El_Mas.currentIndex())==0)&((self.El_Menos.currentIndex())==0)):
            RLC_Continuar = G1_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

        if (((self.El_Mas.currentIndex()) == 0) & ((self.El_Menos.currentIndex()) == 1)):
            RLC_Continuar = G2_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

        if (((self.El_Mas.currentIndex()) == 0) & ((self.El_Menos.currentIndex()) == 2)):
            RLC_Continuar = G3_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

        if (((self.El_Mas.currentIndex()) == 1) & ((self.El_Menos.currentIndex()) == 1)):
            RLC_Continuar = G4_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

        if (((self.El_Mas.currentIndex()) == 1) & ((self.El_Menos.currentIndex()) == 2)):
            RLC_Continuar = G5_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

        if (((self.El_Mas.currentIndex()) == 2) & ((self.El_Menos.currentIndex()) == 2)):
            RLC_Continuar = G6_Screen()
            widget1.addWidget(RLC_Continuar)
            widget1.setCurrentIndex(widget1.currentIndex() + 1)

############################################################################################
class G1_Screen(QDialog):
    def __init__(self):
        super(G1_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC_2.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)

    def gotoBack_RLC_2(self):
        Back_RLC_2 = RLC_Screen()
        widget1.addWidget(Back_RLC_2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):
        if (len(self.Res.text()) == 0):
            Resis = 1.0
        else:
            Resis = float(self.Res.text())
        if (len(self.Ind.text()) == 0):
            Induc = 1.0
        else:
            Induc = float(self.Ind.text())
        if (len(self.Cap.text()) == 0):
            Capa = 1.0
        else:
            Capa = float(self.Cap.text())

        sys = signal.TransferFunction([Resis*Capa,0], [Induc * Capa, Capa * Resis,1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()


class G2_Screen(QDialog):
    def __init__(self):
        super(G2_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC_2.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)

    def gotoBack_RLC_2(self):
        Back_RLC_2 = RLC_Screen()
        widget1.addWidget(Back_RLC_2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):
        if (len(self.Res.text()) == 0):
            Resis = 1.0
        else:
            Resis = float(self.Res.text())
        if (len(self.Ind.text()) == 0):
            Induc = 1.0
        else:
            Induc = float(self.Ind.text())
        if (len(self.Cap.text()) == 0):
            Capa = 1.0
        else:
            Capa = float(self.Cap.text())

        sys = signal.TransferFunction([1], [Induc * Capa, Capa * Resis,1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()


class G3_Screen(QDialog):
    def __init__(self):
        super(G3_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC_2.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)


    def gotoBack_RLC_2(self):
        Back_RLC_2 = RLC_Screen()
        widget1.addWidget(Back_RLC_2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):

        sys = signal.TransferFunction([1], [1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()

class G4_Screen(QDialog):
    def __init__(self):
        super(G4_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC_2.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)

    def gotoBack_RLC_2(self):
        Back_RLC_2 = RLC_Screen()
        widget1.addWidget(Back_RLC_2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):
        if (len(self.Res.text()) == 0):
            Resis = 1.0
        else:
            Resis = float(self.Res.text())
        if (len(self.Ind.text()) == 0):
            Induc = 1.0
        else:
            Induc = float(self.Ind.text())
        if (len(self.Cap.text()) == 0):
            Capa = 1.0
        else:
            Capa = float(self.Cap.text())

        sys = signal.TransferFunction([Induc * Capa,0,0], [Induc * Capa, Capa * Resis,1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()


class G5_Screen(QDialog):
    def __init__(self):
        super(G5_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC_2.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)

    def gotoBack_RLC_2(self):
        Back_RLC_2 = RLC_Screen()
        widget1.addWidget(Back_RLC_2)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):
        if (len(self.Res.text()) == 0):
            Resis = 1.0
        else:
            Resis = float(self.Res.text())
        if (len(self.Ind.text()) == 0):
            Induc = 1.0
        else:
            Induc = float(self.Ind.text())
        if (len(self.Cap.text()) == 0):
            Capa = 1.0
        else:
            Capa = float(self.Cap.text())

        sys = signal.TransferFunction([Induc * Capa,0,1], [Induc * Capa, Capa * Resis,1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()


class G6_Screen(QDialog):
    def __init__(self):
        super(G6_Screen, self).__init__()
        loadUi("Circuito_RLC_serie_2.ui", self)
        self.Back_RLC.clicked.connect(self.gotoBack_RLC_2)
        self.RLC_Continuar_2.clicked.connect(self.gotoRLC_Continuar_2)

    def gotoBack_RLC_2(self):
        Back_RLC = RLC_Screen()
        widget1.addWidget(Back_RLC)
        widget1.setCurrentIndex(widget1.currentIndex() + 1)

    def gotoRLC_Continuar_2(self):
        if (len(self.Res.text()) == 0):
            Resis = 1.0
        else:
            Resis = float(self.Res.text())
        if (len(self.Ind.text()) == 0):
            Induc = 1.0
        else:
            Induc = float(self.Ind.text())
        if (len(self.Cap.text()) == 0):
            Capa = 1.0
        else:
            Capa = float(self.Cap.text())

        sys = signal.TransferFunction([1], [Induc * Capa, Capa * Resis,1])
        w, mag, phase = signal.bode(sys)
        plt.figure()

        plt.semilogx(w, mag)  # Bode magnitude plot
        plt.figure()
        plt.title("Diagrama de Amplitud")
        plt.xlabel("Hz")
        plt.ylabel(["|H(jw)|"])
        plt.semilogx(w, phase)  # Bode phase plot
        plt.show()
        plt.title("Diagrama de Fase")
        plt.xlabel("Hz")
        plt.ylabel(["|_H(jw)"])
        plt.show()

############################################################################################
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

        if (len(self.P1_G_Senoide.text()) == 0):
            P1senoideG = 1.0
        else:
            P1senoideG = float(self.P1_G_Senoide.text())

        if (len(self.P1_F_Senoide.text()) == 0):
            P1senoideF = 1.0
        else:
            P1senoideF = float(self.P1_F_Senoide.text())

        if (len(self.P1_A_Senoide.text()) == 0):
            P1senoideA = 1.0
        else:
            P1senoideA = float(self.P1_A_Senoide.text())

        if((self.P1_Filtro.currentIndex())==0):
            sys = signal.TransferFunction([(P1senoideG*2*np.pi)], [1 / (P1senoideP*2*np.pi), 1])
            w, mag, phase = signal.bode(sys)
            plt.figure()

            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.show()

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=(np.sin(2*np.pi*P1senoideF*t)*P1senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()



        if ((self.P1_Filtro.currentIndex()) == 1):
            sys = signal.TransferFunction([(P1senoideG*2*np.pi)/(P1senoideP*2*np.pi),0], [1 / (2*np.pi*P1senoideP), 1])
            w, mag, phase = signal.bode(sys)
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=(np.sin(2 * np.pi * P1senoideF * t) * P1senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P1_Filtro.currentIndex()) == 2):
            sys = signal.TransferFunction([(-1/(P1senoideP*2*np.pi)),1], [(1/(P1senoideP*2*np.pi)),1])
            w, mag, phase = signal.bode(sys)
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=(np.sin(2 * np.pi * P1senoideF * t) * P1senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
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
        P1pulsoP = float(self.P1_P_Pulso.text())


        if (len(self.P1_G_Pulso.text())== 0):
            P1pulsoG=1.0
        else:
            P1pulsoG = float(self.P1_G_Pulso.text())

        if((self.P1_Filtro.currentIndex()) == 0):
            sys = signal.TransferFunction([(P1pulsoG*2*np.pi)], [1/(2*np.pi*P1pulsoP), 1])
            w, mag, phase = signal.bode(sys)
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t)
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P1_Filtro.currentIndex()) == 1):
            sys = signal.TransferFunction([(P1pulsoG*2*np.pi)/(2*np.pi*P1pulsoP),0], [1 / (2*np.pi*P1pulsoP), 1])
            w, mag, phase = signal.bode(sys)
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys , T=t)
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P1_Filtro.currentIndex()) == 2):
            sys = signal.TransferFunction([(-1/(P1pulsoP*2*np.pi)),1], [(1 / (P1pulsoP*2*np.pi)), 1])
            w, mag, phase = signal.bode(sys)
            plt.figure()
            plt.title("Diagrama de Amplitud")
            plt.xlabel("Hz")
            plt.ylabel(["|H(jw)|"])
            plt.semilogx(w, mag)  # Bode magnitude plot
            plt.figure()
            plt.title("Diagrama de Fase")
            plt.xlabel("Hz")
            plt.ylabel(["|_H(jw)"])
            plt.semilogx(w, phase)  # Bode phase plot
            plt.show()

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t)
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()





################################################################################
################################################################################

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
        if (len(self.P2_W0_Senoide.text()) == 0):
            P2senoideF = 1
        else:
            P2senoideF = float(self.P2_F_Senoide.text())
        if (len(self.P2_W0_Senoide.text()) == 0):
            P2senoideA = 1
        else:
            P2senoideA = float(self.P2_A_Senoide.text())
        if(len(self.P2_W0_Senoide.text())==0):
            P2senoideW0 = 1
        else:
            P2senoideW0 = (float(self.P2_W0_Senoide.text()) / (2*np.pi))
        if (len(self.P2_G_Senoide.text()) == 0):
            P2senoideG = 1
        else:
            P2senoideG = float(self.P2_G_Senoide.text())
        if (len(self.P2_PHI_Senoide.text()) == 0):
            P2senoidePHI = 1
        else:
            P2senoidePHI = float(self.P2_PHI_Senoide.text())



        if((self.P2_Filtro.currentIndex()) == 0):
            sys = signal.TransferFunction([P2senoideG], [(1/P2senoideW0)**2,2*(P2senoidePHI/P2senoideW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=((np.sin(2*np.pi*P2senoideF*t))*P2senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()


            w, H = signal.freqresp(sys)  #diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P2_Filtro.currentIndex()) == 1):
            sys = signal.TransferFunction([P2senoideG * ((1 / P2senoideW0) ** 2), 0, 0],
                                          [(1 / P2senoideW0) ** 2, 2 * (P2senoidePHI / P2senoideW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=((np.sin(2 * np.pi * P2senoideF * t)) * P2senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        

        if ((self.P2_Filtro.currentIndex()) == 3):
            sys = signal.TransferFunction([0,P2senoideG * 2 * (P2senoidePHI / P2senoideW0), 0],[(1 / P2senoideW0) ** 2, 2 * (P2senoidePHI / P2senoideW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=((np.sin(2 * np.pi * P2senoideF * t)) * P2senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P2_Filtro.currentIndex()) == 4):
            sys = signal.TransferFunction([P2senoideG*((1 / P2senoideW0)**2), 0, 1],[(1 / P2senoideW0) ** 2, 2 * (P2senoidePHI / P2senoideW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            Sin_Response = signal.lsim(sys, U=((np.sin(2 * np.pi * P2senoideF * t)) * P2senoideA), T=t)

            plt.figure(figsize=(13, 4))
            plt.plot(Sin_Response[0], Sin_Response[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()



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
        #if (len(self.P2_W0_Pulso.text()) == 0):
            #P2pulsoA = 1
        #else:
            #P2pulsoA = float(self.P1_A_Pulso.text())
        if (len(self.P2_W0_Pulso.text()) == 0):
            P2pulsoW0 = 1
        else:
            P2pulsoW0 = (float(self.P2_W0_Pulso.text()) / (2 * np.pi))
        if (len(self.P2_G_Pulso.text()) == 0):
            P2pulsoG = 1
        else:
            P2pulsoG = float(self.P2_G_Pulso.text())
        if (len(self.P2_PHI_Pulso.text()) == 0):
            P2pulsoPHI = 1
        else:
            P2pulsoPHI = float(self.P2_PHI_Pulso.text())

        if ((self.P2_Filtro.currentIndex()) == 0):
            sys = signal.TransferFunction([P2pulsoG], [(1 / P2pulsoW0) ** 2, 2 * (P2pulsoPHI / P2pulsoW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t)
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P2_Filtro.currentIndex()) == 1):
            sys = signal.TransferFunction([P2pulsoG*(1/P2pulsoW0),0,0], [(1 / P2pulsoW0) ** 2, 2 * (P2pulsoPHI / P2pulsoW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t )
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()




        if ((self.P2_Filtro.currentIndex()) == 3):
            sys = signal.TransferFunction([0,P2pulsoG * 2 * (P2pulsoPHI / P2pulsoW0), 0],[(1 / P2pulsoW0) ** 2, 2 * (P2pulsoPHI / P2pulsoW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t )
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

        if ((self.P2_Filtro.currentIndex()) == 4):
            sys = signal.TransferFunction([P2pulsoG*((1 / P2pulsoW0)**2), 0, 1],[(1 / P2pulsoW0) ** 2, 2 * (P2pulsoPHI / P2pulsoW0), 1])
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

            t = np.linspace(0, 20, num=1000)
            h = signal.step(sys, T=t)
            plt.figure(figsize=(13, 4))
            plt.plot(h[0], h[1])
            plt.title('Respuesta al escalón con SciPy')
            plt.xlabel(r't [s]')
            plt.ylabel(r'Out [V]')
            plt.grid()
            plt.subplots_adjust(top=1)
            plt.show()

            w, H = signal.freqresp(sys)  # diagrama de Nyquist
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
            ax1.plot(H.real, H.imag)
            ax1.plot(H.real, -H.imag)
            ax2.plot(sys.zeros.real, sys.zeros.imag, 'o')
            ax2.plot(sys.poles.real, sys.poles.imag, 'x')
            plt.show()

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
