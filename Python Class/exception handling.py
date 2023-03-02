# exception  =  events detected during execution that interrupt the flopw of a program


try:    #usa-se o  try geralmente me inputs em que os resultados podem ser confusos, como no caso da divisao por 0 
    numerador = int(input("Enter a number for divide: "))
    denominador = int(input("Enter a number to divide by: "))
    result = numerador / denominador   
except ZeroDivisionError:
    print("Voce nao pode dividir por 0")
except ValueError:
    print("Digite apenas valores")
else:
    print(result)
#finally: --->comando que sempre e executado no final do codigo 



#except Exception:
    #print("Algo deu errado")
    





