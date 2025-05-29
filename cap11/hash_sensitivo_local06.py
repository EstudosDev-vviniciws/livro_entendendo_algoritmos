'''
Próximos Passos - 7. Hash Sensitivo Local (simplificado com MinHash):
Objetivo: Demonstrar como calcular a similaridade entre conjuntos de
palavras usando o índice de Jaccard, uma técnica básica relacionada
ao Hash Sensitivo Local (LSH).
'''

def jaccard_similaridade(conjunto1, conjunto2):
    inter  = len(conjunto1 & conjunto2)
    uni = len(conjunto1 | conjunto2)
    return inter / uni

a = set("algoritimo estrutura dados".split())
b = set("estrutura de dados algoritmo".split())

print(f"Similaridade: {jaccard_similaridade(a, b):.2f}")