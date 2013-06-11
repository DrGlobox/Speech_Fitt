#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Test(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle(u"Résultats")
        self.resize(600,600)
        self.createInterface()
        self.hide()

        self.dateDebut = QTime.currentTime()


    def createInterface(self):
