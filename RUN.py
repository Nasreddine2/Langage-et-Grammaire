import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QSpinBox, QLabel
from PyQt5.QtGui import QIcon
import PyQt5.QtGui as QtGui #pour les icones
from PyQt5.QtCore import pyqtSlot
import itertools 
from collections import OrderedDict
import TP_p2 as p2
import os
aList = []
flist = []

#PARTIE 1 :

#appartence T={a,b,c} nedireha
def Appartenance_a_b_c(word):
    cpt=1
    for i in range(len(word)):
        if(word[i] != 'a' and word[i]!='b' and word[i]!='c' ):
            return -1
    return cpt

#elle prend en parametre un mot et renvoie son inverse 
def mirroir_mot(word):
    
    return(word[::-1])

#elle prend en parametre un mot et un entier (exposant) et renvoi la puissance du mot
def puissance_mot(word,n):
    d=""
    for i in range(n):
        d=d+word
    return d

#PARTIE 2 :

# elle permet de generer toutes les combainaisons possible des mots de taille k avec les caractere de l'ensemble des motes (ens) T*={a,b}
def Liste_De_Combinaison(ens, k):
    aList[:] = []
    n = len(ens)
    All_combin(ens, "", n, k)
    return aList

def All_combin(ens, prefix, n, k):
    if (k == 0) :
        aList.append(prefix)
        return
    
    for i in range(n):
        newPrefix = prefix + ens[i]
        All_combin(ens, newPrefix, n, k - 1)

#fonction qui genere les mot de taille N de la grammaire donnee nedireha
def generer_L(n):
 
 if(n==3):
        return ("abb")
 flist[:] = []       
 if (n>3):
        #partie gauche
        lg=Liste_De_Combinaison(['a', 'b'],n-3)
        lg=[s + "abb" for s in lg]
        
        flist.extend(lg)
        #partie droite
        ld=Liste_De_Combinaison(['a', 'b'],n-3)
        ld=["abb" + s for s in ld]
        
        flist.extend(ld)
        
        if(n==4):
            return flist
        #milieu
        if(n-3>=2):
            i=n-3-1
            while i>0:
                lmg=Liste_De_Combinaison(['a', 'b'],i)
                lmg=[s + "abb" for s in lmg]
                
                lmd=Liste_De_Combinaison(['a', 'b'],n-3-i)
                
                lorg=[]

                for element in itertools.product(lmg,lmd):#produit cartesien lmg lmd
                    lorg.append(element)
                res = [''.join(o) for o in lorg] #transformer lorg de tuple en liste res
                flist.extend(res)
                i=i-1
        return flist


#PARTIE 3 :

#appartence T={a,b} nedireha
def Appartenance_a_b(word):
    cpt=1
    for i in range(len(word)):
        if(word[i] != 'a' and word[i]!='b'):
            return -1
    return cpt
#calculer le nombre de a de debut de la chaine jusqua tombee sur un autre caractere nedireha
def Nombre_De_a(word):
    cpt=0
    for i in range(len(word)):
        if(word[i]=='a'):
            cpt=cpt+1
        else:
            return cpt
    return cpt
