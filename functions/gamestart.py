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

"""
ce paquet contient des fonctions en rapport
une partie de qui veut ganger des millions en cours
"""

#import
import os
import sys
os.chdir("../classes")
sys.path.append(os.getcwd())
from pallier import Pallier
from question import Question
from managerpallier import ManagerPallier
from managerquestion import ManagerQuestion
os.chdir("../functions")
import pickle

#functions
def biggest(liste):
    """
    cette fonctions retourne le plus grand element d'une liste
    """
    big=""
    for elt in liste:
        if(len(elt)>len(big)):
            big=elt
    return big
def reset(filename):
    """
    cette fonction remet un fichier ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â  zero
    """
    file=open(filename,"w")
    file.close()

def save(filename,*params):
    """
    cette fonction permet de sauvegarder
    les parmetres d'une partie en cours
    """
    liste=[]
    for param in params:
        with open(filename,"rb") as file:
            if(not file.readline()):
                createdico=True
            else:
                createdico=False
        if(createdico):
            with open("game/partie.txt","wb") as file:
                pickle.Pickler(file).dump([])
        with open(filename,"wb") as file:
            liste.append(param)
            pickle.Pickler(file).dump(liste)
def savescore(joueur,score):
    """
    cette fonction enregistre le score d'un joueur
    les scores sont conserver dans un dictionnaire
    """
    with open("game/scores.txt","rb") as file:
            if(not file.readline()):
                createdico=True
            else:
                createdico=False
    if(createdico):
            with open("game/scores.txt","wb") as file:
                pickle.Pickler(file).dump({})
    with open("game/scores.txt","rb") as file:
            dico=pickle.Unpickler(file).load()
    if(joueur in dico.keys()):
        if(dico[joueur]<score):
            dico[joueur]=score
    else:
        dico[joueur]=score
    with open("game/scores.txt","wb") as file:
        pickle.Pickler(file).dump(dico)
def getscores():
    with open("game/scores.txt","rb") as file:
            dico=pickle.Unpickler(file).load()
    liste1=[]
    liste2=[]
    for elt,val in dico.items():
        liste1.append(elt)
        liste2.append(dico[elt])
    n=len(liste2)
    for i in range(0,n-1):
        minval2=liste2[i]
        for j in range(i,n):
            if(liste2[j]<minval2):
                ech=liste2[i]
                liste2[i]=liste2[j]
                liste2[j]=ech
                ech=liste1[i]
                liste1[i]=liste1[j]
                liste1[j]=ech
    liste1.reverse()
    liste2.reverse()
    return liste1, liste2

def load(filename):
    """
    cette fonction permet de charger un parametre d'un fichier
    """
    with open(filename,"rb") as file:
        param=pickle.Unpickler(file).load()
    return param

def play(joueur,old=True):
    """
    lance la partie en cours si old=True
    sinon commmence une nouvelle partie
    """
    if(old):
        donnees=load("game/partie.txt")
        pallier=donnees[0]
        gain=donnees[1]
        joueur=donnees[2]
    else:
        reset("game/partie.txt")
        pallier=Pallier()
        gain=0
    manpal=ManagerPallier()
    manpal.load(pallier)
    manquest=ManagerQuestion()
    correct=True
    end=False
    reponse=""
    ok={"Y","YES","O","OUI","SAVE","SAUVEGARDER","S"}
    sortie={"Q","QUIT","QUITTER"}
    while(correct and (end==False) and (reponse not in sortie)):
        manpal.showallprice(pallier)
        question=manquest.load(pallier)
        manquest.show(question)
        print("")
        #print("Votre gain:",gain,"fcfa")
        reponse=input()
        reponse=reponse.upper()

        if(reponse!=question.reponse):
            correct=False
        else:
            if(pallier.numquestion==4 and pallier.niveau==3):
                end=True
            else:
                gain=manpal.getcurprice(pallier)
                manpal.nextquestion(pallier)
                manpal.load(pallier)
    if(correct==True and end==True):
        savescore(joueur,gain)
        print("FELICITATION VOUS AVEZ REMPORTER LE MILLION")
        print("")
    elif(reponse in sortie):
        keep=input("Voulez-vous sauver la partie")
        keep=keep.upper()
        if(keep in ok):
            save("game/partie.txt",pallier,gain,joueur)
    else:
        savescore(joueur,gain)
        reset("game/partie.txt")
        print("Dommage pour le million, vous repartez avec la somme de:",gain,"francs cfa")
        print("")











