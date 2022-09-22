import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction,QTextEdit, QLineEdit, QMessageBox, QSpinBox, QLabel
from PyQt5.QtGui import *
import PyQt5.QtGui as QtGui #pour les icones
from PyQt5.QtCore import pyqtSlot
import itertools 
from collections import OrderedDict
#from p2 import Ui_MainWindow
aList = []
flist = []



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
        #----------------------------------------------------------------------------------
     
        self.label = QLabel("TP THL",self)
        self.label.setGeometry(460, 10, 1080, 50)
        self.label.setFont(QtGui.QFont ("Times New Roman", 30))
        
        #-----------------------------------------------------------------------------------

        self.label = QLabel("Partie 2 : Introduire la taille des mots à générer puis cliquer sur générer",self)
        self.label.setGeometry(20, 45, 1080, 40)
        self.label.setFont(QtGui.QFont ("Helvetica", 15))

        # Create a button for part 2 in the window
        self.button2 = QPushButton('Generer', self)
        self.button2.move(280,90)
        self.button2.resize(200,40)
        self.button2.setFont(QtGui.QFont ("Arial", 15))
        self.button2.setStyleSheet (" background-color: #e63946 ")
        
        # Create SpinBox
        self.spin = QSpinBox(self)
        self.spin.move(20,90)
        self.spin.resize(100,50)
        self.spin.setFont(QtGui.QFont ("Arial", 15))

        self.textbox1 = QTextEdit(self)
        self.textbox1.move(10, 150)
        self.textbox1.resize(1060,550)
        self.textbox1.setFont(QtGui.QFont ("Arial", 15))
        

        # connect button to function on_click
        self.button2.clicked.connect(self.generer)

        #-----------------------------------------------------------------------------------

        self.show()

        

    @pyqtSlot()
    def generer(self):
        
        n = self.spin.value()
        flist=generer_L(n)
        
        if( n > 3):
            nvlist = list(OrderedDict.fromkeys(flist))
        
            self.textbox1.setText("Les Mots Sont : "+str(nvlist))
            #print(str(len(nvlist))+" mots sont : "+str(nvlist))
        else:
         if( n == 3):
            nvlist = list(OrderedDict.fromkeys(flist))
            self.textbox1.setText("Le Mot Est : ['abb']")
            #QMessageBox.question(self, 'TP THL', "Le mot est : \n" + "['abb']" , QMessageBox.Ok, QMessageBox.Ok)
         else:
            QMessageBox.question(self, 'TP THL', " La grammaire G ne contient pas des mots de taille inferieure à 3 ", QMessageBox.Ok, QMessageBox.Ok)     
        self.spin.clear()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

