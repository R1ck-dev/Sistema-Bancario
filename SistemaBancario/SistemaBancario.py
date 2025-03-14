from time import sleep  # Importa a função sleep para pausar a execução por um tempo determinado
from datetime import datetime, timedelta  # Importa as classes para manipulação de datas e horários
import pytz  # Biblioteca para manipulação de fusos horários (importada, mas não utilizada)
from menu import menu, menu_deposito, menu_extrato, menu_saque, menu_criar_usuario, menu_criar_conta, menu_deletar_conta, menu_listar_usuarios
from transacoes import saque, deposito, extrato_, criar_usuario, criar_conta, deletar_conta, listar_usuarios

# Definição de variáveis globais
saldo = 1000.00  # Saldo inicial da conta
cont_saque_diarios = 0  # Contador de saques diários realizados
extrato = list()  # Lista para armazenar o extrato das transações
dia_atual = datetime.now()  # Obtém a data e hora atual
dia_atual_formatado = dia_atual.strftime("%d/%m/%Y %Hh%M")  # Formata a data para exibição
data_dia_atual = dia_atual.strftime("%d")  # Captura apenas o dia do mês atual
usuarios_dict = {}  # Dicionário para armazenar usuários
contas_dict = {}  # Dicionário para armazenar contas bancárias
numero_conta = 0  # Contador para o número da conta

# Loop principal do sistema bancário
while True:
    # Verifica se o dia mudou para resetar o limite de saques diários
    if data_dia_atual != datetime.now().strftime("%d"):
        cont_saque_diarios = 0  # Reseta o contador de saques

    menu()  # Exibe o menu principal
    operacao = int(input("\nIndique a operação desejada: "))  # Solicita a opção do usuário
    print()
    
    # Verifica se a opção informada é válida
    if str(operacao) not in '12345678':
        print('ERRO! Opção Inválida')
        continue

    # Opção de saque
    elif operacao == 1:
        menu_saque(saldo, cont_saque_diarios)  # Exibe o menu de saque
        saldo, cont_saque_diarios, extrato = saque(saldo=saldo, cont_saque_diarios=cont_saque_diarios, extrato=extrato)        

    # Opção de depósito
    elif operacao == 2:
        menu_deposito(saldo, cont_saque_diarios)  # Exibe o menu de depósito
        saldo, cont_saque_diarios, extrato = deposito(saldo, cont_saque_diarios, extrato) 

    # Opção de visualização do extrato
    elif operacao == 3:
        menu_extrato(saldo, cont_saque_diarios)  # Exibe o menu de extrato
        extrato = extrato_(extrato)
    
    # Opção para cadastrar um novo usuário
    elif operacao == 4:
        menu_criar_usuario()
        usuarios_dict = criar_usuario(usuarios_dict)
        
    # Opção para criar uma conta bancária para um usuário existente
    elif operacao == 5:
        menu_criar_conta()
        usuarios_dict, contas_dict, numero_conta = criar_conta(usuarios_dict, contas_dict, numero_conta)
        
    # Opção para excluir um usuário
    elif operacao == 6:
        menu_deletar_conta()
        usuarios_dict = deletar_conta(usuarios_dict)
    
    # Opção para visualizar contas de um usuário específico
    elif operacao == 7:
        menu_listar_usuarios()
        usuarios_dict, contas_dict = listar_usuarios(usuarios_dict, contas_dict)
    
    # Opção para sair do sistema
    elif operacao == 8:
        break  # Encerra o loop e finaliza o programa
    
    sleep(2)  # Aguarda 2 segundos antes de retornar ao menu
