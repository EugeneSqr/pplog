import pytest

from .log_entry_parser import get_selections

@pytest.mark.parametrize('empty_log_entry', ['', None])
def test_get_selections_empty_input_returns_no_selections(empty_log_entry):
    assert list(get_selections(empty_log_entry)) == []

def test_get_selections_python_object_selections():
    _assert_selections(
        get_selections("test {'a':1} log {'b':'bb'} entry"),
        ["{'a':1}", "{'b':'bb'}"],
        [{'a': 1}, {'b': 'bb'}])

def test_get_selections_json_object_selections():
    _assert_selections(
        get_selections('test {} log {"a":1} entry {b}'),
        ['{}', '{"a":1}', '{b}'],
        [{}, {'a': 1}, None])

def test_get_selections_both_python_and_json_selections():
    _assert_selections(
        get_selections('test {"a":1} log {\'a\':2} entry {b}'),
        ['{"a":1}', "{'a':2}", '{b}'],
        [{'a': 1}, {'a': 2}, None] )

def test_get_selections_nested_structures():
    log_entry = 'test {"a":{"a.b":{}}} entry {\'b\':[{\'b.b\': 1}, {}, {}]}'
    _assert_selections(
        get_selections(log_entry),
        ['{"a":{"a.b":{}}}', '{\'b\':[{\'b.b\': 1}, {}, {}]}'],
        [{'a': {'a.b': {}}}, {'b':[{'b.b':1}, {}, {}]}])

def _assert_selections(actual, serialized, deserialized):
    for i, selection in enumerate(actual):
        assert selection.serialize() == serialized[i]
        assert selection.deserialize() == deserialized[i]
