def sacar (*, saque_extrato, conta, valor, saques_diarios, LIMITE_MAXIMO):
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

saque_extrato = ""
saques_diarios = 0
conta = 0
LIMITE_MAXIMO = 500
valor = float(input('Qual valor deseja sacar? '))

saque_extrato, conta, saques_diarios = sacar(saque_extrato= saque_extrato, conta= conta, valor= valor, saques_diarios= saques_diarios, LIMITE_MAXIMO= LIMITE_MAXIMO)

def depositar(conta, valor, deposito_extrato):
    if valor >= 0.1:
            conta += valor
            deposito_extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')
    else:
            print('O valor informado é inválido')
    
    return conta, deposito_extrato

deposito_extrato = ""
valor = float(input('Qual valor deseja depositar? '))

conta, deposito_extrato = depositar(conta, valor, deposito_extrato)

def exibir_extrato(conta, *, extrato, saque_extrato, deposito_extrato):
    
    extrato = deposito_extrato + saque_extrato
    print('################## EXTRATO ##################')
    print(f'Não foram realizadas movimentações.\n Saldo: R$ {conta:.2f}' if not extrato else extrato)
    print(extrato)
    
    return conta, extrato

extrato = deposito_extrato + saque_extrato
conta, extrato = exibir_extrato(conta, extrato= extrato)

def cadastrar_usuario():
 []
  #Em progresso 