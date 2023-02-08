def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject(subjects: list):
    print(subjects)
    return input('Введите первые две буквы названия предмета: ').lower()

def who_answer():
    return input('Кто будет отвечать? (введите номер ученика): ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def check_mark():
    print('Такой оценки не бывает!')

def mark_subject(subject: str):
    print(f'Oценки по {subject}: ')

def get_student(students: list):
    while True:
        who = who_answer()       
        if who == 'exit':
            return who
        who = int(who) - 1
        if who in range(len(students)):
            print(f'Отвечает {students[who]}')
            return students[who]
        print('Нет такого ученика!')

def get_subject(subjects: list):
    while True:
        str = input_subject(subjects)
        for subject in subjects:
            if subject.startswith(str):
                return subject
        print('Такого предмета в этом классе нет!')
        