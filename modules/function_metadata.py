import ast
from uuid import UUID
from collections import defaultdict


class FunctionMetadata:
    def __init__(self, ast_node: ast.FunctionDef, namespace_id: UUID, closure_environment: list[tuple[UUID, defaultdict]] = []) -> None:
        self.namespace_id = namespace_id
        self.ast_node = ast_node
        self.closure_environment = closure_environment

        self.call_args_cache: dict = {}