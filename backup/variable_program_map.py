import ast
from modules.variable_type_store import VariableTypeStore
from modules.type_lattice import Unassigned

class VariableProgramMap():
    def __init__(self, file: str) -> None:
        self.file = file
        self.file_tree = self.build_file_tree(self.file)
        self.program_map = {}
    
    def trace(self, code_block) -> None:
        analyze_code_block(self.file_tree.body)
           
     def analyze_code_block():
        for node in code_block:
            # Control flow
            if (isinstance(node, ast.If) or isinstance(node)):
                if_block = analyze_code_block(node.body)
                else_block = analyze_code_block(node.orelse)

            # Assign statement
            elif (isinstance(node, ast.AugAssign) or isinstance(node, ast.Assign)):
                if isinstance(node, ast.Assign):
                    # Handles multi-assignment
                    if isinstance(node.targets[0], ast.Tuple):
                        for right_expr,left_expr in zip(node.targets[0].elts, node.value.elts):
                            self.evaluate_expr(right_expr, left_expr)
                    else:
                        right_expr = node.targets[0] 
                        left_expr =  node.value
                        self.evaluate_expr(right_expr, left_expr)

                elif isinstance(node, ast.AugAssign):
                    right_expr = node.target
                    left_expr =  node.value
                    self.evaluate_expr(right_expr, left_expr)


    def evaluate_expr(self, right_expr, left_expr):
        line = right_expr.lineno
        identifier = right_expr.id
        if identifier not in self.program_map:
            self.program_map[identifier] = VariableTypeStore(identifier)
        
        raw_type = Unassigned()

        if isinstance(left_expr, ast.Constant):
            raw_obj = ast.literal_eval(left_expr)
            raw_type = type(raw_obj)

        elif isinstance(left_expr, ast.Name):
            # TODO
            # Add checks if the leftmost identifier doesnt exist in the program! (Users can make mistakes in their code)
            left_identifier = left_expr.id 
            left_identifier_variable_store = self.program_map[left_identifier]
            left_identifier_type = left_identifier_variable_store.type_at(line)
            raw_type = left_identifier_type
        # TODO
        # requires control flow analysis
        elif isinstance(left_expr, ast.Call):
            pass

        if not isinstance(raw_type, Unassigned):
            self.program_map[identifier].update(line, raw_type)

    def build_file_tree(self, file: str) -> ast.Module:
        with open(file) as f:
            tree = ast.parse(f.read())
            return tree

    def __str__(self) -> str:
        return "\n\n".join(str(store) for store in self.program_map.values())

    def __repr__(self) -> str:
        return f"VariableProgramMap(file={self.file!r}, program_map={self.program_map!r})"
