#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from browser import *
from speech import *

class MainWindow():

    def __init__(self):

        self.window = QMainWindow()
        self.window.setWindowTitle(u"Speech Fitts")
        self.window.resize(640,400)
        self.createInterface()
        self.createSpeech()

    def show(self):
        self.window.show()

    def createSpeech(self):
        self.speech = Speech()
        self.window.connect(self.speech,SIGNAL("understand"),self.understand)

    def createInterface(self):
        self.prevButton = QPushButton(u"Précédent")
        self.prevButton.setIcon(QIcon("./Icon/fleche-gauche.png"))
        self.window.connect(self.prevButton,SIGNAL("clicked()"),self.prevPage)
        self.nextButton = QPushButton(u"Suivant")
        self.nextButton.setIcon(QIcon("./Icon/fleche-droite.png"))
        self.window.connect(self.nextButton,SIGNAL("clicked()"),self.nextPage)
        self.homeButton = QPushButton(u"Home")
        self.homeButton.setIcon(QIcon("./Icon/home.png"))
        self.window.connect(self.homeButton,SIGNAL("clicked()"),self.homePage)

        self.window.statusBar().showMessage("OK")
        
        self.cmdButton = QPushButton(u"Lancer écoute")

        self.browser = BrowserWidget(self.window)
        self.browser.setStyleSheet("background-color:white;");


        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.nextButton)
        layout.addWidget(self.homeButton)
        layout.addStretch()
        layout.addWidget(self.cmdButton)

        bigLayout = QVBoxLayout()
        bigLayout.addLayout(layout)
        bigLayout.addWidget(self.browser)

        self.menu = QWidget()
        self.menu.setLayout(bigLayout)
        self.window.setCentralWidget(self.menu)

    def prevPage(self):
        nextPath = self.browser.curDir.path()
        self.browser.curDir.cdUp()
        self.browser.dirClicked(self.browser.curDir.path())
        self.browser.nextPath = nextPath

    def nextPage(self):
        self.browser.dirClicked(self.browser.nextPath)

    def homePage(self):
        self.browser.dirClicked(QDir.homePath())

    def understand(self,line):
        if line != "":
            self.window.statusBar().showMessage(u"Écoute : "+line);
        print " >> ",line
