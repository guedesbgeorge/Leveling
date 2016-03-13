# Banco de palavras e dicas.
palavras = [("carro", "Veiculo automotor."),
            ("lampada", "Fornece luz, ilumina o ambiente."),
            ("computador", "Usado para programar.")];


# Quantidade de tentativas permitidas.
tentativas = 4;

# Imprimindo boas vindas e instrucoes.
print("Bem-vindo ao jogo da forca!")
print("Voce pode errar até " + str(tentativas) + " vezes em cada palavra.")
print("Lembre-se das letras que voce errou para nao digita-las novamente!")
print("Vamos comecar!")

# Iniciando loop para cada palavra.
acertou = False;
for palavra in palavras:
    acertos = [];
    for i in range(0, len(palavra[0])):
        acertos.append(False);
    print("Dica: " + palavra[1] + " A palavra tem " + str(len(palavra[0])) + " letras.");
    for i in range(0, len(palavra[0])):
        print(" _ ", end = "");
    print();
    while(tentativas > 0 and (not acertou)):
        print("Digite aqui uma letra:")
        userTry = input();
        if userTry in palavra[0]:
            for i in range(0, len(palavra[0])):
                if(userTry == palavra[0][i]):
                    print(" " + userTry+ " ", end = "")
                    acertos[i] = True
                else:
                    if(acertos[i] == True):
                        print(" " + palavra[0][i] + " ", end = "")
                    else:
                        print(" _ ", end = "")
            print();
        else:
            tentativas -= 1;
            print("Voce errou! Resta(m) " + str(tentativas) + " tentativas!")
        testeFim = True;
        for i in range (0, len(acertos)):
            testeFim = testeFim and acertos[i]

        if(testeFim):
            acertou = True

    if(acertou == False):
        print("Voce errou a palavra!")
    else:
        print("Parabens, voce acertou!")

    # Resetando variaveis para o proximo loop.     
    tentativas = 4;
    acertou = False;
