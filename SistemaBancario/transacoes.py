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

def criar_usuario(usuarios_dict):
    nome = str(input("\nNome completo do usuário: "))
    data_nascimento = str(input("Data de nascimento do usuário [xx/xx/xxxx]: "))
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
    data_nascimento = data_nascimento.strftime("%d/%m/%Y")
    cpf = int(input("CPF do usuário: "))
        
    if cpf in usuarios_dict:
        print("CPF já cadastrado!")
        
    else:
        # Coleta informações do endereço
        endereco = list()
        endereco.append(str(input("Endereço - logradouro: ")))
        endereco.append(str(input("Endereço - número: ")))
        endereco.append(str(input("Endereço - bairro: ")))
        endereco.append(str(input("Endereço - Cidade/Sigla Estado: ")))
            
        usuarios_dict[cpf] = []
            
        # Armazena os dados do usuário no dicionário
        usuarios_dict[cpf].append({
            "nome": nome,
            "data de nascimento": data_nascimento,
            "cpf": cpf,
            "endereço": endereco
        })
            
        print("\n|Usuário Criado com Sucesso|\n")
        print(f"Usuários Final: {usuarios_dict}")
    
    return usuarios_dict

def criar_conta(usuarios_dict, contas_dict, numero_conta):
    print("\nEscolha um usuário para criar a conta!")

    for chave in usuarios_dict.keys():
        print(f'{usuarios_dict[chave][0]["nome"]} --- {usuarios_dict[chave][0]["cpf"]}')
    usuario_escolhido = int(input())
        
    # Verifica se o usuário existe e cria a conta
    for chave in usuarios_dict.keys():
        if usuario_escolhido == chave:
            numero_conta += 1
            print("Usuário Encontrado")
            print(f"Criando conta para {usuarios_dict[usuario_escolhido][0]['nome']}")
            
            # Adiciona a conta ao dicionário de contas
            if usuario_escolhido in contas_dict:
                contas_dict[usuario_escolhido].append(['0001', numero_conta, usuarios_dict[usuario_escolhido][0]['nome']])
            else:
                contas_dict[usuario_escolhido] = [['0001', numero_conta, usuarios_dict[usuario_escolhido][0]['nome']]]
        
    print("Conta Criada com Sucesso.")
    print(f"{usuarios_dict[usuario_escolhido][0]['nome']} agora possui {len(contas_dict[usuario_escolhido])} conta(s)")
    print(f'\n{contas_dict}')
    
    return usuarios_dict, contas_dict, numero_conta

def deletar_conta(usuarios_dict):
    print("\nEscolha qual usuário você deseja apagar.")

    for chave in usuarios_dict.keys():
        print(f'--> {usuarios_dict[chave][0]["nome"]} | {usuarios_dict[chave][0]["cpf"]}')
        
    usuario_escolhido = int(input())
    del usuarios_dict[usuario_escolhido]
        
    print(usuarios_dict)
    
    return usuarios_dict

def listar_usuarios(usuarios_dict, contas_dict):
    print("Escolha qual usuário você deseja ver as contas.")

    for chave in usuarios_dict.keys():
        print(f'--> {usuarios_dict[chave][0]["nome"]} | {usuarios_dict[chave][0]["cpf"]}')
        
    usuario_escolhido = int(input())
    print(usuarios_dict)
    if usuario_escolhido in contas_dict:
        for valor in contas_dict[usuario_escolhido]:
            print(f"| CPF: {usuario_escolhido}")
            print(f"| Agência: {valor[0]}")
            print(f"| Número da Conta: {valor[1]}")
            print(f"| Usuário: {valor[2]}")
            print("-" * 30)  
    
    return usuarios_dict, contas_dict