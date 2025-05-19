'''
Algoritmos Gulosos - 2. Problema da Mochila Fracionária:
Objetivo: Você tem uma mochila com capacidade de 5kg.
Escolha os itens de maior valor por quilo.
'''

itens = [
    {'nome': 'Notebook', 'valor': 3000, 'peso': 4},
    {'nome': 'Livro', 'valor': 1500, 'peso': 3},
    {'nome': 'Guitarra', 'valor': 2000, 'peso': 2}
]

def mochila(capacidade, itens):
    itens_ordenados = sorted(itens, key=lambda x: x['valor']/x['peso'], reverse=True)
    total_valor = 0
    mochila = []
    
    for item in itens_ordenados:
        if capacidade <= 0:
            break
        if item['peso'] <= capacidade:
            mochila.append((item['nome'], 1))
            total_valor += item['valor']
            capacidade -= item['peso']
        else:
            fracao = capacidade / item['peso']
            mochila.append((item['nome'], round(fracao, 2)))
            total_valor += item['valor'] * fracao
            capacidade = 0
            
    return mochila, total_valor

resultado, valor = mochila(5, itens)
print("Itens na mochila: ", resultado)
print("Valor total: ", valor)