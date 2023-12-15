import os


def add_file(user):
    file = open(f'files/{user}.txt', 'a+')
    file.close()


def del_file(user):
    try:
        os.remove(f'{user}.txt')
    except Exception:
        print(f'{user} File not found')
