#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


from recorder import *
from sender import *


class Speech(QThread):
    def __init__(self):
        QThread.__init__(self)

        self.sender_1 = Sender(1)
        self.connect(self.sender_1,SIGNAL("understand"),self.understand)
        self.sender_0 = Sender(0)
        self.connect(self.sender_0,SIGNAL("understand"),self.understand)

        self.recorder = Recorder()
        self.connect(self.recorder,SIGNAL("record"),self.recorded)
        self.recorder.start()

        self.running = 0

    def __del__(self):
        self.wait()
        self.recorder.running = False

    def run(self):
        return

    def understand(self,line):
        self.emit(SIGNAL("understand"),line)

    def recorded(self,index):
        if self.running == 0 :
            self.sender_0.analyse(index)
        else:
            self.sender_1.analyse(index)
        self.running = ((self.running+1) % 2)
