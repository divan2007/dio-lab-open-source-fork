color="\033[0m"
print(f'''{color}
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ================================


''')
saldo_conta=0.0
historico=[]
opcao=-1
limite_saques=3
i=limite_saques
limite_valor_saque=500

while opcao!=0:
    opcao=input("Digite uma opção do Menu ou 0 para sair:")
    if opcao=='':
        print(f'''\n{color}Opção inválida.''') 
        continue
    else:
        opcao=int(opcao)
    if opcao==1:
        valor_deposito=float(input("Digite um valor para o depósito:"))
        if valor_deposito>0:
            historico.append(valor_deposito)
            saldo_conta=saldo_conta + valor_deposito
        else:
            print(f'''\n{color}Valor do depósito inválido.''')    
    elif opcao==2:
        if i>0:
            valor_saque=float(input("Digite um valor para o saque:"))
            if saldo_conta<=0 or valor_saque>saldo_conta:
                print( f''' O saque não poderá ser realizado pois não há saldo suficiente na conta.''',end="\n")
            elif valor_saque>limite_valor_saque:
                print( f''' O saque não poderá ultrpassar o de {limite_valor_saque} foi atingido.''',end="\n")
            else:
                saldo_conta=saldo_conta - valor_saque 
                historico.append(-valor_saque)
                i=i-1
        else:
            print( f''' O limite de {limite_saques} saques diários foi atingido. Tente por favor amanhã.''',end="\n")

    elif opcao==3:
        if len(historico)>0:
            color="\033[0m"
            print(f'''{color} ===============  ''',end="\n")
            print( f''' Saldo da conta {saldo_conta}''',end="\n")
            print(f'''{color} ===============  ''',end="\n")
            print(f''' Valor   Tipo da Operação  ''',end="\n")
            print(f''' ===============  ''',end="\n")
            for historicos in historico:
                tipo="saque" if historicos<0 else "Deposito"
                color2="\033[31m " if historicos<0 else"\033[0m"
                print(f'''{color2}R${historicos}   {tipo}  ''',end="\n")

            print(f'''{color} ===============  ''',end="\n")
        else:
          print(f'''\n{color}Não há movimentação na conta para exibir o extrato.''') 
    elif opcao not in (0,1,2,3):
        print(f'''\n{color}Opção inválida digite novamente.''')   
    else:
        break
print(f'''\n{color}Obrigado por usar nosso sistema!!!!''')