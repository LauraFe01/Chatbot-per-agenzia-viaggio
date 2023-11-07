import pandas as pd
import re
import json

data = pd.read_csv("/Users/lauraferretti/Desktop/Tesi/docUfficiale.csv")
data_frame = pd.DataFrame(data, columns=['conversation_id', 'message_id', 'detailed_message_type', 'message_parts', 'created_time', 'actor_id', 'actor_type' ])
pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern_numTel = r"\b(?:\+39)?\s?(?:(?:(?:0|\(?\d{1,4}\)?)\s?\d{2,5}[\s\./]?\d{3}[\s\./]?\d{3,4})|(?:(?:\d{3}[\s\./]?){3,4}\d{2,3})|(?:(?:\d{1,4}[\s-])?\d{5}))\b"
chat_data = pd.DataFrame(columns = ['message'])
dataM = pd.read_csv("/Users/lauraferretti/Desktop/Tesi/messaggi.csv", sep=',')
data_frameM = pd.DataFrame(dataM, columns=['actor_id', 'conversation_id', 'message_id', 'detailed_message_type', 'created_time', 'actor_type', 'message_parts'], )

def merge_rows():
    global data_frame
    global chat_data
    grouped = data_frame.groupby('conversation_id')
    codiceGruppo = data_frame['conversation_id'][0]
    conv_id = [codiceGruppo]
    for index, elemento in data_frame.iterrows():
        if elemento['conversation_id'] != codiceGruppo:
            conv_id.append(elemento['conversation_id'])
            codiceGruppo = elemento['conversation_id']
    l=0
    list1 = []
    list2 = []

    while l < len(conv_id):
        first = grouped.get_group(conv_id[l])
        print(len(first))
        i = min(first.index)
        while i <= (max(first.index)):
            list1 = []
            stringa_list1 = ''
            print(max(first.index))
            while ( i <= (max(first.index)) and first.loc[i, 'actor_type'] == 'user'):

                first.loc[i, 'message_parts'].replace("\r\n", "; ")
                first.loc[i, 'message_parts'].replace("\r", "; ")
                first.loc[i, 'message_parts'].replace("\n", "; ")

                if len(list1) == 0:
                    message = first.loc[i, 'message_parts']
                    actor = first.loc[i, 'actor_id']
                    conversation = first.loc[i, 'conversation_id']
                    id_mess = first.loc[i, 'message_id']
                    type_message = first.loc[i, 'detailed_message_type']
                    date = first.loc[i, 'created_time']
                    actor_type = first.loc[i, 'actor_type']
                    tot = actor + ',' + conversation + ',' + id_mess + ',' + type_message + ',' + date + ',' + actor_type + ',' + message
                    print(tot)
                    list1.append(tot)

                else:
                    list1.append(first.loc[i, 'message_parts'] )

                print(type(chat_data))
                print("list1", list1)
                i += 1
            stringa_list1 = ' '.join(str(num) for num in list1)
            print(stringa_list1)
            chat_data.loc[len(chat_data)] = stringa_list1
                #print(chat_data)
            list2 = []
            stringa_list2 = ''

            while (i <= (max(first.index)) and first.loc[i, 'actor_type'] == 'agent'):

                first.loc[i, 'message_parts'].replace("\r\n", "; ")
                first.loc[i, 'message_parts'].replace("\r", "; ")
                first.loc[i, 'message_parts'].replace("\n", "; ")

                if len(list2) == 0:
                    message = first.loc[i, 'message_parts']
                    actor = first.loc[i, 'actor_id']
                    conversation = first.loc[i, 'conversation_id']
                    id_mess = first.loc[i, 'message_id']
                    type_message = first.loc[i, 'detailed_message_type']
                    date = first.loc[i, 'created_time']
                    actor_type = first.loc[i, 'actor_type']
                    tot2 = actor + ',' + conversation + ',' + id_mess + ',' + type_message + ',' + date + ',' + actor_type + ',' + message
                    print(tot2)
                    list2.append(tot2)
                else:
                    list2.append(first.loc[i, 'message_parts'])
                i += 1
            stringa_list2 = ' '.join(str(num) for num in list2)

            chat_data.loc[len(chat_data)] = stringa_list2
        l+=1

    chat_data.to_csv('/Users/lauraferretti/Desktop/Tesi/messaggi.csv', index=False)


    '''if first.loc[i, 'actor_type'] == 'agent':
                    first.loc[i, 'message_parts'] = first.loc[i, 'message_parts'] + " " + first.loc[i+1, 'message_parts']
                    print(first.loc[i, 'message_parts'])

                first1 = first.drop(first.index[i+1])
                '''
        #i+=1
    print('-------------------')

