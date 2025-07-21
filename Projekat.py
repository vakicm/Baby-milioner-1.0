import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QInputDialog

from Funkcija import ucitaj_pitanja_iz_csv



class Ui_MainWindow(object):
    _osvojeni_iznos = 0
    
    def __init__(self):
        """
        Pocetni ekran, prvobitne vrednosti
        su 0 za oba a u praznu listu ce se dodavati
        stvari
        """
        self.broj_pitanja = 0
        self.broj_pokusaja = 0
        self.pitanja = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Odgovor = QtWidgets.QPushButton(self.centralwidget)
        self.Odgovor.setGeometry(QtCore.QRect(570, 360, 201, 121))
        self.Odgovor.setObjectName("Odgovor")
        
        self.Kutsaodg = QtWidgets.QComboBox(self.centralwidget)
        self.Kutsaodg.setGeometry(QtCore.QRect(90, 360, 451, 121))
        self.Kutsaodg.setObjectName("Kutsaodg")
        
        self.Prost_za_pit = QtWidgets.QLabel(self.centralwidget)
        self.Prost_za_pit.setWordWrap(True)
        self.Prost_za_pit.setGeometry(QtCore.QRect(90, 10, 451, 321))
        self.Prost_za_pit.setObjectName("Prost_za_pit")
        
        self.Response = QtWidgets.QLabel(self.centralwidget)
        self.Response.setGeometry(QtCore.QRect(570, 230, 201, 81))
        self.Response.setObjectName("Response")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.promeni_ime_mainu(MainWindow)
    def promeni_ime_mainu(self, MainWindow):
        """ 
        Menja ime glavnom prozoru i
        ostalim dugmicima
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projekat"))
        self.Prost_za_pit.setText(_translate("MainWindow", "Prostor za pitanje"))
        self.Odgovor.setText(_translate("MainWindow", "Odgovor"))
        self.Response.setText(_translate("MainWindow", "Povratna poruka"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_unos_pit(self):
        """ 
        Princip kao malopre, loop koji se izvrsava dok su ispunjeni uslovi
        """
        
        while True:
            broj_pitanja, okPressed = QInputDialog.getInt(None, "Unesite broj pitanja",
                                                          "Unesite broj pitanja (izmedju 5 i 20):", 15, 5, 20)
            # 15 default value od koje se krece, 5 min vrednost i 20 max
            if okPressed and 5 <= broj_pitanja <= 20:
                self.broj_pitanja = broj_pitanja
                break
            else:
                QtWidgets.QMessageBox.warning(None, "Upozorenje", "Uneli ste nedozvoljeni broj pitanja. Molim unesite ponovo")

    def get_unos_pokusaja(self):
        """ 
        Isto kao gore
        """
        while True:
            broj_pokusaja, okPressed = QInputDialog.getInt(None, "Unesite broj zivota",
                                                           "Unesite broj zivota (do 5):", 3, 0, 5)
            if okPressed and 0 < broj_pokusaja <= 5:
                self.broj_pokusaja = broj_pokusaja
                break
            else:
                QtWidgets.QMessageBox.warning(None, "Upozorenje", "Uneli ste nedozvoljeni broj pokušaja. Molim unesite ponovo.")

    def proveri_odg(self):
        """ 
        Proverava odgovore za sve, isti princip kao u klasi. Dole u azuriraj,
        proveri_kraj i kraj samo poziva fje.
        """                
        if self.broj_pokusaja > 0 and self.broj_pitanja > 0:
            odabrani_odgovor = self.Kutsaodg.currentIndex()
            trenutno_pitanje = self.pitanja[self.broj_pitanja - 1]
            
            if odabrani_odgovor == trenutno_pitanje._odgovori.index(trenutno_pitanje._tacan_odg):
                self.broj_poena(100)
                tacna_poruka = (f"Tačan odgovor!\nIdete dalje!\nTrenutno imate\n{Ui_MainWindow._osvojeni_iznos} evra!")
                self.prikazi_tacan_odg(tacna_poruka)
            else:
                self.broj_pokusaja -= 1
                netacna_poruka = (f"Netačno! Ostalo Vam je još \n{self.broj_pokusaja} života.")
                self.prikazi_netacan_odg(netacna_poruka)
            self.broj_pitanja -= 1
            self.azuriraj()
            self.proveri_kraj()
        else:
            self.kraj("Kraj igre")
            
    def proveri_kraj(self):
        """ 
        Proverava kraj. Ako je broj_pokusaja = 0, znaci da je igrac izgubio jer nema vise zivota, a ako je broj_pitanja = 0,
        to znaci da je pobedio jer nema vise pitanja a broj_pokusaja > 0
        """
        
        if self.broj_pokusaja == 0:
            QtWidgets.QMessageBox.information(None, "Kraj igre", "Ostalo Vam je 0 života.\nPao si na ispitu!")
            sys.exit()
        elif self.broj_pitanja == 0:
            QtWidgets.QMessageBox.information(None,"Kraj igre", "Položio si ispit! Srećno na FON-u!")
            sys.exit()

    def prikazi_tacan_odg(self, tacna_poruka):
        """ 
        Prikazuje tacan odg
        """
        self.Response.setText(tacna_poruka)
        
    def prikazi_netacan_odg(self, netacna_poruka):
        """ 
        Prikazuje netacan odg
        """
        self.Response.setText(netacna_poruka)
        
    def azuriraj(self):
        """ 
        Azurira pitanja, ako ima pitanja ide dalje, ako nema prikaze poruku
        zavrsetka
        """
        if self.broj_pitanja > 0:
            trenutno_pitanje = self.pitanja[self.broj_pitanja - 1]
            self.Prost_za_pit.setText(trenutno_pitanje._pitanje)
            self.Kutsaodg.clear()
            self.Kutsaodg.addItems(trenutno_pitanje._odgovori)
        else:
            self.Prost_za_pit.setText("Pobedili ste!")
            self.Kutsaodg.clear()
            
    def broj_poena(self, poeni):
        """  
        Dodaje poene
        """
        Ui_MainWindow._osvojeni_iznos += poeni
    
    def kraj_igre(self, poruka):
        """ 
        Eng game poruka
        """
        QtWidgets.QMessageBox.information(None, "Kraj igre", poruka)
        sys.exit()

    def retranslateUi(self, MainWindow):
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Odgovor.setText(_translate("MainWindow", "Odgovor"))
        self.Kutsaodg.setText(_translate("MainWindow", "Kutija sa odgovorom"))
        self.Prost_za_pit.setText(_translate("MainWindow", "TextLabel"))
        self.Response.setText(_translate("MainWindow", "TextLabel"))
        """
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    ui.pitanja = ucitaj_pitanja_iz_csv()
         
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui.get_unos_pit()
    ui.get_unos_pokusaja()
    ui.azuriraj()

    ui.Odgovor.clicked.connect(ui.proveri_odg)

    sys.exit(app.exec_())


if __name__ == "__main__":  
    main()