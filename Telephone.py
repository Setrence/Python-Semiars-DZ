# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

tele_book = []

def open_file ():
    with open('Teleph.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(':')
        contact = {'name' : fields[0], 'telephone' : fields[1], 'comment' : fields[2]}
        tele_book.append(contact)
    print('\nТелефонная книга открыта!')

def save_file ():
    data = []
    for contact in tele_book:
        data.append(':'.join(contact.values()))
    data = '\n'.join(data)
    with open('Teleph.txt', 'w', encoding='UTF-8') as file:
        file.write(data)
    print('\nКонтакты успешно сохранены!')


def add_contact():
    name = input('Введите Ф И О: ')
    telephone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name' : name, 'telephone' : telephone, 'comment' : comment}

def show_contact(telebook):
    for i, contact in enumerate(telebook, 1):
        print(f'{i}. {contact.get("name"):<30}'
              f'{contact.get("telephone"):<10}'
              f'{contact.get("comment"):<10}')

def change_contact(telebook: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else telebook[index - 1].get('name'),
            'telephone': contact.get('telephone') if contact.get('telephone') else telebook[index - 1].get('telephone'),
            'comment': contact.get('comment') if contact.get('comment') else telebook[index - 1].get('comment')}

def indexx(message: str):
    return int(input(message))

def change_cont (contact, index):
    tele_book.pop(index - 1)
    tele_book.insert(index - 1, contact)

def find_contact(telebook):
    result = []
    znak = input('Введите поиск: ')
    for contact in telebook:
        for soderz in contact.values():
            if znak.lower() in soderz.lower():
                result.append(contact)
    return result

def dell_contact (tele_book, index):
    tele_book.pop(index - 1)

def menu ():
    while True:
        print('\n1. Открыть файл телефонной книги \n2. Сохранить файл телефонной'
              ' книги \n3. Показать все контакты'
              '\n4. Найти контакт \n5. Добавить контакт \n6. Изменить контакт \n7. Удалить контакт \n8. Выход')
        choose = int(input('Выберите пункт меню: '))
        if choose == 1:
            open_file()
        elif choose == 2:
            save_file()
        elif choose == 3:
            show_contact(tele_book)
        elif choose == 4:
            result = find_contact(tele_book)
            show_contact(result)
        elif choose == 5:
            tele_book.append(add_contact())
            print('\nКонтакт успешно добавлен!')
        elif choose == 6:
            show_contact(tele_book)
            index = indexx('Введите номер изменяемого контакта: ')
            contact = change_contact(tele_book, index)
            change_cont(contact, index)
            print('\nКонтакт успешно изменен!')
        elif choose == 7:
            show_contact(tele_book)
            index = indexx('Введите номер удаляемого контакта: ')
            dell_contact(tele_book, index)
            print('\nКонтакт успешно удален!')
        elif choose == 8:
            break

menu()
