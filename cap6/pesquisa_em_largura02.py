'''
Pesquisa em largura:
Objetivo: Modifique o algoritmo de BFS para retornar
o caminho completo (lista de nós) entre origem e destino.
'''

def caminho_mais_curto(grafo, origim, destino):
    from collections import deque
    
    fila = deque()
    fila.append([origim])
    visitados = set()
    
    while fila:
        caminho = fila.popleft()
        no = caminho[-1]
        
        if no == destino:
            return caminho
        
        if no not in visitados:
            for visiznho in grafo.get(no, []):
                novo_caminho = list(caminho)
                novo_caminho.append(visiznho)
                fila.append(novo_caminho)
            visitados.add(no)
            
    return True

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


print(caminho_mais_curto(grafo, "voce", "thom"))