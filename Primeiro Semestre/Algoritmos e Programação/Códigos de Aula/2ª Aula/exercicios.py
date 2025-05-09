#Aprendendo Python e práticando:

'''
Q1 - Calcule a média ponderada de um aluno. Considere para isso três notas com pesos:
-prova A (3)
-prova B (5)
-trabalhos (2)
'''
#Input:
provaA = float(input("Informe nota prova A: "))
provaB = float(input("Informe nota prova B: "))
trabalhos = float(input("Informe nota trabalhos: "))

notaFinal = (provaA * 0.3) + (provaB * 0.5) + (trabalhos * 0.2)

#Output:
print(" Media final: ", notaFinal)

'''
Q2 - Receba dois valores, calcule e exiba os resultados das operações de soma, subtração,
divisão e multiplicação entre estes dois números.
'''

#Input:
x = int(input("Informe primeiro valor: "))
y = int(input("Informe segundo valor: "))

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y

#Output:
print("Resultado da soma: ", soma)
print("Resultado da soma: ", subtracao)
print("Resultado da soma: ", multiplicacao)
print("Resultado da soma: ", divisao)

'''
Q3 - Leia um valor de temperatura em graus Celsius, calcule e exiba a temperatura 
correspondente em graus Kelvin (sabendo que Kelvin = Celsius + 273)
'''
#Input:
celsius = int(input("Informe temperatura (Celsius): "))

kelvin = celsius + 273

#Output:
print("Temperatura correspondente Kelvin: ", kelvin)

'''
Q4 - Leia a quotação do dólar do dia e uma quantidade de Reais a ser convertida para
dólares. A final, exibir o valor correspondente em dólares aos Reais informados.
'''
#Input:
quotacao = float(input("Informe valor do Dólar do dia: "))
reais = float(input("Informe valor em Reais a converter: "))

conversao = reais / quotacao

#Output:
print("Valor em dolares: ", conversao)

'''
Q5 - Calcule a quantidade de cerveja, em litros, consumida por um bloco de carnaval. Para 
isso considere que uma garrafa de cerveja possui 600ml e uma caixa possui24 garrafas.
O algortimo deverá ler a quantidade de caixas consumidas e retornara quantidade equivalente
em litros.
'''
#Input:
caixas = int(input("Informe quantidade de caixas de cerveja: "))

litros = caixas * 24 * 0.6

#Output:
print("Quantidade de litros: ", litros)

'''
Q6 - Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada qual sendo
vendido respectivamente por 10, 12 e 15 reais. Implemente um programa em que o usuário
forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda e 
retorne o valor a ser cobrado.
'''
#Input:
p = int(input("Informe quantidade de camisetas P a adquirir: "))
m = int(input("Informe quantidade de camisetas M a adquirir: "))
g = int(input("Informe quantidade de camisetas G a adquirir: "))

total = (p * 10) + (m * 12) + (g * 15)

#Output:
print("Total a pagar: R$", total)

'''
Q7 - Calcule a quantidade de dias informada pelo usuário e converta para o formato de anos,
meses e dias restantes.
'''
#Input:
dias = int(input('Informe a quantidade dias: '))

#1 ano = 365 dias
anos = dias // 365

resto = dias - (anos * 365)

#30 dias = 1 mes
meses = resto // 30
resto = resto - (meses * 30)

#Output
print("Anos: ", anos)
print("Meses: ", meses)
print("Dias: ", resto)
