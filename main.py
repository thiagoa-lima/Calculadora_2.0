from tkinter import *
import datetime

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
tela_principal = ""
tela_equacao = ""
memoria = ""
memoria_01 = 0
cont_clique_resultado = 0
total = 0
operador = ""

# label
valores = StringVar()
equacao = StringVar()

# função
def novos_valores(event):
    global tela_principal
    global cont_clique_resultado

    tela_principal = str(tela_principal) + str(event)
    # passando valor para a tela
    valores.set(tela_principal)

    cont_clique_resultado = 0

def limpa_ultimo_digito():
    global tela_principal
    global cont_clique_resultado

    tela_principal = tela_principal[:-1]

    valores.set(tela_principal)

    cont_clique_resultado = 0

def limpar_tela_principal():
    global tela_principal
    global memoria
    global cont_clique_resultado

    tela_principal = ""
    memoria = ""
    valores.set("")

    cont_clique_resultado = 0

def limpar_tudo():
    global tela_principal
    global memoria
    global cont_clique_resultado

    tela_principal = ""
    memoria = ""
    valores.set("")
    equacao.set("")

    cont_clique_resultado = 0

def operadores_matematicos(event):
    global tela_principal
    global tela_equacao
    global memoria
    global cont_clique_resultado
    global operador
    global total
    global memoria_01

    tela_equacao = str(memoria) + str(tela_principal) + str(event)
    equacao.set(tela_equacao)

    memoria = tela_equacao
    tela_principal = ""

    operador = str(event)

    cont_clique_resultado = 0
    print(tela_equacao)

    tela_equacao = str(memoria) + str(tela_principal)

def percentual():
    global tela_principal
    global tela_equacao
    global memoria
    global cont_clique_resultado

    tela_principal = float(tela_principal)/100
    tela_principal = round(tela_principal, 6)
    valores.set(tela_principal)

    equacao.set(tela_equacao)

    cont_clique_resultado = 0

def resultado():
    global tela_equacao
    global tela_principal
    global memoria
    global cont_clique_resultado
    global total
    global memoria_01

    if cont_clique_resultado == 0:
        tela_equacao = str(memoria) + str(tela_principal)
        total = eval(tela_equacao)
        total = round(total, 6)

        tela_equacao = str(memoria) + str(tela_principal) + " ="
        equacao.set(tela_equacao)

        valores.set(total)
        memoria_01 = tela_principal

        tela_principal = ""
        memoria = total

        cont_clique_resultado += 1

    else:
        tela_equacao = str(memoria) + str(operador) + str(memoria_01)
        total = eval(tela_equacao)
        valores.set(total)

        tela_equacao = str(memoria) + str(operador) + str(memoria_01) + " ="
        equacao.set(tela_equacao)

        memoria = total

        cont_clique_resultado += 1


label_01 = Label(janela, text="Meu primeiro projeto em tKinter", font="Abadi 9", fg="#000066", pady=5)
label_01.place(x=50, y=0)

label_02 = Label(janela, textvariable=valores, font="Abadi 31 bold", fg="#404040", bd=1, relief="flat", width=13, height=1, anchor=E, pady=2,padx=7)
label_02.place(x=50, y=57)

label_03 = Label(janela, textvariable=equacao, font="Abadi 12", fg="#404040", relief="flat", width=35, height=1, anchor=E, padx=12)
label_03.place(x=50, y=33)

# label com borda
# label_02_border = Frame(janela, background=azul)
# label_02 = Label(label_02_border, textvariable=valores, font="Abadi 20 bold", bd=1, fg="#404040", relief="solid", width=24, height=2, anchor=E, padx=20)
# label_02.pack(padx=1, pady=1)
# label_02_border.place(x=50, y=30)

btn_00 = Button(janela, command=limpa_ultimo_digito, text="⟸", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_00.place(x=400, y=56)

# Primeira Fileira
btn_01 = Button(janela, command=lambda: novos_valores("7"), text="7", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_01.place(x=50, y=120)
btn_02 = Button(janela, command=lambda: novos_valores("8"), text="8", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_02.place(x=136, y=120)
btn_03 = Button(janela, command=lambda: novos_valores("9"), text="9", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_03.place(x=222, y=120)
btn_04 = Button(janela, command=lambda: operadores_matematicos(" * "), text="x", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_04.place(x=314, y=120)
btn_05 = Button(janela, command=limpar_tela_principal, text="C", font="Abadi 20 bold", bg=vermelho, fg="#000066", relief="groove", width=4, height=1)
btn_05.place(x=400, y=120)

# Segunda Fileira
btn_06 = Button(janela, command=lambda: novos_valores("4"), text="4", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_06.place(x=50, y=184)
btn_07 = Button(janela, command=lambda: novos_valores("5"), text="5", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_07.place(x=136, y=184)
btn_08 = Button(janela, command=lambda: novos_valores("6"), text="6", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_08.place(x=222, y=184)
btn_09 = Button(janela, command=lambda: operadores_matematicos(" / "), text="/", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_09.place(x=314, y=184)
btn_10 = Button(janela, command=limpar_tudo, text="CE", font="Abadi 20 bold", bg=azul, fg="#000066", relief="groove", width=4, height=1)
btn_10.place(x=400, y=184)

# Terceira Fileira
btn_10 = Button(janela, command=lambda: novos_valores("1"), text="1", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_10.place(x=50, y=248)
btn_11 = Button(janela, command=lambda: novos_valores("2"), text="2", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_11.place(x=136, y=248)
btn_12 = Button(janela, command=lambda: novos_valores("3"), text="3", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_12.place(x=222, y=248)
btn_13 = Button(janela, command=lambda: operadores_matematicos(" - "), text="-", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_13.place(x=314, y=248)
btn_14 = Button(janela, command=lambda: operadores_matematicos(" + "), text="+", font="Abadi 20 bold", bg=verde, fg="#000066", relief="groove", width=4, height=1)
btn_14.place(x=314, y=312)
btn_15 = Button(janela, command=percentual, text="%", font="Abadi 20 bold", bg=verde, fg="#000066", relief="groove", width=4, height=1)
btn_15.place(x=400, y=248)

# Quarta Fileira
btn_16 = Button(janela, command=lambda: novos_valores("0"), text="0", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=9, height=1)
btn_16.place(x=50, y=312)
btn_17 = Button(janela, command=lambda: novos_valores("."), text=".", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_17.place(x=222, y=312)
btn_18 = Button(janela, command=lambda: operadores_matematicos(" + "), text="+", font="Abadi 20 bold", bg=cinza, fg="#000066", relief="groove", width=4, height=1)
btn_18.place(x=314, y=312)
btn_19 = Button(janela, command=resultado, text="=", font="Abadi 20 bold", bg=amarelo, fg="#000066", relief="groove", width=4, height=1)
btn_19.place(x=400, y=312)

janela.mainloop()
