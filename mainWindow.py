#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from browser import *
from speech import *
from helpBox import *
from analyser import *
from editor import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__ (self)
        self.setWindowTitle(u"Speech Fitts")
        self.resize(640,400)

        self.createInterface()
        self.createHelp()
        self.createAnalyser()
        self.createSpeech()

        self.modeEditor = False
        self.toggleTextEditor(False)

    def createAnalyser(self):
        self.analyser = Analyser(self.browser, self.editor, self.comment)
        self.connect(self,SIGNAL("analyse"),self.analyser.analyse)
        self.connect(self.analyser,SIGNAL("speech_directory"),self.goPage)
        self.connect(self.analyser,SIGNAL("speech_file"),self.openFile)
        self.connect(self.analyser,SIGNAL("speech_return"),self.prevPage)
        self.connect(self.analyser,SIGNAL("speech_home"),self.homePage)
        self.connect(self.analyser,SIGNAL("speech_help"),self.helpWigdet.toggleShow)
        self.connect(self.analyser,SIGNAL("speech_close_help"),self.helpWigdet.toggleShow)
        self.connect(self.analyser,SIGNAL("speech_close_document"),self.quitEditor)
        self.connect(self.analyser,SIGNAL("speech_select"),self.selectText)

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
        self.quitButton = QPushButton(u"Quitter")
        self.quitButton.setIcon(QIcon("./Icon/home.png"))
        self.connect(self.quitButton,SIGNAL("clicked()"),self.quitEditor)

        self.comment = QLabel("")

        self.statusBar().showMessage("OK")
        
        self.helpButton = QPushButton(u"?")

        self.browser = BrowserWidget(self)
        self.browser.setStyleSheet("background-color:white;");
        self.connect(self.browser,SIGNAL("file_clicked"),self.openFile)

        self.editor = Editor(self)
        self.editor.hide()


        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.homeButton)
        layout.addWidget(self.quitButton)
        layout.addStretch()
        layout.addWidget(self.comment)
        layout.addStretch()
        layout.addWidget(self.helpButton)

        bigLayout = QVBoxLayout()
        bigLayout.addLayout(layout)
        bigLayout.addWidget(self.browser)
        bigLayout.addWidget(self.editor)

        self.menu = QWidget()
        self.menu.setLayout(bigLayout)
        self.setCentralWidget(self.menu)


    def toggleTextEditor(self,boolean):
        self.modeEditor = boolean
        if boolean:
            self.browser.hide()
            self.editor.show()
            self.prevButton.hide()
            self.homeButton.hide()
            self.quitButton.show()
        else:
            self.browser.show()
            self.editor.hide()
            self.prevButton.show()
            self.homeButton.show()
            self.quitButton.hide()

    def openFile(self,path):
        if not self.modeEditor: 
            self.toggleTextEditor(True)
            self.editor.setFile(path)

    def quitEditor(self):
        if self.modeEditor: 
            self.toggleTextEditor(False)

    def goPage(self,path):
        if not self.modeEditor: 
            self.browser.dirClicked(path)

    def prevPage(self):
        if not self.modeEditor: 
            self.browser.dirClicked(self.browser.prevPath)

    def homePage(self):
        if not self.modeEditor: 
            self.browser.dirClicked(QDir.homePath())

    def selectText(self, sentence):
        if self.modeEditor:
            self.editor.find(sentence)
            cursor = self.editor.textCursor()
            cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor,
                    len(sentence))

    def understand(self,line):
        if line != "":
            self.emit(SIGNAL("analyse"),line)
            self.statusBar().showMessage(u"Écoute : "+line);
        print " >> ",line
