# Classe Cliente <=============================
class Cliente:
    def __init__(self, nome, valorDaConta):
        self.nome = nome
        self.valorDaConta = valorDaConta
    
    def __repr__(self):
        return f'{self.nome} - {self.valorDaConta}'

# Classe Nodo <=============================
class Nodo:
    def __init__(self, dado = 0, proximoNodo = None):
        self.dado = dado
        self.proximo = proximoNodo
    
    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
    
    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo

# Classe Lista <=============================
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
    
    # MÉTODO IMPLEMENTADO <=============================
    # Calcula o gasto médio dos clientes na lista
    def calcularGastoMedio(self):
        # Impede a execução do método, caso a lista esteja vazia
        if self.tamanhoDaLista == 0 or not self.head:
            print('A lista está vazia.\n')
            return

        # Define os valores iniciais para começar a repetição while
        gastoTotal = 0
        nodoAlvo = self.head

        # Repetição While: Busca o valorDaConta do cliente alvo, soma ao gastoTotal e passa para o próximo node
            # Repete enquanto o nodoAlvo for diferente de None
        while (nodoAlvo):
            dadosDoNodo = nodoAlvo.dado
            gastoTotal += dadosDoNodo.valorDaConta
            nodoAlvo = nodoAlvo.proximo
        
        # Realiza o cálculo da média e impreme o gastoTotal e o gastoMedio
        gastoMedio = gastoTotal / self.tamanhoDaLista
        print(f'O Gasto Total dos clientes foi de: {gastoTotal} \nO Gasto Médio por clientes foi de: {"{:.2f}".format(gastoMedio)}\n')
        return gastoMedio

# Implementação <=============================
listaEncadeada = ListaSimplesmenteEncadeada()
# Deve retorna "A lista está vazia"
listaEncadeada.calcularGastoMedio()

cliente1 = Cliente('Cliente1', 200)
listaEncadeada.insere(cliente1)
cliente2 = Cliente('Cliente2', 300)
listaEncadeada.insere(cliente2)
cliente3 = Cliente('Cliente3', 100)
listaEncadeada.insere(cliente3)

# Deve retornar a soma dos valores gastos pelos clientes inseridos acima (600) e a média deles
listaEncadeada.calcularGastoMedio()

# Ao remover o primeiro node, deve retonar apenas a soma do valor dos outros dois clientes (500) e a média deles
listaEncadeada.delete()
listaEncadeada.calcularGastoMedio()

# Funciona com valores flutuantes
cliente4 = Cliente('Cliente', 99.99)
listaEncadeada.insere(cliente4)
cliente5 = Cliente('Cliente', 169.49)
listaEncadeada.insere(cliente5)
listaEncadeada.calcularGastoMedio()