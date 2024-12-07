import math
import random
import json
import time

print("BEM VINDO ao gerador de mundos e sistemas de traveller! Usando de base o core e o World Builders Handbook")

estrela_final = {}
classe_estrela = "Class V"
Tipo_estrela = ""
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
star_mass_and_temp = {
    "O0": {
        "Mass": {"Class Ia": 200, "Class Ib": 150, "Class II": 130, "Class III": 110, "Class IV": 90, "Class V": 2, "Class VI": 2},
        "Temperature": "50,000K",
        "Colour": "Blue"
    },
    "O5": {
        "Mass": {"Class Ia": 80, "Class Ib": 60, "Class II": 40, "Class III": 30, "Class IV": 20, "Class V": 1.5, "Class VI": 1.5},
        "Temperature": "40,000K",
        "Colour": "Blue White"
    },
    "B0": {
        "Mass": {"Class Ia": 60, "Class Ib": 40, "Class II": 30, "Class III": 20, "Class IV": 18, "Class V": 0.5, "Class VI": 0.5},
        "Temperature": "30,000K",
        "Colour": "Blue White"
    },
    "B5": {
        "Mass": {"Class Ia": 30, "Class Ib": 25, "Class II": 20, "Class III": 10, "Class IV": 10, "Class V": 0.4, "Class VI": 0.4},
        "Temperature": "15,000K",
        "Colour": "Blue White"
    },
    "A0": {
        "Mass": {"Class Ia": 20, "Class Ib": 15, "Class II": 14, "Class III": 8, "Class IV": 4, "Class V": 2.2, "Class VI": 2.2},
        "Temperature": "10,000K",
        "Colour": "White"
    },
    "A5": {
        "Mass": {"Class Ia": 15, "Class Ib": 13, "Class II": 11, "Class III": 6, "Class IV": 2.3, "Class V": 1.8, "Class VI": 1.8},
        "Temperature": "8,000K",
        "Colour": "White"
    },
    "F0": {
        "Mass": {"Class Ia": 13, "Class Ib": 12, "Class II": 10, "Class III": 4, "Class IV": 2, "Class V": 1.5, "Class VI": 1.5},
        "Temperature": "7,500K",
        "Colour": "Yellow White"
    },
    "F5": {
        "Mass": {"Class Ia": 12, "Class Ib": 10, "Class II": 8, "Class III": 3, "Class IV": 1.5, "Class V": 1.3, "Class VI": 1.3},
        "Temperature": "6,500K",
        "Colour": "Yellow White"
    },
    "G0": {
        "Mass": {"Class Ia": 12, "Class Ib": 10, "Class II": 8, "Class III": 2.5, "Class IV": 1.7, "Class V": 1.1, "Class VI": 0.8},
        "Temperature": "6,000K",
        "Colour": "Yellow"
    },
    "G5": {
        "Mass": {"Class Ia": 13, "Class Ib": 11, "Class II": 10, "Class III": 2.4, "Class IV": 1.2, "Class V": 0.9, "Class VI": 0.7},
        "Temperature": "5,600K",
        "Colour": "Yellow"
    },
    "K0": {
        "Mass": {"Class Ia": 14, "Class Ib": 12, "Class II": 10, "Class III": 1.1, "Class IV": 1.5, "Class V": 0.8, "Class VI": 0.6},
        "Temperature": "5,200K",
        "Colour": "Light Orange"
    },
    "K5": {
        "Mass": {"Class Ia": 18, "Class Ib": 13, "Class II": 12, "Class III": 1.5, "Class IV": 0.7, "Class V": 0.5, "Class VI": 0.4},
        "Temperature": "4,400K",
        "Colour": "Orange Red"
    },
    "M0": {
        "Mass": {"Class Ia": 20, "Class Ib": 15, "Class II": 14, "Class III": 2, "Class IV": 0.5, "Class V": 0.5, "Class VI": 0.4},
        "Temperature": "3,700K",
        "Colour": "Orange Red"
    },
    "M5": {
        "Mass": {"Class Ia": 25, "Class Ib": 20, "Class II": 16, "Class III": 2.4, "Class IV": 0.16, "Class V": 0.12, "Class VI": 0.12},
        "Temperature": "3,000K",
        "Colour": "Orange Red"
    },
    "M9": {
        "Mass": {"Class Ia": 30, "Class Ib": 25, "Class II": 18, "Class III": 8, "Class IV": 0.08, "Class V": 0.075, "Class VI": 0.075},
        "Temperature": "2,400K",
        "Colour": "Orange Red"
    }
}
star_diameter = {
    "O0": {
        "Diameter": {"Class Ia": 25, "Class Ib": 24, "Class II": 22, "Class III": 21, "Class IV": 20, "Class V": 20, "Class VI": 0.18}
    },
    "O5": {
        "Diameter": {"Class Ia": 22, "Class Ib": 21, "Class II": 18, "Class III": 15, "Class IV": 12, "Class V": 12, "Class VI": 0.18}
    },
    "B0": {
        "Diameter": {"Class Ia": 20, "Class Ib": 14, "Class II": 12, "Class III": 10, "Class IV": 8, "Class V": 7, "Class VI": 0.2}
    },
    "B5": {
        "Diameter": {"Class Ia": 60, "Class Ib": 25, "Class II": 14, "Class III": 6, "Class IV": 5, "Class V": 3.5, "Class VI": 0.5}
    },
    "A0": {
        "Diameter": {"Class Ia": 120, "Class Ib": 50, "Class II": 25, "Class III": 10, "Class IV": 8, "Class V": 4, "Class VI": 2.2}
    },
    "A5": {
        "Diameter": {"Class Ia": 180, "Class Ib": 75, "Class II": 45, "Class III": 5, "Class IV": 3, "Class V": 2, "Class VI": None}
    },
    "F0": {
        "Diameter": {"Class Ia": 210, "Class Ib": 85, "Class II": 50, "Class III": 5, "Class IV": 3, "Class V": 1.7, "Class VI": None}
    },
    "F5": {
        "Diameter": {"Class Ia": 280, "Class Ib": 115, "Class II": 66, "Class III": 5, "Class IV": 2, "Class V": 1.5, "Class VI": None}
    },
    "G0": {
        "Diameter": {"Class Ia": 330, "Class Ib": 135, "Class II": 77, "Class III": 10, "Class IV": 3, "Class V": 1.1, "Class VI": 0.8}
    },
    "G5": {
        "Diameter": {"Class Ia": 360, "Class Ib": 150, "Class II": 80, "Class III": 10, "Class IV": 2.4, "Class V": 0.95, "Class VI": 0.7}
    },
    "K0": {
        "Diameter": {"Class Ia": 420, "Class Ib": 180, "Class II": 110, "Class III": 20, "Class IV": 6, "Class V": 0.9, "Class VI": 0.6}
    },
    "K5": {
        "Diameter": {"Class Ia": 600, "Class Ib": 260, "Class II": 160, "Class III": 40, "Class IV": 8, "Class V": 0.8, "Class VI": 0.5}
    },
    "M0": {
        "Diameter": {"Class Ia": 900, "Class Ib": 380, "Class II": 230, "Class III": 60, "Class IV": 7, "Class V": 0.7, "Class VI": 0.4}
    },
    "M5": {
        "Diameter": {"Class Ia": 1_200, "Class Ib": 600, "Class II": 350, "Class III": 100, "Class IV": None, "Class V": 0.2, "Class VI": 0.1}
    },
    "M9": {
        "Diameter": {"Class Ia": 1_800, "Class Ib": 800, "Class II": 500, "Class III": 200, "Class IV": None, "Class V": 0.1, "Class VI": 0.08}
    }
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
    print("Calculando Subtype...")
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

