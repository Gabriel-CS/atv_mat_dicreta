from math import sqrt
import numpy as np

teclas = [
    ["q", "_", "w", "_", "e", "_", "r", "_", "t", "_", "y", "_", "u", "_", "i", "_", "o", "_", "p", "_"],
    ["_", "a", "_", "s", "_", "d", "_", "f", "_", "g", "_", "h", "_", "j", "_", "k", "_", "l", "_", "ç"],
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

def Distancia_Levenshtein(palavra1, palavra2):
    # `tam_1` e `tam_2` é o número total de caracteres em `palavra1` e `palavra2`, respectivamente
    (tam_p1, tam_p2) = (len(palavra1), len(palavra2))

    T = [[0 for x in range(tam_p2 + 1)] for y in range(tam_p1 + 1)]

    for i in range(1, tam_p1 + 1):
        T[i][0] = i                    # (caso 1)

    # inserindo todos os caracteres
    for j in range(1, tam_p2 + 1):
        T[0][j] = j                    # (caso 1)

    # preenche a tabela de pesquisa de forma baipalavra1o para cima
    for i in range(1, tam_p1 + 1):

        for j in range(1, tam_p2 + 1):
            if palavra1[i - 1] == palavra2[j - 1]:             # (caso 2)
                custo = 0                        # (caso 2)
            else:
                custo = 1                        # (caso 3c)

            T[i][j] = min(T[i - 1][j] + 1,       # Deleção de # (caso 3b)
                        T[i][j - 1] + 1,         # Inserção de # (caso 3a)
                        T[i - 1][j - 1] + custo) # substituir (caso 2 + 3c)

    return T[tam_p1][tam_p2]

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