# nombre de b dans le mot entier nedireha
def Nombre_De_b(word):
    cpt=0
    for i in range(len(word)):
        if(word[i]=='b'):
            cpt=cpt+1
    return cpt



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'TP THL'
        self.left = 650
        self.top = 250
        self.width = 1080
        self.height = 720
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet("background-color: #900C3F;")
        self.setWindowIcon(QtGui.QIcon('didine.ico'))
        #-----------------------------------------------------------------------------------


        self.label = QLabel("TP THL",self)
        self.label.setGeometry(460, 10, 1080, 50)
        self.label.setFont(QtGui.QFont ("Times New Roman", 30))
        


        self.label = QLabel("Partie 1 : Calcul du miroir et la puissance d'un mot",self)
        self.label.setGeometry(20, 75, 1080, 50)
        self.label.setFont(QtGui.QFont ("Helvetica", 15))
        


        # Create a button for part 2 in the window
        self.button1 = QPushButton('Miroir', self)
        self.button1.move(400,148)
        self.button1.resize(200,40)
        self.button1.setFont(QtGui.QFont ("Arial", 15))
        self.button1.setStyleSheet (" background-color: #e63946 ")
        

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 130)
        self.textbox1.resize(350,80)
        self.textbox1.setFont(QtGui.QFont ("Arial", 15))
        # connect button to function on_click
        self.button1.clicked.connect(self.mirroir)
       
        
        #-----------------------------------------------------------------------------------
        # Create a button for part 2 in the window
        self.button1 = QPushButton('Puissance', self)
        self.button1.move(640,260)
        self.button1.resize(200,40)
        self.button1.setFont(QtGui.QFont ("Arial", 15))
        self.button1.setStyleSheet (" background-color: #e63946 ")
        
        # Create SpinBox
        self.spin1 = QSpinBox(self)
        self.spin1.move(400,235)
        self.spin1.resize(200,80)
        self.spin1.setFont(QtGui.QFont ("Arial", 15))

 
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 235)
        self.textbox2.resize(350,80)
        self.textbox2.setFont(QtGui.QFont ("Arial", 15))

        # connect button to function on_click
        self.button1.clicked.connect(self.puissance)
        
        #-----------------------------------------------------------------------------------

        self.label = QLabel("Partie 2 : Introduire la taille des mots à générer puis cliquer sur générer",self)
        self.label.setGeometry(20, 320, 1080, 40)
        self.label.setFont(QtGui.QFont ("Helvetica", 15))

        # Create a button for part 2 in the window
        self.button2 = QPushButton('Lancer La partie 2 du tp', self)
        self.button2.move(280,390)
        self.button2.resize(300,40)
        self.button2.setFont(QtGui.QFont ("Arial", 15))
        self.button2.setStyleSheet (" background-color: #e63946 ")
        


        # connect button to function on_click
        self.button2.clicked.connect(self.generer)

        #-----------------------------------------------------------------------------------
        self.label3 = QLabel("Partie 3 : Introduire le mot et cliquer sur Ok pour vérifier si le mot appartient au langage G",self)
  
        # setting geometry
        self.label3.setGeometry(20,460, 1080, 40)
        self.label3.setFont(QtGui.QFont ("Helvetica", 15))

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 520)
        self.textbox.resize(700,80)
        self.textbox.setFont(QtGui.QFont ("Arial", 15))
        
        # Create a button for part 3 in the window
        self.button = QPushButton('Ok ', self)
        self.button.resize(200,40)
        self.button.move(780,540)
        self.button.setFont(QtGui.QFont ("Arial", 15))
        self.button.setStyleSheet (" background-color: #e63946 ")
        

        self.label = QLabel("REALISER PAR :",self)
        self.label.setGeometry(500, 650, 380, 40)
        self.label.setFont(QtGui.QFont ("Arial", 10))

        self.label = QLabel(" \nHAMMOUDI NASREDDINE & CHEKIKENE HADIL ",self)
        self.label.setGeometry(390, 660, 380, 40)
        self.label.setFont(QtGui.QFont ("Arial", 10))

        self.label = QLabel(" \nFEZOUI YACINE & BELGUELOUL HAYDER ",self)
        self.label.setGeometry(400, 680, 380, 40)
        self.label.setFont(QtGui.QFont ("Arial", 10))

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

        
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        if(Appartenance_a_b(textboxValue)<0):
         QMessageBox.question(self, 'TP THL', "La chaine ne doit contenir que des 'a' ou des 'b'.", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if(Nombre_De_a(textboxValue)>= 2*Nombre_De_b(textboxValue)  ):
                if(textboxValue==""):
                    QMessageBox.question(self, 'TP THL', "Le mot vide (epsilon) appartient au langage L(G).", QMessageBox.Ok, QMessageBox.Ok)
                else:
                    QMessageBox.question(self, 'TP THL', "La chaine : " + textboxValue + " existe  dans le langage L(G).", QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.question(self, 'TP THL', "La chaine : " + textboxValue + " n'existe pas dans le langage L(G).", QMessageBox.Ok, QMessageBox.Ok)
            
        self.textbox.setText("")
        
    @pyqtSlot()
    def mirroir(self):
        textboxValue = self.textbox1.text()
        if(Appartenance_a_b_c(textboxValue)<0):
            QMessageBox.question(self, 'TP THL', "La chaine ne doit contenir que des 'a', des 'b' ou des 'c'. ", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if (textboxValue==""):
                QMessageBox.question(self, 'TP THL', "Le miroir du mot est : Le mot vide (epsilone) "  , QMessageBox.Ok, QMessageBox.Ok)       
            else:   
                QMessageBox.question(self, 'TP THL', "Le miroir du mot est : " + mirroir_mot(textboxValue) , QMessageBox.Ok, QMessageBox.Ok)       
        self.textbox1.setText("")

    @pyqtSlot()
    def puissance(self):
        textboxValue = self.textbox2.text()
        n = self.spin1.value()
        if(Appartenance_a_b_c(textboxValue)<0):
            QMessageBox.question(self, 'TP THL', "La chaine ne doit contenir que des 'a', des 'b' ou des 'c'. ", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if (textboxValue=="" or n==0):
                QMessageBox.question(self, 'TP THL', "La puissance  du mot est : Le mot vide (epsilone) "  , QMessageBox.Ok, QMessageBox.Ok)       
            else:   
                QMessageBox.question(self, 'TP THL', "La puissance  du mot est : " + puissance_mot(textboxValue,n) , QMessageBox.Ok, QMessageBox.Ok)       
        self.textbox2.setText("")
        self.spin1.clear()

    @pyqtSlot()
    def generer(self):
        os.system("TP_p2.py")
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


