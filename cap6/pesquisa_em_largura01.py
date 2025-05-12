'''
Pesquisa em largura:
Objetivo: Implemente um grafo representando amizades e use BFS 
para verificar se existe uma conexão entre duas pessoas.
'''

from collections import deque

def existe_conexao(grafo, origem, destino):
    fila = deque()
    fila += grafo[origem]
    visitados = set()
    
    while fila:
        pessoa = fila.popleft()
        if pessoa == destino:
            return True
        if pessoa not in visitados:
            fila +=grafo.get(pessoa, [])
            visitados.add(pessoa)
    return False
    
grafo = {
    "Ana": ["Carlos", "Bianca"],
    "Carlos": ["Daniel"],
    "Bianca": ["Regina"],
    "Daniel": [],
    "Regina": []
}

print(existe_conexao(grafo, "Ana", "Regina"))
print(existe_conexao(grafo, "Ana", "Rafael"))
    