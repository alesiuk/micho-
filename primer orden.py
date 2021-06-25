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

