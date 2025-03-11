# 💰 Sistema Bancário Simples

Este é um sistema bancário implementado em Python que permite ao usuário realizar operações básicas como saque, depósito e visualização do extrato. Ele inclui um sistema de controle de limites diários e registro preciso das transações com data e hora.

## ✨ Funcionalidades
- 🏧 **Saque**: Permite realizar saques com um limite de **R$500,00 por transação** e um máximo de **10 transações diárias**.
- 💵 **Depósito**: O usuário pode adicionar qualquer valor ao saldo da conta.
- 📜 **Extrato com Data e Hora**: Todas as transações são registradas com a data e hora exatas, permitindo um histórico detalhado.
- 🔟 **Limite Diário de Transações**: O sistema permite até **10 transações por dia** (saques e depósitos combinados).
- ⏳ **Reset Automático dos Limites**: O contador de transações diárias é **automaticamente zerado à meia-noite**.
- 🚫 **Bloqueio de Transações Após o Limite**: Se o limite diário for atingido, novas operações são bloqueadas e uma mensagem é exibida.
- 🚪 **Sair**: Opção para encerrar o sistema.

## ⚙️ Requisitos
- 🐍 Python 3.x

## 🚀 Como Executar o Programa
1. Certifique-se de ter o Python instalado em seu computador.
2. Salve o código em um arquivo `.py` (por exemplo, `sistema_bancario.py`).
3. Execute o script no terminal:
   ```sh
   python sistema_bancario.py


## 📌 Estrutura do Sistema
O programa é baseado em um loop principal que exibe um menu interativo para o usuário, permitindo que ele escolha entre as opções disponíveis.
Cada operação tem um menu próprio para guiar o usuário durante a interação.

### 🔍 Lógica de Funcionamento
- 💲  Saldo Inicial: A conta começa com um saldo de R$1000,00.
- 📆 Registro de Transações: Cada saque e depósito é armazenado no extrato com data e hora.
- ❌ Limite de Saque: O programa impede que o usuário saque um valor maior do que o saldo disponível ou acima do limite por transação.
- 🔄 Limite Diário: O usuário pode realizar até 10 transações por dia (saques e depósitos somados).
- ⏳ Renovação Automática do Limite: À meia-noite, o contador de transações é reiniciado automaticamente.
- 🚫 Bloqueio de Transações Excedentes: Se o usuário atingir o limite diário, novas operações não serão permitidas até o dia seguinte.

## 🔧 Ainda em Desenvolvimento
- 🔑 Implementar um sistema de autenticação para o usuário.
- 🗄️ Armazenar os dados do saldo e extrato em um banco de dados ou arquivo.
- 🖥️ Criar uma interface gráfica para melhor interatividade.

## 👨‍💻 Autor
Desenvolvido como um projeto de estudo em Python para aprendizado de manipulação de variáveis e controle de fluxo.

### 📎 Contato
- GitHub: [R1ck-dev](https://github.com/R1ck-dev)
- LinkedIn: [Henrique Marangoni](https://www.linkedin.com/in/henrique-marangoni-484845239/)
