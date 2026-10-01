# Progetto 1 - Smart Library

## Scenario

Una persona desidera gestire la propria biblioteca personale tramite un'applicazione da riga di comando. L'applicazione deve consentire di registrare libri, effettuare ricerche e ottenere semplici statistiche sulla collezione.

## Obiettivo

Realizzare un'applicazione Python organizzata in **moduli** e **package** che permetta di gestire una biblioteca personale.

L'applicazione deve essere eseguibile tramite il file `main.py` e presentare un menu testuale per l'interazione con l'utente.

## Struttura suggerita per il progetto

```text
library/
│
├── main.py
│
└── biblioteca/
    ├── __init__.py
    ├── gestione.py
    ├── ricerca.py
    └── utility.py
```

## Funzionalità richieste

L'applicazione deve permettere di:

1. Inserire un nuovo libro.
2. Visualizzare tutti i libri registrati.
3. Cercare un libro tramite titolo.
4. Filtrare i libri pubblicati dopo un certo anno.
5. Visualizzare statistiche sulla collezione.
6. Terminare il programma.


## Modellazione dei dati

Ogni libro deve essere rappresentato tramite un dizionario.

Esempio:

```python
{
    "titolo": "Python Basics",
    "autore": "Mario Rossi",
    "anno": 2024,
    "categorie": {"python", "programmazione"}
}
```

## Vincoli

Dimostrare l'utilizzo nel codice:

- Variabili e tipi di dati primitivi
- Input e output
- Operatori relazionali e logici
- Strutture condizionali
- Cicli
- Funzioni
- Moduli
- Package
- Liste
- Dizionari
- Tuple
- Set
- Gestione delle eccezioni tramite `try-except`

## Utilizzo suggerito delle strutture dati

| Struttura | Utilizzo |
|------------|------------|
| List | Archivio completo dei libri |
| Dict | Informazioni di un libro |
| Set | Categorie del libro |
| Tuple | Statistiche restituite dalle funzioni |

E' possibile scegliere un approccio diverso purchè compatibile con le buone pratiche dello sviluppo software e lo stile Python.

## Gestione errori

L'applicazione deve gestire almeno:

- Inserimento di anni non numerici
- Campi obbligatori vuoti
- Ricerche senza risultati
- Scelte menu non valide

## Opzionale 

Implementare una o più funzionalità aggiuntive:

- Conteggio libri per categoria
- Ricerca parziale nel titolo
- Autore con più libri presenti
- Ordinamento alfabetico dei risultati

## Consegna

Consegnare:

- Codice sorgente completo
- Package organizzato correttamente
- Commenti essenziali nelle funzioni principali
- Output di esempio che dimostri il funzionamento dell'applicazione
