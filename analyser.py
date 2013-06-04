#!/usr/bin/python
#-*-coding:utf8-*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

from levenshtein import *

OPEN = [u"ouvrir",u"ouvre",u"va",u"dossier",u"fichier",u"ouvre"]
RETURN = [u"retour",u"arrière",u"reviens",u"non",u"nan"]
SELECT = [u"sélectionne", u"sélection", u"sélectionnez", u"trouvent", u"trouver"]
ERASE = [u"efface", u"supprime", u"enlève", u"suprime", u"effacer", u"supprimer", u"enlever"]
SAVE = [u"sauvegarde", u"enregistre", u"sauvegarder", u"enregistrer"]
HOME = [u"accueil",u"source",u"home"]
HELP = [u"aide",u"comment"]
CLOSE = [u"fermer",u"quitter",u"retour"]
WHAT_CLOSE = [u"aide"]
THANK = [u"merci"]

#Attention: garder l'espace à la fin
IGNORE = [u"j'ai dit ",u"je répète "]

tolerance_max = 2

class Analyser(QThread):
    def __init__(self,browser, editor, comment):
        QThread.__init__(self)
        self.browser = browser
        self.editor = editor
        self.comment = comment
        self.running = True
        self.order = []

    def __del__(self):
        self.wait()

    def run(self):
        sentence =  ""
        while len(self.order) :
            self.comment.setText("")
            sentence = self.order.pop(0).split()
            action = self.getAction(sentence)
            if action == "open" : self.open_command(" ".join(sentence[1:]))
            elif action == "return" : self.retour_command()
            elif action == "close" : self.close_command(" ".join(sentence[1:]))
            elif action == "home" : self.home_command()
            elif action == "help" : self.help_command()
            elif action == "thank" : self.thank_command()
            elif action == "select" : self.select_command(" ".join(sentence[1:]))
            elif action == "erase" : self.erase_command()
            elif action == "save" : self.save_command()
            else : self.open_command(" ".join(sentence))

    def analyse(self,sentence):
        sentence = self.delete_accent(sentence.lower())
        for ignore in IGNORE :
            sentence = sentence.replace(ignore,u"")
        lenght = len(self.order)
        self.order.append(sentence)
        if not lenght : self.start()

    def getAction(self,sentence):
        if sentence[0] in OPEN: return "open"
        if sentence[0] in RETURN: return "return"
        if sentence[0] in HOME: return "home"
        if sentence[0] in HELP: return "help"
        if sentence[0] in CLOSE: return "close"
        if sentence[0] in THANK: return "thank"
        if sentence[0] in SELECT: return "select"
        if sentence[0] in ERASE: return "erase"
        if sentence[0] in SAVE: return "save"
        return "unknow"

    def thank_command(self):
        self.comment.setText(":D")
    
    def retour_command(self):
        self.emit(SIGNAL("speech_return"))

    def help_command(self):
        self.emit(SIGNAL("speech_help"))

    def home_command(self):
        self.emit(SIGNAL("speech_home"))

    def close_command(self,sentence):
        for component in WHAT_CLOSE :
            if levenshtein(str(sentence), component) <= tolerance_max :
                if component == u"aide": 
                    self.emit(SIGNAL("speech_close_help"))
                    return
        self.emit(SIGNAL("speech_close_document"))


    def open_command(self,sentence):
        if sentence == "" : return
        directory  = QDir(self.browser.curDir.path())
        for component in directory.entryList(QDir.Dirs):
            sentence = sentence.encode('ascii', 'ignore')
            if levenshtein(str(sentence), component.toLower()) <= tolerance_max :
                path = directory.path()+"/"+component
                self.emit(SIGNAL("speech_directory"),path)
                return
        for component in directory.entryList(QDir.Files):
           # if levenshtein(str(sentence), component.toLower()) <= tolerance_max or \
           #        levenshtein(str(sentence), component.split('.')[0].toLower()) <= tolerance_max :
           if levenshtein(str(sentence), component.split('.')[0].toLower()) <= tolerance_max and \
                   component.split('.')[1] == "txt" :
                path = directory.path()+"/"+component
                self.emit(SIGNAL("speech_file"),path)
                return
        self.comment.setText(":(")


    def select_command(self, sentence):
        if sentence == "" or self.editor.isVisible() == False : return
        if self.editor.find(sentence):
            self.emit(SIGNAL("speech_select"),sentence)

    def erase_command(self):
        if self.editor.isVisible == False : return
        self.emit(SIGNAL("speech_erase"))

    def save_command(self):
        if self.editor.isVisible == False : return
        self.emit(SIGNAL("speech_save"))

    def delete_accent(self, ligne):
        accent = [u'é', u'è', u'ê', u'à', u'ù', u'û', u'ç', u'ô', u'î', u'ï', u'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
        i = 0
        while i < len(accent):
            ligne = ligne.replace(accent[i], sans_accent[i])
            i += 1
        return ligne

