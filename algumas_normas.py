#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:50:13 2019

@author: laura
"""

# algumas normas (distâncias) no plano

import numpy as np

def Euclediana(a,b,tamanho):
    norma=0
    for i in range(tamanho):
        norma=(a[i]-b[i])**2+norma
    norma=(norma)**(1/2)
    return norma
def Manhattan(a,b,tamanho):
    norma=0
    for i in range(tamanho):
        if((a[i]-b[i])>=0):
            norma=(a[i]-b[i])+norma
        else:
            norma=-(a[i]-b[i])+norma
    return norma
def Tabuleiro_de_xadrez(a,b,tamanho):
    norma=0
    maior=0
    if(a[0]-b[0])>=0:
        maior=a[0]-b[0]
    else:
        maior=-(a[0]-b[0])
    
    for i in range(tamanho):
        if((a[i]-b[i])>=0):
            if((a[i]-b[i])>=maior):
                maior=(a[i]-b[i])
        else:
            if((b[i]-a[i])>=maior):
                maior=(b[i]-a[i])
    norma=maior
    return norma


a=[2,3]
b=[-1,0]
tamanho=2

euc=Euclediana(a,b,tamanho)
man=Manhattan(a,b,tamanho)
tab=Tabuleiro_de_xadrez(a,b,tamanho)

print('distancia euclideana=',euc)    
print('/n')
print('distancia manhattan=',man)    
print('/n')
print('distancia do tabuleiro de xadrez=',tab)    