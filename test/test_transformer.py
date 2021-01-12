import pytest

from pplog import transformer

def test_transform_invalid_query_returns_data_itself():
    data = {'a': 1}
    assert transformer.transform(data, 'x') == data

@pytest.mark.parametrize('empty_data', ['', None, {}])
def test_transform_empty_data_returns_none(empty_data):
    assert transformer.transform(empty_data, '.') == [empty_data]
