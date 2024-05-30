#Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastras usuário(cliente) e cadastrar conta bancária. 

#Precisamos deixar o codigo mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário e criar conta corrente(vincular com o usuário)

#Devemos criar funções para todas operações do sistema. Para exercitar tudo o que aprendemos neste modulo, cada função vai ter que ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por voce da forma que achar melhor.

#O programa deve armazenar usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não pode cadastrar 2 usuários com o mesmo CPF.

def deposito(conta, valor, extrato):
        valor = float(input('Qual valor deseja depositar? '))
        if valor >= 0.1:
            conta += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')
        else:
            print('O valor informado é inválido')
        return conta, extrato
        
def saque(*, conta, valor, saques_diarios, LIMITE_MAXIMO, extrato):
        if saques_diarios < 3:
            valor = float(input('Qual valor deseja sacar? '))
            if valor >= 0.1 and valor <= LIMITE_MAXIMO and conta - valor >= 0:
                print('Saque realizado com sucesso')
                conta -= valor
                saques_diarios += 1
                extrato += f"Saque no valor de R$ {valor:.2f}\n"
            elif valor > LIMITE_MAXIMO:
                print('Limite máximo de 500 reais por saque. Tente novamente.')
            elif conta - valor < 0:
                print('Saldo insuficiente para saque')
        else:
            print('Limite de saques diários atingido.')
        return conta, saques_diarios, extrato
    
def exibir_extrato(conta,*, extrato):
      print('################## EXTRATO ##################')
      print(f'Não foram realizadas movimentações.\nSaldo: R$ {conta:.2f}' if not extrato else f'{extrato}\nSaldo: R$ {conta:.2f}')
      return conta, extrato

def criar_usuario(lista_usuarios, usuarios, cpf):
    lista_usuarios = [usuarios]
    usuarios = [cpf]
    input('Bem vindo ao cadastro do usuário!, digite seu nome completo:')
    input('Digite sua data de nascimento: ')
    cpf = input(' Digite o seu CPF: ')
    input('Digite seu endereço neste formato: logradouro,nro - bairro - cidade/sigla estado. ')
    for usuarios in lista_usuarios:
        if usuarios[cpf] == usuarios[cpf]:
            print('Só é permitido 1 numero de CPF por usuário, Tente novamente.')
            break
    return lista_usuarios

def criar_conta(AGENCIA, n_conta, conta_corrente):
    input(f'''Bem vindo, sua conta foi criada!\nSua conta é {conta_corrente}''')
    AGENCIA = '0001'
    n_conta = 1
    conta_corrente = f'{AGENCIA}-{n_conta}'
    if criar_conta is True:
        n_conta += 1
    return AGENCIA, n_conta
extrato = ""
conta = 0
valor = 0
saques_diarios = 0
LIMITE_MAXIMO = 500
lista_usuarios = []
conta_corrente = []


while True:
    
    criar_usuario('')

    menu = input('''Bem vindo ao banco! Digite:
 - d (Deposito)
 - s (Saque)
 - e (Extrato)
 - q (Sair)
 ''')
    
    if menu == 'd' :
        deposito()
    
    elif menu == 's':
        saque()
        
    elif menu == 'e':
        exibir_extrato()
    
    elif menu == 'q':
        print('Obrigado por utilizar os serviços de nosso banco!')
        break
    else:
        print('Ocorreu um erro, tente novamente')