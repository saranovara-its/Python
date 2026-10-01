import Lezione1.mathutil as mat       # ho importato il file: mathutil.py che contiene le funzioni matematiche

from Lezione1.mathutil import *

numeri = [7, 8, 9, 10, 5]

print(f"La media dei numeri è: {mat.calcolo_media(numeri)}")
print(f"La varianza dei numeri è: {mat.calcolo_varianza(numeri)}")
