import time

#colums = ['id','sexo','idade','renda','escolaridade','idioma','pais','longitude','longitude']

#SELECT pais, sexo, count(*) FROM pop GROUP BY pais, sexo;
def query_1(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]

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
    print("Time query1:",fim-inicio,"sec")

#SELECT pais, sexo, idade, count(*) FROM pop GROUP BY pais, sexo, idade;
def query_2(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]
        idade = split_tmp[2]

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
    print("Time query2:",fim-inicio,"sec")

#SELECT pais, sexo, avg(renda) FROM pop GROUP BY pais, sexo;
def query_3(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]
        renda = split_tmp[3]

        if pais not in paises:
            paises[pais] = {sexo:[1,int(renda)]}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = [1,int(renda)]
            else:
                paises[pais][sexo][0] += 1
                paises[pais][sexo][1] += int(renda)
    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y][1]/paises[x][y][0])'''
    print("Time query3:",fim-inicio,"sec")

def query_4(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]
        idade = split_tmp[2]

        if pais not in paises:
            paises[pais] = {sexo:[1,int(idade,2)]}
        else:
            if sexo not in paises[pais]:
                paises[pais][sexo] = [1,int(idade,2)]
            else:
                paises[pais][sexo][0] += 1
                paises[pais][sexo][1] += int(idade,2)
    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y][1]/paises[x][y][0])'''
    print("Time query4:",fim-inicio,"sec")

def query_5(file):
    paises = {}

    inicio = time.time()  
    
    for f in file:        
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]

        if pais == '1111' and pais not in paises:
            paises[pais] = {sexo:1}
        elif pais == '1111' and pais in paises:
            if sexo not in paises[pais]:
                paises[pais][sexo] = 1
            else:
                paises[pais][sexo] += 1
    fim = time.time()

    ''''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query5: ",fim-inicio,"sec")


def query_6(file):
    paises = {}

    inicio = time.time()  
    
    for f in file:        
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]

        if pais == '1111' and pais not in paises:
            if sexo == '1':
                paises[pais] = {sexo:1}
        elif pais == '1111' and pais in paises:
            if sexo == '1':
                paises[pais][sexo] += 1
                
    fim = time.time()

    '''for x in paises:
        for y in paises[x]:
            print(x,":",y,":",paises[x][y])'''
    print("Time query6: ",fim-inicio,"sec")

from operator import itemgetter

def query_7(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        sexo = split_tmp[1]

        if int(pais) >= 0 and int(pais) <= 1111:
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
def query_adv1(file):
    idiomas = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        idioma = split_tmp[5]
        pais = split_tmp[6]

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
def query_adv2(file):
    paises = {}

    inicio = time.time()
    for f in file:
        split_tmp = f.split(',')
        pais = split_tmp[6]
        escolaridade = split_tmp[4]

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
    

def open_file(name_file):
    f = open(name_file,'r')
    return f

query_1(open_file('export.csv'))
query_2(open_file('export.csv'))
query_3(open_file('export.csv'))
query_4(open_file('export.csv'))
query_5(open_file('export.csv'))
query_6(open_file('export.csv'))
query_7(open_file('export.csv'))
query_adv1(open_file('export.csv'))
query_adv2(open_file('export.csv'))
#query_adv3(open_file('export.csv'))

