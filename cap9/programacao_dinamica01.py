'''
Programação Dinâmica - 1. Problema da Mochila 0/1 (Clássico):
Objetivo: Escreva uma função que retorne o valor máximo que pode
ser carregado na mochila, sem ultrapassar a capacidade.
'''

def mochila(pesos, valores, capacidade):
    n = len(pesos)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                incluir = valores[i - 1] + tabela[i - 1][w - pesos[i - 1]]
                excluir = tabela[i - 1][w]
                tabela[i][w] = max(incluir, excluir)
            else:
                tabela[i][w] = tabela[i - 1][w]
    
    return tabela[n][capacidade]

print(mochila([1, 2, 3], [1500, 2000, 3000], 4))