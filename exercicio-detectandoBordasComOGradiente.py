#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:12:35 2019

@author: laura
"""

#Bibliotecas 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from PIL import Image

#carregando a imagem
img = Image.open('folha.jpg').convert('L')

#convertendo a imagem em matriz
M = np.array(img)

n,m = np.shape(M) #ordem da matriz



#Plotando a imagem em tons de cinza

fig0 = plt.figure()

ax0 = fig0.add_subplot(111)

ax0.matshow(M, cmap='Greys')



#################################
#calculando o Gradiente
#################################

# Variaveis auxiliares para armazenar 
# G = Gradiente
# nG = norma do gradiente.

nG = np.zeros((n,m))
G  = np.zeros((n,m))


# loop para "varrer" os elementos da matriz
# de forma que seja possivel calcular as 
# derivadas parciais por diferenças centrais.

for i in range(1,n-1):
    for j in range(1,m-1):
        fx = (M[i+1,j]-2*M[i,j]+M[i-1,j])
        fy = (M[i,j+1]-2*M[i,j]+M[i,j-1])
        
        nG[i,j] = ((fx)**2 + (fy)**2)**0.5 
        if (nG[i,j] != 0.0):
            G[i,j]=1

        
#Plotando o grafico das normas do gradiente.
fig2 = plt.figure()
fig3 = plt.figure()
ax2 = fig2.add_subplot(111)
ax3= fig3.add_subplot(111)
ax2.matshow(G, cmap='Greys')
ax3.matshow(nG, cmap='Greys')






########################################
########################################
# Curiosidades
########################################
#
##gerando uma malha para plotar em 3D
#x = range(n)
#y = range(m)
#X,Y = np.meshgrid(x,y)
#
#fig = plt.figure()
#
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(X,Y,M,rstride=1, cstride=1,linewidth=0, antialiased=False)
#





plt.show()
