class Carros:
    """
    Classe dedicada ao cadastramento de carros 
    Entradas: modelo, ano, marca, cor, placa, km
    """

    def __init__(self, modelo, ano, marca, cor, placa, km):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.cor = cor
        self.placa = placa
        self.km = km
    
    def mostrar_infos(self):
        print("#"*20)
        print(f"O carro de placa {self.placa} é:")
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Marca:", self.marca)
        print("Cor:", self.cor)
        print("Km:", self.km)
        print("#"*20)



