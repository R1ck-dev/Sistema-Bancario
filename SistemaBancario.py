from time import sleep  # Importa a função sleep para pausar a execução por um tempo determinado
from datetime import datetime, timedelta  # Importa as classes para manipulação de datas e horários
import pytz  # Biblioteca para manipulação de fusos horários (importada, mas não utilizada)

# Definição de variáveis globais
saldo = 1000.00  # Saldo inicial da conta
cont_saque_diarios = 0  # Contador de saques diários realizados
extrato = list()  # Lista para armazenar o extrato das transações
dia_atual = datetime.now()  # Obtém a data e hora atual
dia_atual_formatado = dia_atual.strftime("%d/%m/%Y %Hh%M")  # Formata a data para exibição
data_dia_atual = dia_atual.strftime("%d")  # Captura apenas o dia do mês atual

# Função para exibir o menu principal
def menu():
    tam = len('Sistema Bancário - MENU') + 4  # Define o tamanho da linha de separação
    print('-' * tam)
    print('Sistema Bancário - MENU'.center(tam))  # Centraliza o título do menu
    print('-' * tam)
    print('\n[1] Saque')
    print('[2] Depósito')
    print('[3] Visualizar Extrato')
    print('[4] Sair\n')
    print('-' * tam)

# Função para exibir o menu de saque
def menu_saque():
    tam = len('Sistema Bancário - SAQUE') + 4
    print('-' * tam)
    print('Sistema Bancário - SAQUE'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}')  # Exibe o saldo atual
    print(f'Transações Restantes --> {10 - cont_saque_diarios}\n')  # Exibe quantos saques ainda podem ser realizados
    print('-' * tam)

# Função para exibir o menu de depósito
def menu_deposito():
    tam = len('Sistema Bancário - DEPÓSITO') + 4
    print('-' * tam)
    print('Sistema Bancário - DEPÓSITO'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo antes do depósito
    print(f'Transações Restantes --> {10 - cont_saque_diarios}\n')  # Exibe quantos saques ainda podem ser realizados
    print('-' * tam)

# Função para exibir o menu de extrato
def menu_extrato():
    tam = len('Sistema Bancário - EXTRATO') + 4
    print('-' * tam)
    print('Sistema Bancário - EXTRATO'.center(tam))
    print('-' * tam)
    print(f'\nSaldo Atual -->  R${saldo:.2f}\n')  # Exibe o saldo atual ao visualizar o extrato

# Loop principal do sistema bancário
while True:
    # Verifica se o dia mudou para resetar o limite de saques diários
    if data_dia_atual != datetime.now().strftime("%d"):
        cont_saque_diarios = 0  # Reseta o contador de saques

    menu()  # Exibe o menu principal
    operacao = int(input("Indique a operação desejada: "))  # Solicita a opção do usuário
    
    # Verifica se a opção informada é válida
    if str(operacao) not in '1234':
        print('ERRO! Opção Inválida')
        continue

    # Opção de saque
    elif operacao == 1:
        menu_saque()  # Exibe o menu de saque
        if cont_saque_diarios < 10:  # Verifica se o usuário ainda tem saques disponíveis no dia
            valor_saque = float(input('Indique o valor de saque: '))  # Solicita o valor do saque
            if valor_saque <= 500:  # Verifica se o valor do saque não ultrapassa o limite de R$500,00
                if valor_saque <= saldo:  # Verifica se há saldo suficiente para o saque
                    saldo -= valor_saque  # Deduz o valor do saque do saldo
                    print('Operação realizada com sucesso!')
                    print(f'Seu saldo atual é de R${saldo:.2f}')
                    # Registra o saque no extrato com data e hora
                    extrato.append(f'Saque -> R${valor_saque:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]')
                    cont_saque_diarios += 1  # Incrementa o contador de saques diários
                else:
                    print('Valor do saque excede o seu saldo atual.')
                    print(f'Saldo Atual = R${saldo:.2f}')
            else:
                print('Valor de saque é maior do que o limite de R$500,00')
        else:
            print('Quantidade máxima de transações diárias excedida')

    # Opção de depósito
    elif operacao == 2:
        menu_deposito()  # Exibe o menu de depósito
        if cont_saque_diarios < 10:  # Verifica se o usuário ainda pode realizar transações
            valor_deposito = float(input('Indique o valor de depósito: '))  # Solicita o valor do depósito
            saldo += valor_deposito  # Adiciona o valor depositado ao saldo
            print('Operação realizada com sucesso!')
            cont_saque_diarios += 1  # Incrementa o contador de transações diárias
            print(f'Seu saldo atual é de R${saldo:.2f}')
            # Registra o depósito no extrato com data e hora
            extrato.append(f'Depósito -> R${valor_deposito:.2f} [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]')
        else:
            print('Quantidade máxima de transações diárias excedida')

    # Opção de visualização do extrato
    elif operacao == 3:
        menu_extrato()  # Exibe o menu de extrato
        if extrato:
            for transacao in extrato:  # Percorre a lista de extrato e exibe cada transação
                print(f'{transacao}\n')
        else:
            print('Nenhuma transação realizada até o momento.\n')

    # Opção para sair do sistema
    elif operacao == 4:
        break  # Encerra o loop e finaliza o programa

    sleep(2)  # Aguarda 2 segundos antes de retornar ao menu
