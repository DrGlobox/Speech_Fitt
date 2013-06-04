#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


class Recorder(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.running = False

    def __del__(self):
        self.wait()

    def run(self):
        self.running = True
        index = 0
        while self.running :
            #print "record : ",index
            p=subprocess.Popen(["./recorder.sh",str(index)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            p.stdout.readline()
            self.emit(SIGNAL("record"),index)
            index = ((index+1) % 4)
        return