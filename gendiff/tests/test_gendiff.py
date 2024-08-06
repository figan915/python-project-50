from gendiff.gendiff_func import generate_diff
import pytest
import json


def load_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)


@pytest.mark.parametrize(
    "file1, file2, correct_result", [
        ('./gendiff/tests/fixtures/file1.json',
         './gendiff/tests/fixtures/file2.json',
         './gendiff/tests/fixtures/correct_result_flat.txt')])
def test_gendiff(file1, file2, correct_result):
    file1_data = load_file(file1)
    file2_data = load_file(file2)
    with open(correct_result) as cr:
        result = cr.read()
        diff = generate_diff(file1_data, file2_data)
        assert result == diff
