import yaml
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

# Carrega a configuração a partir do arquivo YAML
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

def create_pipeline(vector_store):
    """
    Cria um pipeline de QA baseado em recuperação com LangChain.

    Args:
        vector_store (FAISS): Armazenamento vetorial com documentos indexados.

    Returns:
        RetrievalQA: Pipeline configurado para responder perguntas com base nos documentos fornecidos.
    """
    # Configura o modelo LLM (GPT-3.5-turbo ou GPT-4)
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # Troque para "gpt-4" se necessário
        temperature=0.7,  # Controla a criatividade das respostas
        openai_api_key=config['OPENAI_API_KEY']
    )

    # Cria um retriever a partir do armazenamento vetorial
    retriever = vector_store.as_retriever()

    # Cria o pipeline de QA com o modelo LLM e o retriever
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    return qa
