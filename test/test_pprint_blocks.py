import pytest

from pplog import pprint_blocks

@pytest.mark.parametrize('empty_log_entry', ['', None])
def test_get_empty_input_returns_no_blocks(empty_log_entry):
    assert list(pprint_blocks.get(empty_log_entry)) == []

def test_get_python_object_blocks():
    expected_raw = ["{'a':1}", "{a}", "{}"]
    expected_parsed = [{'a': 1}, None, {}]
    for i, block in enumerate(pprint_blocks.get("test {'a':1} {a} log {} entry")):
        _assert_block(block, expected_raw[i], expected_parsed[i])

def _assert_block(actual, raw, parsed):
    assert actual.raw == raw
    assert actual.parsed == parsed
