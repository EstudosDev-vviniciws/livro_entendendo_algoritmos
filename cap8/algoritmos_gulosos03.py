'''
Algoritmos Gulosos - 3. Problema da Cobertura de Conjuntos:
Objetivo: Escolha o menor número de estações
que cubram todos os estados necessários.
'''

estacoes = {
    'kone': {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}

estados_necessarios = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

estados_finais = set()

while estados_necessarios:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados & estados_necessarios
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_necessarios -= estados_cobertos
    estados_finais.add(melhor_estacao)
    
print("Estações escolhidas: ", estados_finais)