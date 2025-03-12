# Função para exibir o menu principal
def menu():
    tam = len('Sistema Bancário - MENU') + 4  # Define o tamanho da linha de separação
    print('-' * tam)
    print('Sistema Bancário - MENU'.center(tam))  # Centraliza o título do menu
    print('-' * tam)
    print('\n[1] Saque')
    print('[2] Depósito')
    print('[3] Visualizar Extrato')
    print('[4] Criar Usuário')
    print('[5] Criar Conta Corrente')
    print('[6] Apagar Usuário/Conta')
    print('[7] Listar Usuários')
    print('[8] Sair\n')
    print('-' * tam)

# Função para exibir o menu de saque
def menu_saque(saldo, cont_saque_diarios):
    tam = len('Sistema Bancário - SAQUE') + 4
    print('-' * tam)
    print('Sistema Bancário - SAQUE'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}')  # Exibe o saldo atual
    print(f'Transações Restantes --> {10 - cont_saque_diarios}\n')  # Exibe quantos saques ainda podem ser realizados
    print('-' * tam)

# Função para exibir o menu de depósito
def menu_deposito(saldo, cont_saque_diarios):
    tam = len('Sistema Bancário - DEPÓSITO') + 4
    print('-' * tam)
    print('Sistema Bancário - DEPÓSITO'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo antes do depósito
    print(f'Transações Restantes --> {10 - cont_saque_diarios}\n')  # Exibe quantos saques ainda podem ser realizados
    print('-' * tam)

# Função para exibir o menu de extrato
def menu_extrato(saldo, cont_saque_diarios):
    tam = len('Sistema Bancário - EXTRATO') + 4
    print('-' * tam)
    print('Sistema Bancário - EXTRATO'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo atual ao visualizar o extrato