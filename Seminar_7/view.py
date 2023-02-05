def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл', 
                'Сохранить файл', 
                'Новый контакт', 
                'Изменить контакт', 
                'Удалить контакт', 
                'Найти контакт', 
                'Выйти из программы']
    print('\nВыберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Телефонная книга пустая или не загружена')

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно!!')

def change_success():
    print("Контакт успешно изменен!")
def change_fail():
   print("Такого контакта в телефонной книге нет") 
def change_nothing():
   print("Нечего менять!") 
def delete_nothing():
   print("Нечего удалять!") 
def delete_success():
    print("Контакт успешно удален!")

def new_contact():
    name = input('Введите Имя и Фамилию контакта: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def change_contact(change_contact: list):
    many_contacts = False
    change_list = []
    if len(change_contact) > 1:
        many_contacts = True
        print('Найдено больше 1 контакта')
    for item in change_contact:
        print()
        if many_contacts:
            print(f'{item[0]} {item[1]} ({item[2]})')
            print('Хотите изменить этот контакт?')
            if input('1 - да, 2 - нет: ') == '1':    
                change_list.append(change(item))
            else:
                continue
        else:
            change_list.append(change(item))
    return change_list

def change(item: list):
    contact = {}
    name = input("Введите новое имя контакта: ")
    phone = input("Введите новый номер телефона контакта: ")
    comment = input("Введите новый комментарий к контакту: ")

    contact.update({'old_name' : item[0], 'new_name' : name})
    contact.update({'old_phone' : item[1], 'new_phone' : phone})
    contact.update({'old_comment' : item[2], 'new_comment' : comment})
    return contact

def delete_contact(change_contact: list):
    change_list = []
    for item in change_contact:
        print()
        print(f'{item[0]} {item[1]} ({item[2]})')
        print('Хотите удалить этот контакт?')
        if input('1 - да, 2 - нет: ') == '1':    
            change_list.append(item)
        else:
            continue
    return change_list

def check_save(diff: list):
    if(len(diff) > 0): 
        print('Телефонная книга изменена, сохранить изменения перед выходом?')
        return input('1 - да, 2 - нет: ') == '1'