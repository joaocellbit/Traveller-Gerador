import math
import random

star_types = {
    2: {"Type": "Special", "Hot": "A", "Special": "Class VI", "Unusual": "Peculiar", "Giants": "Class III", "Peculiar": "Black Hole"},
    3: {"Type": "M", "Hot": "A", "Special": "Class VI", "Unusual": "Class VI", "Giants": "Class III", "Peculiar": "Pulsar"},
    4: {"Type": "M", "Hot": "A", "Special": "Class VI", "Unusual": "Class IV", "Giants": "Class III", "Peculiar": "Neutron Star"},
    5: {"Type": "M", "Hot": "A", "Special": "Class VI", "Unusual": "BD", "Giants": "Class III", "Peculiar": "Nebula"},
    6: {"Type": "M", "Hot": "A", "Special": "Class IV", "Unusual": "BD", "Giants": "Class III", "Peculiar": "Nebula"},
    7: {"Type": "K", "Hot": "A", "Special": "Class IV", "Unusual": "BD", "Giants": "Class III", "Peculiar": "Protostar"},
    8: {"Type": "K", "Hot": "A", "Special": "Class IV", "Unusual": "D", "Giants": "Class III", "Peculiar": "Protostar"},
    9: {"Type": "G", "Hot": "A", "Special": "Class III", "Unusual": "D", "Giants": "Class II", "Peculiar": "Protostar"},
    10: {"Type": "G", "Hot": "B", "Special": "Class III", "Unusual": "D", "Giants": "Class II", "Peculiar": "Star Cluster"},
    11: {"Type": "F", "Hot": "B", "Special": "Giants", "Unusual": "Class III", "Giants": "Class Ib", "Peculiar": "Anomaly"},
    12: {"Type": "Hot", "Hot": "O", "Special": "Giants", "Unusual": "Giants", "Giants": "Class Ia", "Peculiar": "Anomaly"},
}

print("BEM VINDO ao gerador de mundos e sistemas de traveller! Usando de base o core e o World Builders Handbook")
usuario = input("pronto pra começar? y pra sim, n pra nao ")

def roll_2d():
    return random.randint(1, 6) + random.randint(1, 6)

def Greador():
    print("gerando estrela...")
    dado = roll_2d()
    print(f"Rolagem inicial: {dado}")
    
    estrela = star_types[dado]
    if dado <= 2:
        print("sistema especial!")
        dado = roll_2d()
        estrela_especial = star_types[dado]
        print(f"a estrela especial é {estrela_especial['Special']}")
        dado = roll_2d() + 1
        if  estrela_especial['Special'] ==  "Class IV" and 3 <= dado <= 6:
            dado = dado + 5
        else:
            estrela = star_types[dado]
            if  estrela_especial['Special'] ==  "Class VI" and estrela['Type'] == "F":
                estrela['Type'] = "G"
            print(f"Estrela do tipo: {estrela['Type']} {estrela_especial['Special']}")
        if dado >= 12:
            print("HOT!")
            dado = roll_2d()
            estrela = star_types[dado]
            if  estrela_especial['Special'] ==  "Class VI" and estrela['HOT'] == "A" :
                estrela['HOT'] = "B"
            print(f"Estrela do tipo: {estrela['Hot']} {estrela_especial['Special']}")
    elif dado >= 12:
        print("HOT!")
        dado = roll_2d()
        estrela = star_types[dado]
        print(f"Estrela do tipo: {estrela['Hot']}")
    else:
        print(f"Estrela do tipo: {estrela['Type']}")

if usuario == "y":
    Greador()
else:
    print("q pena :C")