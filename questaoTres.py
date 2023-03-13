# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

# Leitura padrão de arquivo JSON
def read_json_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
    return data

def return_lowest_value(data):
    lowest_value = 9999999
    for i in range(len(data)):
        if data[i]['valor'] < lowest_value and data[i]['valor'] != 0: # Como o arquivo JSON está formatado da maneira ideal, é necessário iterar como uma lista e não como um dicionário, pois o objeto é uma lista de dicionários.
            # O valor 0 é ignorado, como pedido no enunciado.
            lowest_value = data[i]['valor']
    return lowest_value

def return_highest_value(data):
    highest_value = 0
    for i in range(len(data)):
        if data[i]['valor'] > highest_value:
            highest_value = data[i]['valor']
    
    return highest_value

def return_average_value(data):
    total = 0
    for i in range(len(data)):
        total += data[i]['valor']
    average = total / len(data) # Aqui o uso de List facilita o cálculo, já que o tamanho da lista é conhecido.
    return average

def days_over_average(data):
    average = return_average_value(data)
    days = 0
    for i in range(len(data)):
        if data[i]['valor'] > average:
            days += 1
    return days

def main():
    data = read_json_file("dados.json")
    print("Menor valor: ", return_lowest_value(data))
    print("Maior valor: ", return_highest_value(data))
    print("Valor médio: ", return_average_value(data))
    print("Dias cujo valor foi acima da média: ", days_over_average(data))

main()