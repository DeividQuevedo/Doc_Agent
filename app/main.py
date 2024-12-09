import sys
import os

# Mostra os caminhos atuais no sys.path
print("PYTHONPATH:", sys.path)

# Adiciona o diretório raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
print("Novo PYTHONPATH:", sys.path)

from langchain_config.document_loarder import load_documents
from langchain_config.qa_pipline import create_pipeline

def main():
    folder_path = input("Digite o caminho da pasta com documentos (.txt): ").strip()
    index = load_documents(folder_path)

    if not index:
        print("Nenhum documento foi carregado. Encerrando.")
        return

    while True:
        query = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
        if query.lower() == "sair":
            print("Encerrando... Até logo!")
            break

        pipeline = create_pipeline(index)
        response = pipeline.run(query)
        print("\nResposta:", response)

if __name__ == "__main__":
    main()
