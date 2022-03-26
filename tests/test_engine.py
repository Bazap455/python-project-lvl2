import pytest
from gendiff.engine import generate_diff


@pytest.fixture
def expected_json():
    f = open('tests/fixtures/expected_json.txt')
    return f.read()


def test_generate_diff(expected_json):
    diff = generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json',
    )
    assert diff == expected_json
