import requests

#print("Ciao")

#str = "ha"
#print(str * 3) 

eta = 21
nome = "Sara"
adult = eta >= 18

if adult is True:
    print(f"Mi chiamo {nome} e sono maggiorenne perché ho {eta} anni")
else:
    print(f"Mi chiamo{nome} e sono minorenne perché ho {eta} anni")

type(eta)
print(type(eta))




#esercizio 1 col prof

studenti = 28
corso = "AI, LLM, ML - Python"
superato = False

#print(corso+studenti)

#print(corso+" "+str(studenti))

print(type(studenti))
print(type(corso))
print(type(superato))

corso = "Javascript"

print(corso[2:6])

# corso[4] = "S"  # This will raise an error because strings are immutable

print(f"Gli studenti del corso {corso} sono {studenti}")

print("Gli studenti del corso %s sono %d, %s" % (corso, studenti, superato))

valutazione = 27

if valutazione > 18:
    superato = True

print(superato)


num2 = True + studenti

print("num2: "+str(num2))

print(studenti * 3)


#esercizio 2

#input = (input("Scrivi il tuo numero: "))

#risultato = input
#print(risultato + 10)
#print(risultato * 2)
#print(risultato ** 2)

#print("Il tuo numero è: " + str(risultato))

#col prof

num = input("Inserisci un numero intero: ")

#num2 = int(num)  # Convert the input string to an integer

#num = int(num)  # Convert the input string to an integer

#num3 = int(input("Inserisci un numero intero: "))

try:
    my_number = int(num)
    print("Hai inserito il numero "+num)
except ValueError as e:
    print(num+" non è un numero valido")
    print(e)
finally:
    print("Qui ci arrivo sempre")

print("Lunghezza input: "+str(len(num)))

serie = [1, 2, 3, 4, 5]

print(f"Lunghezza della serie: {len(serie)}")

num1, num2, num3 = input("Inserisci tre numeri separati da uno spazio: ").split(" " )

print(num1+" "+num2+" "+num3)

nome = "Francesco"
nome = nome.replace("o", "0")
print(nome)

nome = "Giuseppe"
nome = nome.replace("p", "3")
print(nome)

#esercizio 3

num1 = 33
num2 = 42

confronto = (num1 > num2)


