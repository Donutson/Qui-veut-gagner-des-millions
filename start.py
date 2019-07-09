#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     09/07/2019
# Copyright:   (c) HP 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import
import os
import sys
os.chdir("classes")
sys.path.append(os.getcwd())
from game import Jeu
os.chdir("..")

#menu principal
continuer=True
board="     Qui Veut Gagner Des Millions    \n\n"
liste=["nouvelle partie"]
newgame={"N","NEW","1"}
lastgame={}
voirscores={"V","VOIR","2"}
aide={"A","AIDE","HELP","3"}
quitter={"Q","QUIT","QUITTER","4"}
j=0
while(continuer):
    j+=1
    if(j==1):
        print("         BIENVENUE DANS          \n")
    with open("game/partie.txt","rb") as file:
        if(file.readline()):
            liste.append("continuer partie")
            lastgame={"C","CONTINUER","2"}
            voirscores={"V","VOIR","3"}
            aide={"A","AIDE","HELP","4"}
            quitter={"Q","QUIT","QUITTER","5"}
    liste.append("voir les scores")
    liste.append("aide")
    liste.append("quitter")
    i=1
    for elt in liste:
        board+=str(i)+"- "+elt+"\n"
        i+=1
    print(board)
    board="     Qui Veut Gagner Des Millions    \n\n"
    liste=["nouvelle partie"]
    choix=input("Que voulez vous faire?")
    choix=choix.upper()
    if(choix in newgame):
        nom=input("Entrer votre nom")
        jeu=Jeu(nom)
        jeu.newgame()
    elif(choix in lastgame):
        jeu=Jeu()
        jeu.lastgame()
    elif(choix in voirscores):
        jeu=Jeu()
        jeu.showscores()
    elif(choix in aide):
        jeu=Jeu()
        jeu.showhelp()
    else:
        continuer=False
        print("Merci d'voir jouer!!!")







