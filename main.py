from distancias import Distancia_Levenshtein, Distancia_Euclidiana, Distancia_Angular, teclasProximas

def inverter_palavras(dic):
    return [palavra[::-1] for palavra in dic]

def remover_duplicadas(lista):
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    return lista_unica

def busca_binaria(dicionario, prefixo, inicio, fim):
    if inicio > fim:
        return -1
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

def busca_palavras(dicionario, prefixo, palavra_original, invertido, limite=5):
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
        distLev = Distancia_Levenshtein(palavra_original, palavra)
        if invertido:
            distEuc = Distancia_Euclidiana(palavra_original[::-1], palavra[::-1])
            distAng = Distancia_Angular(palavra_original[::-1], palavra[::-1])
        else:
            distEuc = Distancia_Euclidiana(palavra_original, palavra)
            distAng = Distancia_Angular(palavra_original, palavra)
        if distLev < 5:
            dados = {"nome": palavra, "distLev": distLev, "distEuc": distEuc, "distAng": distAng}
            if len(lista) < limite:
                lista.append(dados)
            else:
                maior_dist = max(lista, key=lambda x: x['distLev'])
                if distLev < maior_dist['distLev']:
                    lista.remove(maior_dist)
                    lista.append(dados)
        i += 1
    return lista

def main(dicionario, dicionario_inv, palavra, original, lista):
    # Buscar no dicionário normal
    prefixo = palavra[:len(palavra) // 2]
    resultado_normal = busca_palavras(dicionario, prefixo, original, False)
    # Buscar no dicionário invertido
    palavra_invertida_original = original[::-1]
    prefixo_invertido = palavra_invertida_original[:len(palavra_invertida_original) // 2]
    resultado_invertido = busca_palavras(dicionario_inv, prefixo_invertido, palavra_invertida_original, True)
    resultado_invertido = [{"nome": item["nome"][::-1], "distLev": item["distLev"], "distEuc": item["distEuc"], "distAng": item["distAng"]} for item in resultado_invertido]
    # Ajustar resultado total
    resultado_total = resultado_normal + resultado_invertido + lista
    resultado_total = remover_duplicadas(resultado_total)
    resultado_total.sort(key=lambda x: x['distLev'])
    resultado_total = resultado_total[:5]
    if len(resultado_total) == 5:
        for v in resultado_total:
            print(f'Palavra: {v["nome"]}, Distância Levenshtein: {v["distLev"]}, Distância Euclidiana: {v["distEuc"]}, Distância Angular: {v["distAng"]}')
    else:
        if len(palavra) > 1:
            palavra = palavra[:len(palavra)-1]
            return main(dicionario, dicionario_inv, palavra, original, resultado_total)
        else:
            letra = teclasProximas(palavra)
            return main(dicionario, dicionario_inv, letra[0], original, resultado_total)
    
if  __name__ == '__main__':
    with open('palavras-br.txt', 'r', encoding='utf-8') as file:
        dicionario = [palavra.strip() for palavra in file]
    dicionario_inv = sorted(inverter_palavras(dicionario))
    palavra = input("Defina uma palavra: (Vazio para parar) ")
    while len(palavra) >= 1:
        main(dicionario, dicionario_inv, palavra, palavra, [])
        palavra = input("Defina uma palavra: (Vazio para parar) ")

'''
palavras = ['gato', 'cachorro']
    print(f'Distância de Levenshtein (ou distância de edição) : {Distancia_Levenshtein(palavras[0], len(palavras[0]), palavras[1], len(palavras[1]))}')
    print(f'Distância Euclidiana : {Distancia_Euclidiana(palavras[0], palavras[1])}')
    print(f'Distância Ângular : {Distancia_Angular(palavras[0], palavras[1])}')
'''