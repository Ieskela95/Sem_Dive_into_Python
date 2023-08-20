import time
from getpass import getuser


class MyString(str):


    def __new__(cls, *args, **kwargs):

        instance = super().__new__(cls, *args, **kwargs)
        instance.name = getuser()
        instance.log = time.ctime()
        return instance

    def __repr__(self):

        return f'MyString("{self}")'


my_str = MyString('text')
print(f'Сама строка(объект): "{my_str}", имя автора: "{my_str.name}", дата/время: "{my_str.log}"')
print(f'{my_str = }')
