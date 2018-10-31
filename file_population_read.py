import time
import threading
from threading import Thread
from os import urandom

#1-sexo,7-idade,10-renda,2-escolaridade,12-dioma,8-país,24-localizador
paises={}

def get_file():
    return open('table.txt','rb')

def read_file(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    while (cont < limit):
        tmp = buffer_bytes.read(nRead)
        '''print("sexo:",get_sexo(tmp))
        print("idade:",get_idade(tmp))
        print("renda:",get_renda(tmp))
        print("escolaridade:",get_escolaridade(tmp))
        print("idioma:",get_idioma(tmp))
        print("pais:",get_pais(tmp))
        print("localidade:",get_localidade(tmp))'''
        cont += 1
    #print(cont)

#SELECT pais, sexo, idade, count(*) FROM pop GROUP BY pais, sexo, idade;
def query_1(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)

        if pais not in paises:
            paises[pais] = {sexo:1}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = 1
            else:
                paises[pais][sexo] += 1
    fim = time.time()
    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    #print("Reg:",cont)
    print("Time query1:",fim-inicio)

#SELECT pais, sexo, idade, count(*) FROM pop GROUP BY pais, sexo, idade;
def query_2(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)
        idade = get_idade(tmp)

        if pais not in paises:
            paises[pais] = {sexo:{idade:1}}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = {idade:1}
            else:
                if idade not in paises[pais][sexo]:
                    paises[pais][sexo][idade] = 1
                else:
                    paises[pais][sexo][idade] += 1
                    
    fim = time.time()
    '''for pais in paises:
        for sexo in paises[pais]:
            for idade in paises[pais][sexo]:
                print(pais,":",sexo,":",idade,':',paises[pais][sexo][idade])'''
    #print("Reg:",cont)
    print("Time query2:",fim-inicio)

#SELECT pais, sexo, avg(renda) FROM pop GROUP BY pais, sexo;
def query_3(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)
        renda = get_renda(tmp)

        if pais not in paises:
            paises[pais] = {sexo:[1,renda]}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = [1,renda]
            else:
                paises[pais][sexo][0] += 1
                paises[pais][sexo][1] += renda
    fim = time.time()
    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y][1]/paises[x][y][0])'''
    #print("Reg:",cont)
    print("Time query3:",fim-inicio)

#SELECT país, sexo, avg(idade) FROM pessoas GROUP BY país, sexo
def query_4(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)
        idade = get_idade(tmp)

        if pais not in paises:
            paises[pais] = {sexo:[1,idade]}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = [1,idade]
            else:
                paises[pais][sexo][0] += 1
                paises[pais][sexo][1] += idade
    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y][1]/paises[x][y][0])'''
    print("Time query4:",fim-inicio,"sec")

#SELECT país, sexo, count(*) FROM pessoas WHERE país = 15 GROUP BY país, sexo;
def query_5(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)

        if pais == 15:
            if pais not in paises:
                paises[pais] = {sexo:1}
            else:
                if sexo not in paises[pais]:
                    paises[pais][sexo] = 1
                else:
                    paises[pais][sexo] += 1

    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query5: ",fim-inicio,"sec")

#SELECT país, sexo, count(*) FROM pessoas WHERE país = 15 AND sexo = 1 GROUP BY país, sexo;
def query_6(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)

        if pais == 15:
            if pais not in paises:
                if sexo:
                    paises[pais] = {sexo:1}
            elif sexo:
                paises[pais][sexo] += 1
                
    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query6: ",fim-inicio,"sec")

