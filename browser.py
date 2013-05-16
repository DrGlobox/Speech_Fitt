#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from directory import *

class BrowserWidget(QWidget):

    def __init__(self,parent):
        QWidget.__init__ (self,parent)
        self.createInterface()
        self.curDir = QDir.home()
        self.changeDir(self.curDir)

    def createInterface(self):
        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.setStyleSheet("background-color:white;");

    def changeDir(self,directory):
        dirIteration= QDirIterator(directory)
        dirList = []
        while dirIteration.hasNext():
            dirList += [dirIteration.next()]
        i=j=0
        for dire in dirList:
            dirWidget = Directory(self,dire)
            self.gridLayout.addWidget(dirWidget,i,j)
            self.connect(dirWidget,SIGNAL("clicked"),self.dirClicked)
            i+=1
            if i == 5 :
                i = 0
                j+=1

    def dirClicked(self,path):
        while self.gridLayout.takeAt(0): pass
        directory = QDir(path)
        self.curDir = directory
        self.changeDir(directory)
