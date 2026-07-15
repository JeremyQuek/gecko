from enum import Enum
from dataclasses import dataclass
from uuid import UUID

class Scope(Enum):
    BUILTIN = "B"
    GLOBAL = "G"
    ENCLOSING = "E"
    LOCAL = "L"

@dataclass
class ScopeFrame:
    namespace_id: UUID
    symbol_table: object
    scope_kind: Scope
