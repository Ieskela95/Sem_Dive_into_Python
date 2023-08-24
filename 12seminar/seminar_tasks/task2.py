import json


class Factorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._arg_archive = []
            cls._instance._number_archive = []
            cls._instance._factorial = 1
        return cls._instance

    def __call__(self, num):
        self._arg_archive.append(num)
        self.num = num
        factorial = 1
        for i in range(num):
            factorial *= (i + 1)
        self._number_archive.append(factorial)
        return factorial

    def __str__(self):
        return f'{self._arg_archive}, {self._number_archive}'

    def number_archive(self):
        return self._arg_archive, self._number_archive

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.res = dict(zip(self._arg_archive, self._number_archive))
        self.json_file = open('file.json', 'w')
        json.dump(self.res, self.json_file, indent=2)
        self.json_file.close()


fac = Factorial()
print(fac(3))
print(fac(4))
print(fac(5))
print(fac.number_archive())

jw = Factorial()
with jw as cm:
    cm(7)
