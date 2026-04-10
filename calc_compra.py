valor = float(input("Valor: "))
menu_choose = int(input("Forma de pagamento:\n[1] À Vista \n[2]Parcelado \n"))

if menu_choose == 1:
    menu_choose2 = int(input("[1] Dinheiro \n[2] Pix \n[3] Crédito \n"))
    if menu_choose2 == 1 or menu_choose2 == 2:
        final_valor = valor - (valor*(15/100))
        print(f"Valor final do produto: {final_valor}")
    elif menu_choose2 == 3:
        final_valor = valor - (valor * (10/100))
        print(f"Valor final do produto: {final_valor}")
    else:
        print("Opção inválida!")
else:
    menu_choose3 = int(input("[1] Parcelado em 2x \n[2] Parcelado em 3x ou mais \n"))
    if menu_choose3 == 1:
        final_valor = valor / 2
        print(f"O valor total do produto é {valor}, sendo em duas parcelas de {final_valor}")
    elif menu_choose3 == 2:
        parcela = int(input("Quantidade de parcelas desejadas: "))
        if parcela >= 3:
            final_valor = (valor + (valor * (10/100))) / parcela
            print(f"O valor total das parcelas é de: {final_valor}")
        else:
            print("Opção inválida!")
    else:
        print("Opção inválida!")
