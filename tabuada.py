tabuada = int(input("Insira um número: "))


print(f"Tabuada do {tabuada}")
for multiplicador in range(1, 11):
    resultado = tabuada * multiplicador
    print(f"{tabuada} x {multiplicador} = {resultado}")