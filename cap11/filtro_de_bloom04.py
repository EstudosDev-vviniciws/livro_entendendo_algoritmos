'''
Próximos Passos - 4. Filtro de Bloom (Simples com Hash):
Objetivo: Demonstrar como funciona um Filtro de Bloom,
uma estrutura de dados eficiente para verificar se um elemento
possivelmente pertence a um conjunto, usando múltiplas funções
de hash e ocupando pouca memória.
'''

import hashlib

class BloomFilter:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.bits = [0] * tamanho
        
    def _hashes(self, palavra):
        h1 = int(hashlib.sha256(palavra.encode()).hexdigest(), 16) % self.tamanho
        h2 = int(hashlib.md5(palavra.encode()).hexdigest(), 16) % self.tamanho
        return [h1, h2]
    
    def adicionar(self, palavra):
        for h in self._hashes(palavra):
            self.bits[h] = 1
            
    def verificar(self, palavra):
        return all(self.bits[h] for h in self._hashes(palavra))
    

filtro = BloomFilter(20)
filtro.adicionar("python")
print(filtro.verificar("python"))
print(filtro.verificar("java"))