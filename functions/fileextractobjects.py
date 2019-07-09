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
ce paquet contient des fonctions utiles
pour recuperer des objets d'un fichier
"""

from random import randrange
import pickle

def nbobjects(filename):
    """
    retourne le nombre d'objet d'un fichier
    """
    with open(filename,"rb") as file:
        taker=pickle.Unpickler(file)
        count=len(taker.load())
    return count
def ntom(n,m):
    """
    retourne une liste d'entiers allant de n Ã  m
    """
    liste=[]
    for i in range(n,m+1):
        liste.append(i)
    return liste
def getobject(n,filename,taille):
    """
    retourne le n ieme objet d'un fichier
    """
    file=open(filename,"rb")
    taker=pickle.Unpickler(file)
    nb=taille
    if(n<=nb):
        for i in ntom(1,n-1):
            taker.load()
        lignen=taker.load()
        file.close()
        return lignen
    file.close()
    print("Le fichier ne possede pas autant de ligne")

def takeobjectsalea(nombre,filename):
    """
    retourne n objets de facon aleatoire d'un fichier
    nombre etant le nombre d'objet voulu
    """
    with open(filename,"rb") as file:
        liste=pickle.Unpickler(file).load()
    taille=nbobjects(filename)
    index=ntom(0,taille)
    lignes=[]
    for i in range(0,nombre):
        nb=len(index)-1
        alea=randrange(nb)
        ligne=liste[index[alea]]
        del(index[alea])
        lignes.append(ligne)

    return lignes

