'''
Tabela hash:
Objetivo: Crie um programa que cadastre nomes em uma lista, mas
impedindo nomes repetidos, usando uma tabela hash (dicionário).
'''

cadastrados = {}

def cadastrar(nome):
    if nome in cadastrados:
        print(f"{nome} já cadastrado.")
    else:
        cadastrados[nome] = True
        print(f"{nome} cadastrado com sucesso!")
        
cadastrar("Vinícius")
cadastrar("Paulo")
cadastrar("Henrique")
cadastrar("Vinicius")