#merge_rows()
def sort_dataframe():
    global data_frame

    data_frame = data_frame.sort_values(by=['conversation_id', 'created_time'])
    print(data_frame.to_string())


def modify_message_parts():
    global data_frame
    message = []
    i=0

    for element in data_frame['message_parts']:

        json_data = json.loads(element)
        if 'text' in json_data[0]:
            print(json_data[0]['text']['content'])
            message.append('"'+json_data[0]['text']['content'].replace('\r\n',' ') + '"')
        elif "image" in data_frame['message_parts']:
            message.append('"'+json_data[0]["text"]["content"].replace('\r\n',' ') + '"' )
        else:
            message.append("messaggio non disponibile")
            #data_frame['message_parts'] = message
        i +=1

    data_frame['message_parts'] = message



def delete_rows_message(message):
    global data_frame

    to_drop = data_frame[data_frame['message_parts'] == message]
    print(to_drop.index)
    data_frame = data_frame.drop(to_drop.index)


def delete_rows_type(tipo):
    global data_frame

    to_drop = data_frame[data_frame['detailed_message_type'] == tipo]
    print(to_drop.index)
    data_frame = data_frame.drop(to_drop.index)

    return to_drop

def change_message(tipo):
    global data_frame

    for index, column in data_frame.iterrows():
        if column['detailed_message_type'] == tipo:
            column['message_parts'] = "[{\"text\":{\"content\":\"La problematica sembrerebbe interessare il reparto tecnico, verrà informato immediatamente.\"}}]"


def delete_entire_conversation(to_drop):
    global data_frame

    for index, column in to_drop.iterrows():
        #print(f"Valore della riga {index}: id={column['conversation_id']}")
        for index1, column1 in data_frame.iterrows():
            if column['conversation_id'] == column1['conversation_id']:
                print(column1['conversation_id'])
                #data_frame = data_frame.drop(data_frame.index)

def delete_rows_pattern(pattern):
    rows = []
    global data_frame
    i=0
    for index, column in data_frame.iterrows():
        riga_trovata = re.findall(pattern, column['message_parts'])
        if len(riga_trovata) > 0:
            print(f"{index}", riga_trovata)
            i+=1
            rows.append(index)

    data_frame = data_frame.drop(rows)
    print(i)

#change_message('FRESHDESK_TICKET_CREATE_MESSAGE') #questo comando deve essere eseguito necessariamente prima di delete_rows_pattern
#delete_rows_pattern(pattern_numTel)
#delete_rows_pattern(pattern_email)
#delete_rows_type('STATUS_CHANGE_REOPENED')
#delete_rows_type('STATUS_CHANGE_ASSIGNED')
#delete_rows_type('PRIVATE_NOTE')
#delete_rows_type('OFFLINE_MESSAGE')
#delete_rows_type('AWAY_MESSAGE')
#delete_rows_type('STATUS_CHANGE_RESOLVED')
#modify_message_parts()
#delete_rows_message("messaggio non disponibile")
#sort_dataframe()
#data_frame.to_csv('/Users/lauraferretti/Desktop/Tesi/docUfficiale.csv', index=False )
#merge_rows()
#delete_entire_conversation(delete_rows_type('NORMAL'))
#num_trovato = re.findall(r, column['message_parts'])
#num_trovato1 = re.findall(rg, column['message_parts'])

#def drop_email_numTel ():
#conversation_id = pd.DataFrame(away_message, columns=['conversation_id'])
#rows_to_drop = (away_message['conversation_id'] == df['conversation_id'])
