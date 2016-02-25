import math
### Exercicio 2
##
##n = int(input("Digite aqui o numero que voce deseja calcular fatorial\n"))
##resultado = 1;
##
##while(n > 0):
##    resultado = resultado*n;
##    n = n - 1;
##
##print(resultado);

### Exercicio 6
##n = int(input("Digite aqui o numero que voce quer calcular a raiz cubica\n"));
##count = 1;
##while(count < int(math.sqrt(n))):
##    if(count * count * count == n):
##        break;
##    else:
##        count += 1
##
##print(count)

# Exercicio 7
n = int(input("Digite aqui qual o numero da sequencia de fibonacci voce deseja saber\n"))
a = 1;
b = 1;
aux = 2;
resultado = 1;
if(n >= 2):
    while(aux <= n):
        resultado = a + b;
        a = b;
        b = resultado;
        aux += 1;

print(resultado);
