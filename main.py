
from distancias import Distancia_Levenshtein, Distancia_Euclidiana, Distancia_Angular

def main():
    with open('palavras-br.txt', 'r', encoding='utf-8') as file:
        dicionario = {palavra.strip() for palavra in file}
    palavra = "tese"
    lista = []
    i = 0
    for word in dicionario:
        i += 1
        if (abs(len(palavra) - len(word)) <= 3):
            dist = Distancia_Levenshtein(palavra, len(palavra), word, len(word))
            if dist < 5:
                print(i)
                dados = {"nome": word, "dist": dist}
                lista.append(dados)
    print(lista)

    
if  __name__ == '__main__':
    main()

'''
palavras = ['gato', 'cachorro']
    print(f'Distância de Levenshtein (ou distância de edição) : {Distancia_Levenshtein(palavras[0], len(palavras[0]), palavras[1], len(palavras[1]))}')
    print(f'Distância Euclidiana : {Distancia_Euclidiana(palavras[0], palavras[1])}')
    print(f'Distância Ângular : {Distancia_Angular(palavras[0], palavras[1])}')
'''