from datetime import datetime, timedelta  # Importa as classes para manipulação de datas e horários
import pytz  # Biblioteca para manipulação de fusos horários (importada, mas não utilizada)

def saque(*, saldo, cont_saque_diarios, extrato):
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
    
    return saldo, cont_saque_diarios, extrato
    

def deposito(saldo, cont_saque_diarios, extrato, /):
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
        
    return saldo, cont_saque_diarios, extrato


def extrato_(extrato):
    if extrato:
        for transacao in extrato:  # Percorre a lista de extrato e exibe cada transação
            print(f'{transacao}\n')
    else:
        print('Nenhuma transação realizada até o momento.\n')
        
    return extrato