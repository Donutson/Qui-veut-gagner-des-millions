#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     08/07/2019
# Copyright:   (c) HP 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import
import os
import sys
os.chdir("../functions")
sys.path.append(os.getcwd())
from gamestart import reset,play,save,getscores,biggest
os.chdir("../classes")

#class
class Jeu:
    """
    cette contient les fonctionnalitÃƒÂ©s pour faire
    une partie de qui veut gagner des millions
    """
    def __init__(self,joueur=""):
        self.joueur=joueur
    def newgame(self):
        """
        debute une nouvelle partie
        """
        play(self.joueur,old=False)
    def lastgame(self):
        """
        permet de continuer la derniere si non finie
        """
        play(self.joueur)
    def showscores(self):
        joueurs,scores=getscores()
        big=biggest(joueurs)
        n=len(big)
        message="TABLEAU DES SCORES".center(20+n)
        message+="\n"
        n=len(message)
        for i in range(0,n):
            message+="-"
        n=len(scores)
        message+="\n"
        for i in range(0,n):
            message+=joueurs[i]+": "+str(scores[i])
            if(scores[i]==1000000):
                message+="  Master"
            message+="\n"
        print(message)
    def showhelp(self):
        aide="""
                       Objectif
---------------------------------------------------------
Le but du jeu est d'atteindre le million tout en répondant
correctement a une serie de question
Bonne parti a vous...
        """
        print(aide)









