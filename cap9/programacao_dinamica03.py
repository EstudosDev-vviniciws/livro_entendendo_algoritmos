'''
Programação Dinâmica - 3. Maior Substring Comum:
Objetivo: Dadas duas strings, encontre o tamanho
da maior substring comum contínua.
'''

def maior_subtring_comum(s1, s2):
    m, n = len(s1), len(s2)
    tabela = [[0] * (n - 1) for _ in range(m + 1)]
    max_len = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
                max_len = max(max_len, tabela[i][j])
                
    return max_len

print(maior_subtring_comum("bluefish", "bluebird"))