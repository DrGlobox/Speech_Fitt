#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TestBox(QWidget):

    def __init__(self,modeEditor):
        QWidget.__init__(self)
        self.setWindowTitle(u"Résultats")
        self.resize(300,300)
        self.modeEditor = modeEditor
        if not modeEditor:
            self.createInterfaceNavigation()


        self.show()

        self.isRunning = False
        self.dateDebut = False
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
        self.connect(self.startButton,SIGNAL("clicked()"),self.toggleTest)

        layout4 = QHBoxLayout()
        self.result = QLabel("")
        layout4.addWidget(self.result)



        layout1 = QVBoxLayout(self)
        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addWidget(self.startButton)
        layout1.addLayout(layout4)


    def toggleTest(self):
        if self.isRunning :
            self.isRunning = False
            self.dateFin = QTime.currentTime()
            r = self.dateDebut.secsTo(self.dateFin)
            self.result.setText(u"Résultat : " + str(r) + u" seconde(s)")
            self.pathText.setEnabled(True)
            self.fileText.setEnabled(True)
            
        else :
            self.isRunning = True
            self.dateDebut = QTime.currentTime()
            self.pathText.setEnabled(False)
            self.fileText.setEnabled(False)

    

    def testPath(self,path):
        filename = path.split("/")[-1]
        directory = path.split("/")[-2]
        if self.pathText.text() == directory and self.fileText.text() == filename :
            self.toggleTest()


