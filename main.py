from tkinter import *

janela = Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela.geometry("520x400")

# Cores
vermelho = "#ff9999"
cinza = "#e6e6ff"
azul = "#9999ff"
verde = "#99ff99"
amarelo = "#ffff99"


# variável todos os valores
todos_valores = ""

# label
valores = StringVar()

# função
def novos_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # passando valor para a tela
    valores.set(todos_valores)

def limpar_valor():
    global todos_valores
    todos_valores = ""
    valores.set("")

def resultado():
    global todos_valores
    resultado = eval(todos_valores)
    valores.set(str(resultado))
    todos_valores = ""

def percentual():
    global todos_valores
    percentual = eval(todos_valores)/100
    valores.set(str(percentual))
    todos_valores = ""


label_01 = Label(janela, text="Meu primeiro projeto em tKinter", font="Abadi 9", fg="#000066", pady=5)
label_01.place(x=50, y=8)

label_02_border = Frame(janela, background=azul)
label_02 = Label(label_02_border, textvariable=valores, font="Abadi 20", bd=1, fg="#404040", relief="solid", width=24, height=2, anchor=E, padx=20)
label_02.pack(padx=1, pady=1)
label_02_border.place(x=50, y=30)

# Primeira Fileira
btn_01 = Button(janela, command=lambda: novos_valores("7"), text="7", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_01.place(x=50, y=120)
btn_02 = Button(janela, command=lambda: novos_valores("8"), text="8", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_02.place(x=136, y=120)
btn_03 = Button(janela, command=lambda: novos_valores("9"), text="9", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_03.place(x=222, y=120)
btn_04 = Button(janela, command=percentual, text="%", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_04.place(x=314, y=120)
btn_04 = Button(janela, command=limpar_valor, text="C", font="Abadi 20 bold", bg=vermelho, fg="#000066", relief="groove", width=4, height=1)
btn_04.place(x=400, y=120)

# Segunda Fileira
btn_05 = Button(janela, command=lambda: novos_valores("4"), text="4", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_05.place(x=50, y=184)
btn_06 = Button(janela, command=lambda: novos_valores("5"), text="5", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_06.place(x=136, y=184)
btn_07 = Button(janela, command=lambda: novos_valores("6"), text="6", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_07.place(x=222, y=184)
btn_08 = Button(janela, command=lambda: novos_valores("/"), text="/", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_08.place(x=314, y=184)
btn_09 = Button(janela, command=lambda: novos_valores("*"), text="*", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_09.place(x=400, y=184)

# Terceira Fileira
btn_10 = Button(janela, command=lambda: novos_valores("1"), text="1", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_10.place(x=50, y=248)
btn_11 = Button(janela, command=lambda: novos_valores("2"), text="2", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_11.place(x=136, y=248)
btn_12 = Button(janela, command=lambda: novos_valores("3"), text="3", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_12.place(x=222, y=248)
btn_13 = Button(janela, command=lambda: novos_valores("-"), text="-", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_13.place(x=314, y=248)
btn_14 = Button(janela, command=lambda: novos_valores("+"), text="+", font="Abadi 20 bold", bg=verde, fg="#000066", relief="groove", width=4, height=3)
btn_14.place(x=400, y=248)

# Quarta Fileira
btn_15 = Button(janela, command=lambda: novos_valores("0"), text="0", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=9, height=1)
btn_15.place(x=50, y=312)
btn_16 = Button(janela, command=lambda: novos_valores("."), text=".", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_16.place(x=222, y=312)
btn_17 = Button(janela, command=resultado, text="=", font="Abadi 20 bold", bg=amarelo, fg="#000066", relief="groove", width=4, height=1)
btn_17.place(x=314, y=312)

janela.mainloop()
