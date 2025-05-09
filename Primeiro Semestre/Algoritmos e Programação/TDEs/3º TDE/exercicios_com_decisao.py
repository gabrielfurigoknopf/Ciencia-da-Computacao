'''
Nome: Gabriel Furigo Knopf
Matricula: 199030
'''
#Lista de exercicios 03: Algoritmos com decisão.

#Q1 - cardápio de uma lancheria.
cardapio = {
    10: {"descricao": "Cachorro-quente", "preco": 1.10},
    11: {"descricao": "Bauru simples", "preco": 1.30},
    12: {"descricao": "Bauru com ovo", "preco": 1.50},
    13: {"descricao": "Hamburguer", "preco": 1.10},
    14: {"descricao": "Cheeseburger", "preco": 1.30},
    15: {"descricao": "Refrigerante", "preco": 1.50}
}


def calcular_valor():
    print("Cardápio:")
    for codigo, item in cardapio.items():
        print(f"Cod {codigo}: {item['descricao']} - R${item['preco']:.2f}")
    
    codigo = int(input("Digite o código do item desejado: "))
    
    if codigo not in cardapio:
        print("Código inválido. Por favor, digite um código válido.")
        return
    
    quantidade = int(input("Digite a quantidade: "))
    
    preco_unitario = cardapio[codigo]["preco"]
    valor_total = preco_unitario * quantidade
    
    print(f"Item: {cardapio[codigo]['descricao']}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Unitário: R${preco_unitario:.2f}")
    print(f"Valor Total: R${valor_total:.2f}")

calcular_valor()

'''
#Q2 - Em uma determinada cidade, a passagem escolar representa 60% do valor da passagem 
normal. Cada estudante tem direito a adquirir até 50 passagens escolares por mês letivo 
com desconto, podendo adquirir mais passagens, mas sem o desconto. Desenvolva um algoritmo
que receba o valor da passagem normal e o número de passagens a serem adquiridas,calcule e
apresente o valor da passagem escolar e o montante a ser pago pelas passagens adquiridas.
'''

valor_passagem_normal = float(input("Digite o valor da passagem normal (R$): "))
valor_passagem_escolar = valor_passagem_normal * 0.60
numero_passagens = int(input("Digite o número de passagens a serem adquiridas: "))
limite_passagens_escolar = 50

if numero_passagens <= limite_passagens_escolar:
    valor_total = numero_passagens * valor_passagem_escolar
else:
    passagens_com_desconto = limite_passagens_escolar
    valor_total_com_desconto = passagens_com_desconto * valor_passagem_escolar
    passagens_normais = numero_passagens - limite_passagens_escolar
    valor_passagem_normal_extra = passagens_normais * valor_passagem_normal
    valor_total = valor_total_com_desconto + valor_passagem_normal_extra

print(f"Valor da passagem escolar: R${valor_passagem_escolar:.2f}")
print(f"Montante a ser pago: R${valor_total:.2f}")

'''
Q3 - Elaborar um algoritmo que lê 2 valores a e b, verifica se são múltiplos um do outro e
os escreve com a mensagem: São múltiplos ou Não são múltiplos.
'''

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

if a % b == 0 or b % a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")

'''
Q4 - Desenvolva um algoritmo que leia o nome de uma pessoa, o dia e o mês de seu nascimento
e sem seguida apresente o nome da pessoa e o seu signo.
'''
nome = input("Digite o nome da pessoa: ")
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))

if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
    signo = "Aquário"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Peixes"
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Áries"
elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 21):
    signo = "Touro"
elif (mes == 5 and dia >= 22) or (mes == 6 and dia <= 21):
    signo = "Gêmeos"
elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 22):
    signo = "Câncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "Leão"
elif (mes == 8 and dia >= 24) or (mes == 9 and dia <= 22):
    signo = "Virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
    signo = "Libra"
elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
    signo = "Escorpião"
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
    signo = "Sagitário"
else:
    signo = "Capricórnio"

print(f"{nome} - {signo}")

'''
Q5 - Elabore um algoritmo que leia o nome e a idade de três pessoas e após a leitura escreva o nome da pessoa mais
velha e o nome da pessoa mais nova. Considere que não existem idades iguais.
'''
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

nome3 = input("Digite o nome da terceira pessoa: ")
idade3 = int(input("Digite a idade da terceira pessoa: "))

if idade1 > idade2 and idade1 > idade3:
    mais_velho = nome1
    if idade2 < idade3:
        mais_novo = nome2
    else:
        mais_novo = nome3
elif idade2 > idade1 and idade2 > idade3:
    mais_velho = nome2
    if idade1 < idade3:
        mais_novo = nome1
    else:
        mais_novo = nome3
else:
    mais_velho = nome3
    if idade1 < idade2:
        mais_novo = nome1
    else:
        mais_novo = nome2

print(f"Mais velho: {mais_velho}")
print(f"Mais novo: {mais_novo}")



