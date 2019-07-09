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
import os
import sys
os.chdir("../functions")
sys.path.append(os.getcwd())
from error import typeError
os.chdir("../classes")

class Propositions:
    """
    cette class represente la structure des propositions pour
    le jeu qui veut gagner des millions
    """
    def __init__(self, A, B, C, D):
        if(type(A)!=type(B) or type(B)!=type(C) or type(C)!=type(D) or type(D)!=type("")):
            typeError("les propositions sont des chaines")
        self.values={"A":A,"B": B,"C": C,"D": D}