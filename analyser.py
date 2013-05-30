#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

OPEN = [u"ouvrir",u"ouvre",u"va",u"dossier"]
RETURN = [u"retour",u"arrière"]
HOME = [u"acceuil"]

class Analyser(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.running = True
        self.order = []

    def __del__(self):
        self.wait()

    def run(self):
        sentence =  ""
        while len(self.order) :
            sentence = self.order.pop(0).lower().split()
            action = self.getAction(sentence)
            print sentence," -> ",action

    def analyse(self,sentence):
        lenght = len(self.order)
        self.order.append(sentence)
        if not lenght : self.start()

    def getAction(self,sentence):
        if sentence[0] in OPEN: return "open"
        if sentence[0] in RETURN: return "return"
        if sentence[0] in HOME: return "home"
        return "unknow"
