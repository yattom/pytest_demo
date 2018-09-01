import pytest

@pytest.fixture
def my_fixture():
    return ['some', 'data', 'for', 'test']

def test_upper(my_fixture):
    upper = [s.upper() for s in my_fixture]
    assert upper[3] == 'TEST'

@pytest.fixture
def test_file():
    f = open("test.bin", "rb")
    yield f
    f.close()

def test_read(test_file):
    assert test_file.read() == b'test\r\n'

import requests

def test_mocker(mocker):
    class DummyRequest:
        status_code = 200
    mocker.patch('requests.get', return_value=DummyRequest())
    r = requests.get('https://example.com')
    assert r.status_code == 200




