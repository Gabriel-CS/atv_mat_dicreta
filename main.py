from math import sqrt
import numpy as np

def Ajustar_tam(palavra1, palavra2):
    # Ajusta os tamanhos das palavras pelo comprimento, não pela comparação direta de strings
    if len(palavra1) > len(palavra2):
        palavra2 = palavra2.ljust(len(palavra1))
    elif len(palavra2) > len(palavra1):
        palavra1 = palavra1.ljust(len(palavra2))
    
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

    dist_euclid = sqrt(sum((i - j)**2 for i, j in zip(palavra1, palavra2)))

    return dist_euclid

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

if  __name__ == '__main__':
    palavras = ['gato', 'cachorro']
    print(f'Distância de Levenshtein (ou distância de edição) : {Distancia_Levenshtein(palavras[0], len(palavras[0]), palavras[1], len(palavras[1]))}')
    print(f'Distância Euclidiana : {Distancia_Euclidiana(palavras[0], palavras[1])}')
    print(f'Distância Ângular : {Distancia_Angular(palavras[0], palavras[1])}')
