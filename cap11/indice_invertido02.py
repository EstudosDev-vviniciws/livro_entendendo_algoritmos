'''
Próximos Passos - 2. Índice Invertido:
Objetivo: Crie um índice invertido para uma
lista de documentos (strings).
'''

from collections import defaultdict

documentos = [
    "algoritmo e estrutura de dados",
    "estrutura de dados em python",
    "busca com algoritmo eficiente"
]

indice = defaultdict(set)

for i, doc in enumerate(documentos):
    for palavra in doc.split():
        indice[palavra].add(i)
        
print(dict(indice))