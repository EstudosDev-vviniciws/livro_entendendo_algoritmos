'''
Pesquisa em largura:
Objetivo: Utilize BFS para encontrar uma pessoa cujo nome termina com "m" no grafo abaixo.
'''

from collections import deque

def pessoa_e_vendedora(nome):
    return nome[-1] == 'm'

def busca_vendedor(grafo, inicio):
    fila = deque()
    fila += grafo[inicio]
    verificados = set()
    
    while fila:
        pessoa = fila.popleft()
        if pessoa not in verificados:
            if pessoa_e_vendedora(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return pessoa
            else:
                fila += grafo[pessoa]
                verificados.add(pessoa)
            
    return None

grafo = {
    "voce": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "peggy": [],
    "anuj": [],
    "thom": [],
    "jonny": []
}

print(busca_vendedor(grafo, "voce"))