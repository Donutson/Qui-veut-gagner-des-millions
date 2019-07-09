#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     07/07/2019
# Copyright:   (c) HP 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import
from propositions import Propositions
import os
import sys
os.chdir("../functions")
sys.path.append(os.getcwd())
from error import Typeerror,typeError,setvalueError
os.chdir("../classes")
#prise des classes pour la gestion des erreurs
classPropositions=Propositions("A","","","")
#class
class Question:
    """
    Cette classe represente la structure d'une question
    pour le jeu qui veut gagner des millions
    """
    reponseset={"A","B","C","D"}

    def __init__(self, enonce, propositions, reponse):
        Typeerror(enonce,"l'enonce se doit d'etre une chaine", "")
        Typeerror(propositions,"propositions se doit d'etre une instance de Prpositions", classPropositions)
        setvalueError(reponse,Question.reponseset,"reponse ne peut prendre que les valeurs A, B, C et D")
        self.enonce=enonce
        self.propositions=propositions
        self.reponse=reponse
