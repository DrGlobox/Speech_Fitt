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

        self.dires = []
        self.files = []

        self.createInterface()
        self.curDir = QDir.current()
        self.changeDir(self.curDir)

        self.prevPath = self.curDir.path()
        self.nextPath = self.curDir.path()

    def createInterface(self):
        self.setGeometry(0,0,600,350)
        self.setWidgetResizable(True)
        self.setEnabled(True)
        self.scrollingWidget = QWidget(self)
        self.setWidget(self.scrollingWidget)
        self.VLayout = QVBoxLayout(self.scrollingWidget)
        self.scrollingWidget.setLayout(self.VLayout)

    def changeDir(self,directory):
        i=j=0
        for component in directory.entryList(QDir.Dirs):
            path = directory.path()+"/"+component
            if component == "." : 
                path = directory.path() 
            elif component == ".." : 
                tmpDir = QDir(directory)
                tmpDir.cdUp()
                path = tmpDir.path()
            dirWidget = Directory(self.scrollingWidget,component,path)
            dirWidget.setGeometry(i,j,100,100)
            dirWidget.show()
            self.dires.append(dirWidget)
            self.connect(dirWidget,SIGNAL("clicked"),self.dirClicked)
            i+=110; 
            if i >= (self.width()-100) : j+=110; i=0

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
            component.close()
        self.dires = []
        for component in self.files:
            component.setParent(None)
            component.close()
        self.files = []
