from modules.type_lattice import Unassigned

class VariableIndexStore():
    def __init__(self, identity):
        self.identity = identity
        self.store = {0: Unassigned}

    def update(self, line, _type):
        self.store[line] = _type
    
    def type_at(self, line):
        latest = None

        for assignment_line, _type in self.store.items():
            if assignment_line > line:
                break
            latest = _type

        return latest
    
    def __str__(self):
        rows = "\n".join(
            f"    [{line}: {getattr(_type, '__name__', _type)}]"
            for line, _type in self.store.items()
            if _type is not Unassigned
        )
        header = f"  variable_store({self.identity})"
        return f"{header}\n{rows}" if rows else f"{header}\n    [empty store]"

    def __repr__(self):
        return f"VariableTypeStore(identity={self.identity!r}, store={self.store!r})"
        

