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
from pallier import Pallier
import pickle
import os
import sys
os.chdir("../functions")
sys.path.append(os.getcwd())
from error import Typeerror,setvalueError
from fileextractobjects import takeobjectsalea,nbobjects
os.chdir("../classes")

#prise des classes pour la gestion des erreurs
classPallier=Pallier()

#fonction pratique
def reverse(liste):
    """
    cette fonction retourne une liste dont
    les elements sont ceux de la liste passer en parametre
    mais dans l'ordre inverse
    """
    n=len(liste)-1
    liste1=[]
    while(n>-1):
        liste1.append(liste[n])
        n-=1
    return liste1

#class
class ManagerPallier:
    """
    cette classe est censee gerer toutes les actions possibles
    sur un pallie du jeu qui veut gagner des millions
    """
    pallier3=reverse(Pallier.pallier3)
    pallier2=reverse(Pallier.pallier2)
    pallier1=reverse(Pallier.pallier1)
    pyramide=[pallier3,pallier2,pallier1]
    def load(self,pallier):
        """
        cette methode doit charger les questions pour un pallier
        """
        setvalueError(pallier.niveau,Pallier.niveauset,"niveau ne peut prendre que les valeurs 1,2 et 3")
        if(pallier.niveau==1):
            filename="questions/pallier1.txt"
        elif(pallier.niveau==2):
            filename="questions/pallier2.txt"
        else:
            filename="questions/pallier3.txt"
        taille=nbobjects(filename)
        nombre=5
        questions=takeobjectsalea(nombre,filename)
        pallier.questions= questions
    def nextpallier(self,pallier):
        """
        cette methode permet d'aller au pallier suivant
        """
        Typeerror(pallier,"pallier doit etre une instance de pallier",classPallier)
        self.nextpricevalue(pallier)
        pallier+1

    def nextpricevalue(self,pallier):
        Typeerror(pallier,"pallier doit etre une instance de pallier",classPallier)
        if(pallier.niveau==1):
            pallier.gains=Pallier.pallier2
        elif(pallier.niveau==2):
            pallier.gains=Pallier.pallier3
    def nextquestion(self,pallier):
        """
        cette methode se charge de faaire
        ÃƒÆ’Ã‚Â©voluer le numero des questions au cours du jeu
        """
        Typeerror(pallier,"pallier doit etre une instance de pallier",classPallier)
        if(pallier.numquestion<4):
            pallier.numquestion+=1
        else:
            self.nextpallier(pallier)
            pallier.numquestion=0
    def getcurprice(self,pallier):
        """
        cette methode retourne le gain courant du joueur
        """
        Typeerror(pallier,"pallier doit etre une instance de pallier",classPallier)
        return (pallier.gains[pallier.numquestion])*10000
    def showallprice(self,pallier):
        """
        cette methode affiche la pyramide des gains
        pour le jeu qui veut gagner des milllions
        """
        allprice="     PYRAMIDE DES GAINS  \n"
        n=len(allprice)-1
        curprice=self.getcurprice(pallier)
        for i in range(0,n):
            allprice+="-"
        allprice+="\n"
        for gaingroup in ManagerPallier.pyramide:
            for gain in gaingroup:
                m=len(str(gain*10000))
                if((gain*10000)==curprice):
                    for j in range(0,n-m-3):
                        allprice+="*"
                    allprice+="| "+str(gain*10000)+"| \n"
                else:
                    for j in range(0,n-m):
                        allprice+=" "
                    allprice+=str(gain*10000)+"\n"
            for i in range(0,n):
                allprice+="-"
            allprice+="\n"
        print(allprice,end="")





























