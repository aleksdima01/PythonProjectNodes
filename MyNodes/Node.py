print('''\t1. Открыть файл
\t2. Сохранить файл
\t3. Показать все заметки
\t4. Добавить заметку
\t5. Изменить заметку
\t6. Удалить заметку
\t7. Показать заметки в порядке добавления или изменения
\t8. Выход''')

from pathlib import Path
from datetime import datetime

path = Path(Path.cwd(), "Node.json")
# path = "ProjectNodes\MyNodes\Node.json"

node_list = []


def open_file():
    if node_list:
        print("Файл уже загружен!")
    else:
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                node = []
                for field in line.split(';'):
                    node.append(field.strip())
                node_list.append(node)
        print('Файл успешно загружен')
        print(path.name)


def save_file():
    with open(path, 'w', encoding='UTF-8') as file:
        for line in node_list:
            node = "; ".join(line)
            file.write(f'{node}\n')
    print("Файл сохранен!")


def show_nodes():
    if len(node_list) == 0:
        print("Заметок пока нет!")
    for i, nodes in enumerate(node_list, 1):
        print(f'{i}. \t{nodes[0]} \t{nodes[1]} \t{nodes[2]} \t{nodes[3]}')


def add_node():
    print("Создание заметки:")
    header = input('Введите заголовок заметки: ')
    body = input('Введите содержание заметки: ')
    time = datetime.now()
    time = time.strftime("%x, %H:%M:%S")
    number = len(node_list) + 1
    node_list.append(list([f'Заметка #{number}', f'Заголовок: {header}', f'Содержание заметки: {body}',
                           f'Время создания или изменения заметки: {time}']))
    print("Заметка успешно создана! Сохраните файл!")


def modify_node():
    number_node = []
    for i, nodes in enumerate(node_list, 1):
        print(f'{i}. \t{nodes[0]}\t{nodes[1]}\t{nodes[2]}\t{nodes[3]}')
        number_node.append(i)
    b = True
    while b:
        try:
            modify_number = int(input("Введите номер заметки для изменения:"))
            b = False
        except ValueError:
            print("Введены неправильные данные! Повторите ввод!")
    while modify_number not in number_node:
        modify_number = int(input("Введите правильно номер заметки для изменения:"))
    print(node_list[modify_number - 1])
    header = input('Введите заголовок заметки: ')
    body = input('Введите содержание заметки: ')
    time = datetime.now()
    time = time.strftime("%x, %H:%M:%S")
    node_list.pop(modify_number - 1)
    node_list.insert(modify_number - 1,
                     list([f'Заметка #{modify_number}', f'Заголовок: {header}', f'Содержание заметки: {body}',
                           f'Время создания или изменения заметки: {time}']))
    print("Заметка успешно отредактирована! Сохраните файл!")


def delete_node():
    number_node = []
    for i, nodes in enumerate(node_list, 1):
        print(f'{i}. \t{nodes[0]}\t{nodes[1]}\t{nodes[2]}\t{nodes[3]}')
        number_node.append(i)
    b = True
    while b:
        try:
            del_number = int(input("Введите номер заметки для удаления:"))
            b = False
        except ValueError:
            print("Введены неправильные данные! Повторите ввод!")
    while del_number not in number_node:
        del_number = int(input("Введите правильно номер заметки для удаления:"))
    node_list.pop(del_number - 1)
    for i in range(del_number - 1, len(node_list)):
        node_list[i][0] = f'Заметка #{i + 1}'
    print("Заметка удалена! Сохраните файл!")


def node_sort():
    number_node = node_list.copy()
    number_node.sort(key=lambda x: x[3])
    for i, nodes in enumerate(number_node, 1):
        print(f'{i}. \t{nodes[0]}\t{nodes[1]}\t{nodes[2]}\t{nodes[3]}')


b = True
while b:
    try:
        number = int(input('Введите пункт меню:'))
        b = False
    except ValueError:
        print("Введены неправильные данные! Повторите ввод!")
while number != 8 and number != 1:
    try:
        number = int(input('Сначала откройте файл или выйдите: '))
    except ValueError:
        print("Введены неправильные данные! Повторите ввод!")
if number == 1:
    open_file()
else:
    print("Выход!")
    exit()
while True:
    b = True
    while b:
        try:
            number = int(input('Введите пункт меню: '))
            b = False
        except ValueError:
            print("Введены неправильные данные! Повторите ввод!")
    match number:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            print("Список заметок:")
            show_nodes()
        case 4:
            print("Выбрано добавление заметки!")
            add_node()
        case 5:
            print("Выбрано изменение заметки!")
            modify_node()
        case 6:
            print("Выбрано удаление заметки!")
            delete_node()
        case 7:
            print("Выбран показ заметок по дате добавления или изменения!")
            node_sort()
        case 8:
            print("Выход!")
            break
        case _:
            print("Введите правильный пункт меню:")
