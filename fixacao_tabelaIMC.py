peso = float(input("Peso: "))
altura = float(input("Altura: "))

IMC = peso / (altura) ** 2

if IMC < 18.5:
    print(f"Abaixo do peso ideal! {IMC}")

elif IMC >= 18.6 and IMC <= 24.9:
    print(f"Parabens! Peso ideal! {IMC}")

elif IMC >= 25.0 and IMC <= 29.9:
    print(f"Levemente acima do peso! {IMC}")

elif IMC >= 30.0 and 34.9:
    print(f"Obesidade grau I! {IMC}")

elif IMC >= 35.0 and 39.9:
    print(f"Obesidade grau II(severa)! {IMC}")

elif IMC >= 40.0:
    print(f"Obesidade grau III(mórbida) {IMC}")
