import random


#usato per estrarre le domande per fare training e test, il file training set lo uso per fare fine tuning
# Apri il file in modalità di lettura
with open("file_json_26-05_prepared_prepared.jsonl", 'r') as file:
    # Leggi tutte le righe del file
    righe = file.readlines()

# Controlla se il numero di righe nel file è inferiore a 1400
if len(righe) < 1400:
    print("Il file contiene meno di 1400 righe.")
else:
    # Estrai casualmente 1400 indici unici
    indici_casuali = random.sample(range(len(righe)), 1400)

    # Crea una nuova lista di righe estratte casualmente
    righe_estratte = [righe[indice] for indice in indici_casuali]

    # Rimuovi le righe estratte dal file originale
    righe_restanti = [riga for indice, riga in enumerate(righe) if indice not in indici_casuali]

    # Salva le righe rimanenti nel file originale
    with open('training_set.jsonl', 'w') as file_modificato:
        file_modificato.writelines(righe_restanti)

    # Salva le righe estratte in un nuovo file
    with open('test_set1.jsonl', 'w') as nuovo_file:
        nuovo_file.writelines(righe_estratte)

    print("Estrazione completata. Le righe estratte sono state salvate in 'righe_estratte.txt'. Le righe estratte sono state rimosse dal file originale.")

