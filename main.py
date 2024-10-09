from distancias import Distancia_Levenshtein, Distancia_Euclidiana, Distancia_Angular, teclasProximas
from time import time 

def inverter_palavras(dic):
    return [palavra[::-1] for palavra in dic]

def remover_duplicadas(lista):
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    return lista_unica

def busca_binaria(dicionario, prefixo, inicio, fim):
    prefixo = prefixo.lower()
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    palavra_meio = dicionario[meio].lower()

    if palavra_meio.startswith(prefixo):
        if meio == 0 or not dicionario[meio - 1].lower().startswith(prefixo):
            return meio
        else:
            return busca_binaria(dicionario, prefixo, inicio, meio - 1)
    elif palavra_meio < prefixo:
        return busca_binaria(dicionario, prefixo, meio + 1, fim)
    else:
        return busca_binaria(dicionario, prefixo, inicio, meio - 1)

def Edicao(palavra_original, palavra, lista, limite):
    distLev = Distancia_Levenshtein(palavra_original, palavra)

    dados = {"nome": palavra, "distLev": distLev}
        
    if len(lista) < limite:
        lista.append(dados)
    else:
        maior_dist = max(lista, key=lambda x: x['distLev'])
        if distLev < maior_dist['distLev']:
            lista.remove(maior_dist)
            lista.append(dados)
    return lista

def Eucliciana(palavra_original, palavra, lista, limite):
    distEuc = Distancia_Euclidiana(palavra_original, palavra)

    dados = {"nome": palavra,"distEuc": distEuc}
    
    if len(lista) < limite:
        lista.append(dados)
    else:
        maior_dist = max(lista, key=lambda x: x['distEuc'])
        if distEuc < maior_dist['distEuc']:
            lista.remove(maior_dist)
            lista.append(dados)
    return lista

def Angular(palavra_original, palavra, lista, limite):
    distAng = Distancia_Angular(palavra_original, palavra)

    dados = {"nome": palavra,"distAng": distAng}
        
    if len(lista) < limite:
        lista.append(dados)
    else:
        maior_dist = max(lista, key=lambda x: x['distAng'])
        if distAng < maior_dist['distAng']:
            lista.remove(maior_dist)
            lista.append(dados)
    return lista

def busca_palavras(dicionario, prefixo, palavra_original, invertido, dist, limite=5):
    index = busca_binaria(dicionario, prefixo, 0, len(dicionario) - 1)

    if index == -1:
        return []
    
    lista = []
    i = index

    while i < len(dicionario):
        palavra = dicionario[i]
        if not palavra.lower().startswith(prefixo.lower()):
            break
        if palavra_original == palavra:
            i += 1
            continue

        if dist == 1:
            lista = Edicao(palavra_original, palavra, lista, limite)
        elif dist == 2:
            lista = Eucliciana(palavra_original, palavra, lista, limite)
        elif dist == 3:
            lista = Angular(palavra_original, palavra, lista, limite)
        else:
            print('Tipo de distância indisponivel: ')
            break

        i += 1
    return lista

def main(dicionario, dicionario_inv, palavra, original, dist = 1, lista=[]):
    # Buscar no dicionário normal
    prefixo = palavra[:len(palavra) // 2]
    resultado_normal = busca_palavras(dicionario, prefixo, original, False, dist)
    
    # Buscar no dicionário invertido
    palavra_invertida_original = original[::-1]
    prefixo_invertido = palavra_invertida_original[:len(palavra_invertida_original) // 2]
    resultado_invertido = busca_palavras(dicionario_inv, prefixo_invertido, palavra_invertida_original, True, dist)
    
    if dist == 1:
        resultado_invertido = [{"nome": item["nome"][::-1], "distLev": item["distLev"]} for item in resultado_invertido]

        resultado_total = resultado_normal + resultado_invertido + lista
        resultado_total = remover_duplicadas(resultado_total)
        resultado_total.sort(key=lambda x: x['distLev'])
        resultado_total = resultado_total[:5]
    elif dist == 2: 
        resultado_invertido = [{"nome": item["nome"][::-1], "distEuc": item["distEuc"]} for item in resultado_invertido]

        resultado_total = resultado_normal + resultado_invertido + lista
        resultado_total = remover_duplicadas(resultado_total)
        resultado_total.sort(key=lambda x: x['distEuc'])
        resultado_total = resultado_total[:5]
    elif dist == 3:
        resultado_invertido = [{"nome": item["nome"][::-1], "distAng": item["distAng"]} for item in resultado_invertido]

        resultado_total = resultado_normal + resultado_invertido + lista
        resultado_total = remover_duplicadas(resultado_total)
        resultado_total.sort(key=lambda x: x['distAng'])
        resultado_total = resultado_total[:5]
    else:
        print('Tipo de distancia indisponivel: ')
    
    if len(resultado_total) == 5:
        for v in resultado_total:
            if dist == 1:
                print(f'Palavra: {v["nome"]}, Distância Levenshtein: {v["distLev"]}')
            elif dist == 2:
                print(f'Palavra: {v["nome"]}, Distância Euclidiana: {v["distEuc"]}')
            elif dist == 3:
                print(f'Palavra: {v["nome"]}, Distância Angular: {v["distAng"]}')
    else:
        if len(palavra) > 1:
            palavra = palavra[:len(palavra)-1]
            return main(dicionario, dicionario_inv, palavra, original, dist, resultado_total)
        else:
            letra = teclasProximas(palavra)
            print(letra)
            return main(dicionario, dicionario_inv, letra, original, dist, resultado_total)
    
if  __name__ == '__main__':
    inicio = time()
    with open('palavras-br.txt', 'r', encoding='utf-8') as file:
        dicionario = [palavra.strip() for palavra in file]
        
    dicionario_inv = sorted(inverter_palavras(dicionario))
    palavras = ['Vomputador', 'parallepedo', 'taca', 'iseia', 'tetse', 'frigodifico', 'podigono']
    
    dist = 2

    for palavra in palavras:
        print(f'Correções sugerida para a palavra: {palavra}')
        main(dicionario, dicionario_inv, palavra, palavra, dist)
        print('\n')

    fim = time()
    print(f'tempo de Execução: {fim - inicio}')

    # palavra = input("Defina uma palavra: (Vazio para parar): ").lower()
    # while len(palavra) >= 1:
    #     main(dicionario, dicionario_inv, palavra, palavra)
    #     palavra = input("Defina uma palavra: (Vazio para parar): ").lower() 
