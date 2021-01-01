import pickle


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __dict__(self):
        return {'a': self.a, 'b': self.b}

    def __str__(self):
        return f'MyClass({self.a},{self.b})'

    def sum(self, a, b):
        return self.a + self.b


def serialization_deserialization(a):
    with open('a.pickle', 'wb') as f:
        pickle.dump(a, f)
    with open('a.pickle', 'rb') as f:
        out = pickle.load(f)
    assert type(a) == type(out)
    assert a == out
    print('serialized and deserialized')
    return None


data2 = print
serialization_deserialization(data2)
data3 = pickle.load
serialization_deserialization(data3)
data4 = MyClass
serialization_deserialization(data4)
data5 = MyClass.sum
serialization_deserialization(data5)
data6 = open('ex. 1.txt')
serialization_deserialization(data6)  # TypeError: cannot serialize '_io.TextIOWrapper' object
data1 = iter([1, 2, 3])
serialization_deserialization(data1)  # при десериализации изменяется итератор, поэтому появляется AssertionError



