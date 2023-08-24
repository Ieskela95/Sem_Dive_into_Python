class Square:

    def __init__(self, a, b):
        self._a = a
        if b is None:
            self._b = a
        else:
            self._b = b

    def __str__(self):
        return f'Square, со сторонами {self._a} & {self._b}'

    def __add__(self, other):
        if isinstance(other, Square):
            return Square(self._a + other._a, self._b + other._b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Square):
            if other._a > self._a or other._b > self._b:
                raise ValueError('Такой прямоугольник невозможен')
            return Square(self._a - other._a, self._b - other._b)
        return NotImplemented

    def get_area(self):
        return self._a * self._b

    def get_perimetr(self):
        return 2 * (self._a + self._b)

    def repr(self):
        return f"Square({self._a}, {self._b})"

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('ValueError')

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('ValueError')


obj_a = Square(5, 6)
print(obj_a)
obj_a.a = 10
print(obj_a)
try:
    obj_a.b = -10
except ValueError as e:
    print(e)
