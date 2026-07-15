from enum import Enum
from dataclasses import dataclass, field
from uuid import UUID

class Scope(Enum):
    BUILTIN = "B"
    GLOBAL = "G"
    ENCLOSING = "E"
    LOCAL = "L"
    CLASS = "C"

BUILTIN = Scope.BUILTIN
GLOBAL = Scope.GLOBAL
ENCLOSING = Scope.ENCLOSING
LOCAL = Scope.LOCAL
CLASS = Scope.CLASS

@dataclass
class ScopeFrame:
    namespace_id: UUID
    symbol_table: object
    scope_kind: Scope
    start_line: int = 0
    end_line: int = 0
    modified_symbol_scopes: dict = field(default_factory=dict)

@dataclass 
class GlobalScope(ScopeFrame):
    pass

@dataclass
class FunctionScope(ScopeFrame):
    pass

@dataclass
class BranchScope(ScopeFrame):
    pass

@dataclass
class ClassScope(ScopeFrame):
    pass
