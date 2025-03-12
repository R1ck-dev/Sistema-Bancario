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
# usuarios = list()
usuarios = [
    ['Henrique', '11/08/2005', 54994479852, ['Rua Curitiba', '66', 'Celia Mota', 'Barueri/SP São Paulo']]
    ]
usuarios_dict = {
    '12345678900': {
        "nome": "Henrique",
        "data de nascimento": "11/08/2005",
        "cpf": 12345678900,
        "endereço": ['Rua Curitiba', '66', 'Celia Mota', 'Barueri/SP São Paulo']
    },
    '98765432100': {
        "nome": "Guilherme",
        "data de nascimento": "20/03/1998",
        "cpf": 98765432100,
        "endereço": ['Rua das Palmeiras', '102', 'Centro', 'São Paulo/SP São Paulo']
    },
    '11223344556': {
        "nome": "Giovanna",
        "data de nascimento": "15/07/2000",
        "cpf": 11223344556,
        "endereço": ['Av. Brasil', '45', 'Bela Vista', 'São Paulo/SP São Paulo']
    },
    '55667788990': {
        "nome": "Chappie",
        "data de nascimento": "03/12/1995",
        "cpf": 55667788990,
        "endereço": ['Rua dos Lírios', '38', 'Vila Mariana', 'São Paulo/SP São Paulo']
    },
    '66778899001': {
        "nome": "Melaine",
        "data de nascimento": "28/02/1992",
        "cpf": 66778899001,
        "endereço": ['Rua dos Eucaliptos', '77', 'Jardim das Flores', 'São Paulo/SP São Paulo']
    }
}
contas_dict = {}
id_conta = 0


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

    # Opção para sair do sistema
    elif operacao == 8:
        break  # Encerra o loop e finaliza o programa
    
    elif operacao == 4:
        # usuarios_aux = list()
        # nome = str(input("Nome completo do usuário: "))
        # usuarios_aux.append(nome)
        # data_nascimento = str(input("Data de nascimento do usuários [xx/xx/xxxx]: "))
        # data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        # data_nascimento = data_nascimento.strftime("%d/%m/%Y")
        # usuarios_aux.append(data_nascimento)
        # cpf = int(input("CPF do usuário: "))
        # usuarios_aux.append(cpf)
        # endereço = list()
        # endereço.append(str(input("Endereço - logradouro: ")))
        # endereço.append(str(input("Endereço - numero: ")))
        # endereço.append(str(input("Endereço - bairro: ")))
        # endereço.append(str(input("Endereço - Cidade/Sigla Estado: ")))
        # usuarios_aux.append(endereço.copy())
        # endereço.clear()
        # usuarios.append(usuarios_aux.copy())
        # usuarios_aux.clear()
        
        # print(f"Usuários Final: {usuarios}")
        
        nome = str(input("Nome completo do usuário: "))
        data_nascimento = str(input("Data de nascimento do usuários [xx/xx/xxxx]: "))
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        data_nascimento = data_nascimento.strftime("%d/%m/%Y")
        cpf = int(input("CPF do usuário: "))
        endereço = list()
        endereço.append(str(input("Endereço - logradouro: ")))
        endereço.append(str(input("Endereço - numero: ")))
        endereço.append(str(input("Endereço - bairro: ")))
        endereço.append(str(input("Endereço - Cidade/Sigla Estado: ")))
        usuarios_dict[cpf] = {
            "nome": nome,
            "data de nascimento": data_nascimento,
            "cpf": cpf,
            "endereço": endereço
        }
        
        print(f"Usuários Final: {usuarios_dict}")
        
        
    elif operacao == 5:
        usuario_escolhido = str(input("CPF do Usuário: "))
        for cpf_cont in usuarios_dict.keys():
            if usuario_escolhido == cpf_cont:
                print("Usuário Encontrado!")
                print(f"Criando Conta para {usuarios_dict[usuario_escolhido]['nome']}")
        # print("Deseja Criar Conta Corrente para qual Usuário:")
        # for id_usuario, dados in usuarios_dict.items():
        #     print(f"CPF: [{id_usuario}] - Nome: {dados['nome']}")
        # usuario_escolhido = int(input())
        # if usuario_escolhido > len(usuarios):
        #     print("Usuário Inexistente!")
        #     continue
        
        
        # contas_dict[usuarios_dict[cpf]]
        
        

    sleep(2)  # Aguarda 2 segundos antes de retornar ao menu
