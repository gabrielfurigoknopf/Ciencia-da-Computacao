'''
Q2 - Trate os erros (exceções) no código utilizando try e except para capturar e lidar com
exceções de forma controlada.
'''

try:
  # descomente a linha abaixo para ver o que acontece  
  # x = 10/0
  print(x)
except NameError:
  print("Variavel x nao foi definida")
except:
  print("Houve um erro")