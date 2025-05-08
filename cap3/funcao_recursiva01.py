'''
Caso-base e o Caso recursivo:
Objetivo: Implemente uma função recursiva contagem_regressiva(n) que imprima os números de n até 1.
'''

def contagem_regressiva(n):
    print(n)
    if n <= 1:
        return
    contagem_regressiva(n - 1)
    
print(contagem_regressiva(6))