# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
    
def arriscar(*args):
    try:
        word = palavra.get();
        palpite = userGuess.get();
        global corrente
        if(palpite in word):
            tkinter.messagebox.showinfo("", "Acertou!")
            aux = True;
            corrente = ""
            for i in range (0, len(word)):
                if palpite == word[i]:
                    check[i] = True
                aux = aux and check[i]
                if(check[i]):
                    corrente = corrente + " " + word[i] + " "
                else:
                    corrente = corrente + " _ "
            global label
            label.config(text=corrente, font = "Times 40");
            label.update_idletasks()
            if(aux):
                tkinter.messagebox.showinfo("", "Parabéns, você acertou a palavra!")
                root.destroy()
        else:
            tkinter.messagebox.showinfo("", "A palavra não contém essa letra!")
            global tentativas
            tentativas = tentativas + 1
            global w, img
            img = PhotoImage(file="img/f" + str(tentativas + 1) + ".gif")
            w.create_image(0,0, anchor=NW, image=img)
            w.update_idletasks()
            if(tentativas == 4):
                tkinter.messagebox.showinfo("", "Você perdeu! A palavra era '" + word + "'!")
                root.destroy()
            else:
                tkinter.messagebox.showinfo("", "Resta(m) " + str(4 - tentativas) + " tentativas")
    except ValueError:
        pass
    
def cadastrar(*args):
    ttk.Label(mainframe, text="Dica: " + dica.get(), font = "Times 16 bold").grid(row=29, sticky=W)
    global corrente, check
    for i in range(0, len(palavra.get())):
        corrente = corrente + " _ "
        check.append(False);
    global label
    label = ttk.Label(mainframe, text=corrente, font = "Times 40")
    label.grid(column = 3, row=30, sticky=W)
    dica_entry.delete(0, 'end');

# Iniciando
root = Tk()
root.title("Jogo da forca")

# Declarando variaveis globais
corrente = ""
check = [];
tentativas = 0;

# Configurando o frame principal
mainframe = ttk.Frame(root, padding="18 18 72 72")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Campos de entrada
palavra = StringVar()
palavra_entry = ttk.Entry(mainframe, width=7, textvariable=palavra, show="*")
palavra_entry.grid(column=10, row=1, sticky=(W, E))

dica = StringVar()
dica_entry = ttk.Entry(mainframe, width=7, textvariable=dica)
dica_entry.grid(column=10, row=2, sticky=(W, E))

userGuess = StringVar();
userGuess_entry = ttk.Entry(mainframe, width=7, textvariable=userGuess)
userGuess_entry.grid(column=10, row=7, sticky=(W, E))

# Botoes
ttk.Button(mainframe, text="Arriscar", command=arriscar).grid(column=12, row=7, sticky=W)
ttk.Button(mainframe, text="Ok", command=cadastrar).grid(column=12, row=2, sticky=W)

# Labels
ttk.Label(mainframe, text="Jogador 1, digite aqui a palavra a ser advinhada:").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Jogador 1, digite aqui a dica:").grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Jogador 2, digite aqui o seu palpite:").grid(column=0, row=7, sticky=W)

# Canvas
canvas_width = 275
canvas_height = 372
w = Canvas(mainframe,width=canvas_width,height=canvas_height)
w.grid(column =30, row = 25)
img = PhotoImage(file="img/f1.gif")
w.create_image(0,0, anchor=NW, image=img)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mainloop();
