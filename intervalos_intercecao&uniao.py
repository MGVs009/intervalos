import tkinter as tk

FOA_I1 = False
FOA_F1 = False

print("O teu primeiro intervalo comeca com", "[", "ou", "]", "?")
input_II = str(input())

if input_II == "]":
    FOA_I1 = True
else:
    FOA_I1 = False

print("OKAY!, O teu intervalo comeca em que numero?")
a1 = int(input())

print("Fixe!, O teu intervalo acaba em que numero?")
b1 = int(input())

print("O teu primeiro intervalo acaba com", "[", "ou", "]", "?")
input_FI = str(input())

if input_FI == "]":
    FOA_F1 = False
else:
    FOA_F1 = True

Intervalo1 = f"{input_II}{a1},{b1}{input_FI}"

if FOA_I1 == True:
    a1 += 1

if FOA_F1 == True:
    b1 -= 1

dic_intervalo = {a1, b1}

print("O teu segundo intervalo comeca com", "[", "ou", "]", "?")
input_2I = str(input())

if input_2I == "]":
    FOA_I2 = True
else:
    FOA_I2 = False

print("OKAY!, O teu segundo intervalo comeca em que numero?")
a2 = int(input())

print("Fixe!, O teu segundo intervalo acaba em que numero?")
b2 = int(input())

print("O teu segundo intervalo acaba com", "[", "ou", "]", "?")
input_F2 = str(input())

if input_F2 == "]":
    FOA_F2 = False
else:
    FOA_F2 = True

Intervalo2 = f"{input_2I}{a2},{b2}{input_F2}"

if FOA_I2 == True:
    a2 += 1

if FOA_F2 == True:
    b2 -= 1

Todos_Intervalo1 = set()
Todos_Intervalo2 = set()

for i1 in range(a1, b1 + 1):
    Todos_Intervalo1.add(i1)

for i2 in range(a2, b2 + 1):
    Todos_Intervalo2.add(i2)

print(Intervalo1)
print(Intervalo2)

def intercecao():
    print(sorted(Todos_Intervalo1.intersection(Todos_Intervalo2)))

def uniao():
    print(sorted(Todos_Intervalo1.union(Todos_Intervalo2)))

