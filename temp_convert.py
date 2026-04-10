escolha = int(input("Escolha a conversão desejada:\n[1] Fahrenheit - Celsius \n[2]Celsius - Fahrenheit\n "))

if escolha == 1:
    F = float(input("Informe a temperatura: "))
    C = (F - 32) / 1.8
    print(f"Temperatura: {C}ºC")
elif escolha == 2:
    C = float(input("Insira a temperatura: "))
    F = (C * 9/5) + 32
    print(f"Temperatura: {F}ºF")
else:
    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")
    