# Chatbot_per_agenzia_viaggio
Questo chatbot è stato sviluppato come parte di un progetto di tesi triennale per il corso di laurea in Ingegneria Informatica e dell'Automazione. L'obiettivo principale di questo sistema è fornire risposte accurate ed appropriate alle domande degli utenti sul dominio specifico. Il chatbot è stato realizzato effettuando in una prima fase il fine tuning sul modello base ADA di GPT3 e successivamente è stata passata una knowledge base tramite l'uso di GPT Index. Per garantire la privacy, non è possibile fornire il dataset originale con cui è stato effettuato il fine tuning.

## Processo realizzativo

### Preprocessing dei dati

Per realizzare il sistema chatbot, innanzitutto è stato effettuato un accurato preprocessing dei dati a disposizione. 
Il dataset utilizzato è costituito da un file csv contenente i messaggi inviati dagli utenti e le risposte fornite dagli agenti, in più altre informazioni tra cui l'id della conversazione di riferimento e il ruolo del mittente del messaggio (USER/AGENT). 

La fase di data preprocessing è stata di cruciale importanza al fine di eliminare tutti i dati sensibili e di ristrutturare il dataset per renderlo conforme con quanto richiesto dall'API di OpenAI.

All'interno della directory **data_preprocessing** è presente il codice python, costituito da varie funzioni, utilizzato per effettuare il preprocessing dei dati.

### Creazione file JSONL

Il passo successivo è consistito nel creare un file JSONL con coppie prompt-completion, le domande dei clienti erano corrispondenti ai prompt e le risposte degli agenti alle completion. 

All'interno della directory **csv_to_JSONL** è presente il codice python utilizzato per realizzare il file JSONL a partire dal file csv e il codice utilizzato per la suddivisione del dataset in training set e testing set.

### Realizzazione del fine tuning

Una volta creato il file JSONL e validato è stato effettuato il fine tuning sul modello ADA di GPT3 utilizzando l'API messa a disposizione da OpenAI

### Trasferimento della knowledge base e creazione ddell'interfaccia grafica
Il chatbot,infine, è stato dotato di una knowledge base attraverso l'utilizzo di GPT Index.
Questa knowledge base fornisce al chatbot un contesto per generare risposte più pertinenti e precise. 
Inoltre, è stata realizzata un'interfaccia grafica, tramite l'uso di Gradio, per l'interazione degli utenti con il chatbot, rendendo l'esperienza più intuitiva e user-friendly.
 
## Uso del chatbot
All'interno del file **chatbot_tesi.py** è riportato il codice per utilizzare il chatbot creato. Prima dell'utilizzo bisogna creare, all'interno della directory contenente lo script, una cartella docs contenente dei file in formato .txt con informazioni inerenti alle strutture ricettive desiderate. Questi documenti costituiranno la knowledge base a cui il chatbot attingerà per rispondere alle domande degli utenti.

## Autore
Laura Ferretti

