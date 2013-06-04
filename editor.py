#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Editor(QTextEdit):
    def __init__(self,parent):
        QTextEdit.__init__ (self,parent)
        self.path = ""

    def setFile(self,path):
        print path
        f = open(path, 'r')
        self.path = path
        txt = ""
        self.clear();
        for line in f:
            line = unicode(line, "utf-8")
            txt = self.toPlainText() + line
            self.clear();
            self.setText(txt);

    def writeFile(self):
        f = open(self.path, 'w')
        txt = self.toPlainText()
        f.write(txt)
