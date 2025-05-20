'''
Algoritmos Gulosos - 5. Desafio: Cobertura de Subconjuntos (NP-completo):
Objetivo: Você tem um universo de números e subconjuntos. 
Encontre o menor número de subconjuntos que cobre o universo.
'''

universo = {1, 2, 3, 4, 5}
subconjuntos ={
    'S1': {1, 2},
    'S2': {2, 3, 4},
    'S3': {4, 5},
    'S4': {1, 5}
}

cobertura = set()
usados = set()

while universo:
    melhor = None
    cobertos = set()
    for nome, subconjunto in subconjuntos.items():
        inter = subconjunto & universo
        if len(inter) > len(cobertos):
            melhor = nome
            cobertos = inter
    universo -= cobertos
    usados.add(melhor)
        
print("Subconjuntos usados:", usados)