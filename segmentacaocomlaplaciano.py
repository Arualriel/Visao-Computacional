#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:50:58 2019

@author: laura
"""



import numpy as np
from PIL import Image
import time
import matplotlib.pyplot as plt

#
#def erosao(matriz):
#    n,m=np.shape(matriz)
#    for i in range(1,n-1):
#        for j in range(1, m-1):
#            if(matriz[i,j+1]==255)and(matriz[i+1,j]==255)and(matriz[i,j-1]==255)and(matriz[i-1,j]==255):
#                matriz[i,j]=255
#    return matriz

def binarizar(matriz,L):
    n,m=matriz.shape
    B=np.zeros((n,m))
    for i in range(n-1):
        for j in range(m-1):
            if matriz[i,j]>=L:
                B[i,j]=255
    return B

def contornograd(matriz): 
    n,m=matriz.shape
    fx,fy=0,0
    norma=0
    M=np.zeros((n,m))
    for j in range(m-1):
        for i in range(n-1):
            if (j==0) or (i==0) or (i==(n-1)):
                fy=(matriz[i,j+1]-matriz[i,j])
                fx=(matriz[i+1,j]-matriz[i,j])
            if(j==(m-1)):
                fy=(matriz[i,j]-matriz[i,j-1])
                fx=(matriz[i,j]-matriz[i-1,j])
                
            if (j!=0) and (i!=0) and (i!=(n-1)) and (j!=(m-1)):
                fy=((matriz[i,j+1]-matriz[i,j-1]))
                fx=((matriz[i+1,j]-matriz[i-1,j]))
                
            norma=int((fx**2+fy**2)**(1/2))
            if norma>255:
                norma=255
                
            M[i,j]= norma
    return M
 

def EFG(fx,fy):
    traco,det,E,F,G=0,0,0,0,0
    l1,l2,maximo=0,0,0
    E=(1+fx**2)
    F=(fx*fy)
    G=(1+fy**2)
    traco=E+G
    det=E*G-F**2
    delta=(traco**2-4*det)
    l1=(traco+(delta)**(1/2))/2
    l2=(traco-(delta)**(1/2))/2
    if abs(l1)>=abs(l2):
        maximo=int(abs(l1))
    else:
        maximo=int(abs(l2))
    if maximo>=255:
        maximo=255
        
    
    return maximo


def contornoepg(matriz): 
    n,m=matriz.shape
    fx,fy,ro=0,0,0

    M=np.empty((n,m))
    for i in range(n-1):
        for j in range(m-1):
            if (j==0) or (i==0) or (i==(n-1)):
                fy=(matriz[i,j+1]-matriz[i,j])
                fx=(matriz[i+1,j]-matriz[i,j])
            if(j==(m-1)):
                fy=(matriz[i,j]-matriz[i,j-1])
                fx=(matriz[i,j]-matriz[i-1,j])
                
            if (j!=0) and (i!=0) and (i!=(n-1)) and (j!=(m-1)):
                fy=((matriz[i,j+1]-matriz[i,j-1]))
                fx=((matriz[i+1,j]-matriz[i-1,j]))
            ro=EFG(fx,fy)    

            M[i,j]=ro
    return M

def contornolap(matriz): 
    n,m=matriz.shape
    fx,fy=0,0
    lap=0
    maior=0
    M=np.zeros((n,m))
    M[:,:]=255
    print(M)
    for j in range(m-1):
        for i in range(n-1):
            if (j==0) or (i==0) or (i==(n-1)):
                fy=(matriz[i,j+1]-matriz[i,j])
                fx=(matriz[i+1,j]-matriz[i,j])
            if(j==(m-1)):
                fy=(matriz[i,j]-matriz[i,j-1])
                fx=(matriz[i,j]-matriz[i-1,j])
                
            if (j!=0) and (i!=0) and (i!=(n-1)) and (j!=(m-1)):
                fy=((matriz[i,j+1]-2*matriz[i,j]+matriz[i,j-1])/2)
                fx=((matriz[i+1,j]-2*matriz[i,j]+matriz[i-1,j])/2)
                
            
            
            lap=255-int(abs(fx+fy))
            
            if lap>=maior:
                maior =lap
            
            if lap<0:
                lap=0
                 
            if lap<255:
                lap=0

            M[i,j]= lap
    print (maior)
    return M

def contornohess(matriz):
    M=matriz
    n,m = np.shape(M)
    detH = np.zeros((n,m))
    B = np.zeros((n,m))

    h1 = 5000
    h2=0.5
    for i in range(1,n-1):
        for j in range(1,m-1):
            fxx = (M[i+1,j]-2.0*M[i,j] + M[i-1,j])
            fyy = (M[i,j+1]-2.0*M[i,j] + M[i,j-1])
            fxy = 0.25*(M[i+1,j+1]-M[i-1,j+1] - M[i+1,j-1] + M[i-1,j-1])
            
            n1=(fxx**2+fxy**2)**0.5
            n2=(fyy**2+fxy**2)**0.5
            
            if(n1!=0)and(n2!=0):
                a11=fxx/n1
                a12=fxy/n1
                a21=fxy/n2
                a22=fyy/n2
            
            
            
                detH[i,j] = np.abs(a11*a22-a21*a12)
                if detH[i,j] < h2:
                    B[i,j]=255
            else:
                detH[i,j] = np.abs(fxx*fyy-fxy**2.0)
                if detH[i,j] > h1:
                    B[i,j]=255

    return B
      
tempoinicio=time.time()                
img1 = Image.open('img456.png').convert('L')
#img1.show()
matriz = np.array(img1)
L1,L2,L3,L4,L5,L6=110,120,100,110,115,115  
#plt.hist(matriz, bins='auto')  
#plt.title("Histogram with 'auto' bins")
#plt.show()
M=binarizar(matriz,L6)
img = Image.fromarray(M)
img.show()
#

tempolap=time.time()
#M4=contornolap(matriz)
#
#img4 = Image.fromarray(M4)
#img4.show()
#M45=M+M4
#img7 = Image.fromarray(M45)
#img7.show()
#
##tempolap=time.time()-tempolap
##img4.save('4-3.png')
#
##tempograd=time.time()
#M2=contornograd(matriz)
#img2 = Image.fromarray(M2)
#img2.show()
##tempograd=time.time()-tempograd
##img2.save('2-3.png')
#
##tempoepg=time.time()
#M3=contornoepg(matriz)
#img3 = Image.fromarray(M3)
#img3.show()
##tempoepg=time.time()-tempoepg
##img3.save('3-3.png')
#
#
##
##tempohess=time.time()
#M5=contornohess(matriz)
#img5 = Image.fromarray(M5)
#img5.show()
##tempohess=time.time()-tempohess
##img5.save('5-3.png')
##tempofinal=time.time()-tempoinicio
#M23456=-M45+M2+M3-M5
#img25 = Image.fromarray(M23456)
#img25.show()
##
##print("segundos gradiente",tempograd)
##print("segundos primeira forma fundamental",tempoepg)
##print("segundos laplaciano",tempolap)
##print("segundos hessiana",tempohess)
##print("segundos final",tempofinal)