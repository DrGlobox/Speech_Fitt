#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TestBox(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle(u"Résultats")
        self.resize(300,300)
        self.modeEditor = False
        self.editor = False
        self.button = False

        self.createInterfaceNavigation()
        self.createInterfaceEditor()


        self.isRunning = False
        self.positionDebut= ""
        self.dateDebut = False
        self.positionFin= ""
        self.dateFin = False


    def createInterfaceNavigation(self):

        layout2 = QHBoxLayout()
        layout2.addWidget(QLabel("Chemin : "))
        self.pathText = QLineEdit()
        layout2.addWidget(self.pathText)

        layout3 = QHBoxLayout()
        layout3.addWidget(QLabel("Fichier : "))
        self.fileText = QLineEdit()
        layout3.addWidget(self.fileText)

        self.startButton = QPushButton("Go !")
        self.connect(self.startButton,SIGNAL("clicked()"),self.startTest)

        layout4 = QHBoxLayout()
        self.result = QLabel("")
        layout4.addWidget(self.result)

        self.navigation_layout = QVBoxLayout()
        self.navigation_layout.addLayout(layout2)
        self.navigation_layout.addLayout(layout3)
        self.navigation_layout.addWidget(self.startButton)
        self.navigation_layout.addLayout(layout4)
     
    def createInterfaceEditor(self):
        layout5 = QHBoxLayout()
        layout5.addWidget(QLabel("Mot ou Expression : "))
        self.wordText = QLineEdit()
        layout5.addWidget(self.wordText)

        layout4 = QHBoxLayout()
        layout4.addWidget(self.result)

        self.editor_layout = QVBoxLayout()
        self.editor_layout.addLayout(layout5)
        self.editor_layout.addWidget(self.startButton)
        self.editor_layout.addLayout(layout4)

    def startTest(self):
        if self.isRunning :
            self.button.setIcon(QIcon("./Icon/play.png"))
            self.isRunning = False
            self.dateFin = QTime.currentTime()
            r = self.dateDebut.secsTo(self.dateFin)
            self.startButton.setEnabled(True)
            affichage = ""
            if self.modeEditor :
                self.wordText.setEnabled(True)
                C = self.positionFin
                L = len(self.editor.toPlainText().split("\n")) -1
                mouse,keyboard = self.calcul_editeur_GOMS(C,L)
                affichage = u"Résultat : " + str(r) + u" seconde(s)\n"
                affichage+= u"\n avec le clavier : "+ str(keyboard) + u" seconde(s)"
                affichage+= u"\n avec la souris : "+ str(mouse) + u" seconde(s)"
            else:
                mouse,keyboard = self.calcul_navigation_GOMS(self.positionDebut,self.positionFin)
                affichage = u"Résultat : " + str(r) + u" seconde(s)\n"
                affichage+= u"\n avec le clavier : "+ str(keyboard) + u" seconde(s)"
                affichage+= u"\n avec la souris : "+ str(mouse) + u" seconde(s)"
                self.pathText.setEnabled(True)
                self.fileText.setEnabled(True)
            self.result.setText(affichage)
        else :
            self.isRunning = True
            self.button.setIcon(QIcon("./Icon/stop.png"))
            self.dateDebut = QTime.currentTime()
            self.startButton.setEnabled(False)
            if self.modeEditor :
                self.wordText.setEnabled(False)
            else:
                self.positionDebut = QDir.current().absolutePath()
                self.pathText.setEnabled(False)
                self.fileText.setEnabled(False)

    def testSelection(self,selection):

        if self.wordText.text().toLower() == selection:
            C = -1
            i =0
            L = str(self.editor.toPlainText()).split("\n")
            while C == -1 :
                C = L[i].lower().find(selection)
                i+=1
            self.positionFin = C
            self.startTest()
    

    def testPath(self,path):
        filename = path.split("/")[-1]
        directory = path.split("/")[-2]
        if self.pathText.text() == directory and self.fileText.text() == filename :
            path = path.split("/")[:-1]
            self.positionFin = path.join("/")
            self.startTest()

    def toggle(self):
        if self.isHidden() :
            self.show()
            if self.modeEditor :  self.setLayout(self.editor_layout)
            else:                 self.setLayout(self.navigation_layout)
        else :
            self.hide()


    def calcul_editeur_GOMS(self,C,L):
        
        

        TH = 0.43
        TM = 1.35
        TP = 1.10
        TK = 0.2

        mouse = 2*TH + TP + TK + TM
        keyboard = 2*TH + TK*(1 + L + 2*C)
        return mouse,keyboard

    def calcul_navigation_GOMS(self,origin,final):

        origin = str(origin).split("/")
        final = str(final).split("/")
        diff = final[len(origin):]

        m = 0
        for mot in diff :
            m += len(mot)

        if len(diff) != 0:
            m/=len(diff)
        else:
            m = 0 

        h = len(diff)

        TH = 0.43
        TM = 1.35
        TP = 1.10
        TK = 0.2

        mouse = (2*TH + (h+1)*TM + (h+1)*TP + 2*(h+1)*TK)
        keyboard = (h+2)*TH + ((h+1)*(m+1)+5)*TK
        return mouse,keyboard
