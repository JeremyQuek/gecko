import ast
from modules.variable_program_map import VariableProgramMap

if __name__=="__main__":
    variable_map = VariableProgramMap("tests/control_flow.py")
    variable_map.trace()
    print(variable_map)
