#Esercizio 1: contare le variabili

def conta_vocali(frase):
    vocali = "aeiouAEIOU"
    totale = 0
    for carattere in frase:
        if carattere in vocali:
            totale += 1
    return totale  
    

print(conta_vocali("Questo è il numero di caratteri in questa frase"))
print(conta_vocali("aeiou"))       
print(conta_vocali("AEIOU"))       
print(conta_vocali("Python"))  
print(conta_vocali("bcdfg"))       
print(conta_vocali("")) 



#Esercizio 2: creazione e utilizzo di un modulo = guarda main.py e mathutil.py



#Esercizio 3: funzione con parametri dinamici

# def processa(*args, **kwargs):
#     totale = 0
#     for arg in args:
#         try:
#             totale += arg
#         except TypeError:
#             print(f"Valore non valido: {arg}")
#     chiavi_ordinate = sorted(kwargs)
#     print("Chiavi ordinate:", chiavi_ordinate)

#     kwargs_ordinati = {chiave: kwargs[chiave] for chiave in chiavi_ordinate}
#     return {"somma": totale, "kwargs": kwargs_ordinati}

# print(processa(1, 2.5, "ciao", 4, None, z=1, a=2, m=3))
# print(processa(10, "x", [1, 2], 5))
# print(processa())
# print(processa("a", "b", nome="Sara", eta=25))



#fatto col prof il 3

# isinstance() serve a verificare se un oggetto è un'istanza o una sottoclasse di una 
# determinata classe o tipo di dato.

def esegui_somma(*args, **kwargs):
    print(type(args[0]))
    print(len(args))

    if isinstance(args[0], list):
        print("Inserisci lista come primo parametro")

    sum = 0

    for x in args[0]:
        try:
            sum += float(x)
        except:
            print(f"Valore non accettabile: {x}")

    print(type(kwargs))
        
    return sum

    print(f"Dict con params: {sorted(kwargs)}")

    output = {}

    for key in sorted(kwargs):
        output[key] = kwargs[key]

    print(f"kwargs orig: {kwargs}")
    print("kwargs sorted: {output}")


numbers = [1, 2, 3] 

somma = esegui_somma("numbers", eta = 42, nome = "Luigi")

print(somma)
    