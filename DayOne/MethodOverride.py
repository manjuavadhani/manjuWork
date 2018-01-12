class Box:
    def __init__(self, size):
        self.size = size

    def __mul__(self, other):
        return Box(self.size * other.size)

    def __str__(self):
        return '[{}:{}]'.format(self.__class__.__name__, self.size)

if __name__ == '__main__':
    b1 = Box(1)
    print(type(b1))
    b2 = Box(5)
    b3 = b1 * b2
    print(b3)