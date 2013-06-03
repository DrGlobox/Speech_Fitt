#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Editor(QTextEdit):
    def __init__(self,parent):
        QTextEdit.__init__ (self,parent)

    def setFile(self,path):
        f = open(path)
        txt = ""
        self.clear();
        for line in f:
            line = unicode(line, "utf-8")
            txt = self.toPlainText() + line
            self.clear();
            self.setText(txt);
