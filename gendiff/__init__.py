from gendiff.cli import parser
from gendiff.gendiff_func import generate_diff
from gendiff.file_loader import load_json_file


__all__ = [
    'generate_diff',
    'load_json_file',
    'main'
]


def main():
    args = parser.parse_args()
    file1_data = load_json_file(args.first_file)
    file2_data = load_json_file(args.second_file)

    print(generate_diff(file1_data, file2_data))


if __name__ == '__main__':
    main()
