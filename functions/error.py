#-------------------------------------------------------------------------------
# Name:        module2
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
ce paquet est censÃ©e gÃ©rer les differentes
erruers possibles concernant le type ou
l'ensemble de valeurs possible pour nos variables/objets
dans le jeu qui veut gagner des millions
"""


#erreurs basique
def typeError(message):
    raise TypeError(message)

def valueError(message):
    raise ValueError(message)

#erreur concernant les types
def Typeerror(element,message,classe):
    if( type(element) != type(classe)):
            typeError(message)

#erreurs concernant les valeurs
def setvalueError(element,ensemble,message):
    if(element not in ensemble):
            valueError(message)