#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 09:32:07 2019

@author: laura
"""

import numpy as np
from PIL import Image
import time


#Entrada: Matriz binaria.
#
img = Image.open('mine.png').convert('L') #abrir
#img.show()
B = np.array(img) ##matriz
#print(B)

#B=np.zeros((51,51))
#B[25,25]=1

#Determinando as posições dos elementos diferentes de zero.
tempoinicio=time.time()
m,n = np.shape(B) #ordem da matriz
print(m,n)
for i in range(m):
    for j in range(n):
        if B[i,j]>=127:
            B[i,j]=0
        else:
            B[i,j]=1

#Busca de elementos nao nulos
aux = []
for i in range(n):
    for j in range(m):
        if B[i,j] != 0.0:
            aux = aux + [[i,j]]
#matriz com os indices de elementos nao nulos
N = np.matrix(aux)

p = len(N) #numero de elementos nao nulos.
D = np.zeros((m,n)) #matriz de distancias
A = np.zeros((m,n))
C = np.zeros((m,n))
for i in range(n):
    for j in range(m):
        if B[i,j] == 0.0 :
            u = (i,j)
            
            auxD = np.zeros(p)
            auxA = np.zeros(p)
            auxC = np.zeros(p)
            for k in range(p):
                v = N[k,:]
                
                u = np.array(u)
                v = np.array(v)
                w=np.array(u-v)
                #print (len(w))
                dist1 = np.linalg.norm(u-v)
               # maximo=-1
                #print (w)
                #distancia man
                
#                for i in range(len(w)):
#                    if abs(w[0,i])>=maximo:
#                        maximo=abs(w[0,i])
#                dist=maximo
                
                dist2=abs(w[0,1])+abs(w[0,0])
                dist3=max(abs(w[0,1]),abs(w[0,0]))
                #print (dist)
                
                auxD[k] = dist1
                auxA[k] = dist2
                auxC[k] = dist3
                
            
            D[i,j] = np.min(auxD)
            A[i,j]=np.min (auxA)
            C[i,j]=np.min (auxC)
            #print (A,C,D)
            
   

print("segundos",time.time()-tempoinicio)

import matplotlib.pyplot as plt



plt.matshow(D)
plt.matshow(A)
plt.matshow(C)
plt.show()
