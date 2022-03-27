import pytest
from gendiff.engine import generate_diff


@pytest.fixture
def expected_result():
    f = open('tests/fixtures/expected_result.txt')
    return f.read()


def test_generate_diff_json(expected_result):
    diff = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    )
    assert diff == expected_result


def test_generate_diff_yaml(expected_result):
    diff = generate_diff(
        'tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yaml',
    )
    assert diff == expected_result
