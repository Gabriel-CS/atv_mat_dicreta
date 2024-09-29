from distancias import Distancia_Levenshtein, Distancia_Euclidiana, Distancia_Angular, teclasProximas

def inverter_palavras(dic):
    return [palavra[::-1] for palavra in dic]

def busca_binaria(dicionario, prefixo, inicio, fim):
    if inicio > fim:
        return None
    meio = (inicio + fim) // 2
    palavra_meio = dicionario[meio]
    if palavra_meio.lower().startswith(prefixo.lower()):
        if meio == 0 or not dicionario[meio - 1].lower().startswith(prefixo.lower()):
            return meio
        else:
            return busca_binaria(dicionario, prefixo, inicio, meio - 1)
    elif palavra_meio.lower() < prefixo.lower():
        return busca_binaria(dicionario, prefixo, meio + 1, fim)
    else:
        return busca_binaria(dicionario, prefixo, inicio, meio - 1)

def busca_palavras(dicionario, prefixo, palavra_original, limite=5):
    index = busca_binaria(dicionario, prefixo, 0, len(dicionario) - 1)
    if index is None:
        return []
    lista = []
    i = index
    while i < len(dicionario):
        palavra = dicionario[i]
        if not palavra.lower().startswith(prefixo.lower()):
            break
        dist = Distancia_Levenshtein(palavra_original, len(palavra_original), palavra, len(palavra))
        if dist < 5:
            dados = {"nome": palavra, "dist": dist}
            if len(lista) < limite:
                lista.append(dados)
            else:
                maior_dist = max(lista, key=lambda x: x['dist'])
                if dist < maior_dist['dist']:
                    lista.remove(maior_dist)
                    lista.append(dados)
        i += 1
    return lista

def main(dicionario, dicionario_inv):
    palavra = input("Defina uma palavra: ")
    prefixo = palavra[:len(palavra) // 2 + 1]
    # Buscar no dicionário normal
    resultado_normal = busca_palavras(dicionario, prefixo, palavra)
    print(resultado_normal)
    # Buscar no dicionário invertido
    palavra_invertida = palavra[::-1]
    prefixo_invertido = palavra_invertida[:len(palavra_invertida) // 2 + 1]
    resultado_invertido = busca_palavras(dicionario_inv, prefixo_invertido, palavra_invertida)
    resultado_invertido = [{"nome": item["nome"][::-1], "dist": item["dist"]} for item in resultado_invertido]
    
    resultado_total = resultado_normal + resultado_invertido
    print(resultado_total)
    
if  __name__ == '__main__':
    with open('palavras-br.txt', 'r', encoding='utf-8') as file:
        dicionario = [palavra.strip() for palavra in file]
    dicionario_inv = sorted(inverter_palavras(dicionario))
    main(dicionario, dicionario_inv)
    #print(teclasProximas("f"))

'''
palavras = ['gato', 'cachorro']
    print(f'Distância de Levenshtein (ou distância de edição) : {Distancia_Levenshtein(palavras[0], len(palavras[0]), palavras[1], len(palavras[1]))}')
    print(f'Distância Euclidiana : {Distancia_Euclidiana(palavras[0], palavras[1])}')
    print(f'Distância Ângular : {Distancia_Angular(palavras[0], palavras[1])}')
'''