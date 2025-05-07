lista = [1, 3, 5, 10, 12, 20]

def busca_binaria(lista, valor):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute == valor:
            return meio
        elif chute > valor:
            alto = meio - 1
        else:
            baixo = meio + 1
    return -1
    
print(busca_binaria(lista, 3))