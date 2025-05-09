'''
Nome: Gabriel Furigo Knopf
Matrícula: 199030
'''

#Lista de exercícios 01: Algoritmos Sequenciais.

'''
#Q1 - Calcule a média ponderada de um aluno. Considere para isso três notas com pesos 3
(prova A), 5 (prova B) e 2 (trabalhos).
'''
#Input - Solicitação ao usuário:
nota_a = float(input("Digite a nota da prova A:"))
nota_b = float(input("Digite a nota da prova B:"))
nota_trabalhos = float(input("Digite a nota dos trabalhos:"))

#Cálculo da soma ponderada:
soma_ponderada = (nota_a * peso_a) + (nota_b * peso_b) + (nota_trabalhos * peso_trabalhos)
soma_pesos = peso_a + peso_b + peso_trabalhos

#Cálculo da média ponderada:
media_ponderada = soma_ponderada / soma_pesos

#Output - Exibição do resultado:
print(f"A média ponderada do aluno é: {media_ponderada:.2f}")

'''
Q2 - Receba dois valores, calcule e exiba os resultados das operações de soma, subtração,
divisão e multiplicação entre estes dois números.
'''
#Input - Solicitação ao usuário:
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

#Cálculo das operações:
soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2

if valor2 != 0:
    divisao = valor1 / valor2
else:
    divisao = "Não é possível dividir por zero"

#Output - Exibição dos resultados:
print(f"Soma: {valor1} + {valor2} = {soma}")
print(f"Subtração: {valor1} - {valor2} = {subtracao}")
print(f"Multiplicação: {valor1} * {valor2} = {multiplicacao}")
print(f"Divisão: {valor1} / {valor2} = {divisao}")

'''
Q3 - Leia um valor de temperatura em graus Celsius, calcule e exiba a temperatura
correspondente em graus Kelvin (sabendo que Kelvin = Celsius + 273)
'''
#Input - Solicitação ao usuário:
celsius = float(input("Digite a temperatura em graus Celsius: "))

#Calcula a temperatura em graus Kelvin:
kelvin = celsius + 273

#Output - Exibição do resultado:
print(f"A temperatura em graus Kelvin é: {kelvin:.2f}")

'''
Q4 - Leia a quotação do dólar do dia e uma quantidade de Reais a ser convertida para
dólares. A final, exibir o valor correspondente em dólares aos Reais informados.
'''
#Input - Solicitação ao usuário:
cotacao_dolar = float(input("Digite a cotação do dólar do dia: "))
quantidade_reais = float(input("Digite a quantidade de Reais a ser convertida: "))

#Calcula o valor correspondente em dólares:
valor_dolares = quantidade_reais / cotacao_dolar

#Output - Exibição do resultado:
print(f"Valor correspondente em dólares: ${valor_dolares:.2f}")

'''
Q5 - Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval.Para isso
considere que uma garrafa de cerveja possui 600ml e uma caixa possui 24 garrafas.O algortimo
deverá ler a quantidade de caixas consumidas e retornar a quantidade equivalente em litros.
'''
#Input - Solicitação ao usuário:
quantidade_caixas = int(input("Digite a quantidade de caixas de cerveja consumidas: "))

#Definição da quantidade de garrafas por caixa e a quantidade de cerveja por garrafa:
garrafas_por_caixa = 24
ml_por_garrafa = 600

#Calcula a quantidade total de cerveja em mililitros:
total_ml = quantidade_caixas * garrafas_por_caixa * ml_por_garrafa

#Conversão da quantidade total para litros:
total_litros = total_ml / 1000

#Output - Exibição do resultado:
print(f"A quantidade total de cerveja consumida é: {total_litros:.2f} litros")

'''
Q6 - Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada qual sendo vendido
respectivamente por 10, 12 e 15 reais. Implemente um programa em que o usuário forneça a quantidade
de camisetas pequenas, médias e grandes referentes a uma venda e retorne o valor a ser cobrado.
'''
#Input - Solicitação ao usuário:
quantidade_pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
quantidade_medianas = int(input("Digite a quantidade de camisetas médias: "))
quantidade_grandes = int(input("Digite a quantidade de camisetas grandes: "))

#Definição dos preços das camisetas:
preco_pequena = 10
preco_mediu = 12
preco_grande = 15

#Calcula o valor total da venda:
valor_total = (quantidade_pequenas * preco_pequena) + (quantidade_medianas * preco_mediu) + (quantidade_grandes * preco_grande)

#Output - Exibição do resultado:
print(f"O valor total a ser cobrado é: R$ {valor_total:.2f}")

'''
Q7 -  Leia um número correspondendo a uma quantidade de dias e após, calcule e mostre a quantidade 
de anos, meses e dias correspondentes.Para facilitar o cálculo, considere ano com 365 dias e mês
com 30 dias.
'''
#ex.: 400 equivale a 1 ano, 1 mês e 5 dias
#Input - Solicitação ao usuário:
total_dias = int(input("Digite a quantidade de dias: "))

#Definição da quantidade de dias em um ano e em um mês:
dias_por_ano = 365
dias_por_mes = 30

#Calcula a quantidade de anos:
anos = total_dias // dias_por_ano
dias_restantes = total_dias % dias_por_ano

#Calcula a quantidade de meses:
meses = dias_restantes // dias_por_mes
dias_restantes = dias_restantes % dias_por_mes

#Output - Exibição do resultado:
print(f"{total_dias} dias equivalem a {anos} ano(s), {meses} mês(es) e {dias_restantes} dia(s).")

