'''
Busca Simples:
Escreva uma função que use busca simples para encontrar um valor em uma
lista desordenada. A função deve retornar o índice do valor ou -1 se não encontrar.
'''

def busca_simples(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        
    return -1

print(busca_simples([5, 3, 6, 7, 8, 0], 5))
    