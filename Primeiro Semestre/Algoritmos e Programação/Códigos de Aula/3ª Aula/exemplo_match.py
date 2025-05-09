#Q1 - Identifique o nome do dia da semana com base em um número informado pelo usuário.

#Input:
dia = int(input("Informe o dia da semana (1 - 7): "))                      

match dia:
    case 1:
        print ("Domingo")
    case 2:
        print ("Segunda-feira")
    case 3:
        print ("Terça-feira")
    case 4:
        print ("Quarta-feira")
    case 5:
        print ("Quinta-feira")
    case 6:
        print ("Sexta-feira")
    case 7:
        print ("Sábado")
    case other :
        print("Dia inválido")
    
