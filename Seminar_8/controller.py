import view
import model

def start():
    model.set_class(view.input_class())    
    subjects = model.get_subjects()
    model.set_subject(view.get_subject(subjects))
    view.mark_subject(model.subject)

    model.open_file()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)

        students = list(journal.keys())
        student = view.get_student(students)
        if student == 'exit':
            break

        while True:
            mark = int(view.what_mark())
            if mark in range(1, 6):
                model.student_mark(student, mark)
                break
            else:
                view.check_mark()
                continue
    model.save_file()
