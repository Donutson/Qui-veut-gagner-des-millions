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

#class
class Pallier:
    """
    Cette classe represente la structure d'un
    pallier pour le jeu qui veut gagner des millions
    """
    pallier1=[1,2,3,5,10]
    pallier2=[15,20,25,30,50]
    pallier3=[60,70,80,90,100]
    niveauset={1,2,3}
    def __init__(self):
        self._niveau=1
        self._questions=[]
        self._gains=Pallier.pallier1
        self._numquestion=0
    #getter
    def __get__niveau(self):
        return self._niveau
    def __get__questions(self):
        return self._questions
    def __get__gains(self):
        return self._gains
    def __get__numquestion(self):
        return self._numquestion
    #setter
    def __set__niveau(self, valeur):
        if( valeur!=4):
            self._niveau=valeur
    def __set__questions(self, questions):
        self._questions=questions
    def __set__gains(self, gains):
        self._gains=gains
    def __set__numquestion(self, num):
        self._numquestion=num
    #methode special
    def __add__(self, pas):
        """
        il suffit de faire pallier+pas
        pour augmenter le niveau du pas donnÃƒÆ’Ã‚Â© voulu
        """
        self.__set__niveau(self.niveau+pas)
    #property
    niveau=property(__get__niveau,__set__niveau)
    questions=property(__get__questions,__set__questions)
    gains=property(__get__gains,__set__gains)
    numquestion=property(__get__numquestion,__set__numquestion)


