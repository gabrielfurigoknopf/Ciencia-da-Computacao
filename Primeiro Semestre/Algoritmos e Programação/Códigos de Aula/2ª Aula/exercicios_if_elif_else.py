#Aprendendo Python e práticando:

#Exercícios utilizando if, elif e else:
'''
Q1 - Determine qual dos três valores informados é o maior, ou identificar se todos são
iguais?! (utilize if, elif e else).
'''
#Input:
x = int(input("Informe valor 1: "))
y = int(input("Informe valor 2: "))
z = int(input("Informe valor 3: "))

if x > y and x > z :
    print("x é o maior")
elif y > x and y > z :
    print("y é o maior")
elif z > x and z > y :
    print("z é o maior")
else :
    #Output:
    print("numeros iguais")

'''
Q2 - Compare dois números (a e b) e determine qual é maior, ou se são iguais?! (utilize if, 
elif e else).
'''
#Input:
a = 44
b = 33
if a > b :
    #Output:
    print("A é maior que B")
elif b > a :
    #Output:
    print("B é maior que A")
else :
# elif a == b :
    #Output:
    print("A é igual a B")

'''
Q3 - Encontre o maior e o menor valor entre três números (a, b e c) informados! (utilize if, 
elif e else).
'''
#Input:
a = 44
b = 33
c = 50

if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

#Output:
print("Maior valor: ", maior)
print("Menor valor: ", menor)
