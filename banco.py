d = str
s = str
e = str
q = str
saque_extrato = ""
deposito_extrato = ""
conta = 0
valor_depositado = 0
valor_saque = 0
saques_diarios = 0
LIMITE_MAXIMO = 500
extrato = saque_extrato and deposito_extrato
while True:

    menu = input('''Bem vindo ao banco! Digite:
 - d (Deposito)
 - s (Saque)
 - e (Extrato)
 - q (Sair)
 ''')

    if menu == 'd' :
        valor_depositado = float(input('Qual valor deseja depositar? '))
        if valor_depositado >= 0.1:
            conta += valor_depositado
            deposito_extrato += f"Depósito no valor de R$ {valor_depositado:.2f}\n"
            print('Depósito realizado com sucesso!')
        else:
            print('O valor informado é inválido')

    elif menu == 's':
        if saques_diarios < 3:
            valor_saque = float(input('Qual valor deseja sacar? '))
            if valor_saque >= 0.1 and valor_saque <= LIMITE_MAXIMO and conta - valor_saque >= 0:
                print('Saque realizado com sucesso')
                conta -= valor_saque
                saques_diarios += 1
                saque_extrato += f"Saque no valor de R$ {valor_saque:.2f}\n"
            elif valor_saque > LIMITE_MAXIMO:
                print('Limite máximo de 500 reais por saque. Tente novamente.')
            elif conta - valor_saque < 0:
                print('Saldo insuficiente para saque')
        else:
            print('Limite de saques diários atingido.')
    elif menu == 'e':
      print('################## EXTRATO ##################')
      print(f'Não foram realizadas movimentações.\n Saldo: R$ {conta:.2f}' if not extrato else extrato)
      print(f'{deposito_extrato}{saque_extrato}')

    elif menu == 'q':
        print('Obrigado por utilizar os serviços de nosso banco!')
        break
    else:
        print('Ocorreu um erro, tente novamente')