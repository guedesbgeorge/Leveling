# Exercicio 12
# Jogo de advinhacao
# Mensagem de explicacao
print("Bem-vindo ao jogo da advinhacao.\n",
      "Ao inicio de cada rodada, o primeiro jogador deve digitar um numero e em seguida",
      "o segundo jogador tera 3 tentativas para advinhar.\n A cada tentativa, será",
      "informado se o palpite é menor, maior ou igual ao numero correto. \n",
      "O jogo continuará infinitamente até que o jogador 1 digite 'fim'\n",
      "Vamos comecar!\n\n");

# Inicio do jogo
continuar = True;
while(continuar):
    # Pega a entrada do jogador 1
    print("Jogador 1, digite dois numeros entre 0 e 100 ou digite 'fim' caso queira encerrar o jogo.")
    jogador1Entrada1 = input();
    # Procede para a execucao de uma rodada
    if(jogador1Entrada1 != "fim"):
        jogador1Entrada1 = int(jogador1Entrada1);
        if(jogador1Entrada1 < 0 or jogador1Entrada1 > 100): # Exercicio 1
            print("Numero invalido.");
            break;
        jogador1Entrada2 = int(input()); # Exercicio 3
        if(jogador1Entrada2 < 0 or jogador1Entrada2 > 100):
            print("Numero invalido.");
            break;
        # Some o numero digitado da tela
        for i in range(0, 40):
            print("\n")

        i = 1;
        acertou = False; # Exercicio 2
        # 3 tentativas para o jogador 2
        limiteAceitavel = 20;
        while(i <=3 and (not acertou)):
            print("Jogador 2, essa é sua", i, "tentativa. Qual o numero que o jogador 1 escolheu?");
            jogador2Entrada = int(input());
            if(jogador2Entrada != jogador1Entrada1 and jogador2Entrada != jogador1Entrada2):
                if(jogador1Entrada1 > jogador1Entrada2):
                    maior = jogador1Entrada1;
                    menor = jogador1Entrada2;
                else:
                    maior = jogador1Entrada2;
                    menor = jogador1Entrada1;

                if(jogador2Entrada > maior):
                    print("Seu palpite é maior que o maior dos numeros.")
                    if(abs(jogador2Entrada - maior) > limiteAceitavel): # Exercicio 4
                        print("Seu numero esta muito longe do maior numero! =/")
                        break;
                elif(jogador2Entrada < menor):
                    print("Seu palpite é menor que o menor dos numeros.")
                    if(abs(jogador2Entrada - menor) > limiteAceitavel):
                        print("Seu numero esta muito longe do menor numero! =/")
                        break;
                else:
                    print("Seu palpite esta entre os numeros.")
                    if(abs(jogador2Entrada - maior) > limiteAceitavel or abs(jogador2Entrada - menor) > limiteAceitavel):
                        print("Seu palpite esta muito longe dos numeros!")
                        break;
            else:
                acertou = True;
                print("Acertou!");
            i = i + 1;
        if (i == 4 and (not acertou)):
            print("Voce perdeu!")
    # Fim do jogo
    else:
        continuar = False;
        print("Fim de jogo!")
