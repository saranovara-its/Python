import statistics

import math

# esercizio 1: utilizzo delle condizioni

# numero = int(input("Scrivi il tuo numero: "))
# if numero > 0:
#      print("Il numero è positivo")
# elif numero < 0:
#      print("Il numero è negativo")
# else:
#      print("Il numero è zero")

# #esercizio 2: utilizzo dei cicli

# for i in range(numero):
#     print(f"Iterazione {i+1}")


#eserczio 3: combinazione di cicli, condizioni, eccezioni

 
numeri = []
try:
    for i in range(5):
        n = int(input(f"Scrivi un numero {i+1}: "))
        if n < 0:
            print("Hai inserito un numero negativo, non posso calcolare la media")
            break
        numeri.append(n)
    else:
        risultato = sum(numeri) / len(numeri)
        print(f"La media dei numeri inseriti è: {risultato}")
except ValueError:
    print("Non hai inserito un numero valido")


print(f"Media dei numeri (statistics): {statistics.mean(numeri)}")

