import ast

FILE = "tests/types.py"

with open(FILE) as f:
    tree = ast.parse(f.read())


def print_line(tree, lineno, include_attributess):
    # Dump the top-level statement that starts on the given source line.
    for node in tree.body:
        if getattr(node, "lineno", None) == lineno:
            print(ast.dump(node, indent=2, include_attributes=include_attributess))
# Full annotated dump of the raw ast lib output for quick back reference.
print(ast.dump(tree, indent=2, include_attributes=True))

# Example: dump just the nodes on line 2.
# print_line(tree, 21, False)
