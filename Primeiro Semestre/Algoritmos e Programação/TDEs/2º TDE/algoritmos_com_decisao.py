'''
Nome: Gabriel Furigo Knopf
Matrícula: 199030
'''
#Lista de Exercícios 02: Algoritmos com Decisão.

#Q1 - Leia um valor inteiro e em seguida apresenta uma mensagem se o número é PAR ou IMPAR.

#Input:
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    #Output:
    print("O número é PAR")
else:
    #Output:
    print("O número é ÍMPAR")

#Q2 - Leia dois valores inteiros e diferentes em seguida apresenta o MAIOR e o MENOR número.
    
#Input:
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    #Output:
    print("O maior número é:", numero1)
    print("O menor número é:", numero2)
else:
    #Output:
    print("O maior número é:", numero2)
    print("O menor número é:", numero1)

'''
#Q3 - Leia 3 notas de um aluno e em seguida calcule a média aritmética e mostre, além do 
valor da média, uma mensagem de "APROVADO", caso a média seja igual ou superior a 7, ou a
mensagem "REPROVADO", caso contrário.
'''
#Input:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

#Output:
print("A média do aluno é:", media)
if media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

'''   
#Q4 - Leia 3 valores inteiros e diferentes e a seguir, encontre e exiba o maior, o menor e
o intermediário.
'''
#input: 
valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))
valor3 = int(input("Digite o terceiro valor inteiro: "))

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
    if valor2 < valor3:
        intermediario = valor2
        maior = valor3
    else:
        intermediario = valor3
        maior = valor2
elif valor2 < valor1 and valor2 < valor3:
    menor = valor2
    if valor1 < valor3:
        intermediario = valor1
        maior = valor3
    else:
        intermediario = valor3
        maior = valor1
else:
    menor = valor3
    if valor1 < valor2:
        intermediario = valor1
        maior = valor2
    else:
        intermediario = valor2
        maior = valor1

#Output:
print("Menor valor:", menor)
print("Intermediário valor:", intermediario)
print("Maior valor:", maior)

#Q5 - Leia a idade de um nadador e a seguir classifique-o em uma das seguintes categorias:

#Input:
idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Adulto"
else:
    categoria = "Idade fora das categorias"

#Output:
print("Categoria do nadador:", categoria)

'''
Q6 - Uma empresa concederá um aumento de salário aos seus funcionários, variável de acordo
com o cargo, conforme a tabela abaixo. Leia o salário e o cargo de um funcionário e calcule
o novo salário. Se o cargo do funcionário não estiver na tabela, ele deverá, então, receber
40% de aumento. Mostre o salário antigo, o novo salário e a diferença.
'''
#Input:
salario = float(input("Digite o salário do funcionário: "))
codigo_cargo = int(input("Digite o código do cargo (101 - Gerente, 102 - Engenheiro, 103 - Técnico): "))

if codigo_cargo == 101:
    percentual_aumento = 0.10  
elif codigo_cargo == 102:
    percentual_aumento = 0.20 
elif codigo_cargo == 103:
    percentual_aumento = 0.30  
else:
    percentual_aumento = 0.40 

novo_salario = salario * (1 + percentual_aumento)
diferenca = novo_salario - salario

#Output:
print(f"Salário antigo: R${salario:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")
print(f"Diferença: R${diferenca:.2f}")

'''
Q7 - Ler 3 valores inteiros. Verificar se estes valores não formam um triângulo, neste caso, mostrar mensagem de erro.
Caso contrário, apresentar mensagem identificando o tipo do triângulo formado (isósceles, 
equilátero ou escaleno).
'''
#Input:
a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
  
    if a == b == c:
        tipo_triangulo = "Equilátero"
    elif a == b or a == c or b == c:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
    
    #Output:
    print("Os valores formam um triângulo", tipo_triangulo)
else:
    print("Os valores não formam um triângulo")

''' 
Q8 - Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2 em que
o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.
'''
#Input:    
valor = int(input("Digite o valor em reais: "))

notas_100 = valor // 100
valor %= 100

notas_50 = valor // 50
valor %= 50

notas_20 = valor // 20
valor %= 20

notas_10 = valor // 10
valor %= 10

notas_5 = valor // 5
valor %= 5

notas_2 = valor // 2
valor %= 2

#Output:
print("Valor fornecido:", valor)
print("Notas de 100 reais:", notas_100)
print("Notas de 50 reais:", notas_50)
print("Notas de 20 reais:", notas_20)
print("Notas de 10 reais:", notas_10)
print("Notas de 5 reais:", notas_5)
print("Notas de 2 reais:", notas_2)
print("Notas de 1 real:", valor)

'''
Q9 - Calcule o imposto de renda de um contribuinte, onde o usuário informe o valor anual 
recebido e o sistema mostra o cálculo do imposto de renda de acordo com a tabela progressiva abaixo.
'''
#Input:
valor_anual = float(input("Digite o valor anual recebido: "))

imposto = 0.0

if valor_anual <= 17989.80:
    imposto = 0.0
elif valor_anual <= 26961.00:
    imposto = (valor_anual - 17989.80) * 0.075
elif valor_anual <= 35948.40:
    imposto = (26961.00 - 17989.80) * 0.075 + (valor_anual - 26961.00) * 0.15
elif valor_anual <= 44918.28:
    imposto = (26961.00 - 17989.80) * 0.075 + (35948.40 - 26961.00) * 0.15 + (valor_anual - 35948.40) * 0.225
else:
    imposto = (26961.00 - 17989.80) * 0.075 + (35948.40 - 26961.00) * 0.15 + (44918.28 - 35948.40) * 0.225 + (valor_anual - 44918.28) * 0.275

#Output:
print(f"Valor anual recebido: R${valor_anual:.2f}")
print(f"Imposto de renda a pagar: R${imposto:.2f}")

'''
Q10 - Leia uma data informada pelo usuário (dia, mês e ano) e determine se aquela data é 
válida ou não. Uma data é considerada válida quando:
'''
#Input:
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if ano < 0 or ano > 3000:
    data_valida = False
else:
    if mes < 1 or mes > 12:
        data_valida = False
    else:
        if mes in [4, 6, 9, 11]:  
            if 1 <= dia <= 30:
                data_valida = True
            else:
                data_valida = False
        elif mes == 2:  
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if 1 <= dia <= 29:
                    data_valida = True
                else:
                    data_valida = False
            else:
                if 1 <= dia <= 28:
                    data_valida = True
                else:
                    data_valida = False
        else:  
            if 1 <= dia <= 31:
                data_valida = True
            else:
                data_valida = False
                
if data_valida:
    #Output:
    print("A data é válida.")
else:
    print("A data não é válida.")

