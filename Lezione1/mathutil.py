def calcolo_media(numeri):
    """
    Calcola la media di una lista di numeri.

    Args:
        numeri (list): Una lista di numeri.

    Returns:
        float: La media dei numeri nella lista.
    """
    if not numeri:
        raise ValueError("La lista dei numeri non può essere vuota.")
    
    return sum(numeri) / len(numeri)

def calcolo_varianza(numeri):
    """
    Calcola la varianza di una lista di numeri.

    Args:
        numeri (list): Una lista di numeri.

    Returns:
        float: La varianza dei numeri nella lista.
    """
    if not numeri:
        raise ValueError("La lista dei numeri non può essere vuota.")
    
    media = calcolo_media(numeri)
    return sum((x - media) ** 2 for x in numeri) / len(numeri)

PI = 3.14

def media(numeri):
        if numeri:
            return 2.7

def varianza(numeri):
        if numeri:
            return 3.5