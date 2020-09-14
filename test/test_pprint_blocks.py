import pytest

from pplog import pprint_blocks

@pytest.mark.parametrize('empty_log_entry', ['', None])
def test_get_empty_input_returns_no_blocks(empty_log_entry):
    assert list(pprint_blocks.get(empty_log_entry)) == []

def test_get_python_object_blocks():
    expected_raw = ["{'a':1}", "{'b':'bb'}"]
    expected_parsed = [{'a': 1}, {'b': 'bb'}]
    for i, block in enumerate(pprint_blocks.get("test {'a':1} log {'b':'bb'} entry")):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_empty_blocks_ignored():
    expected_raw = ["{'a':1}"]
    expected_parsed = [{'a': 1}]
    for i, block in enumerate(pprint_blocks.get("test {} log {'a':1} entry {b}")):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_json_object_blocks():
    expected_raw = ['{"a":1}']
    expected_parsed = [{'a': 1}]
    for i, block in enumerate(pprint_blocks.get('test {} log {"a":1} entry {b}')):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_get_both_python_and_json_objects():
    expected_raw = ['{"a":1}', "{'a':2}"]
    expected_parsed = [{'a': 1}, {'a': 2}]
    for i, block in enumerate(pprint_blocks.get('test {"a":1} log {\'a\':2} entry {b}')):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def test_transform_invalid_query_returns_data_itself():
    data = {'a': 1}
    assert pprint_blocks.transform(data, 'x') == data

@pytest.mark.parametrize('empty_data', ['', None, {}])
def test_transform_empty_data_returns_none(empty_data):
    assert pprint_blocks.transform(empty_data, '.') == empty_data

def _assert_block(actual, raw, parsed):
    assert actual.raw == raw
    assert actual.parsed == parsed
