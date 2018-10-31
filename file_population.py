from threading import Thread
import time
import random
from os import urandom
from time import time

arq = open('table.txt','wb')

linhas = 0 #Id
nThreads = 10

#Gerador de Dados binarios

def gerarDados(contador):
    global linhas, nThreads
    
    while contador < 10:
        #print("Requisição: ", linhas)
 
        #texto = str(linhas) + "," + sexo + "," + idade + "," + renda + "," + escolaridade + "," + idioma + "," + pais + "," + latitude + "," + longitude + "\n"
        arq.write(urandom(80000000))

        #linhas += 1
        contador += 1
    print(time()-inicio)

def gerarThread():
    return Thread(target=gerarDados,args=[0])

def gerarVariasThreads():
    global nThreads, thread
    
    for _ in range(nThreads):
        gerarThread().start()

inicio = time()
gerarVariasThreads()
