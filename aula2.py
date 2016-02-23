### Exercicio 1, 2 e 3
### Banco de perguntas e respostas
##perguntas = [ "Em que ano se iniciou a serie?",
##              "Quantas temporadas existem?",
##              "Qual o nome do ator que interpreta o personagem Sheldon Cooper?",
##              "Qual a profissão do personagem Rajesh?",
##              "Qual o apelido dado ao personagem Howard Wolowitz pelos seus colegas de trabalho na NASA?",
##              "Qual o sobrenome do personagem Leonard?"];
##respostas = ["2007",
##             "9",
##             "Jim Parsons",
##             "Astrofisico",
##             "Froot Loops",
##             "Hofstadter"];
##
##perguntaMultiplaEscolha = [["Qual o estado em que a serie se passa?",
##                           ["a) Oklahoma", "b) California", "c) Nebraska", "d) Ohio"], "b"]]
##
### Imprimindo mensagem de inicio e setando o score inicial
##print('Bem-vindo ao jogo de perguntas e respostas sobre a serie de TV "The Big Bang Theory!"');
##print("Vamos comecar!");
##score = 0;
##
### Mostrando as perguntas e esperando as respostas
##for i in range(0, len(perguntas)):
##    print(perguntas[i]);
##    respostaUsuario = input();
##    if(respostaUsuario == respostas[i]):
##        print("Resposta correta!");
##        score = score + 10;
##    else:
##        print("Resposta errada!");
##        score = score - 10; # Subtraindo pontos (Exercicio 2)
##
### Pergunta de multipla escolha (Exercicio 3)
##for pergunta in perguntaMultiplaEscolha:
##    print(pergunta[0])
##    for i in range(0, len(pergunta[1])):
##        print(pergunta[1][i])
##    alternativaUsuario = input();
##    if(alternativaUsuario == pergunta[2]):
##        print("Resposta correta!");
##        score = score + 10;
##    else:
##        print("Resposta errada!");
##        score = score - 10; # Subtraindo pontos (Exercicio 2
##        
##    
### Finalizando o jogo
##print("Fim de jogo!");
##if (score >= 50): # Parabéns condicional (Exercicio 1)
##    print("Parabéns! Seu score foi", score, "de um maximo de 70 pontos possiveis!")
##else:
##    print("Seu score foi", score, "de um maximo de 70 pontos possiveis!");

##################################################################################################
##
# Jogo de advinhacao
# Mensagem de explicacao
##print("Bem-vindo ao jogo da advinhacao.\n",
##      "Ao inicio de cada rodada, o primeiro jogador deve digitar um numero e em seguida",
##      "o segundo jogador tera 3 tentativas para advinhar.\n A cada tentativa, será",
##      "informado se o palpite é menor, maior ou igual ao numero correto. \n",
##      "O jogo continuará infinitamente até que o jogador 1 digite 'fim'\n",
##      "Vamos comecar!\n\n");
##
### Inicio do jogo
##continuar = True;
##while(continuar):
##    # Pega a entrada do jogador 1
##    print("Jogador 1, digite um numero entre 0 e 30 ou digite 'fim' caso queira encerrar o jogo.")
##    jogador1Entrada = input(); 
##    # Procede para a execucao de uma rodada
##    if(jogador1Entrada != "fim"):
##        jogador1Entrada = int(jogador1Entrada); # Exercicio4
##        # Some o numero digitado da tela
##        for i in range(0, 40):
##            print("\n")
##
##        i = 1;
##        acertou = False;
##        # 3 tentativas para o jogador 2
##        while(i <=3 and (not acertou)):
##            print("Jogador 2, essa é sua", i, "tentativa. Qual o numero que o jogador 1 escolheu?");
##            jogador2Entrada = int(input());
##            if(jogador2Entrada > jogador1Entrada):
##                print("Seu palpite eh maior que o valor escolhido pelo jogador 1.");
##            elif(jogador2Entrada < jogador1Entrada):
##                print("Seu palpite eh menor que o valor escolhido pelo jogador 1.");
##            else:
##                acertou = True; # Exercicio 11
##                print("Acertou!");
##            i = i + 1;
##    # Fim do jogo
##    else:
##        continuar = False;
##        print("Fim de jogo!")

#############################################################################################
# Exercicio 5
##print("Digite um numero entre 100 e 999");
##entradaUsuario = int(input());
##if(entradaUsuario < 100 or entradaUsuario > 999):
##    print("Voce digitou um numero invalido.")
##else:
##    resto = entradaUsuario%3;
##    if(resto == 0):
##        print(entradaUsuario, "eh divisivel por 3.");
##    else:
##        print(entradaUsuario, "nao eh divisivel por 3.");

