from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import warnings
    
def test(*args):
    try:
        if(int(userNumber1.get()) < int(userNumber2.get())):
            value1 = int(userNumber1.get());
            value2 = int(userNumber2.get());
        else:
            value1 = int(userNumber2.get());
            value2 = int(userNumber1.get());
        guess = int(userGuess.get())
        if(guess == value1 or guess == value2):
            tkinter.messagebox.showinfo("", "Acertou!")
            root.destroy()
        elif(guess > value2):
            tkinter.messagebox.showinfo("", "Seu palpite é maior do que o maior dos números!")
            global tentativas;
            tentativas = tentativas - 1
            if(tentativas == 0):
                tkinter.messagebox.showinfo("", "Você perdeu!")
                root.destroy()
            else:
                tkinter.messagebox.showinfo("", "Resta(m) " + str(tentativas) + " tentativas")
        elif(guess < value1):
            tkinter.messagebox.showinfo("", "Seu palpite é menor do que o menor dos números!")
            global tentativas;
            tentativas = tentativas - 1
            if(tentativas == 0):
                tkinter.messagebox.showinfo("", "Você perdeu!")
                root.destroy()
            else:
                tkinter.messagebox.showinfo("", "Resta(m) " + str(tentativas) + " tentativas")
        else:
            tkinter.messagebox.showinfo("", "Seu palpite está entre os números!")
            global tentativas;
            tentativas = tentativas - 1
            if(tentativas == 0):
                tkinter.messagebox.showinfo("", "Você perdeu!")
                root.destroy()
            else:
                tkinter.messagebox.showinfo("", "Resta(m) " + str(tentativas) + " tentativas")
    except ValueError:
        pass

root = Tk()
root.title("Jogo da adivinhação")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

global tentativas;
tentativas = 3;

userNumber1 = StringVar()
userNumber1_entry = ttk.Entry(mainframe, width=7, textvariable=userNumber1, show="*")
userNumber1_entry.grid(column=10, row=1, sticky=(W, E))

userNumber2 = StringVar()
userNumber2_entry = ttk.Entry(mainframe, width=7, textvariable=userNumber2, show="*")
userNumber2_entry.grid(column=10, row=2, sticky=(W, E))

userGuess = StringVar();
userGuess_entry = ttk.Entry(mainframe, width=7, textvariable=userGuess)
userGuess_entry.grid(column=10, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Advinhar", command=test).grid(column=10, row=4, sticky=W)

ttk.Label(mainframe, text="Jogador 1, digite aqui o primeiro número a ser advinhado:").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Jogador 1, digite aqui o segundo número a ser advinhado:").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Jogador 2, digite aqui o seu palpite:").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

mainloop();


