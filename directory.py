#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Directory(QWidget):

    def __init__(self,parent,path):
        QWidget.__init__ (self,parent)
        self.path = path
        self.name = path.split("/")[-1]
        self.createInterface()


    def createInterface(self):
        self.resize(50,50)
        layout = QVBoxLayout()
        #add image 
        label = QLabel(self.name)
        layout.addWidget(label)
        self.setLayout(layout)

    def mousePressEvent(self,event):
        self.emit(SIGNAL("clicked"),self.path)


