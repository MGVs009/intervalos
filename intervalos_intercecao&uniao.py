import tkinter as tk
import math 
root = tk.Tk()
root.title("Intervalos")
root.geometry("960x540")

inputtxt = tk.Text(root, height=1, width=3)
inputtxt.pack(pady=100)

Pergunta = "O teu primeiro intervalo comeca com [ ou ] ?"
lbl = tk.Label(root, text=Pergunta)
lbl.pack()

btn = tk.Button(root, text="Submeter")
btn.pack()

FOA_I1 = False
FOA_F1 = False

estado = 0

def passo():
    global estado, Pergunta, input_II, a1, b1, input_FI, input_2I, a2, b2, input_F2
    global FOA_I1, FOA_F1, FOA_I2, FOA_F2, Intervalo1, Intervalo2
    global Todos_Intervalo1, Todos_Intervalo2, dic_intervalo

    entrada = inputtxt.get("1.0", "end-1c").strip()
    inputtxt.delete("1.0", "end")

    if estado == 0:
        input_II = entrada
        if input_II == "]":
            FOA_I1 = True
        else:
            FOA_I1 = False
        Pergunta = "OKAY!, O teu intervalo comeca em que numero?"
        lbl.config(text=Pergunta)

    elif estado == 1:
        a1 = int(entrada)
        Pergunta = "Fixe!, O teu intervalo acaba em que numero?"
        lbl.config(text=Pergunta)

    elif estado == 2:
        b1 = int(entrada)
        Pergunta = "O teu primeiro intervalo acaba com [ ou ] ?"
        lbl.config(text=Pergunta)

    elif estado == 3:
        input_FI = entrada
        if input_FI == "]":
            FOA_F1 = False
        else:
            FOA_F1 = True
        Pergunta = "O teu segundo intervalo comeca com [ ou ] ?"
        lbl.config(text=Pergunta)

    elif estado == 4:
        input_2I = entrada
        if input_2I == "]":
            FOA_I2 = True
        else:
            FOA_I2 = False
        Pergunta = "OKAY!, O teu segundo intervalo comeca em que numero?"
        lbl.config(text=Pergunta)

    elif estado == 5:
        a2 = int(entrada)
        Pergunta = "Fixe!, O teu segundo intervalo acaba em que numero?"
        lbl.config(text=Pergunta)

    elif estado == 6:
        b2 = int(entrada)
        Pergunta = "O teu segundo intervalo acaba com [ ou ] ?"
        lbl.config(text=Pergunta)

    elif estado == 7:
        input_F2 = entrada
        if input_F2 == "]":
            FOA_F2 = False
        else:
            FOA_F2 = True

        Intervalo1 = f"{input_II}{a1},{b1}{input_FI}"
        if FOA_I1:
            a1 += 1
        if FOA_F1:
            b1 -= 1
        dic_intervalo = {a1, b1}

        Intervalo2 = f"{input_2I}{a2},{b2}{input_F2}"
        if FOA_I2:
            a2 += 1
        if FOA_F2:
            b2 -= 1

        Todos_Intervalo1 = set()
        Todos_Intervalo2 = set()

        for i1 in range(a1, b1 + 1):
            Todos_Intervalo1.add(i1)

        for i2 in range(a2, b2 + 1):
            Todos_Intervalo2.add(i2)

        print(Intervalo1)
        print(Intervalo2)

        inter = sorted(Todos_Intervalo1.intersection(Todos_Intervalo2))
        #Removido porque está a dar erro # uni = sorted(Todos_Intervalo1.union(Todos_Intervalo2))

        resultado = f"{Intervalo1}\n{Intervalo2}\nInterseção: {inter}" #\nUnião: {uni}
        lbl.config(text=resultado)

        return

    estado += 1

btn.config(command=passo)
root.bind("<Return>", lambda event: btn.invoke())

root.mainloop()

