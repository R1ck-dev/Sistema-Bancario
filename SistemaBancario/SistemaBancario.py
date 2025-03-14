from time import sleep  # Importa a função sleep para pausar a execução por um tempo determinado
from datetime import datetime, timedelta  # Importa as classes para manipulação de datas e horários
import pytz  # Biblioteca para manipulação de fusos horários (importada, mas não utilizada)
from menu import menu, menu_deposito, menu_extrato, menu_saque
from transacoes import saque, deposito, extrato_

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
    operacao = int(input("Indique a operação desejada: "))  # Solicita a opção do usuário
    
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
        nome = str(input("Nome completo do usuário: "))
        data_nascimento = str(input("Data de nascimento do usuário [xx/xx/xxxx]: "))
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        data_nascimento = data_nascimento.strftime("%d/%m/%Y")
        cpf = int(input("CPF do usuário: "))
        
        # Coleta informações do endereço
        endereco = list()
        endereco.append(str(input("Endereço - logradouro: ")))
        endereco.append(str(input("Endereço - número: ")))
        endereco.append(str(input("Endereço - bairro: ")))
        endereco.append(str(input("Endereço - Cidade/Sigla Estado: ")))
        
        # Armazena os dados do usuário no dicionário
        usuarios_dict[cpf] = {
            "nome": nome,
            "data de nascimento": data_nascimento,
            "cpf": cpf,
            "endereço": endereco
        }
        
        print(f"Usuários Final: {usuarios_dict}")
    
    # Opção para criar uma conta bancária para um usuário existente
    elif operacao == 5:
        print("Escolha um usuário para criar a conta!")
        for chave in usuarios_dict.keys():
            print(f'{usuarios_dict[chave]["nome"]} --- {usuarios_dict[chave]["cpf"]}')
        
        usuario_escolhido = int(input())
        
        # Verifica se o usuário existe e cria a conta
        for chave in usuarios_dict.keys():
            if usuario_escolhido == chave:
                numero_conta += 1
                print("Usuário Encontrado")
                print(f"Criando conta para {usuarios_dict[usuario_escolhido]['nome']}")
                
                # Adiciona a conta ao dicionário de contas
                if usuario_escolhido in contas_dict:
                    contas_dict[usuario_escolhido].append(['0001', numero_conta, usuarios_dict[usuario_escolhido]['nome']])
                else:
                    contas_dict[usuario_escolhido] = [['0001', numero_conta, usuarios_dict[usuario_escolhido]['nome']]]
        
        print("Conta Criada com Sucesso.")
        print(f"{usuarios_dict[usuario_escolhido]['nome']} agora possui {len(contas_dict[usuario_escolhido])} conta(s)")
        print(f'\n{contas_dict}')
    
    # Opção para excluir um usuário
    elif operacao == 6:
        print("Escolha qual usuário você deseja apagar.")
        c = 0
        for chave in usuarios_dict.keys():
            print(f'[{c}] {usuarios_dict[chave]["nome"]} --- {usuarios_dict[chave]["cpf"]}')
            c += 1
        usuario_escolhido = int(input())
        del usuarios_dict[usuario_escolhido]
        
        print(usuarios_dict)
    
    # Opção para visualizar contas de um usuário específico
    elif operacao == 7:
        print("Escolha qual usuário você deseja ver as contas.")
        c = 0
        for chave in usuarios_dict.keys():
            print(f'[{c}] {usuarios_dict[chave]["nome"]} --- {usuarios_dict[chave]["cpf"]}')
            c += 1
        usuario_escolhido = int(input())
        
        if usuario_escolhido in contas_dict:
            for valor in contas_dict[usuario_escolhido]:
                print(f"| CPF: {usuario_escolhido}")
                print(f"| Agência: {valor[0]}")
                print(f"| Número da Conta: {valor[1]}")
                print(f"| Usuário: {valor[2]}")
                print("-" * 30)  
    
    # Opção para sair do sistema
    elif operacao == 8:
        break  # Encerra o loop e finaliza o programa
    
    sleep(2)  # Aguarda 2 segundos antes de retornar ao menu
