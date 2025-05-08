'''
Caso-base e o Caso recursivo:
Objetivo: Crie uma função recursiva fatorial(n) que calcule o fatorial de n.
'''

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial (n-1)


n = int(input("Digite um número: "))    
print(f"O fatorial de {n} é: {fatorial(n)}")