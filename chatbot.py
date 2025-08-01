import os 
import openai
import streamlit as st 

openai.api_key = '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'

def gerar_resposta(entrada):
    resposta = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'Você irá me recomendar um filme ou série baseado no que eu disser. forneça nome, ano de lançamento, gênero, avaliação do tmdb, elenco, diretor e uma breve sinopse, e também quantidade de temporadas caso seja uma série. Pegando sempre as informações do TMDB. '},
            {'role': 'user', 'content': entrada}
        ],
        max_tokens=500,
        temperature=0.7,
    )   
    return resposta.choices[0].message['content']

st.set_page_config(layout='centered')
st.image("image.png", width=300)
st.title('Pernalonga cinéfilo - Chatbot')
st.write('Eu sou o Pernalonga, um chatbot cinéfilo que irá te recomendar um filme ou série baseado no que você me disser.')

question = st.text_input('Digite o que deve ter no que você deseja assistir:', placeholder='Exemplo: quero assistir uma comédia dos anos 1950 que tenha a Bette Davis.')

if question:
    resposta = gerar_resposta(question)
    st.text_area('Resposta do Pernalonga:', value=resposta, height=300)
    

