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
#Funcao de classificacao do Perceptron
#contida na biblioteca Scikit-Learn
from sklearn.linear_model import Perceptron
#Plotando graficos
import matplotlib.pyplot as plt



###########################
##Funcoes do seu programa##
###########################

#binariza a imagem
def binarizar(img,L):
    matriz = np.array(img)
    n,m=matriz.shape
    B=np.zeros((n,m))
    for i in range(n-1):
        for j in range(m-1):
            if matriz[i,j]>=L:
                B[i,j]=255
    img = Image.fromarray(B)
    return img


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
    ##binarizando as imagens
    #imgsb=[binarizar(imgO,128) for imgO in imgsO ]
    
    imgs = [ imgO.resize((nlin, ncol)) for imgO in imgsO] #imgsb
    
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

#imagens de mao aberta
pastaA1 = pasta+'/maoAberta/p1'
pastaA2 = pasta+'/maoAberta/p2'
pastaA3 = pasta+'/maoAberta/p3'
pastaA4 = pasta+'/maoAberta/p4'

#imagens de mao fechada
pastaF1 = pasta+'/maoFechada/p1'
pastaF2 = pasta+'/maoFechada/p2'
pastaF3 = pasta+'/maoFechada/p3'
pastaF4 = pasta+'/maoFechada/p4'

###carregando as imagens

###aberta
X1 = carregaImagens(pastaA1)
X2 = carregaImagens(pastaA2)
X3 = carregaImagens(pastaA3)

###fechada
X4 = carregaImagens(pastaF1)
X5 = carregaImagens(pastaF2)
X6 = carregaImagens(pastaF3)
#aqui vamos converter todos os dados em uma unica matriz de entrada
X = X2
#for Xi in [X2,X3,X4,X5,X6]:
for Xi in [X3,X5,X6]: ########teste:X1 e X4
    X = np.concatenate((X,Xi))

Conjuntoteste=X1
Conjuntoteste=np.concatenate((Conjuntoteste,X4))

#Aplicando o PCA sobre os dados
pca = decomposition.PCA(n_components=2)
pca.fit(X)
cts=decomposition.PCA(n_components=2)
cts.fit(Conjuntoteste)

#Representacao em Dimensao Reduzida
Y = pca.transform(X) 
CT=cts.transform(Conjuntoteste)
#Plotando os graficos
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

####rotulos para a classificacao
#Dados em 2D

#rotulos
K=np.zeros(800)
K[:400],K[400:]=0,1


####conjunto teste###
##X1 (aberta) e X4 (fechada)##


###################################
### Aplicando o Perceptron sobre os
### dados de treinamento
###################################


clf = Perceptron(tol=1e-10)
clf.fit(Y, K)
#Aplicando o Classificador sobre o conjunto de Teste,
classificador = clf.predict(CT)


###graficos###

cores = ['r','b'] # vermelho e azul

#plotando o conjunto de treinamento
for k,p in enumerate(Y): # k varia nos indices de X (como se X fosse apenas 
                         # um vetor) e p varia nos pontos de X 
    px = p[0]
    py = p[1]

    cor = cores[int(K[k])] 

    plt.scatter(px,py,c=cor)

#plotando o conjunto de testes
#com o perceptron aplicado
cores = ['g','orange'] # verde e laranja 
for k,q in enumerate(CT):
    qx = q[0]
    qy = q[1]

    indice = classificador[k]
    cor = cores[int(indice)]

    plt.scatter(qx,qy,c=cor)


#Delimitando os pontos
#extremos na tela de visualizacao
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()


# Cria a grade a ser aplicada no modelo
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)


# Plota as margens dos conjuntos.
ax.contour(XX, YY, Z,  colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])


###########Calculando o erro####
erro1=0
erro2=0
for i in range(len(classificador)):
    if(i<=199):
        if (classificador[i]!=0):
            erro1=erro1+1
    if(i>199):
        if(classificador[i]!=1):
            erro2=erro2+1

errototal=(erro1+erro2)/4
erroab=erro1/2
errofe=erro2/2
print('Erro:',errototal,'%')
print('Erro Mao aberta:',erroab,'%')
print('Erro Mao fechada:',errofe,'%')


#Exibe os graficos

 
plt.show()
