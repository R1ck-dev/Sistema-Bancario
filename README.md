# 💰 Sistema Bancário Simples

Este é um sistema bancário simples implementado em Python que permite ao usuário realizar operações básicas como saque, depósito e visualização do extrato. Desenvolvido como método de aprendizado para o bootcamp Suzano - Python Developer (DIO)

## ✨ Funcionalidades
- 🏧 **Saque**: Permite realizar saques com um limite de R$500,00 por transação e um limite de 3 saques diários.
- 💵 **Depósito**: Permite adicionar saldo à conta do usuário.
- 📜 **Visualização de Extrato**: Exibe todas as transações realizadas.
- 🚪 **Sair**: Encerra o sistema.

## ⚙️ Requisitos
- 🐍 Python 3.x

## 🚀 Como Executar o Programa
    1. Certifique-se de ter o Python instalado no seu computador.
    2. Salve o código em um arquivo com extensão `.py` (por exemplo, `sistema_bancario.py`).
    3. Execute o script no terminal ou prompt de comando:
   ```sh
   python sistema_bancario.py
   ```

## 📌 Estrutura do Sistema
O programa é baseado em um loop principal que exibe um menu interativo para o usuário, permitindo que ele escolha entre as opções disponíveis.
Cada operação tem um menu próprio para guiar o usuário durante a interação.

### 🔍 Lógica de Funcionamento
- 💲 O saldo inicial da conta é de R$1000,00.
- 📝 O extrato é armazenado em uma lista que registra todas as transações realizadas.
- ❌ O programa impede que o usuário saque um valor maior do que o saldo disponível ou acima do limite por transação.
- ⏳ Há uma pausa de 2 segundos antes de retornar ao menu principal após cada operação.

## 🔧 Ainda em Desenvolvimento
- 🔑 Implementar um sistema de autenticação para o usuário.
- 🗄️ Armazenar os dados do saldo e extrato em um banco de dados ou arquivo.
- 🖥️ Criar uma interface gráfica para melhor interatividade.

## 👨‍💻 Autor
Desenvolvido como um projeto de estudo em Python para aprendizado de manipulação de variáveis e controle de fluxo.

### 📎 Contato
- GitHub: [R1ck-dev](https://github.com/R1ck-dev)
- LinkedIn: [Henrique Marangoni](https://www.linkedin.com/in/henrique-marangoni-484845239/)
