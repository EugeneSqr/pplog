import pytest

from pplog import parser

@pytest.mark.parametrize('empty_log_entry', ['', None])
def test_parse_log_entry_empty_input_returns_no_blocks(empty_log_entry):
    assert list(parser.parse_log_entry(empty_log_entry)) == []

def test_parse_log_entry_python_object_blocks():
    _assert_blocks(
        parser.parse_log_entry("test {'a':1} log {'b':'bb'} entry"),
        ["{'a':1}", "{'b':'bb'}"],
        [{'a': 1}, {'b': 'bb'}])

def test_parse_log_entry_json_object_blocks():
    _assert_blocks(
        parser.parse_log_entry('test {} log {"a":1} entry {b}'),
        ['{"a":1}'],
        [{'a': 1}])
#
def test_parse_log_entry_empty_blocks_ignored():
    _assert_blocks(
        parser.parse_log_entry("test {} log {'a':1} entry {b}"),
        ["{'a':1}"],
        [{'a': 1}])

def test_parse_log_entry_both_python_and_json_objects():
    _assert_blocks(
        parser.parse_log_entry('test {"a":1} log {\'a\':2} entry {b}'),
        ['{"a":1}', "{'a':2}"],
        [{'a': 1}, {'a': 2}])

def test_parse_log_entry_nested_structures():
    log_entry = 'test {"a":{"a.b":{}}} entry {\'b\':[{\'b.b\': 1}, {}, {}]}'
    _assert_blocks(
        parser.parse_log_entry(log_entry),
        ['{"a":{"a.b":{}}}', '{\'b\':[{\'b.b\': 1}, {}, {}]}'],
        [{'a': {'a.b': {}}}, {'b':[{'b.b':1}, {}, {}]}])

def _assert_blocks(actual, raw, parsed):
    for i, block in enumerate(actual):
        assert block.raw == raw[i]
        assert block.parsed == parsed[i]
