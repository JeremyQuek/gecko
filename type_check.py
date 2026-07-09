import argparse

from modules.variable_program_map import VariableProgramMap

def main():
    parser = argparse.ArgumentParser(
        description="Static Type Analysis Engine"
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Python source file to analyse",
    )

    args = parser.parse_args()

    variable_map = VariableProgramMap(args.file)
    variable_map.trace()
    print(variable_map)


if __name__ == "__main__":
    main()