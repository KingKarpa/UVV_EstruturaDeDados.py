class Clinte:
    def __init__(self, nome, valorDaConta):
        self.nome = nome
        self.valorDaConta = valorDaConta
    
    def __repr__(self):
        return f'{self.nome} - {self.valorDaConta}'

class Nodo:
    def __init__(self, dado = 0, proximoNodo = None):
        self.dado = dado
        self.proximo = proximoNodo
    
    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
    
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo

class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.head = None
        self.tamanhoDaLista = 0
    
    def insere(self, novoDado):
        novoDado = Nodo(novoDado)
        novoDado.proximo = self.head
        self.head = novoDado
        self.tamanhoDaLista += 1
    
    def delete(self):
        if self.head == None:
            print('A lista já está vazia')
        
        else:
            self.head = self.head.proximo
            self.tamanhoDaLista -= 1
