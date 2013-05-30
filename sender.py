#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import subprocess


class Sender(QThread):
    def __init__(self,id_):
        QThread.__init__(self)
        self.index = "-1"
        self.id_ = id_

    def __del__(self):
        self.wait()

    def run(self):
        #print "[",self.id_,"] send : ",self.index
        p=subprocess.Popen(["./send.sh",str(self.index)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        line = unicode(p.stdout.readline(), "utf-8")
        self.emit(SIGNAL("understand"),line)

    def analyse(self,index):
        self.index = index
        self.start()
