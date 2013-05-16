#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


class Speech(QThread):
    def __init__(self,index):
        QThread.__init__(self)
        self.index = index

    def __del__(self):
        self.wait()

    def run(self):
        p=subprocess.Popen(["./speech.sh"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        line = p.stdout.readline()
        self.emit(SIGNAL("understand"),self.index,line)
        return
