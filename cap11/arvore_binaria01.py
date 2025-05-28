'''
Próximos Passos - 1. Árvores Binárias de Busca:
Objetivo: Implemente uma árvore binária de busca com 
inserção, busca e travessia em ordem.
'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        
class arvore_binaria:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)
        
    def _inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        else:
            no.direita = self._inserir(no.direita, valor)
        return no
    
    def em_ordem(self):
        self._em_ordem(self.raiz)
        
    def _em_ordem(self, no):
        if no is None:
            return
        self._em_ordem(no.esquerda)
        print(no.valor, end=" ")
        self._em_ordem(no.direita)
        
arvore = arvore_binaria()
valores = [10, 5, 2, 7, 15, 20]

for valor in valores:
    arvore.inserir(valor)
    
arvore.em_ordem()
    