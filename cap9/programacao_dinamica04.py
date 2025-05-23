'''
Programação Dinâmica - 4. Maior Subsequência Comum:
Objetivo: Dadas duas strings, encontre a maior subsequência
comum (caracteres em ordem, mas não necessariamente contínuos).
'''

def maior_subsequencia_comum(s1, s2):
    m, n = len(s1), len(s2)
    tabela = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])
    
    return tabela[i][j]

print(maior_subsequencia_comum("fosh", "fort"))
