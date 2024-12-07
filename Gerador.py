import math
import random
import json
import time

print("BEM VINDO ao gerador de mundos e sistemas de traveller! Usando de base o core e o World Builders Handbook")

estrela_final = {}
classe_estrela = "Class V"
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
star_subtype = {
    2: {"Numeric": 0, "M-type": 8},
    3: {"Numeric": 1, "M-type": 6},
    4: {"Numeric": 3, "M-type": 5},
    5: {"Numeric": 5, "M-type": 4},
    6: {"Numeric": 7, "M-type": 0},
    7: {"Numeric": 9, "M-type": 2},
    8: {"Numeric": 8, "M-type": 1},
    9: {"Numeric": 6, "M-type": 3},
    10: {"Numeric": 4, "M-type": 5},
    11: {"Numeric": 2, "M-type": 7},
    12: {"Numeric": 0, "M-type": 9},
}

def roll_2d():
    return random.randint(1, 6) + random.randint(1, 6)

def Gerador():
    print("gerando estrela...")
    dado = roll_2d()
    global classe_estrela
    print(f"Rolagem inicial: {dado}")
    estrela = star_types[dado]
    if dado <= 2:
        print("sistema especial!")
        dado = roll_2d()
        estrela_especial = star_types[dado]
        print(f"a estrela especial é {estrela_especial['Special']}")
        dado = roll_2d() + 1
        if estrela_especial['Special'] == "Giants":
            estrela = star_types[dado]
            dado = roll_2d() + 1
            estrela_especial = star_types[dado]
            classe_estrela = estrela_especial['Giants']
            print(f"Estrela do tipo: {estrela['Type']} {estrela_especial['Giants']}")  
        elif  estrela_especial['Special'] ==  "Class IV" and 3 <= dado <= 6:
            dado = dado + 5
            estrela = star_types[dado]
            print(f"Estrela do tipo: {estrela['Type']} {estrela_especial['Special']}")
            classe_estrela = estrela_especial['Special']
        elif dado >= 12:
            print("HOT!")
            dado = roll_2d()
            estrela = star_types[dado]
            if  estrela_especial['Special'] ==  "Class IV" and estrela['HOT'] == "O" :
                estrela['HOT'] = "B"

            if  estrela_especial['Special'] ==  "Class VI" and estrela['HOT'] == "A" :
                estrela['HOT'] = "B"
            print(f"Estrela do tipo: {estrela['Hot']} {estrela_especial['Special']}")
            estrela["Type"] = estrela['Hot']
            classe_estrela = estrela_especial['Special']
        else:
            estrela = star_types[dado]
            if  estrela_especial['Special'] ==  "Class VI" and estrela['Type'] == "F":
                estrela['Type'] = "G"
            print(f"Estrela do tipo: {estrela['Type']} {estrela_especial['Special']}")
            classe_estrela = estrela_especial['Special']
            
    elif dado >= 12:
        print("HOT!")
        dado = roll_2d()
        estrela = star_types[dado]
        print(f"Estrela do tipo: {estrela['Hot']}")
        estrela["Type"] = estrela['Hot']
    else:
        print(f"Estrela do tipo: {estrela['Type']}")
    print("Clculando Subtype...")
    dado = roll_2d()
    print("dado subtype: ",dado)
    sub_tipo = star_subtype[dado]
    if estrela["Type"] == "M":
        print(f"sua estrela é {estrela['Type']}{sub_tipo['M-type']} {classe_estrela}")
        estrela_final.update({"Type":estrela['Type'], "Subtype":sub_tipo['M-type'],"Class": classe_estrela})
    elif estrela["Type"] == "K" and sub_tipo['Numeric'] > 4 and classe_estrela == "Class IV":
        sub_tipo['Numeric'] = sub_tipo['Numeric'] - 5
        print(f"sua estrela é {estrela['Type']}{sub_tipo['Numeric']} {classe_estrela}")
        estrela_final.update({"Type":estrela['Type'], "Subtype":sub_tipo['Numeric'],"Class": classe_estrela})
    else:
        print(f"sua estrela é {estrela['Type']}{sub_tipo['Numeric']} {classe_estrela}")
        estrela_final.update({"Type":estrela['Type'], "Subtype":sub_tipo['Numeric'],"Class": classe_estrela})



Gerador()
print(estrela_final)

