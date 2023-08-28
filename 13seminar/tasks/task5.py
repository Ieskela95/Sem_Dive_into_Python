import json
import os.path


class Person:

    def init(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.firstname} {self.lastname} {self.sex}'

    def get_age(self):
        return self.__age
class Employee(Person):
    def __init(self, firstname, lastname, sex, age, pers_id):
        if len(pers_id) != 6:
            raise ValueError('Некорректный id!')
        super().init(firstname, lastname, sex, age)
        self.pers_id = pers_id
        self.lvl_id = int(pers_id) % 7
        self.json_data = {self.firstname: [lastname, sex, age, self.lvl_id, pers_id]}
        self.save_in_files()


    def str(self):
        return f'{self.firstname}: уровень: {self.lvl_id}, ID: {self.pers_id}'


    def save_in_files(self):
        try:
            if not os.path.isfile('json_file.json') or os.path.getsize('json_file.json') == 0:
                with open('json_file.json', 'w') as f:
                    f.write('{}')
            with open('json_file.json', 'r') as f_read:
                data = json.load(f_read)
                data.update(self.json_data)
            with open('json_file.json', 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, ensure_ascii=False, indent=2)
        except SystemError as e:
            return f'Ошибка записи! Не удалось открыть файл {e}'


    def eq(self, other):
        if isinstance(other, Employee):
            return self.pers_id == other.pers_id
        return NotImplemented



def user_create():
    user_list = []
    with open('json_file.json', 'r') as f_read:
        data = json.load(f_read)
    for firstname, values in data.items():
        lastname, sex, age, lvl_id, pers_id = values
        user_list.append(Employee(firstname, lastname, sex, age, pers_id))
    return user_list


class Login():
    def user_login(self, user_name, user_id):
        try:
            with open('json_file.json', 'r') as f_read:
                data = json.load(f_read)
            for firstname, values in data.items():
                lastname, sex, age, lvl_id, pers_id = values
                if firstname == user_name and pers_id == user_id:
                    return int(pers_id) % 7
        except:
            raise UserPermissionError(user_id)

    def user_creator(self, data, creator_lvl):
        new_user = Employee(*data)
        if new_user.lvl_id >= creator_lvl:
            return new_user
        else:
            raise UserLevelError(creator_lvl)



e1 = Employee('Вася', 'Иванов', 'М', 30, '123456')
e2 = Employee('Петя', 'Петров', 'М', 25, '654321')
e3 = Employee('Глафира', 'Вениаминовна', 'Ж', 41, '111111')
e4 = ('Антон', 'Анатольевич', 'М', 24, '123456')


us1 = Login()
print(us1.user_creator(e4, us1.user_login('Петя', '654321')))

# print(e1)
# print(e2)
# print(e3)
