#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class HelpBox(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle(u"Aide ")
        self.resize(300,300)
        self.createInterface()
        self.hide()


    def createInterface(self):
        layout = QVBoxLayout(self)
        title = QLabel(u"Besoin d'aide ?")
        corps = QLabel(u"--> et bien débrouille toi")
        layout.addWidget(title)
        layout.addWidget(corps)
        
        exit = QPushButton(u"Fermer")
        self.connect(exit,SIGNAL("clicked()"),self.close)

        layout.addWidget(exit)

    def toggleShow(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
