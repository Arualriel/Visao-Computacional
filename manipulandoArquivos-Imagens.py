###############
##Bibliotecas##
###############

#Bibioteca numerica
import numpy as np

#Manipulacao de imagens
from PIL import Image

#Manipulacao de arquivos
import os

#Modulo contendo a funcao do PCA
from sklearn import decomposition

#Plotando graficos
import matplotlib.pyplot as plt


###########################
##Funcoes do seu programa##
###########################

#carrega as imagens e as converte em vetores (nlin)x(mcol) de dimensao
def carregaImagens(pasta):
    #caminhos dos arquivos contidos na pasta
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    #lista dos arquivos contidos na pasta 
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    #lista os arquivos de imagens com extensao png
    pngs = [arq for arq in arquivos if arq.lower().endswith(".png")]
    #carrega as imagens contidas na lista "pngs"
    imgsO = [Image.open(png).convert('L') for png in pngs]
    #redimensiona as imagens carregadas em "imgsO"
    nlin,ncol = 160,60 
    '''
    aqui pode entrar a segmentacao e transformar as imagens em binarias
    verificar se o erro aumenta ou nao
    '''
    imgs = [ imgO.resize((nlin, ncol)) for imgO in imgsO]
    
    #converte as imagens em matrizes
    mats = [np.array(im) for im in imgs]
    #converte as matrizes em vetores de dimensao n*m
    num, n,m = np.shape(mats)
    vetores = [np.reshape(mat,n*m) for mat in mats]

    return vetores

###############
###principal###
###############

#pasta guarda o caminho onde este script foi armazenado
pasta = os.path.dirname(os.path.abspath(__file__))

###conjunto de treinamento
'''
em cada conjunto ha 200 imagens com reslucao original de 640x240
'''
#imagens de mao aberta
pastaA1 = pasta+'/maoAberta/p1'
pastaA2 = pasta+'/maoAberta/p2'
pastaA3 = pasta+'/maoAberta/p3'

#imagens de mao fechada
pastaF1 = pasta+'/maoFechada/p1'
pastaF2 = pasta+'/maoFechada/p2'
pastaF3 = pasta+'/maoFechada/p3'


###carregando as imagens


X1 = carregaImagens(pastaA1)
X2 = carregaImagens(pastaA2)
X3 = carregaImagens(pastaA3)

X4 = carregaImagens(pastaF1)
X5 = carregaImagens(pastaF2)
X6 = carregaImagens(pastaF3)

#aqui vamps converter todos os dados em uma unica matriz de entrada
X = X1
#for Xi in [X2,X3,X4,X5,X6]:
for Xi in [X2,X3,X4,X5,X6]:
    X = np.concatenate((X,Xi))


#Aplicando o PCA sobre os dados
pca = decomposition.PCA(n_components=2)
pca.fit(X)

#Representacao em Dimensao Reduzida
Y = pca.transform(X) 

#Plotando os graficos
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

#%matplotlib notebook


#Dados em 2D
k1,k2,k3,k4,k5 = 200,400,600,800,1000
#mao aberta
ax1.scatter(Y[:k1,0],Y[:k1,1],c='b')
ax1.scatter(Y[k1:k2,0],Y[k1:k2,1],c='r')
#mao fechada
ax1.scatter(Y[k2:k3,0],Y[k2:k3,1],c='orange')
ax1.scatter(Y[k3:k4,0],Y[k3:k4,1],c='g')

ax1.scatter(Y[k4:k5,0],Y[k4:k5,1],c='k')
ax1.scatter(Y[k5:,0],Y[k5:,1],c='m')


#Exibe os graficos
plt.show()

'''
escolher dois conjuntos para aprendizado e um para teste
usando um classificador (perceptron ou svm)/ ou os dois e comparar
verificar a taxa de erros (quantas sao classificadas de forma errada e
verificar a percentagem de erro)
usar ki como rotulos para auxiliar o classificador
'''