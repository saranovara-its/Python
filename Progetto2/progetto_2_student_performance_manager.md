# Progetto 2 - Student Performance Manager

## Scenario

Un centro di formazione desidera monitorare gli studenti iscritti ai corsi e tenere traccia dei risultati ottenuti nelle verifiche.

L'applicazione dovrà permettere di registrare studenti, corsi e voti, fornendo semplici statistiche sui risultati ottenuti.

## Obiettivo

Realizzare un'applicazione Python organizzata tramite **package** e **moduli** che consenta la gestione di studenti, corsi e voti.

L'applicazione dovrà essere eseguibile tramite il file `main.py` e utilizzare un menu testuale.

## Struttura suggerita del progetto

```text
school/
│
├── main.py
│
└── gestione_studenti/
    ├── __init__.py
    ├── studenti.py
    ├── corsi.py
    ├── statistiche.py
    └── utility.py
```

## Funzionalità richieste

L'applicazione deve permettere di:

1. Inserire un nuovo studente.
2. Registrare uno o più corsi frequentati.
3. Inserire i voti ottenuti.
4. Visualizzare la scheda completa di uno studente.
5. Calcolare media, voto massimo e voto minimo.
6. Mostrare tutti i corsi presenti nel sistema.
7. Terminare il programma.


## Modellazione dei dati

Ogni studente deve essere rappresentato tramite un dizionario.

Esempio:

```python
{
    "anagrafica": ("Mario", "Rossi"),
    "corsi": {"Python", "Machine Learning"},
    "voti": [28, 30, 25]
}
```

E' possibile utilizzare un approccio alternativo purchè compatibile con le buone pratiche Python.


## Vincoli

Dimostrare nel codice l'utilizzo di:

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
| Dict | Archivio degli studenti |
| Tuple | Dati anagrafici dello studente |
| Set | Corsi frequentati |
| List | Elenco dei voti |

E' possibile adottare un approccio alternativo in base alla propria implementazione.

## Gestione errori

L'applicazione deve gestire almeno:

- Voti fuori dal range consentito
- Inserimenti non numerici
- Studenti inesistenti
- Corsi duplicati
- Scelte menu non valide

## Esempio di output atteso

Esempio:

```text
Studente: Mario Rossi

Corsi:
- Python
- Machine Learning

Voti:
[28, 30, 25]

Media: 27.67
Voto massimo: 30
Voto minimo: 25
```

## Opzionale

Implementare una o più funzionalità aggiuntive:

- Studente con media più alta
- Corso più frequentato
- Ricerca per nome o cognome
- Esportazione di un report testuale

## Consegna

Consegnare:

- Codice sorgente completo
- Package organizzato correttamente
- Commenti essenziali nelle funzioni principali
- Output di esempio che dimostri il funzionamento dell'applicazione