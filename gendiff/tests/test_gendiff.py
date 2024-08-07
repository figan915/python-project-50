from gendiff.gendiff_func import generate_diff
import pytest
from gendiff.file_loader import load_file

@pytest.mark.parametrize(
    "file1_json, file2_json, file1_yaml, file2_yaml, correct_result", [
        ('./gendiff/tests/fixtures/file1.json',
         './gendiff/tests/fixtures/file2.json',
         './gendiff/tests/fixtures/file1.yaml',
         './gendiff/tests/fixtures/file2.yaml',
         './gendiff/tests/fixtures/correct_result_flat.txt')])
def test_gendiff(file1_json, file2_json, file1_yaml, file2_yaml, correct_result):
    file1_data = load_file(file1_json)
    file2_data = load_file(file2_json)
    file3_data = load_file(file1_yaml)
    file4_data = load_file(file2_yaml)
    with open(correct_result) as cr:
        expected_result = cr.read().strip()
        diff_json = generate_diff(file1_data, file2_data).strip()
        diff_yaml = generate_diff(file3_data, file4_data).strip()
        assert expected_result == diff_json
        assert expected_result == diff_yaml

