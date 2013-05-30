#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from browser import *
from speech import *
from helpBox import *
from analyser import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__ (self)
        self.setWindowTitle(u"Speech Fitts")
        self.resize(640,400)
        self.createInterface()
        self.createHelp()
        self.createAnalyser()
        self.createSpeech()

    def createAnalyser(self):
        self.analyser = Analyser(self.browser)
        self.connect(self,SIGNAL("analyse"),self.analyser.analyse)
        self.connect(self.analyser,SIGNAL("speech_directory"),self.goPage)
        self.connect(self.analyser,SIGNAL("speech_return"),self.prevPage)
        self.connect(self.analyser,SIGNAL("speech_home"),self.homePage)
        self.connect(self.analyser,SIGNAL("speech_help"),self.helpWigdet.toggleShow)
        self.connect(self.analyser,SIGNAL("speech_close_help"),self.helpWigdet.toggleShow)

    def createHelp(self):
        self.helpWigdet = HelpBox()
        self.connect(self.helpButton,SIGNAL("clicked()"),self.helpWigdet.toggleShow)


    def createSpeech(self):
        self.speech = Speech()
        self.connect(self.speech,SIGNAL("understand"),self.understand)

    def createInterface(self):
        self.prevButton = QPushButton(u"Précédent")
        self.prevButton.setIcon(QIcon("./Icon/fleche-gauche.png"))
        self.connect(self.prevButton,SIGNAL("clicked()"),self.prevPage)
        self.homeButton = QPushButton(u"Accueil")
        self.homeButton.setIcon(QIcon("./Icon/home.png"))
        self.connect(self.homeButton,SIGNAL("clicked()"),self.homePage)

        self.statusBar().showMessage("OK")
        
        self.helpButton = QPushButton(u"?")

        self.browser = BrowserWidget(self)
        self.browser.setStyleSheet("background-color:white;");


        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.homeButton)
        layout.addStretch()
        layout.addWidget(self.helpButton)

        bigLayout = QVBoxLayout()
        bigLayout.addLayout(layout)
        bigLayout.addWidget(self.browser)

        self.menu = QWidget()
        self.menu.setLayout(bigLayout)
        self.setCentralWidget(self.menu)

    def goPage(self,path):
        self.browser.dirClicked(path)

    def prevPage(self):
        self.browser.dirClicked(self.browser.prevPath)

    def homePage(self):
        self.browser.dirClicked(QDir.homePath())

    def understand(self,line):
        if line != "":
            self.emit(SIGNAL("analyse"),line)
            self.statusBar().showMessage(u"Écoute : "+line);
        print " >> ",line
