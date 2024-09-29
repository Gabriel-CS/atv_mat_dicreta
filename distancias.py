from math import sqrt
import numpy as np

teclas = [
    ["q", "_", "w", "_", "e", "_", "r", "_", "t", "_", "y", "_", "u", "_", "i", "_", "o", "_", "p", "_"],
    ["_", "a", "_", "s", "_", "d", "_", "f", "_", "g", "_", "h_", "_", "j", "_", "k", "_", "l", "_", "ç"],
    ["_", "_", "z", "_", "x", "_", "c", "_", "v", "_", "b", "_", "n", "_", "m", "_", "_", "_", "_", "_"],
]

def teclasProximas(key):
    for i, linha in enumerate(teclas):
        if key in linha:
            j = linha.index(key)
            break
    else:
        return []
    vizinhos = [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-2), (i, j+2),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]
    teclas_proximas = []
    for vi, vj in vizinhos:
        if 0 <= vi < len(teclas) and 0 <= vj < len(teclas[vi]) and teclas[vi][vj] != "_":
            teclas_proximas.append(teclas[vi][vj])
    return teclas_proximas


def Ajustar_tam(palavra1, palavra2):
    # Ajusta os tamanhos das palavras pelo comprimento, não pela comparação direta de strings
    tam_p1, tam_p2 = len(palavra1), len(palavra2)
    if tam_p1 > tam_p2:
        palavra2 = palavra2.ljust(tam_p1)
    elif tam_p2 > tam_p1:
        palavra1 = palavra1.ljust(tam_p2)
    
    return palavra1, palavra2

def Distancia_Levenshtein(p1, tam_p1, p2, tam_p2):
    if tam_p1 == 0:      # Caso base: strings vazias (caso 1)
        return tam_p2
    if tam_p2 == 0:      # se os últimos caracteres das strings corresponderem (caso 2)
        return tam_p2

    custo = 0 if (p1[tam_p1 - 1] == p2[tam_p2 - 1]) else 1

    minimo = min(Distancia_Levenshtein(p1, tam_p1 - 1, p2, tam_p2) + 1,         # Deleção de # (caso 3a))
                 Distancia_Levenshtein(p1, tam_p1, p2, tam_p2 - 1) + 1,         # Inserção de # (caso 3b))
                 Distancia_Levenshtein(p1, tam_p1 - 1, p2, tam_p2 - 1) + custo)
    return minimo

def Distancia_Euclidiana(palavra1, palavra2):
    palavra1, palavra2 = Ajustar_tam(palavra1, palavra2)    # adicionando espaços nas palavras com menor tamanho

    # criando listas de valores correspodentes aos codigos dos caracteres na tabela ASCII, e adicionando 0 no caracteres de espaço que foi adicionado na palavra de menor tamanho 

    palavra1 = [ 0 if ord(i) == 32 else ord(i) for i in list(palavra1) ]
    palavra2 = [ 0 if ord(i) == 32 else ord(i) for i in list(palavra2) ]

    dist_euclidiana = sqrt(sum((i - j)**2 for i, j in zip(palavra1, palavra2)))

    return dist_euclidiana

def Distancia_Angular(palavra1, palavra2):
    palavra1, palavra2 = Ajustar_tam(palavra1, palavra2) # Ajusta o tamanho das palavras

    # Convertendo os caracteres em valores correspondetes a tabela ASCII
    palavra1 = [ 0 if ord(i) == 32 else ord(i) for i in list(palavra1) ] # 32 é o côdigo do espaço
    palavra2 = [ 0 if ord(i) == 32 else ord(i) for i in list(palavra2) ]

    # Calculando o modulo das palavras
    mod_p1 = np.linalg.norm(palavra1)
    mod_p2 = np.linalg.norm(palavra2)

    # Calculando o Produto interno 
    prod_escalar = np.dot(palavra1, palavra2)

    cos = prod_escalar / (mod_p1 * mod_p2)

    return np.arccos(cos) # Esse resultado é dado em radianos

def Busca_Binaria(lista, letra):
    tam = len(lista)

    if tam == 0:
        return -1
    
    meio = tam // 2

    if letra == lista[meio]:
        return meio

    elif letra < lista[meio]: # Busca na parte esquerda do array
        return Busca_Binaria(lista[:meio], letra)

    else:
        resultado = Busca_Binaria(lista[meio:], letra) # Busca na parte direita 

        if resultado != -1:
            return meio + resultado
        else:
            return -1