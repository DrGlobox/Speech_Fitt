#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


class Speech(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.IsRunning = True

    def __del__(self):
        self.wait()

    def run(self):
        p=subprocess.Popen(["./speech.sh"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while self.IsRunning :
            line = p.stdout.readline()
            print line
        return
