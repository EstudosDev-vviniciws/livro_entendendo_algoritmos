def busca_simples(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
        
    return -1

print(busca_simples([5, 3, 6, 7, 8, 0], 5))
    