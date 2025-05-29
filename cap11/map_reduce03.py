'''
Próximos Passos - 3. MapReduce Simples – Contagem de Palavras:
Objetivo: Contar a frequência de cada palavra em uma lista de
documentos (strings), simulando o paradigma MapReduce.
'''

from functools import reduce

documentos = [
    "dados algoritmos algoritmos",
    "algoritmos estruturas",
    "estruturas dados"
]

palavras = []
for doc in documentos:
    palavras.extend(doc.split())
    
contagem = {}
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
    
print(contagem)