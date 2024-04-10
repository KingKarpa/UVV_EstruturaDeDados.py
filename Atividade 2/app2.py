# Função que verifique o balanceamento dos parênteses
def verificarParenteses(stringDeParenteses):
    pilha = []

    for caractere in stringDeParenteses:
        # Verifica se o caractere é um parentese de abertura, caso seja, o adiciona na pilha
        if caractere == '(':
            pilha.append(caractere)
        
        # Verifica se o caractere é um parentese de fechamento, caso seja, realiza outras verificações
        elif caractere == ')':
            # Verifica se a pilha está vazia, ou seja, a string começa com fechamento ou há excesso deles. Retorna mensagem negativa e False
            if not pilha:
                print('DESBALANCEADA Tipo 1: A string de parenteses inserida NÃO É balanceada.')
                return False
            
            # Retira o elemento no topo da pilha
            else:
                pilha.pop()
        
        # Desencadeado caso a string possua caracteres diferentes de parenteses. Retorna mensagem negativa e False
        else:
            print('ERRO: Insira apenas parenteses na string!')
            return False
    
    # Verifica se a pilha foi esvaziada, caso tenha, retorna mensagem de sucesso e True
    if not pilha:
        print('BALANCEADA: A string de parenteses inserida É balanceada.')
        return True

    # Desencadeado se a pilha ainda possue parenteses de abertura, ou seja, haviam mais aberturas do que fechamentos na string. Retorna mensagem negativa e False
    else:
        print('DESBALANCEADA Tipo 2: A string de parenteses inserida NÃO É balanceada.')
        return False

# Testando Implementação <=============================
stringBalanceada1 = "(()()()())"
stringBalanceada2 = "(((())))"
stringBalanceada3 = "(()((())()))"
stringDesbalanceada1 = "))(("
stringDesbalanceada2 = "()))"
stringDesbalanceada3 = "((((((())"
stringIncorreta = "(a())"

verificarParenteses(stringBalanceada1)
verificarParenteses(stringBalanceada2)
verificarParenteses(stringBalanceada3)
verificarParenteses(stringDesbalanceada1)
verificarParenteses(stringDesbalanceada2)
verificarParenteses(stringDesbalanceada3)
verificarParenteses(stringIncorreta)