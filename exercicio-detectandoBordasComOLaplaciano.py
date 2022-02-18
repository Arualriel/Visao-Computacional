#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:19:44 2019

@author: laura
"""

import numpy as np

import matplotlib.pylab as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


a = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
	[0,0,0,1,1,0,0,0],[0,0,1,1,1,1,0,0],
	[0,0,1,1,1,1,0,0],[0,0,0,1,1,0,0,0],
	[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

A = np.matrix(a)

#b = [[0,0,0,0],
#	[0,3.0/4.0, 3.0/4.0,0],
#	[0,3.0/4.0, 3.0/4.0,0],
#	[0,0,0,0]]

# = np.matrix(b)

na,ma  =  np.shape(A)
#nb,mb  = np.shape(B)

xa = range(na)
ya = range(ma)

#xb = range(nb)
#yb = range(mb)

Xa,Ya = np.meshgrid(xa,ya)
#Xb,Yb = np.meshgrid(xb,yb)

####################################################
####################################################
fx = np.zeros((na,ma))
fy = np.zeros((na,ma))
G = np.zeros((na,ma))

for i in range(na-1):
    for j in range(ma-1):
        fx[i,j] = A[i+1,j] - A[i,j]        
        fy[i,j] = A[i,j+1] - A[i,j]
        
        G[i,j] = ((fx[i,j])**2 + (fy[i,j])**2)**0.5        
        

#print fx
#print fy
#print G

gradL = np.zeros((na,ma,2))

for i in range(1,na-1):
    for j in range(1,ma-1):
        Lx = 0.5*(A[i+1,j] - A[i-1,j])
        Ly = 0.5*(A[i,j+1] - A[i,j-1])

        gradL[i,j] = [Lx,Ly]




####################################################

fig0 = plt.figure()
ax0 = fig0.add_subplot(111)

ax0.matshow(A, cmap='Greys')




fig1 = plt.figure()
ax1 = fig1.add_subplot(221)

ax1.matshow(A, cmap='Greys')
ax1.grid()


fig2 = plt.figure()
ax2 = fig2.add_subplot(222, projection='3d')





fig3 = plt.figure()
ax3 = fig3.add_subplot(223, projection='3d')

ax3.plot_surface(Xa,Ya,A,rstride=1, cstride=1, cmap=cm.coolwarm,
                                       linewidth=0, antialiased=False)



fig4 = plt.figure()
ax4 = fig4.add_subplot(224)

ax4.quiver( Xa, Ya, gradL[:,:,0], gradL[:,:,1],pivot='mid', units='inches')
ax4.scatter(Xa, Ya , color='r', s=5)








for i in range(na):
    for j in range(ma):
        ax2.scatter(Xa[i,j],Ya[i,j],A[i,j])
        ax1.scatter(Xa[i,j],Ya[i,j])        



#ax3.matshow(B, cmap='Greys')
#ax3.grid()




