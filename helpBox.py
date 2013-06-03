#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class HelpBox(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle(u"Aide ")
        self.resize(300,300)
        self.createInterface()
        self.hide()


    def createInterface(self):
        layout = QVBoxLayout(self)
        title = QLabel(u"<b>Besoin d'aide ?</b>")
        title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed|QSizePolicy.Minimum)
        title.setAlignment(Qt.AlignCenter);

        corps = QLabel(u"\
                <b>Ouvrir un document : </b><br/>\
                &bull;   dire : <i>\"Ouvrir nom_fichier\"</i><br/>\
                &bull;   dire : <i>\"nom_fichier\"</i><br/>\
                <b>Fermer un document : </b><br/>\
                &bull;   dire : <i>\"Fermer Aide\"</i><br/>\
                &bull;   dire : <i>\"Fermer\"</i><br/>\
                &bull;   dire : <i>\"Quitter\"</i><br/>\
                <br/>\
                n'oubliez pas de dire merci !")
        corps.setAlignment(Qt.AlignTop);

        scroll = QScrollArea()
        scroll.setWidget(corps)
        scroll.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

        layout.addWidget(title)
        layout.addWidget(scroll)
        
        exit = QPushButton(u"Fermer")
        self.connect(exit,SIGNAL("clicked()"),self.close)

        layout.addWidget(exit)

    def toggleShow(self):
        if self.isHidden():
            self.show()
        else:
            self.hide()
