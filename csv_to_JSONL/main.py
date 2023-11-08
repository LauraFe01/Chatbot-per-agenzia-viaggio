import json

import pandas as pd

#funzione usata per eliminare dal file tutte le conversazioni che sono state iniziate da un agent
def drop_agent(data_frame):
    value_to_count = 'agent'

    count = data_frame.groupby(' conversation_id')[' actor_type'].first().eq(value_to_count).sum()
    print(f"Il valore {value_to_count} compare {count} volte tra i messaggi.")

    mask = data_frame.groupby(' conversation_id')[' actor_type'].first().eq(value_to_count)

    filtered_df = data_frame.drop(data_frame[data_frame[' conversation_id'].map(mask)].index)

    print(data_frame[data_frame[' conversation_id'].map(mask)].index)
    #print(filtered_df)
    #filtered_df.to_csv('/path/Documento.csv', index=False)


def odd_rows(data_frame):
    group_counts = data_frame.groupby(' conversation_id').size()

    # Filtraggio dei conversation_id con un numero dispari di righe
    odd_counts = group_counts[group_counts % 2 != 0]

    # Stampa dei conversation_id con un numero dispari di righe
    print(odd_counts.index)
    #aggiungo al dataframe solo le conversazioni con un numero pari di righe
    modified_df = data_frame.drop(data_frame[data_frame[' conversation_id'].isin(odd_counts.index)].groupby(' conversation_id').tail(1).index)
    #modified_df.to_csv('/path/Documento.csv', index=False)
    #print(data_frame[data_frame[' conversation_id'].isin(odd_counts.index)].groupby(' conversation_id').tail(1).index)

def csv_to_dataFrame(file_path):

    data = pd.read_csv(file_path)
    data_frame = pd.DataFrame(data)
    print(data_frame.columns)
    return data_frame

#genero il file JSONL ufficiale che poi ho diviso in training e test set
def dataFrame_to_JSONL(data_frame, fileJSON_path):
        prompt_message = ""
        completion_message = ""
        i=0

        while(i <= max(data_frame.index) ):
            if data_frame.loc[i, ' actor_type'] == "user":
                prompt_message = data_frame.loc[i, ' message_parts']
            elif data_frame.loc[i, ' actor_type'] == 'agent':
                completion_message = data_frame.loc[i, ' message_parts']

            if prompt_message != "" and completion_message != "" :
                data = {
                    "prompt": prompt_message,
                    "completion": completion_message
                }
                with open(fileJSON_path, 'a') as file:
                    json.dump(data, file)
                prompt_message = ""
                completion_message = ""
            i+=1



def modifyJSONL(fileJSON):

    with open(fileJSON, 'r') as file:
        contenuto = file.read()

    contenuto_modificato = contenuto.replace('}{', "}\n{")

    with open(fileJSON, 'w') as file:
        file.write(contenuto_modificato)

dataF = csv_to_dataFrame("/path/Documento.csv")
#dataF = csv_to_dataFrame("/path/Documento.csv")     #usato per testare se il file fosse corretto
#odd_rows(dataF)
#dataF = csv_to_dataFrame("/path/Documento.csv")
#drop_agent(dataF)
dataFrame_to_JSONL(dataF, "file.jsonl")
modifyJSONL("file.jsonl")


