'''
Próximos Passos - 6. Simulação de Armazenamento de Senhas com Hash:
Objetivo: Mostrar como armazenar e verificar senhas de forma segura
usando hash, sem guardar a senha original.
'''

import hashlib

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

senha_armazenada = hash_senha("minha_senha_segura")

senha_usuario = "minha_senha_segura"
if hash_senha(senha_usuario) == senha_armazenada:
    print("Senha correta")
else:
    print("Senha incorreta")