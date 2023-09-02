import argparse
import locale
import logging
import os
from collections import namedtuple

locale.setlocale(locale.LC_ALL, "Russian")

logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')


def file_listening(path='.'):
    """
    Рекурсивно обходит заданный каталог и все вложенные директории
    """

    for dir_path, dir_name, file_name in os.walk(path):
        Files = namedtuple('Files', ['item_name', 'file_ext', 'dir_flag', 'parent_path'])
        parent_path = dir_path.split('\\')[-2]

        if dir_name:
            dir_flag = 'Is a directory.'
            exp_dict = Files(dir_name, None, dir_flag, parent_path)
            logging.info(f'{exp_dict}')

        if file_name:
            dir_flag = 'Is a file.'
            for f in file_name:
                exp_dict = Files(f.split('.')[0], f.split('.')[-1], dir_flag, parent_path)
                logging.info(f'{exp_dict}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сканер файлов.')
    parser.add_argument('path', type=str, help='Введите путь: ', default=os.getcwd())
    args = parser.parse_args()
    print(file_listening(args.path))
