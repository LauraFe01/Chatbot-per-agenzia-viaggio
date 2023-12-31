!pip install openai

!pip install gpt_index==0.4.15

!pip install langchain==0.0.96

!pip install gradio

from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import sys
import openai
import os
import langchain

#interfaccia ufficiale, creare ogni volta una cartella "docs" con all'interno i file di knowledge base
openai.api_key= os.getenv("OPENAI_API_KEY", " ")
os.environ["OPENAI_API_KEY"] = " "

# Funzione per costruire l'indice
def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)


    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.6, model_name="ada:ft-personal-2023-07-11-18-47-52", max_tokens=num_outputs))
    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

messages=[]

def add_text(history, text):
    global messages
    history = history + [(text,'')]
    messages = messages + [{"role":'user', 'content': text }]
    return history, ""

def generate_response(history):
    global messages, cost

    # Concatena tutti i messaggi passati per creare la conversazione come prompt
    conversation = "\n".join(msg["content"]+" ->" for msg in messages)
    print("domanda", conversation)

    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(conversation, response_mode="compact")

    messages.append({"role": 'assistant', "content": response.response})
    print("Risposta:", response.response)

    for char in response.response:
        history[-1][1] += char

    chatbot.value = history[-1][1]

    yield history


with gr.Blocks() as demo:

    chatbot = gr.Chatbot(value=[], elem_id="chatbot")
    with gr.Row():
        with gr.Column(scale=1):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Inserire qui la domanda",
            )

    txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=True).then(
            generate_response, inputs =[chatbot],outputs = chatbot)

index = construct_index("/content/docs")
demo.queue()
demo.launch(debug=True)
