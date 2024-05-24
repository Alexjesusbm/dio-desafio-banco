def sacar(*, saque_extrato, conta, valor, saques_diarios, LIMITE_MAXIMO):
    if saques_diarios < 3:
        if valor >= 0.1 and valor <= LIMITE_MAXIMO and conta - valor >= 0:
            print('Saque realizado com sucesso')
            conta -= valor
            saques_diarios += 1
            saque_extrato += f"Saque no valor de R$ {valor:.2f}\n"
        elif valor > LIMITE_MAXIMO:
            print('Limite máximo de 500 reais por saque. Tente novamente.')
        elif conta - valor < 0:
            print('Saldo insuficiente para saque')
    else:
        print('Limite de saques diários atingido.')
    
    return saque_extrato, conta, saques_diarios

def depositar(conta, valor, deposito_extrato):
    if valor >= 0.1:
        conta += valor
        deposito_extrato += f"Depósito no valor de R$ {valor:.2f}\n"
        print('Depósito realizado com sucesso!')
    else:
        print('O valor informado é inválido')
    
    return conta, deposito_extrato

def exibir_extrato(conta, *, extrato):
    print('################## EXTRATO ##################')
    print(f'Não foram realizadas movimentações.\n Saldo: R$ {conta:.2f}' if not extrato else extrato)
    print(f'Saldo: R$ {conta:.2f}')
    return conta, extrato

def cadastrar_usuario(lista_usuarios):
    nome = input('Qual seu nome? ')
    data_nascimento = input('Qual sua data de nascimento? ')
    cpf = input('Qual o seu CPF? ')
    endereco = input('Qual seu endereço? ')
    
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return None
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    lista_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

conta = 0
saque_extrato = ""
deposito_extrato = ""
saques_diarios = 0
LIMITE_MAXIMO = 500
lista_usuarios = []

valor = float(input('Qual valor deseja sacar? '))
saque_extrato, conta, saques_diarios = sacar(saque_extrato=saque_extrato, conta=conta, valor=valor, saques_diarios=saques_diarios, LIMITE_MAXIMO=LIMITE_MAXIMO)

valor = float(input('Qual valor deseja depositar? '))
conta, deposito_extrato = depositar(conta, valor, deposito_extrato)

extrato = deposito_extrato + saque_extrato
conta, extrato = exibir_extrato(conta, extrato=extrato)

cadastrar_usuario(lista_usuarios)
print(lista_usuarios)