#SELECT país, sexo, count(*) FROM pessoas WHERE país >=0 AND país <=15 GROUP BY país, sexo;
def query_7(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        sexo = get_sexo(tmp)

        if pais >= 0 and pais <= 15:
            if pais not in paises:
                paises[pais] = {sexo:1}
            else:
                if sexo not in paises[pais]:
                    paises[pais][sexo] = 1
                else:
                    paises[pais][sexo] += 1

    fim = time.time()
    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query7: ",fim-inicio,"sec")

#SELECT idioma, pais, count(*) FROM pop GROUP BY idioma, pais
def query_adv1(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    idiomas = {}
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        idioma = get_idioma(tmp)

        if idioma not in idiomas:
            idiomas[idioma] = {pais:1}
        else:
            if pais not in idiomas[idioma]:
                idiomas[idioma][pais] = 1
            else:
                idiomas[idioma][pais] += 1
    fim = time.time()
    
    '''for x in idiomas:
        for y in idiomas[x]:
            print(x,":",y,":",idiomas[x][y])'''
    print("Time query_adv1:",fim-inicio,"sec")

#SELECT pais, escolaridade, count(*) FROM pop GROUP BY pais, escolaridade;
def query_adv2(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    global paises
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        pais = get_pais(tmp)
        escolaridade = get_escolaridade(tmp)

        if pais not in paises:
            paises[pais] = {escolaridade:1}
        else:
            if escolaridade not in paises[pais]:
                paises[pais][escolaridade] = 1
            else:
                paises[pais][escolaridade] += 1
    fim = time.time()
    
    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query_adv2:",fim-inicio,"sec")

#SELECT sexo, renda, pais, count(*) FROM pop GROUP BY sexo, renda, pais
def query_adv3(buffer_bytes,limit):
    nRead=8
    cont=0
    limit = limit/8
    sexos = {}
    inicio = time.time()
    while (cont < limit):
        cont+=1
        tmp = buffer_bytes.read(nRead)
        sexo = get_sexo(tmp)
        renda = get_renda(tmp)
        pais = get_pais(tmp)

        if sexo not in sexos:
            sexos[sexo] = {renda:{pais:1}}
        else:
            if renda not in sexos[sexo]:
                sexos[sexo][renda] = {pais:1}
            else:
                if pais not in sexos[sexo][renda]:
                    sexos[sexo][renda][pais] = 1
                else:
                    sexos[sexo][renda][pais] += 1

    fim = time.time()
    for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])
    print("Time query_adv3:",fim-inicio,"sec")

def get_sexo(byte_8):
    return byte_8[0] >> 7

def get_idade(byte_8):
    return byte_8[0] - ((byte_8[0] >> 7) << 7)

def get_renda(byte_8):
    return (byte_8[1]<<2)+(byte_8[2]>>6)

def get_escolaridade(byte_8):
    return (byte_8[2]>>4)-((byte_8[2]>>6)<<2)

def get_idioma(byte_8):
    return ((byte_8[2]-((byte_8[2]>>4)<<4))<<8)+byte_8[3]

def get_pais(byte_8):
    return byte_8[4]

def get_localidade(byte_8):
    return (((byte_8[5]<<8)+byte_8[6])<<8)+byte_8[7]
    
def gerarThread(file,base,salto,function):
    file.seek(base,0)
    return Thread(target=function,args=[file,salto])

def gerarVariasThreads(function):
    n = 10
    salto = 800000000
    thr = []
    for x in range(n):
        #print('base:',x*salto,'\nlimit:',(x*salto)+salto)
        thr.append(gerarThread(get_file(),x*salto,salto,function))
    return thr

#thrs = gerarVariasThreads(read_file)
thrs = gerarVariasThreads(query_1)
#thrs = gerarVariasThreads(query_2)
#thrs = gerarVariasThreads(query_3)
#thrs = gerarVariasThreads(query_4)
#thrs = gerarVariasThreads(query_5)
#thrs = gerarVariasThreads(query_6)
#thrs = gerarVariasThreads(query_7)
#thrs = gerarVariasThreads(query_adv1)
#thrs = gerarVariasThreads(query_adv2)
#thrs = gerarVariasThreads(query_adv3)

ini = time.time()
for t in thrs:
    t.start()

while(len(threading.enumerate())>2):
    time.sleep(1)
    print(time.time()-ini)
fim = time.time()-ini

print(fim,'sec')
