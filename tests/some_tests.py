import pytest

@pytest.fixture
def my_fixture():
    return ['some', 'data', 'for', 'test']

def test_upper(my_fixture):
    upper = [s.upper() for s in my_fixture]
    assert upper[3] == 'TEST'


