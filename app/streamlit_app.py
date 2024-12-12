import sys
import os
import streamlit as st
from pathlib import Path
import shutil

# Ajustar o PYTHONPATH para importar os módulos
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from langchain_config.document_loader import load_documents
from langchain_config.qa_pipline import create_pipeline

# Configuração da página
st.set_page_config(page_title="Agente de Documentos", layout="wide")
st.markdown("<h1 style='text-align: center;'>Agente de Documentos</h1>", unsafe_allow_html=True)

# Inicializar histórico, índice e input na sessão
if "history" not in st.session_state:
    st.session_state["history"] = []

if "index" not in st.session_state:
    st.session_state["index"] = None

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""  # Inicializar o estado do input do usuário

# Função para salvar arquivos no diretório temporário
def save_uploaded_files(uploaded_files):
    temp_dir = Path("temp_files")
    temp_dir.mkdir(exist_ok=True)  # Criar o diretório temporário, se não existir

    for uploaded_file in uploaded_files:
        temp_file_path = temp_dir / uploaded_file.name
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    return str(temp_dir)  # Retornar o caminho do diretório temporário

# Função para limpar arquivos temporários
def clear_temp_dir(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)

# Função para enviar a pergunta (chamado ao pressionar Enter)
def handle_query():
    query = st.session_state["user_input"]
    if query:
        try:
            pipeline = create_pipeline(st.session_state["index"])
            response = pipeline.run({"query": query})
            st.session_state["history"].append((query, response))  # Adicionar ao histórico
            st.session_state["user_input"] = ""  # Limpar o campo de entrada após envio
            st.rerun()  # Atualizar a interface
        except Exception as e:
            st.error(f"Erro ao processar a pergunta: {e}")

# Divisão do layout principal em três colunas (25/50/25)
col1, col2, col3 = st.columns([1, 2, 1], gap="large")

# Coluna da bandeja lateral esquerda
with col1:
    st.markdown("<h3 style='text-align: center;'>Opções</h3>", unsafe_allow_html=True)
    st.info("Espaço reservado para informações adicionais ou outras funcionalidades.")

# Coluna principal do Chat (central)
with col2:
    st.markdown("<h3 style='text-align: center;'>Chat com o Agente</h3>", unsafe_allow_html=True)

    # Histórico de Conversas com barra de rolagem invisível
    st.markdown(
        """
        <div style="height: 400px; overflow-y: auto; padding: 10px; border: 1px solid #ddd;">
        """,
        unsafe_allow_html=True,
    )
    if st.session_state["history"]:
        for user_msg, agent_msg in st.session_state["history"]:
            st.markdown(
                f"""
                <div style='background-color: #d1f7d6; padding: 10px; margin: 10px 0; border-radius: 10px; text-align: right; width: 60%; margin-left: auto;'>
                    <strong>Você:</strong> {user_msg}
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div style='background-color: #d1e7ff; padding: 10px; margin: 10px 0; border-radius: 10px; text-align: left; width: 60%; margin-right: auto;'>
                    <strong>Agente:</strong> {agent_msg}
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("Nenhuma conversa disponível. Envie sua primeira pergunta.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Input do usuário abaixo do histórico
    st.text_input(
        "Digite sua pergunta:",
        value=st.session_state["user_input"],
        key="user_input",
        on_change=handle_query,  # Função chamada ao pressionar Enter
    )

# Coluna da bandeja lateral direita
with col3:
    st.markdown("<h3 style='text-align: center;'>Configuração dos Documentos</h3>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("Envie seus arquivos:", type=["txt", "pdf", "docx"], accept_multiple_files=True)

    if uploaded_files:
        try:
            # Processar arquivos automaticamente
            temp_dir = save_uploaded_files(uploaded_files)
            st.session_state["index"] = load_documents(temp_dir)  # Passar o diretório para `load_documents`
            st.success(f"{len(os.listdir(temp_dir))} documentos processados com sucesso!")
            clear_temp_dir(temp_dir)  # Limpar os arquivos após o processamento
        except Exception as e:
            st.error(f"Erro ao processar os arquivos: {e}")
