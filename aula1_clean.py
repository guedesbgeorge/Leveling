# Banco de perguntas e respostas
perguntas = [ "Em que ano se iniciou a serie?",
              "Quantas temporadas existem?",
              "Qual o nome do ator que interpreta o personagem Sheldon Cooper?",
              "Qual a profissão do personagem Rajesh?",
              "Qual o apelido dado ao personagem Howard Wolowitz pelos seus colegas de trabalho na NASA?",
              "Qual o sobrenome do personagem Leonard?"];
respostas = ["2007",
             "9",
             "Jim Parsons",
             "Astrofisico",
             "Froot Loops",
             "Hofstadter"];

# Imprimindo mensagem de inicio e setando o score inicial
print('Bem-vindo ao jogo de perguntas e respostas sobre a serie de TV "The Big Bang Theory!"');
print("Vamos comecar!");
score = 0;

# Mostrando as perguntas e esperando as respostas
for i in range(0, len(perguntas)):
    print(perguntas[i]);
    respostaUsuario = input();
    if(respostaUsuario == respostas[i]):
        print("Resposta correta!");
        score = score + 10;
    else:
        print("Resposta errada!");
    
# Finalizando o jogo
print("Fim de jogo!");
print("Seu score foi", score, "de um maximo de 60 pontos possiveis!");
