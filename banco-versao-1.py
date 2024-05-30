extrato = ""
conta = 0
valor = 0
saques_diarios = 0
LIMITE_MAXIMO = 500

while True:

    menu = input('''Bem vindo ao banco! Digite:
 - d (Deposito)
 - s (Saque)
 - e (Extrato)
 - q (Sair)
 ''')

    if menu == 'd' :
        valor = float(input('Qual valor deseja depositar? '))
        if valor >= 0.1:
            conta += valor
            extrato += f"Depósito no valor de R$ {valor:.2f}\n"
            print('Depósito realizado com sucesso!')
        else:
            print('O valor informado é inválido')

    elif menu == 's':
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
            
    elif menu == 'e':
      print('################## EXTRATO ##################')
      print(f'Não foram realizadas movimentações.\nSaldo: R$ {conta:.2f}' if not extrato else f'{extrato}\nSaldo: R$ {conta:.2f}')

    elif menu == 'q':
        print('Obrigado por utilizar os serviços de nosso banco!')
        break
    else:
        print('Ocorreu um erro, tente novamente')