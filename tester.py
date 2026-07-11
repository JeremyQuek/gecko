from pathlib import Path
import argparse

from modules.variable_program_map import VariableProgramMap


class Tester:
    def __init__(self, tests_root: Path, directories: list[Path], file_prefix: str | None):
        self.tests_root = tests_root
        self.directories = directories
        self.file_prefix = file_prefix

    def run(self) -> None:
        if self.file_prefix:
            self.run_test_prefix(self.file_prefix)
        else:
            self.run_test_dirs(self.directories)

    def run_test_dirs(self, directories: list[Path]) -> None:
        passed = 0
        total = 0

        for directory in directories:
            p, t = self.run_test_dir(directory)
            passed += p
            total += t

        print(f"\nPassed {passed}/{total} tests.")

    def run_test_dir(self, directory: Path):
        files = sorted(directory.glob("*.py"))

        if not files:
            return 0, 0

        print(f"Running {directory.name}...\n")

        passed = 0
        total = 0

        for file in files:
            total += 1
            if self.run_test_file(file, directory):
                passed += 1

        print()

        return passed, total

    def run_test_prefix(self, prefix: str):
        passed = 0
        total = 0

        print(f"Running tests with prefix '{prefix}'...\n")

        for file in sorted(self.tests_root.rglob(f"{prefix}*.py")):
            total += 1
            if self.run_test_file(file, self.tests_root):
                passed += 1

        print(f"\nPassed {passed}/{total} tests.")

    def run_test_file(self, file: Path, root: Path) -> bool:
        try:
            variable_map = VariableProgramMap(str(file))
            variable_map.trace()

            print(f"✓ {file.relative_to(root)}")
            return True

        except Exception as e:
            print(f"✗ {file.relative_to(root)}")
            print(f"    {e}")
            return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Static Type Analysis Engine"
    )
    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        default=["*"],
        help="One or more test directories (default: all subdirectories of tests)",
    )

    parser.add_argument(
        "-f",
        "--file-prefix",
        help="Only run test files whose names start with this prefix",
    )

    args = parser.parse_args()

    tests_root = Path(__file__).parent / "tests"

    if args.directories == ["*"]:
        directories = [d for d in tests_root.iterdir() if d.is_dir()]
    else:
        directories = [tests_root / name for name in args.directories]

    tester = Tester(tests_root, directories, args.file_prefix)
    tester.run()


if __name__ == "__main__":
    main()
