'''
Próximos Passos - 7. Troca de Chaves Diffie-Hellman (simplificada):
Objetivo: Demonstrar, de forma simplificada, como funciona a troca de
chaves Diffie-Hellman para que duas partes compartilhem uma chave secreta
sem transmiti-la diretamente.
'''

p = 23
g = 5

a = 6
A = pow(g, a, p)

b = 15
B = pow(g, b , p)

chave_A = pow(B, a, p)
chave_B = pow(A, b, p)

print(chave_A == chave_B)
print("Chave compartilhada:", chave_A)