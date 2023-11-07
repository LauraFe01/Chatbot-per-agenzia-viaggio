# Chatbot-per-agenzia-viaggio
Il seguente chatbot è stato realizzato come progetto di tesi triennale per il corso di laurea Ingegneria Informatica e dell'automazione. 
Lo scopo del sistema qui progettatto è quello di rispondere alle domande dell'utente in maniera corrretta e appropriata. Per la realizzazione è stato utilizzato un dataset contenente vari scambi messaggistici tra agenti ed utenti (per motivi di privacy non è stato possibile inserire il dataset).

## directory data_preprocessing
All'interno della directory data_preprocessing è contenuto il codice utilizzato per il preprocessing dei dati, con lo scopo di eliminare dati sensibili (corrispondenti a determinati pattern) e di rendere i dati conformi con quanto richiesto da Openai per l'uso delle API per effettuare fine tuning. 

## directory csv_to_JSONL
All'interno della directory csv_to_JSONL sono contenuti due file: dataset_training_test e main. 

## main
All'interno di questo file è contenuto il codice utilizzato per la creazione del file JSONL a partire dal dataset in formato csv al fine di effettuare il fine tuning sul modello base ADA di GPT3.

## dataset_training_test
All'interno di questo file è presente il codice utilizzato per estrarre il training set e il testing set dal dataset.

## chatbot_tesi
All'interno di questo file è presente il codice per l'uso del chatbot, implementato utilizzando diverse librerie e strumenti, tra cui OpenAI, GPT (Generative Pre-trained Transformer) per la generazione del testo, e Gradio per l'interfaccia utente.
