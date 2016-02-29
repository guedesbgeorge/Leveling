############################################################
### Exercicio 2
##meses = [(1, 31), (2, 29), (3, 31), (4, 30),
##         (5, 31), (6, 30), (7, 31), (8, 31),
##         (9, 30), (10, 31), (11, 30), (12, 31)];
##
##for mes in meses:
##    for i in range(1, mes[1] + 1):
##        if i < 10:
##            print("0" + str(i) + "/", end = "")
##        else:
##            print(str(i) + "/", end = "")
##        if(mes[0] < 10):
##            print("0" + str(mes[0]))
##        else:
##            print(str(mes[0]))
#
##
# Exercicio 10
##palavras = [("carro", "Veiculo automotor"),
##            ("lampada", "Fornece luz, ilumina ambiente"),
##            ("computador", "Usado para programar")];
##
##
##tentativas = 4;
##acertou = False;
##print("Bem-vindo ao jogo da forca!")
##print("Voce pode errar até 4 vezes")
##
##for palavra in palavras:
##    acertos = [];
##    for i in range(0, len(palavra[0])):
##        acertos.append(False);
##    print("Dica: " + palavra[1] + ". A palavra tem " + str(len(palavra[0])) + " letras");
##    for i in range(0, len(palavra[0])):
##        print(" _ ", end = "");
##    print();
##    while(tentativas > 0 and (not acertou)):
##        print("Digite aqui uma letra:")
##        userTry = input();
##        if userTry in palavra[0]:
##            for i in range(0, len(palavra[0])):
##                if(userTry == palavra[0][i]):
##                    print(" " + userTry+ " ", end = "")
##                    acertos[i] = True
##                else:
##                    if(acertos[i] == True):
##                        print(" " + palavra[0][i] + " ", end = "")
##                    else:
##                        print(" _ ", end = "")
##            print();
##        else:
##            tentativas -= 1;
##            print("Voce errou! Resta(m) " + str(tentativas) + " tentativas!")
##        teste = True;
##        for i in range (0, len(acertos)):
##            teste = teste and acertos[i]
##
##        if(teste):
##            acertou = True
##
##    if(acertou == False):
##        print("Voce errou a palavra!")
##    else:
##        print("Parabens, voce acertou!")
##    tentativas = 4;
##    acertou = False;

### Exercicio 1
##user = int(input("Digite aqui um numero:\n"));
##primo = True;
##if(user == 2):
##    print(str(user) + " é primo.")
##else:
##    for i in range(2, user):
##        if(user%i == 0):
##            primo = False
##            break;
##    if(primo):
##        print(str(user) + " é primo.")
##    else:
##        print(str(user) + " nao é primo.")

### Exercicio 3
##user = int(input("Digite aqui um numero:\n"));
##primo = True;
##divisores = [];
##if(user == 2):
##    print(str(user) + " é primo.")
##else:
##    for i in range(2, user):
##        if(user%i == 0):
##            primo = False
##            divisores.append(i);
##if(primo):
##    print(str(user) + " é primo.");
##else:
##    print(str(user) + " não é primo.");
##    print("Os divisores são: ", end = "")
##    for i in range (0, len(divisores)):
##        if i == len(divisores) - 1:
##            print(divisores[i])
##        else:
##            print(str(divisores[i]) + ", ", end = "")

# Exercicio 4: feito na aula 5

# Exercicio 5: TODO

# Exercicio 6: TODO
user = int(input("Digite aqui um numero: \n"));




            



    
     
    
