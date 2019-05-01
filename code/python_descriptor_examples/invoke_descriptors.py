class Descriptor:
    def __init__(self, value):
        self.value = value
    def __get__(self, obj, type=None):
        return 'Descriptor with value {}'.format(self.value)

    def __set__(self, obj, value):
        self.value = value

class Foo:
    d = Descriptor(0)
    def __init__(self):
        pass

if __name__ == '__main__':
    foo = Foo()
    print(foo.d)

    setattr(foo, 'd', 99)
    print(foo.d)

    print("Try to uncomment __set__, then __get__ to see different results")
