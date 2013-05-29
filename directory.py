#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Directory(QWidget):

    def __init__(self,parent,name,path):
        QWidget.__init__ (self,parent)
        self.path = path
        self.name = name
        self.createInterface()
        #self.setStyleSheet("background-color:red;");

    def createInterface(self):
        self.setGeometry(0,0,50,50)
        layout = QVBoxLayout()
        image = QLabel();
        image.setPixmap(QPixmap("./Icon/dossier.png"));
        label = QLabel(self.name)
        layout.addWidget(image)
        layout.addWidget(label)
        self.setLayout(layout)

    def mousePressEvent(self,event):
        self.emit(SIGNAL("clicked"),self.path)


