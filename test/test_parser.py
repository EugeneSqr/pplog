import pytest

from pplog import parser

@pytest.mark.parametrize('empty_log_entry', ['', None])
def test_get_empty_input_returns_no_blocks(empty_log_entry):
    assert list(parser.parse_log_entry(empty_log_entry)) == []

def test_get_python_object_blocks():
    expected_raw = ["{'a':1}", "{'b':'bb'}"]
    expected_parsed = [{'a': 1}, {'b': 'bb'}]
    for i, block in enumerate(parser.parse_log_entry("test {'a':1} log {'b':'bb'} entry")):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_empty_blocks_ignored():
    expected_raw = ["{'a':1}"]
    expected_parsed = [{'a': 1}]
    for i, block in enumerate(parser.parse_log_entry("test {} log {'a':1} entry {b}")):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_json_object_blocks():
    expected_raw = ['{"a":1}']
    expected_parsed = [{'a': 1}]
    for i, block in enumerate(parser.parse_log_entry('test {} log {"a":1} entry {b}')):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_both_python_and_json_objects():
    expected_raw = ['{"a":1}', "{'a':2}"]
    expected_parsed = [{'a': 1}, {'a': 2}]
    for i, block in enumerate(parser.parse_log_entry('test {"a":1} log {\'a\':2} entry {b}')):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def _assert_block(actual, raw, parsed):
    assert actual.raw == raw
    assert actual.parsed == parsed
