GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B", "H"],
    "E": ["B", "H"],
    "F": ["C", "I"],
    "G": ["C", "I"],
    "H": ["D", "E"],
    "I": ["F", "G"]
}

GRAPH_TEST = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': [],
}

class Stack:

    def __init__(self, stack_data = []):
        self.stack_data = stack_data

    def push(self, data):
        self.stack_data.append(data)
        return self

    def pop(self):
        return self.stack_data.pop()
    
    def peek(self):
        return self.stack_data[-1]

    def is_empty(self):
        return bool(len(self.stack_data))

    def size(self):
        return len(self.stack_data)
