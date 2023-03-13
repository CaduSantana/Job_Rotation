# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Optei por usar a fórmula por via de uma função lambda, pois acredito que seja a forma mais simples de se fazer isso.
fibonacci = lambda n: 5*n**2 + 4 if (5*n**2 + 4)**0.5 % 1 == 0 or (5*n**2 - 4)**0.5 % 1 == 0 else False
# Entrada do número
n = int(input('Insira um número: '))

# Retorna a mensagem de acordo com o resultado da função lambda
if fibonacci(n):
    print('O valor inserido pertence a sequência de Fibonacci')
else:
    print('O valor inserido não pertence a sequência de Fibonacci')