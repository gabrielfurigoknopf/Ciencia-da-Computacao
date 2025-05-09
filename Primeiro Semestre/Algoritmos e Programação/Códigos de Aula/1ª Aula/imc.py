# imc.py - primeiro programa em Python (comentário de 1 linha)

""" (comentário de múltiplas linhas)
Exemplo de programa em linguagem Python que recebe valores de peso e altura,
calcula e exibe o Índice de Massa Corporal - IMC

para saber mais, consulte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal

"""

peso = float( input ("Informe seu peso: "))
altura = float ( input ("Informe sua altura: "))

imc = peso / (altura * altura)

print("Seu IMC: ", imc)


