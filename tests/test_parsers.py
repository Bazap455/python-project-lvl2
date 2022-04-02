import pytest
import json
from gendiff.parsers import parse


@pytest.fixture
def data_expected():
    data_expected = json.load(open('tests/fixtures/file1.json'))
    return data_expected


def test_parser(data_expected):
    data_json = parse('tests/fixtures/file1.json')
    data_yaml = parse('tests/fixtures/file1.yaml')
    data_yml = parse('tests/fixtures/file1.yml')

    assert data_json == data_yaml == data_yml == data_expected


def test_parser_with_format_error():
    with pytest.raises(Exception):
        data_json = parse('tests/fixtures/file1.jnos')
