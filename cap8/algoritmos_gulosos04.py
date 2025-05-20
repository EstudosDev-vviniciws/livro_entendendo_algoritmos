'''
Algoritmos Gulosos - 4. Problema do Caixeiro Viajante (TSP) – Força Bruta + Aproximação:
Objetivo: Você deve visitar todas as cidades uma única vez
e retornar à cidade de origem. Aqui, uma aproximação gulosa
é visitar sempre a cidade mais próxima.
'''

import math

cidades = {
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 3),
    'D': (6, 1),
}

def distancia(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def rota_mais_proxima(cidades):
    nao_visitados = set(cidades.keys())
    rota = []
    atual = 'A'
    nao_visitados.remove(atual)
    rota.append(atual)
    
    while nao_visitados:
        proxima = min(nao_visitados, key=lambda cidade: distancia(cidades[atual], cidades[cidade]))

        rota.append(proxima)
        nao_visitados.remove(proxima)
        atual = proxima
        
    rota.append('A')
    return rota

print("Rota aproximada: ", rota_mais_proxima(cidades))