#############################################################################################
# Exercicio 6
##print("Digite um numero entre 100 e 999");
##entradaUsuario = int(input());
##if(entradaUsuario < 100 or entradaUsuario > 999):
##    print("Voce digitou um numero invalido.")
##else:
##    algarismo1 = int(str(entradaUsuario)[0]);
##    algarismo2 = int(str(entradaUsuario)[1]);
##    algarismo3 = int(str(entradaUsuario)[2]);
##    print(algarismo1 + algarismo2 + algarismo3)

#############################################################################################
# Exercicio 7
##numeros = [];
##for i in range(0, 3):
##    print("Digite um numero");
##    numeros = numeros + [int(input())];
##
##ordenados = [];
##if(numeros[0] <= numeros[1] and numeros[0] <= numeros[2]):
##    ordenados = ordenados + [numeros[0]];
##    if(numeros[1] <= numeros[2]):
##        ordenados = ordenados + [numeros[1]];
##        ordenados = ordenados + [numeros[2]];
##    else:
##        ordenados = ordenados + [numeros[2]];
##        ordenados = ordenados + [numeros[1]];
##elif (numeros[1] <= numeros[0] and numeros[1] <= numeros[2]):
##    ordenados = ordenados + [numeros[1]];
##    if(numeros[0] <= numeros[2]):
##        ordenados = ordenados + [numeros[0]];
##        ordenados = ordenados + [numeros[2]];
##    else:
##        ordenados = ordenados + [numeros[2]];
##        ordenados = ordenados + [numeros[0]];
##else:
##    ordenados = ordenados + [numeros[2]];
##    if(numeros[0] <= numeros[1]):
##        ordenados = ordenados + [numeros[0]];
##        ordenados = ordenados + [numeros[1]];
##    else:
##        ordenados = ordenados + [numeros[1]];
##        ordenados = ordenados + [numeros[0]];
##
##print(ordenados);

#############################################################################################
# Exercicio 8
# TODO: Exercicio 10 e acrescentar restricao de denominador 0
print("Digite o operador '+', '-', '*' ou '/'");
operando = input();

if(operando == "+" or operando == "-" or operando == "*" or operando == "/"): # Exercicio 9
    print("Digite o primeiro operando");
    operando1 = int(input());

    print("Digite o segundo operando");
    operando2 = int(input());

    if(operando == "+"):
        resultado = operando1 + operando2;
    elif(operando == "-"):
        resultado = operando1 - operando2;
    elif(operando == "*"):
        resultado = operando1 * operando2;
    elif(operando == "/"):
        resultado = operando1 / operando2;

    print(resultado);
else:
    print("Operador invalido. Fim do programa.")

#############################################################################################
# Exercicio 12
# Jogo de advinhacao
# Mensagem de explicacao
##print("Bem-vindo ao jogo da advinhacao.\n",
##      "Ao inicio de cada rodada, o primeiro jogador deve digitar um numero e em seguida",
##      "o segundo jogador tera 3 tentativas para advinhar.\n A cada tentativa, será",
##      "informado se o palpite é menor, maior ou igual ao numero correto. \n",
##      "O jogo continuará infinitamente até que o jogador 1 digite 'fim'\n",
##      "Vamos comecar!\n\n");
##
### Inicio do jogo
##continuar = True;
##while(continuar):
##    # Pega a entrada do jogador 1
##    print("Jogador 1, digite dois numeros ou digite 'fim' caso queira encerrar o jogo.")
##    jogador1Entrada1 = input();
##    # Procede para a execucao de uma rodada
##    if(jogador1Entrada1 != "fim"):
##        jogador1Entrada1 = int(jogador1Entrada1); # Exercicio4
##        jogador1Entrada2 = int(input());
##        # Some o numero digitado da tela
##        for i in range(0, 40):
##            print("\n")
##
##        i = 1;
##        acertou = False;
##        # 3 tentativas para o jogador 2
##        while(i <=3 and (not acertou)):
##            print("Jogador 2, essa é sua", i, "tentativa. Qual o numero que o jogador 1 escolheu?");
##            jogador2Entrada = int(input());
##            if(jogador2Entrada != jogador1Entrada1 and jogador2Entrada != jogador1Entrada2):
##                if(jogador1Entrada1 > jogador1Entrada2):
##                    maior = jogador1Entrada1;
##                    menor = jogador1Entrada2;
##                else:
##                    maior = jogador1Entrada2;
##                    menor = jogador1Entrada1;
##
##                if(jogador2Entrada > maior):
##                    print("Seu palpite é maior que o maior dos numeros.")
##                elif(jogador2Entrada < menor):
##                    print("Seu palpite é menor que o menor dos numeros.")
##                else:
##                    print("Seu palpite esta entre os numeros.")
##            else:
##                acertou = True; # Exercicio 11
##                print("Acertou!");
##            i = i + 1;
##        if (i == 4 and (not acertou)):
##            print("Voce perdeu!")
##    # Fim do jogo
##    else:
##        continuar = False;
##        print("Fim de jogo!")






