'''
Algoritmo Dijkstra:
Objetivo: Implemente o algoritmo de Dijkstra para encontrar o caminho 
de menor custo entre o nó "inicio" e o nó "fim" no seguinte grafo:

grafo = {
    'inicio': {'a': 10},
    'a': {'b': 20},
    'b': {'fim': 30, 'a': 1},
    'fim': {}
}

'''

grafo = {
    'inicio': {'a': 10},
    'a': {'b': 20},
    'b': {'fim': 30, 'a': 1},
    'fim': {}
}

infinito = float('inf')
custos = {'a': 10, 'b': infinito, 'fim': infinito}
pais = {'a': 'inicio', 'b': None, 'fim': infinito}
processados = []

def ache_menor_custo(custo):
    menor = float('inf')
    menor_no = None
    for no in custos:
        if custo[no] < menor and no not in processados:
            menor = custos[no]
            menor_no = no
    return menor_no

no = ache_menor_custo(custos)
while no:
    custo = custos[no]
    vizinhos = grafo[no]
    for n in vizinhos:
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    processados.append(no)
    no = ache_menor_custo(custos)
    
print("Caminhho de menor custo até fim:", custos['fim'])
print("Pais:", pais)