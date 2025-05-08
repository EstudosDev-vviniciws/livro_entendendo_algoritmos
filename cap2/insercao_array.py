'''
Inserção em Array:
Objetivo: Simular inserção no meio de um array e observar o custo.
'''

lista = [1, 2, 3, 4, 5]

def inserir_em_array(lista, posicao, valor):
    lista.insert(posicao, valor)
    return lista

print(inserir_em_array(lista, 2, 3))