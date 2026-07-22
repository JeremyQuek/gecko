import ast
from collections import defaultdict

import ast_custom
from ast_custom import *
from lexical_environment import LexicalEnvironment

class Node():
    def __init__(self, block = None, enviroment = None):
        self.block = block
        self.enviroment = enviroment
        self.next = []

class TerminalNode(Node): pass
class EntryNode(TerminalNode): pass 
class ExitNode(TerminalNode):pass 

# Regular code node
class BodyNode(Node):pass
# Splinters into a graph that join
class ControlFlowNode(Node):pass
# Splinters into a subgraph
class DefinitionNode(Node): pass


class ControlFlowGraph():
    mapping= {
        ast.FunctionDef : DefinitionNode,
        ast.ClassDef : DefinitionNode,
        ast.For: ControlFlowNode,
        ast.While: ControlFlowNode,
        ast.If: ControlFlowNode,
        ast_custom.Body: BodyNode,
        ast_custom.FunctionBody: BodyNode,
        ast_custom.ClassBody: BodyNode,
        ast_custom.IfBody: BodyNode,
        ast_custom.ElseBody: BodyNode,
        }

    def __init__(self):
        self.entry = EntryNode()
        self.nodes = {self.entry: self.entry}
        self.edges=[]

        # For pretty print
        self._id_counter = 0
        self._node_ids = {id(self.entry): 0}
    
    def insert(self, parent: ast.AST, child: ast.AST)->None:
        u = self.entry if parent is None else self._get_node(parent) 
        v = self._get_node(child)
        u.next.append(v)
        self.edges.append([u,v])


    def _get_node(self, ast_node: ast.AST) -> Node:
        if ast_node not in self.nodes:
            u = self._create_node(ast_node)
            self.nodes[ast_node] = u 
        else:
            u = self.nodes[ast_node]
        return u

    # returns the correct Node Type,
    def _create_node(self, ast_node: ast.AST) -> Node:
        ast_type = type(ast_node)
        node_class = self.mapping[ast_type]
        node = node_class(block=ast_node)

        # For pretty print
        self._id_counter += 1
        self._node_ids[id(node)] = self._id_counter
        return node

    """
    Prints the edge list in a format pasteable into 
    graphonline.top/create_graph_by_edge_list for visual debugging.
    """
    def _pretty_print(self):
        
        for u, v in self.edges:
            print(f"{self._label(u)}-{self._label(v)}")

    def _label(self, node: Node) -> str:
        nid = self._node_ids[id(node)]
        if isinstance(node, EntryNode):
            return f"Entry({nid})"
        if isinstance(node, ExitNode):
            return f"Exit({nid})"
        block = node.block
        if isinstance(block, IfBody):
            return f"IfBody({nid})"
        if isinstance(block, ElseBody):
            return f"ElseBody({nid})"
        if isinstance(block, FunctionBody):
            return f"FuncBody({nid})"
        if isinstance(block, ClassBody):
            return f"ClassBody({nid})"
        if isinstance(block, Body):
            return f"Body({nid})"
        if isinstance(block, ast.FunctionDef):
            return f"FuncDef({nid})"
        if isinstance(block, ast.ClassDef):
            return f"ClassDef({nid})"
        if isinstance(block, ast.If) or isinstance(block, ast.For) or isinstance(block, ast.While):
            return f"Branch({nid})"
        return f"Node({nid})"
    


