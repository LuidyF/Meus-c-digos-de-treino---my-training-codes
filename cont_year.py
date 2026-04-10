from datetime import date

#Definindo função para calcular sua idade mediante entrada de informação do ano de nascimento
def calc_idade():
    ano_atual = date.today().year
    
   
    nascimento = int(input("Insira seu ano de nascimento: "))

    anos = ano_atual - nascimento
    meses = anos * 12
    dias = anos * 365

    print("\nSua idade atual é:")
    print(f"{anos} anos")
    print(f"{meses} meses")
    print(f"{dias} dias")

#Executando função
calc_idade()
