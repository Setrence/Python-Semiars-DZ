import Telebook_final

pb = Telebook_final.PhoneBook('Teleph.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('ведите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(input('Введите индекс контакта, который будем изменять: '))
            name = input('Введите имя (или Enter - оставить без изменений: ')
            phone = input('Введите телефон (или Enter - оставить без изменений: ')
            comment = input('Введите комментарий (или Enter - оставить без изменений: ')
            pb.change(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта, который хотите уалить: '))
            pb.delete(index - 1)
        case 6:
            pb.save()
        case 7:
            break