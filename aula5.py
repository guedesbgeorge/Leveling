# Exercicio 1 esta no arquivo aula1_clean.py

##########################################################

### Exercicio 2
##listaDeNumeros = [];
##continuar = True;
##
##while(continuar):
##    userInput = input();
##    if(userInput != ""):
##        userInput = int(userInput);
##        listaDeNumeros.append(userInput)
##    else:
##        continuar = False
##
##count = 0;
##media = 0;
##
##while(count < len(listaDeNumeros)):
##    media = media + listaDeNumeros[count];
##    count = count + 1;
##
##media = media/len(listaDeNumeros);
##print(media)

##########################################################

### Exercicio 3
##n = int(input("Digite aqui um numero:\n"))
##
##current = 2;
##primos = [];
##
##while(current <= n):
##    if(current == 2):
##        primos.append(2);
##    else:
##        primo = True;
##        aux = 2;
##        while(primo and aux < current):
##            if(current%aux == 0):
##                primo = False
##            aux = aux + 1
##            
##        if(primo):
##            primos.append(current)
##    current = current + 1;
##
##aux = 0;
##while(aux < len(primos)):
##    print(primos[aux], end = "")
##    if(aux != len(primos) - 1):
##        print(", ", end = "")

##########################################################

# Exercicio 4
lista = [];
continuar = True;
print("Digite aqui a lista:")

while(continuar):
    userInput = input();
    if(userInput != ""):
        userInput = int(userInput);
        lista.append(userInput)
    else:
        continuar = False
lista = sorted(lista);

aux = 0;
while(aux < len(lista)):
    print(lista[aux], end = "")
    if(aux != len(lista) - 1):
        print(", ", end = "")
    aux = aux + 1;    
