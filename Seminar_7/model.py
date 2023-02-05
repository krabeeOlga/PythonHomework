
phone_book = []

path ='phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path

    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))  
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))

def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results

def change_phone_book(change_contact: list):
    global phone_book

    for contact in change_contact:
        for line in phone_book:
            if contact.get('old_name') in line:
                line[0] = contact.get('new_name')
                line[1] = contact.get('new_phone')
                line[2] = contact.get('new_comment')

def delete_contact(change_contact: list):
    global phone_book

    for contact in change_contact:
        for i, line in enumerate(phone_book):
            if contact[0] in line:
                del phone_book[i]

def get_diff_book():
    global phone_book
    original = get_original_phone_book()
    t1 = [item for item in original if item not in phone_book]
    t2 = [item for item in phone_book if item not in original]

    return t1 or t2

def get_original_phone_book():
    original_phone_book = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            original_phone_book.append(line.strip().split(';'))
    return original_phone_book