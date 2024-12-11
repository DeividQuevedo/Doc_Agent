import sys
import os

# Mostra os caminhos atuais no sys.path
print("PYTHONPATH:", sys.path)

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
sys.path.append(r'C:\Users\Deivid\Desktop\Agente\doc_agent\Lib\site-packages')

print("Novo PYTHONPATH:", sys.path)

import streamlit as st
from langchain_config.document_loader import load_documents
from langchain_config.qa_pipline import create_pipeline


st.title("Agente de Documentos")
folder_path = st.text_input("Digite o caminho da pasta com documentos (.txt):")

if folder_path:
    index = load_documents(folder_path)
    print(f"Tipo de index: {type(index)}")
    print(f"Atributos de index: {dir(index)}")
    print(f"Atributos de docstore: {dir(index.docstore)}")  # Inspecionar docstore
    print(f"Conteúdo de docstore: {index.docstore}")  # Visualizar conteúdo
    st.success(f"{len(index.docstore._dict)} documentos carregados com sucesso!")




    query = st.text_input("Digite sua pergunta:")
    if query:
        pipeline = create_pipeline(index)
        response = pipeline.invoke({"query": query})
        st.write("Resposta:", response)
