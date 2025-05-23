'''
Programação Dinâmica - 5. Problema da Mochila com Interdependência Simple:
Objetivo: Você só pode levar um "carregador" se levar o notebook.
'''

def mochila_dependente(itens, capacidade):
    n = len(itens)
    max_valor = 0
    
    def backtrack(i, peso_atual, valor_atual, levou_notebook):
        nonlocal max_valor
        if peso_atual > capacidade:
            return
        if i == n:
            max_valor = max(max_valor, valor_atual)
            return
        item = itens[i]
        
        backtrack(i + 1, peso_atual, valor_atual, levou_notebook)
        
        if item["nome"] == "carregador"  and not levou_notebook:
            return
        novo_levou_notebook = levou_notebook or item["nome"] == "notebook"
        backtrack(i + 1, peso_atual + item["peso"], valor_atual + item["valor"], novo_levou_notebook)
        
    backtrack(0, 0, 0, False)
    return max_valor

print(mochila_dependente([
    {"nome": "notebook", "peso": 3, "valor": 2000},
    {"nome": "carregador", "peso": 1, "valor": 500},
    {"nome": "livro", "peso": 2, "valor": 1500}
], 4))