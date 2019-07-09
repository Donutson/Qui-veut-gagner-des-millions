#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     ce module permet l'ajout de questions ÃƒÂ  notre jeu
#              qui veut gager des millions
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
os.chdir("classes")
sys.path.append(os.getcwd())
from question import Question,Propositions
from managerquestion import ManagerQuestion
os.chdir("../functions")
sys.path.append(os.getcwd())
from error import typeError,setvalueError
os.chdir("..")

lettres=["A","B","C","D"]
manquestion=ManagerQuestion()

try:
    n=int(input("combien de questions voulez-vous entrer"))
    pallier=int(input("entrer le numero du pallier auquel appartiennent ces questions"))
    assert pallier in {1,2,3}
except ValueError:
    print("Mauvaises entrees: arret du processus...")
except AssertionError:
    print("le numero du pallier ne peut prendre que les valeurs 1,2 et 3")
else:
    for i in range(0,n):
        propositions=[]
        enonce=input("Entrez l'enonce la question "+ str(i+1))
        for j in range(0,4):
            proposition=input("Entrer la proposition "+lettres[j])
            propositions.append(proposition)
        reponse=input("Entrez la lettre de la bonne reponse")
        reponse=reponse.upper()
        setvalueError(reponse,lettres,"la reponse ne peut prendre que les valeurs A,B,C et D")
        propositions1=Propositions(propositions[0],propositions[1],propositions[2],propositions[3])
        question=Question(enonce,propositions1,reponse)
        manquestion.save(question,pallier)

















