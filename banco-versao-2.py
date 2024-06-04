import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(conta, valor, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta += valor
        extrato += f"Depósito no valor de R$ {valor:.2f}\n"
        print('Depósito realizado com sucesso!')
    else:
        print('O valor informado é inválido')
            
    return conta, extrato


def sacar(*, conta, valor, extrato, LIMITE_MAXIMO, saques_diarios):
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
    return conta, extrato, saques_diarios


def exibir_extrato(conta, /, *, extrato):     
    print('################## EXTRATO ##################')
    print(f'Não foram realizadas movimentações.\nSaldo: R$ {conta:.2f}' if not extrato else f'{extrato}\nSaldo: R$ {conta:.2f}')   


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_MAXIMO = 500
    AGENCIA = "0001"

    extrato = ""
    conta = 0
    saques_diarios = 0
    usuarios = []
    contas = []
    valor = float
    while True:
        opcao = menu()

        if opcao == "d":

            conta, extrato = depositar(conta, valor, extrato)

        elif opcao == "s":
                
            conta, extrato, saques_diarios = sacar(
            conta=conta,
            valor=valor,
            extrato=extrato,
            LIMITE_MAXIMO=LIMITE_MAXIMO,
            saques_diarios=saques_diarios,
            )

        elif opcao == "e":
            exibir_extrato(conta, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()