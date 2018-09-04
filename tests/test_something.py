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

@pytest.fixture
def request_ok(mocker):
    class DummyRequest:
        status_code = 200
    mocker.patch('requests.get', return_value=DummyRequest())

def test_request_ok(request_ok):
    r = requests.get('https://example.com')
    assert r.status_code == 200

@pytest.fixture
def request_response(mocker, request):
    if hasattr(request, 'param'):
        code = request.param['status']
    else:
        code = 200
    class DummyRequest:
        status_code = code
    mocker.patch('requests.get', return_value=DummyRequest())

@pytest.mark.parametrize('request_response', [{'status': 404}], indirect=True)
def test_request_not_found(request_response):
    r = requests.get('https://example.com')
    assert r.status_code == 404


@pytest.fixture
def request_mocker(mocker):
    def set_status_code(status_code):
        code = status_code
        class DummyRequest:
            status_code = code
        mocker.patch('requests.get', return_value=DummyRequest())
    return set_status_code

def test_request_not_found_2(request_mocker):
    request_mocker(status_code=404)
    r = requests.get('https://example.com')
    assert r.status_code == 404


