from threading import Thread
import time
import random

arq = open('table1.txt', 'w')

linhas = 1 #Id
nThreads = 10000
thread = []

#Gerador de Dados binarios

def gerarDados(contador):
    global linhas, nThreads
    
    while contador <= 500:
        sexo = str(bin(random.randint(0,1)))[2:]
        idade = str(bin(random.randint(0,127)))[2:]
        renda = str(bin(random.randint(0,1023)))[2:]
        escolaridade = str(bin(random.randint(0,3)))[2:]
        idioma = str(bin(random.randint(0,4095)))[2:]
        pais = str(bin(random.randint(0,255)))[2:]
        latitude = str(bin(random.randint(0,4095)))[2:]
        longitude = str(bin(random.randint(0,4095)))[2:]

        #print("Requisição: ", linhas)
 
        texto = str(linhas) + "," + sexo + "," + idade + "," + renda + "," + escolaridade + "," + idioma + "," + pais + "," + latitude + "," + longitude + "\n"
        arq.write(texto)

        linhas += 1    
        contador += 1

        if linhas % 100000 == 0:
            print(linhas)
        #time.sleep(0.03)

def gerarThread():
    return Thread(target=gerarDados,args=[1])

def gerarVariasThreads():
    global nThreads, thread
    
    for _ in range(nThreads):
        gerarThread().start()

gerarVariasThreads()

