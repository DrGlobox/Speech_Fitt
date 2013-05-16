#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from directory import *
from files import *

class BrowserWidget(QScrollArea):

    def __init__(self,parent):
        QScrollArea.__init__ (self,parent)
        self.createInterface()
        self.curDir = QDir.home()
        self.changeDir(self.curDir)

        self.prevPath = self.curDir.path()
        self.nextPath = self.curDir.path()

    def createInterface(self):
        self.setGeometry(0,0,600,350)
        self.setWidgetResizable(True)
        self.setEnabled(True)
        self.scrollingWidget = QWidget()
        self.setWidget(self.scrollingWidget)
        self.VLayout = QVBoxLayout(self.scrollingWidget)
        self.scrollingWidget.setLayout(self.VLayout)

    def changeDir(self,directory):
        i=j=0
        self.dires = []
        for component in directory.entryList(QDir.Dirs):
            dirWidget = Directory(self.scrollingWidget,directory.path()+"/"+component)
            dirWidget.setGeometry(i,j,100,100)
            dirWidget.show()
            self.dires += [dirWidget]
            self.connect(dirWidget,SIGNAL("clicked"),self.dirClicked)
            i+=110; 
            if i >= (self.width()-100) : j+=110; i=0
        self.files = []
        directory.setNameFilters(["*.txt"])
        for component in directory.entryList(QDir.Files):
            fileWidget = File(self.scrollingWidget,directory.path()+"/"+component)
            fileWidget.setGeometry(i,j,100,100)
            fileWidget.show()
            self.files += [fileWidget]
            self.connect(fileWidget,SIGNAL("clicked"),self.fileClicked)
            i+=110; 
            if i >= 500 : j+=110; i=0

    def dirClicked(self,path):
        self.update()
        self.cleanDires()
        directory = QDir(path)
        self.curDir = directory
        self.nextPath = self.curDir.path()
        self.changeDir(directory)

    def fileClicked(self,path):
        print path

    def cleanDires(self):
        for component in self.dires:
            component.setParent(None)
            component.deleteLater()
