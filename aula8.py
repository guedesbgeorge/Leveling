# -*- coding: utf-8 -*-
lista = [];
valor = raw_input()
while(valor != ""):
	lista.append(int(valor))
	valor = raw_input()

lista = sorted(lista)
print(lista[len(lista) - 1])
