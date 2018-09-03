import pytest

@pytest.mark.skip
def test_simple_assert():
    assert 1 == 2

@pytest.mark.skip
def test_func_result():
    assert 0 == min(max(1, ord('2')), min(3, max(len('abcd'), 5), 6 + 7 * 8 - 0o11))

class Person:
    def __init__(self, name, birthday, hobby):
        self.name = name
        self.birthday = birthday
        self.hobby = hobby

    def greet(self):
        return ''

class PersonRepository:
    def __init__(self):
        self.repo = {}

    def save(self, person):
        self.repo[person.name] = person

    def load(self, name):
        return self.repo[name]

from collections import namedtuple
BIRTHDAY = namedtuple('BIRTHDAY', ['month', 'day'])

@pytest.mark.skip
def test_person():
    person = Person('yattom', BIRTHDAY(4, 20), ['python', 'woodcraft'])
    repo = PersonRepository()
    repo.save(person)
    assert 'Hello, yattom.  Enjoy python!' == repo.load('yattom').greet()
