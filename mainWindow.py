#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MainWindow():

    def __init__(self):

        self.window = QMainWindow()
        self.window.setWindowTitle("Speech Fitts")
        self.window.resize(640,400)

        self.createInterface()
            
    def show(self):
        self.window.show()

    def createInterface(self):
        self.prevButton = QPushButton("Précédent")
        self.nextButton = QPushButton("Suivant")
        
        self.cmdButton = QPushButton("Lancer écoute")

        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.nextButton)
        layout.addStretch()
        layout.addWidget(self.cmdButton)



        self.menu = QWidget()
        self.menu.setLayout(layout)
        self.window.setCentralWidget(self.menu)

    

