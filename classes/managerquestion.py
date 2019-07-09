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
from question import Question,classPropositions
from pallier import Pallier
import pickle
import os
import sys
os.chdir("../functions")
sys.path.append(os.getcwd())
from error import typeError,Typeerror,setvalueError
os.chdir("../classes")
#prise des classes pour la gestion des erreurs
classQuestion=("", classPropositions, "A")
classPallier=Pallier()

#class
class ManagerQuestion:
    """
    Cette classe est sensee gerer toutes les actions
    qu'on peut effectuer sur une question
    pour le jeu qui veut gagner des millions
    """
    def save(self,question,numpallier):
        """
        cette methode enregistre une question
        """
        #Typeerror(question,"question doit etre une instance de  Question",classQuestion)
        setvalueError(numpallier,Pallier.niveauset,"numpallier ne peut prendre que les valeurs 1,2 et 3")
        if(numpallier==1):
            filename="questions/pallier1.txt"
        elif(numpallier==2):
            filename="questions/pallier2.txt"
        else:
            filename="questions/pallier3.txt"
        with open(filename,"rb") as file:
            if(file.readline()==""):
                createdico=True
            else:
                createdico=False
        if(createdico):
            with open(filename,"wb") as file:
                pickle.Pickler(file).dump([])
        with open(filename,"rb") as file:
            liste=pickle.Unpickler(file).load()
        with open(filename,"wb") as file:
            liste.append(question)
            pickle.Pickler(file).dump(liste)
        file.close()
    def load(self, pallier):
        """
        cette classe permet de recuperer une question du pallier
        """
        #Typeerror(question,"pallier doit etre une instance de pallier",classPallier)
        return pallier.questions[pallier.numquestion]
    def show(self,question):
        """
        cette methode se charge de l'affichage d'une question
        """
        #Typeerror(question,"question doit etre une instance de  Question",classQuestion)
        enonce=question.enonce
        propositions=question.propositions
        j=1
        n=len(enonce)
        print(enonce.center(n+2))
        print("*",end="")
        for i in range(0,n):
            print("-",end="")
        print("*")
        for lettre, proposition in propositions.values.items():
            if(j%2!=0):
                phrase=lettre+": "+proposition+"    "
                print(phrase,end="")
            else:
                phrase=lettre+": "+proposition
                print(phrase)
            j+=1
































