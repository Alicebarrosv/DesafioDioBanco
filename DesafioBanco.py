
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
oi = True

menu = """

ESCOLHA UMA OPÇÃO
[1]Depositar
[2]Sacar
[3]Extrato
[4]Sair

"""

while oi == True:

    opcao = input(menu)
   
    if opcao == "1":
       
        valor = float(input("Digite o valor que deseja depositar: "))
        
        if valor > 0 :
           valor = saldo = saldo + valor
           extrato = extrato + f"Depósito no valor de R${valor:.2f}\n"
        
        else:
            print("Não foi possivel realizar o depósito, verifique o valor")
    
    elif opcao == "2" :
        
        sacar = float(input("Digite o valor que deseja sacar: "))
       
        if sacar > limite :
            print("Você não pode sacar devido o limite de saque de R$500.00")
        
        elif sacar > saldo :
            print("Você não tem saldo suficiente para sacar")
        
        elif numero_saques >= LIMITE_SAQUES :
            print("Você atingiu o limite de saques")
        
        elif sacar > 0 and sacar < saldo: 
            saldo = saldo - sacar
            numero_saques = numero_saques + 1
            extrato = extrato + f"Saque no valor de R${sacar:.2f}\n"
            print("O saque foi realizado com sucesso!!")
        
        else:
            print("Operação falhou! Valor informado incorreto.")
    
    elif opcao == "3" :

        print("----------------Extrato----------------")
        if extrato == "" :
           print("Você não tem movimentações.")
        else:
            print(extrato)
     
    elif opcao == "4" :
        break
   
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")