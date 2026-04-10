#Entrada de escolha de conversão de temperatura
escolha = int(input("Escolha a conversão desejada:\n[1] Fahrenheit - Celsius \n[2]Celsius - Fahrenheit\n "))

#Condição if F para C
if escolha == 1:
    F = float(input("Informe a temperatura: "))
    C = (F - 32) / 1.8
    print(f"Temperatura: {C}ºC")

#Condição C para F
elif escolha == 2:
    C = float(input("Insira a temperatura: "))
    F = (C * 9/5) + 32
    print(f"Temperatura: {F}ºF")

#Erro de escolha
else:
    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")
    
