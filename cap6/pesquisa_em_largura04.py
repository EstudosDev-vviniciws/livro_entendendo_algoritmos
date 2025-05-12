'''
Pesquisa em largura:
Objetivo: Crie uma função que simula o uso do deque como Fila (FIFO)
e outra como Pilha (LIFO). Mostre a ordem de remoção dos elementos.
'''

from collections import deque

def simular_fila():
    fila = deque()
    fila.append("Vinicius")
    fila.append("Vitor")
    fila.append("Vicente")
    print("FIFO - Ordem de saída: ")
    while fila:
        print(fila.popleft())
        
def simular_pilha():
    pilha = deque()
    pilha.append("Vinicius")
    pilha.append("Vitor")
    pilha.append("Vicente")
    print("LIFO - Ordem de saída: ")
    while pilha:
        print(pilha.pop())
            
simular_fila()
simular_pilha()