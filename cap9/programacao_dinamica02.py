'''
Programação Dinâmica - 2. Itinerário de Viagem (prazer vs. tempo):
Objetivo: Você tem 5 horas disponíveis para um passeio. Dadas atrações
com tempo de visita e nível de prazer, escolha as atrações que maximizam
o prazer total.
'''

def melhor_viagem(tempos, prazeres, tempo_total):
    n = len(tempos)
    dp = [[0] * (tempo_total + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for t in range(1, tempo_total + 1):
            if tempos[i - 1] <= t:
                incluir = prazeres[i - 1] + dp[i - 1][t - tempos[i - 1]]
                excluir = dp[i - 1][t]
                dp[i][t] = max(incluir, excluir)
            else:
                dp[i][t] = dp[i - 1][t]
    
    return dp[n][tempo_total]

print(melhor_viagem([1, 2, 3], [100, 300, 350], 5))