from datetime import date

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

calc_idade()