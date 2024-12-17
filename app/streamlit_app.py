import sys
import os
import shutil
import streamlit as st
from pathlib import Path
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

# Ajustar o PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
from langchain_config.document_loader import load_documents
from langchain_config.qa_pipline import create_pipeline

# Configuração da página
st.set_page_config(page_title="Agente de Documentos", layout="centered")

# Inicializar histórico de mensagens na sessão
if "store" not in st.session_state:
    st.session_state["store"] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """Obtém o histórico de mensagens para uma sessão específica."""
    if session_id not in st.session_state["store"]:
        st.session_state["store"][session_id] = InMemoryChatMessageHistory()
    return st.session_state["store"][session_id]

# Criar o histórico para esta sessão
session_id = "default_session"
history = get_session_history(session_id)

# Funções auxiliares
def save_uploaded_files(uploaded_files):
    temp_dir = Path("temp_files")
    temp_dir.mkdir(exist_ok=True)
    for uploaded_file in uploaded_files:
        temp_file_path = temp_dir / uploaded_file.name
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    return str(temp_dir)

def clear_temp_dir(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)

# CSS personalizado para o header fixo
st.markdown(
    """
    <style>
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 15%;
        background-color: var(--background-color);
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        padding: 40px 0;
        z-index: 1000;
        color: var(--text-color);
    }

    /* Configuração padrão (tema claro) */
    :root {
        --background-color: #ffffff; /* Branco */
        --text-color: #000000; /* Preto */
    }

    /* Configuração para tema escuro */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #0E1117; /* Preto */
            --text-color: #ffffff; /* Branco */
        }
    }
    .spacer {
        margin-top: 80px; /* Compensa a altura do header */
    }
    </style>
    <div class="fixed-header">Agente de Documentos</div>
    """,
    unsafe_allow_html=True,
)

# Espaço abaixo do header fixo
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# Sidebar para upload de documentos
with st.sidebar:
    st.subheader("Upload de Documentos")
    uploaded_files = st.file_uploader(
        "Envie seus arquivos:", type=["txt", "pdf", "docx"], accept_multiple_files=True
    )

    if uploaded_files:
        try:
            temp_dir = save_uploaded_files(uploaded_files)
            st.session_state["index"] = load_documents(temp_dir)
            st.success("Documentos processados com sucesso!")
            clear_temp_dir(temp_dir)
        except Exception as e:
            st.error(f"Erro ao processar os arquivos: {e}")

# Layout principal
#st.markdown("<h2 style='text-align: center;'>Histórico de Chat</h2>", unsafe_allow_html=True)

# Histórico de chat
for message in history.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# Entrada do usuário
user_input = st.chat_input("Digite sua pergunta:")

if user_input:
    # Adicionar mensagem do usuário ao histórico
    history.add_message(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Criar resposta do agente
        pipeline = create_pipeline(st.session_state.get("index"))
        response = pipeline.invoke({"query": user_input})

        # Garantir que a resposta seja string
        response_content = response if isinstance(response, str) else str(response)

        # Extrair apenas o conteúdo após 'result: '
        if "result" in response_content:
            response_content = response_content.split("'result':")[1].strip(" {}'")

        # Adicionar resposta ao histórico
        history.add_message(AIMessage(content=response_content))
        with st.chat_message("assistant"):
            st.markdown(response_content)
    except Exception as e:
        st.error(f"Erro ao processar a mensagem: {e}")
