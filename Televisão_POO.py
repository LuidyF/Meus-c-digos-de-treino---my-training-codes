class Televisão:
    def __init__(self, canais=1, som=0):
        self.canais = canais
        self.som = som

    def mudar_canal (self, canal):
        self.canal = canal

        if canal > 0 and canal < 100:
            if canal == 4:
                print("Você está assistindo a TV GLOBO!")
            elif canal == 6:
                print("APENAS MUDE DE CANAL!")
            elif canal == 7:
                print("Você está assistindo a TV BAND!")
            elif canal == 9:
                print("Você está assistindo a TV CNT!")
            elif canal == 11:
                print("Você está assistindo ao SBT!")
            elif canal == 13:
                print("Você está assistindo a REDE RECORD!")

        else:
            print("Tente novamente...")
    
    def mudar_som (self, volume):
        self.volume = volume
        print(f"Volume = {volume}")


#TESTE DA CLASSE
tv = Televisão()
tv.mudar_canal(4)
tv.mudar_som(50)

tv.mudar_canal(11)
tv.mudar_som(20)

tv.mudar_canal(6)

tv.mudar_canal(13)
