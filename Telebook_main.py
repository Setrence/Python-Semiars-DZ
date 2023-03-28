import Telebook_front
import Telebook_back
def start():
    while True:
        pb = Telebook_back.get_phone_book()
        choice = Telebook_front.menu()
        match choice:
            case 1:
                Telebook_back.open_file()
                Telebook_front.show_message ('Файл успешно открыт')
            case 2:
                Telebook_back.save_file()
                Telebook_front.show_message('Файл успешно сохранен')
            case 3:
                Telebook_front.show_contact(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                Telebook_back.add_contact(Telebook_front.add_contact())
            case 5:
                if Telebook_front.show_contact(pb, 'Телефонная книга пуста или не открыта'):
                    index = Telebook_front.indexx('Введите номер изменяемого контакта')
                    contact = Telebook_front.change_contact(pb, index)
                    Telebook_back.change_cont(contact, index)
                    Telebook_front.show_message(f'Контакт {Telebook_back.get_phone_book()[index - 1].get("name")} успешно изменен!')
            case 6:
                search = Telebook_front.search('Введите искомый элемент: ')
                result = Telebook_back.find_contact(search)
                Telebook_front.show_contact(result, 'Контакты не найдены')
            case 7:
                Telebook_front.show_contact(pb, 'Телефонная книга пуста или не открыта')
                index = Telebook_front.indexx('Введите номер удаляемого контакта: ')
                Telebook_back.dell_contact(pb, index)
                Telebook_front.show_message('Файл успешно удален')
            case 8:
                return
