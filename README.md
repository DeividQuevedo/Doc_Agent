# Document_Agent
# Documentação do Projeto

Este documento detalha as dependências necessárias para executar o projeto e fornece instruções sobre como configurar o ambiente.

---

## **Dependências do Projeto**

### **1. Frameworks para Modelos de Linguagem**

#### **LangChain (v0.3.1)**
- Um framework modular para criar pipelines baseados em LLMs (Modelos de Linguagem de Grande Escala).
- Permite integração com múltiplas fontes de dados e ferramentas de armazenamento vetorial.
- **Instalação**: `pip install langchain==0.3.1`

#### **LangChain Community**
- Versão comunitária do LangChain, que adiciona conectores e integrações mais recentes.
- **Instalação**: `pip install langchain-community`

#### **OpenAI (v0.27.10)**
- Cliente oficial para interagir com a API da OpenAI.
- Usado para acessar modelos como GPT-4 e GPT-3.5.
- **Instalação**: `pip install openai==0.27.10`

---

### **2. Interface com o Usuário**

#### **Streamlit (v1.27.0)**
- Framework rápido e intuitivo para criar interfaces web interativas com Python.
- **Instalação**: `pip install streamlit==1.27.0`

---

### **3. Logs e Configurações**

#### **Loguru (v0.6.0)**
- Biblioteca de logging avançada, com suporte a logs formatados e rastreamento dinâmico.
- **Instalação**: `pip install loguru`

---

### **4. Armazenamento Vetorial**

#### **FAISS-CPU**
- Ferramenta para armazenamento e busca em espaços vetoriais, otimizada para CPU.
- Usada para indexação e busca de documentos no projeto.
- **Instalação**: `pip install faiss-cpu`

---

### **5. Utilitários e Simulações**

#### **NumPy (v1.26.4)**
- Biblioteca essencial para manipulação de arrays e cálculos vetoriais.
- **Instalação**: `pip install numpy==1.26.4`

#### **Tiktoken**
- Biblioteca para tokenização eficiente de textos, compatível com modelos da OpenAI.
- **Instalação**: `pip install tiktoken`

#### **Pydantic**
- Biblioteca para validação de dados e tipagem forte em Python.
- **Instalação**: `pip install pydantic`

---

### **6. Configurações Ambientais**

#### **Python-Dotenv**
- Biblioteca para gerenciar variáveis de ambiente a partir de arquivos `.env`.
- **Instalação**: `pip install python-dotenv`

---

## **Configuração do Ambiente**

### **1. Criar um Ambiente Virtual**
Recomenda-se criar um ambiente virtual para instalar as dependências sem interferir no sistema global.

```bash
python -m venv env
source env/bin/activate  # No Windows: .\env\Scripts\activate
```

### **2. Instalar as Dependências**
Use o arquivo `requirements.txt` para instalar todas as dependências necessárias:

```bash
pip install -r requirements.txt
```

---

## **Arquivo `requirements.txt` **

```plaintext
langchain==0.3.1
langchain-community
openai==0.27.10
streamlit==1.27.0
loguru==0.6.0
faiss-cpu
numpy==1.26.4
tiktoken
pydantic
python-dotenv
pypdf2==3.0.1
python-docx==1.1.2         
```

