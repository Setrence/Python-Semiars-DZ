
import text_fields

def menu ():
    print(text_fields.main_menu)
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            return int(choice)
        else:
            print(f'Введите Число от 1 до {length_menu}')

def show_contact(telebook, error_message):
    if not telebook:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(telebook, 1):
            print(f'{i}. {contact.get("name"):<30}'
                  f'{contact.get("telephone"):<10}'
                  f'{contact.get("comment"):<10}')
        return True

def add_contact():
    name = input('Введите Ф И О: ')
    telephone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name' : name, 'telephone' : telephone, 'comment' : comment}

def indexx(message: str):
    return int(input(message))

def search(message):
    return input(message)

def change_contact(telebook: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else telebook[index - 1].get('name'),
            'telephone': contact.get('telephone') if contact.get('telephone') else telebook[index - 1].get('telephone'),
            'comment': contact.get('comment') if contact.get('comment') else telebook[index - 1].get('comment')}

def show_message(message):
    print('-' * len(message))
    print(message)
    print('-' * len(message))