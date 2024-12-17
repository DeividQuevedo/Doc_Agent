from langgraph.graph import LangGraph, Node
from langchain_config.document_loader import DocumentLoader
from langchain_config.text_splitter import TextSplitter
from langchain_config.vector_store import VectorStore
from langchain_config.qa_pipeline import QAPipeline

class GraphBuilder:
    @staticmethod
    def build_graph():
        graph = LangGraph()
        graph.add_node(Node(name="Load Document", func=DocumentLoader.load))
        graph.add_node(Node(name="Split Text", func=TextSplitter.split))
        graph.add_node(Node(name="Create Vector Store", func=VectorStore.create))


        
        graph.add_node(Node(name="QA Pipeline", func=QAPipeline.build))
        
        graph.add_edge("Load Document", "Split Text")
        graph.add_edge("Split Text", "Create Vector Store")
        graph.add_edge("Create Vector Store", "QA Pipeline")
        
        graph.set_input_node("Load Document")
        graph.set_output_node("QA Pipeline")
        
        return graph
