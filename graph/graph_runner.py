class GraphRunner:
    def __init__(self, graph):
        self.graph = graph
    
    def run(self, inputs):
        return self.graph.run(inputs)
