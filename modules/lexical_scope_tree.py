class LexicalScopeTree():
    def __init__(self):
        self.tree = []
    
    def insert(self, entry):
        self.tree.append(entry)