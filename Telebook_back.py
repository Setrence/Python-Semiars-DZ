
tele_book = []
def open_file ():
    with open('Teleph.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(':')
        contact = {'name' : fields[0], 'telephone' : fields[1], 'comment' : fields[2]}
        tele_book.append(contact)

def save_file ():
    data = []
    for contact in tele_book:
        data.append(':'.join(contact.values()))
    data = '\n'.join(data)
    with open('Teleph.txt', 'w', encoding='UTF-8') as file:
        file.write(data)

def get_phone_book():
    return tele_book

def add_contact(contact):
    tele_book.append(contact)

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
