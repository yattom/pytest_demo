import pytest

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


class Person2:
    def __init__(self, name, birthday, hobby):
        self.name = name
        self.birthday = birthday
        self.hobby = hobby

    def greet(self):
        return ''

    def __repr__(self):
        return f'Person("{self.name}", {self.birthday}, {self.hobby})'

class Person2Repository:
    def __init__(self):
        self.repo = {}

    def save(self, person):
        self.repo[person.name] = person

    def load(self, name):
        return self.repo[name]

    def __repr__(self):
        return f'Person2Repository of {list(self.repo.keys())}'


@pytest.fixture
def person_repo():
    repo = PersonRepository()
    person1 = Person('yattom', BIRTHDAY(4, 20), ['python', 'woodcraft'])
    repo.save(person1)
    person2 = Person('kinako', BIRTHDAY(2, 20), ['eating', 'walking'])
    repo.save(person2)
    return repo

@pytest.mark.skip
def test_person(person_repo):
    assert person_repo.load('yattom') == person_repo.load('kinako')

@pytest.fixture
def person2_repo():
    repo = Person2Repository()
    person1 = Person2('yattom', BIRTHDAY(4, 20), ['python', 'woodcraft'])
    repo.save(person1)
    person2 = Person2('kinako', BIRTHDAY(2, 20), ['eating', 'walking'])
    repo.save(person2)
    return repo

@pytest.mark.skip
def test_person2(person2_repo):
    assert person2_repo.load('yattom') == person2_repo.load('kinako')

