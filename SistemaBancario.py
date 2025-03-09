from time import sleep  # Importa a função sleep para pausar a execução por um tempo determinado

# Definição de variáveis globais
saldo = 1000.00  # Saldo inicial da conta
cont_saque_diarios = 3  # Número máximo de saques diários permitidos
extrato = list()  # Lista para armazenar o extrato das transações

# Função para exibir o menu principal
def menu():
    tam = len('Sistema Bancário - MENU')+4  # Define o tamanho da linha de separação
    print('-'*tam)
    print('Sistema Bancário - MENU'.center(tam))  # Centraliza o título do menu
    print('-'*tam)
    print('\n[1] Saque')
    print('[2] Depósito')
    print('[3] Visualizar Extrato')
    print('[4] Sair\n')
    print('-'*tam)

# Função para exibir o menu de saque
def menu_saque():
    tam = len('Sistema Bancário - SAQUE')+4
    print('-'*tam)
    print('Sistema Bancário - SAQUE'.center(tam))
    print('-'*tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}')  # Exibe o saldo atual
    print(f'Saques Restantes --> {cont_saque_diarios}\n')  # Exibe quantos saques ainda podem ser realizados
    print('-'*tam)

# Função para exibir o menu de depósito
def menu_deposito():
    tam = len('Sistema Bancário - DEPÓSITO')+4
    print('-'*tam)
    print('Sistema Bancário - DEPÓSITO'.center(tam))
    print('-'*tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo atual antes do depósito
    print('-'*tam)

# Função para exibir o menu de extrato
def menu_extrato():
    tam = len('Sistema Bancário - EXTRATO')+4
    print('-'*tam)
    print('Sistema Bancário - EXTRATO'.center(tam))
    print('-'*tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo atual no extrato

# Loop principal do sistema bancário
while True:
    menu()  # Exibe o menu principal
    operacao = int(input("Indique a operação desejada: "))  # Solicita a opção do usuário
    
    # Verifica se a opção informada é válida
    if str(operacao) not in '1234':
        print('ERRO! Opção Inválida')
        continue

    # Opção de saque
    elif operacao == 1:
        menu_saque()  # Exibe o menu de saque
        valor_saque = float(input('Indique o valor de saque: '))  # Solicita o valor do saque
        
        if cont_saque_diarios > 0:  # Verifica se ainda há saques disponíveis no dia
            if valor_saque <= 500:  # Verifica se o valor do saque não ultrapassa o limite permitido
                if valor_saque <= saldo:  # Verifica se há saldo suficiente para o saque
                    saldo -= valor_saque  # Deduz o valor do saque do saldo
                    print('Operação realizada com sucesso!')
                    print(f'Seu valor de saldo atual é de R${saldo:.2f}')
                    extrato.append(f'Saque -> R${valor_saque:.2f}')  # Registra o saque no extrato
                    cont_saque_diarios -= 1  # Reduz a quantidade de saques diários restantes
                else:
                    print('Valor do saque excede o seu saldo atual.')
                    print(f'Saldo Atual = R${saldo:.2f}')
            else:
                print('Valor de saque é maior do que limite de R$500,00')
        else:
            print('Quantidades de saques diários máximos excedidos')

    # Opção de depósito
    elif operacao == 2:
        menu_deposito()  # Exibe o menu de depósito
        valor_deposito = float(input('Indique o valor de depósito: '))  # Solicita o valor do depósito
        saldo += valor_deposito  # Adiciona o valor depositado ao saldo
        print('Operação realizada com sucesso!')
        print(f'Seu valor de saldo atual é de R${saldo:.2f}')
        extrato.append(f'Depósito -> R${valor_deposito:.2f}')  # Registra o depósito no extrato

    # Opção de visualização do extrato
    elif operacao == 3:
        menu_extrato()  # Exibe o menu de extrato
        for c in range(len(extrato)):  # Percorre a lista de extrato e exibe cada transação
            print(f'{extrato[c]}\n')

    # Opção para sair do sistema
    elif operacao == 4:
        break  # Sai do loop e encerra o programa

    sleep(2)  # Aguarda 2 segundos antes de retornar ao menu
