import sys
import os
import streamlit as st

# Ajustar o PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
sys.path.append(r'C:\Users\Deivid\Desktop\Agente\doc_agent\Lib\site-packages')

from langchain_config.document_loader import load_documents
from langchain_config.qa_pipline import create_pipeline

# Configuração da página
st.set_page_config(page_title="Agente de Documentos", layout="wide")
st.title("Agente de Documentos")

# Inicializar histórico na sessão
if "history" not in st.session_state:
    st.session_state["history"] = []

# Layout principal com 3 colunas
col1, col2, col3 = st.columns([1, 3, 1], gap="medium")

# Coluna da direita para configurações de arquivos
with col3:
    st.markdown("### Configuração dos Documentos")
    folder_path = st.text_input("Digite o caminho da pasta com documentos (.txt):", "")
    uploaded_files = st.file_uploader("Envie seus arquivos:", type=["txt", "pdf", "docx"], accept_multiple_files=True)

    if folder_path:
        try:
            index = load_documents(folder_path)
            st.success(f"{len(index.docstore._dict)} documentos carregados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao carregar documentos: {e}")

    if uploaded_files:
        st.markdown("### Lista de Arquivos Carregados:")
        for uploaded_file in uploaded_files:
            st.write(uploaded_file.name)

# Coluna central para o chat
with col2:
    st.markdown("### Chat com o Agente")
    chat_container = st.container()
    with chat_container:
        for user_message, bot_message in st.session_state["history"]:
            col_user, col_bot = st.columns([1, 1], gap="small")
            with col_bot:  # Mensagem do sistema
                st.markdown(
                    f"<div style='background-color: #f1f1f1; padding: 10px; border-radius: 10px;'>{bot_message}</div>",
                    unsafe_allow_html=True,
                )
            with col_user:  # Mensagem do usuário
                st.markdown(
                    f"<div style='background-color: #d1f1d1; padding: 10px; border-radius: 10px; text-align: right;'>{user_message}</div>",
                    unsafe_allow_html=True,
                )

# Input na parte inferior central
with col2:
    st.markdown("### Faça uma pergunta:")
    query = st.text_input("Digite sua pergunta:", key="query_input")

    if query:
        try:
            if folder_path:
                pipeline = create_pipeline(index)
                response = pipeline.invoke({"query": query})
                bot_response = response["result"]
            else:
                bot_response = "Por favor, carregue documentos primeiro."

            # Atualizar histórico
            st.session_state["history"].append((query, bot_response))
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao processar a pergunta: {e}")
