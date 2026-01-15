class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

person = Person('Daryl')
try:
    print(person.name)
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
# AttributeError: 'Person' object has no attribute 'name'