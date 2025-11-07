from models.carros import Carros


corolla = Carros(modelo ="Corolla",
                 marca = "Toyota",
                 cor = "preto", 
                 ano = 2000,
                 placa = "IAB-1234",
                 km = 1000000)

carros = [corolla, ]



menu = "Digite:\n" + \
       "C - para CADASTRAR um novo carro. \n" + \
       "R - para BUSCAR um novo carro. \n" + \
       "U - para ATUALIZAR um novo carro. \n" + \
       "D - para DELETAR um novo carro. \n" + \
       "S - para SAIR: "


def cadastrar():
    modelo = input("Digite o modelo:").upper()
    marca = input("Digite a marca:").upper()
    ano = input("Digite a ano:").upper()
    cor = input("Digite a cor:").upper()
    placa = input("Digite a placa:").upper()
    km = input("Digite a km:").upper()
    
    carro = Carros(modelo = modelo, marca = marca, ano = ano, cor = cor, placa = placa, km = km)

    carros.append(carro)
    print("O carro foi cadastrado com sucesso! ")
    carro.mostrar_infos()

def buscar():
    placa = input("Digite a placa, ou TODOS para listar todos os carros: ").upper()
    for carro in carros: 
        # varivel para infirmar se a placa foi encontrada
        if carro.placa == placa or placa == "TODOS":
            carro.mostrar_infos()
            encontrada = True
        if not encontrada:
            print("Carro não encontrado!")
            buscar()

def atualizar():
    placa = input("Digite a placa do carro que deseja atualizar: ").upper()
    for carro in carros:
        if carro.placa == placa:
            carro.mostrar_infos()
            print("Digite os novos dados do carro: ")
            ano = input("Digite a ano:").upper()
            cor = input("Digite a cor:").upper()
            placa = input("Digite a placa:").upper()
            km = input("Digite a km:").upper()
    print("Atualização realizada com sucesso!")


def deletar():
    placa = input("Digite a placa do carro que deseja deletar: ").upper()
    for carro in carros:
        if carro.placa == placa:
            carros.remove(carro)
            print("Carro deletado com sucesso!")
           

print("#"*20)
print("-"*5 + "Programa de cadastro de carros iniciado com sucesso!" +  "-"*5)
print("#"*62)


while True:
    operacao = input(menu).upper()
    if operacao == 'C':
        cadastrar()
    elif operacao == 'R':
        buscar()
    elif operacao == 'U':
        atualizar()
    elif operacao == 'D':
        deletar()
    elif operacao == 'S':
        break
    else:
        print("Comando invalido!!!")


