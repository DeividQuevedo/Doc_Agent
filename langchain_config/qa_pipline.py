import yaml
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

def create_pipeline(vector_store):
    # Configura o modelo LLM
    llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # Ou "gpt-4"
    temperature=0.7,
    openai_api_key = config['OPENAI_API_KEY']
    )

    # Cria o retriever a partir do índice
    retriever = vector_store.as_retriever()

    # Cria o pipeline de QA
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
