class Concrete():
    pass

class Unassigned():
    pass
    
class Unknown():
    pass

class Union():
    def __init__(self):
        self.members = set()

    def __str__(self):
        return " | ".join(
            sorted(
                getattr(m, "__name__", str(m))
                for m in self.members
                if m is not Unassigned
            )
        )

    def __repr__(self):
        return f"Union({{{self.__str__()}}})"

    def __eq__(self, other):
        if not isinstance(other, Union):
            return NotImplemented
        return self.members == other.members

    def __hash__(self):
        return hash(frozenset(self.members))

def join(a, b):
    # ⊥ disappears
    if isinstance(a, Unassigned):
        return b
    if isinstance(b, Unassigned):
        return a
    # ⊤ absorbs
    if isinstance(a, Unknown) or isinstance(b, Unknown):
        return Unknown()
    # identical — no union needed
    if a == b:
        return a
    # case 2a: concrete + concrete
    if not isinstance(a, Union) and not isinstance(b, Union):
        u = Union()
        u.members = {a, b}
        return u
    # case 2b: one is Union, one is concrete
    if isinstance(a, Union) and not isinstance(b, Union):
        u = Union()
        u.members = a.members | {b}
        return u
    if isinstance(b, Union) and not isinstance(a, Union):
        u = Union()
        u.members = b.members | {a}
        return u
    # case 2c: both Union
    u = Union()
    u.members = a.members | b.members
    return u
    