'''
Simulação de Lista Encadeada:
Objetivo: Implementar uma versão simplificada de uma lista encadeada.
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class lista_encadeada:
    def __init__(self):
        self.inicio = None
        
    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
    
    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")
        
lista = lista_encadeada()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)
lista.exibir()