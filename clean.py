import sys
from pathlib import Path

TEXT_FILE_TYPES = ['txt', 'ide', 'cfg']


def clean_file(filepath):
    extension = filepath.suffix.lstrip('.')
    if extension not in TEXT_FILE_TYPES:
        return

    with open(file=filepath) as file:
        lines = file.readlines()

    with open(file=filepath, mode='w') as file:
        while len(lines) > 0:
            if lines[-1].rstrip() != '':
                break
            lines.pop()
        file.writelines([line.rstrip() + '\n' for line in lines])


def clean_all(directory: Path):
    for filepath in directory.rglob('*'):
        if filepath.is_file():
            clean_file(filepath=filepath.resolve())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python clean.py <file1> [file2 ...] | -all')
        sys.exit(1)

    if sys.argv[1] == '-all':
        clean_all(Path.cwd())
        sys.exit(0)

    for arg in sys.argv[1:]:
        filepath = Path(arg).resolve()

        if not filepath.exists():
            print(f'Error: File not found: {filepath}')
            continue

        if not filepath.is_file():
            print(f'Error: Not a file: {filepath}')
            continue

        clean_file(filepath=filepath)
