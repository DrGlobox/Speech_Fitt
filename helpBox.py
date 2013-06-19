#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class HelpBox(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle(u"Aide ")
        self.resize(400,500)
        self.createInterface()
        self.hide()


    def createInterface(self):
        layout = QVBoxLayout(self)
        title = QLabel(u"<b>Besoin d'aide ?</b>")
        title.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed|QSizePolicy.Minimum)
        title.setAlignment(Qt.AlignCenter);

        corps = QLabel(u"\
                <b><i>En mode navigation : </i></b><br/>\
                <b>Ouvrir un document : </b><br/>\
                &bull;   dire : <i>\"Ouvrir nom_fichier\"</i><br/>\
                &bull;   dire : <i>\"nom_fichier\"</i><br/>\
                <b>Fermer un document : </b><br/>\
                &bull;   dire : <i>\"Fermer Aide\"</i><br/>\
                &bull;   dire : <i>\"Fermer\"</i><br/>\
                &bull;   dire : <i>\"Quitter\"</i><br/>\
                <b>Revenir au dossier précédent : </b><br/>\
                &bull;   dire : <i>\"Retour\"<\i><br/>\
                &bull;   dire : <i>\"Reviens\"<\i><br/>\
                <b>Se rendre dans le répertoire personnel : </b><br/>\
                &bull;   dire : <i>\"Accueil\"<\i><br/>\
                <b>Ouvrir l'aide : </b><br/>\
                &bull;   dire : <i>\"Aide\"<\i><br/><br/><br/>\
                <b><i>En mode édition de fichier : </i></b><br/>\
                <b>Sélectionner un mot : </b><br/>\
                &bull;   dire : <i>\"Sélectionne(r) nom_mot\"</i><br/>\
                &bull;   dire : <i>\"Trouve(r) nom_mot\"</i><br/>\
                <b>Effacer une sélection : </b><br/>\
                &bull;   dire : <i>\"Efface(r)\"</i><br/>\
                &bull;   dire : <i>\"Supprime(r)\"</i><br/>\
                <b>Ecrire à l'endroit du curseur : </b><br/>\
                &bull;   dire : <i>\"Ecris/Ecrire expr\"</b><br/>\
                &bull;   dire : <i>\"Insérer\"</b><br/>\
                <b>Sauvegarde le fichier en cours d'édition : </b><br/>\
                &bull;   dire : <i>\"Sauvegarde(r)\"</b><br/>\
                &bull;   dire : <i>\"Enregistre(r)\"</b><br/>\
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
