import view, model

def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()
        
        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                search = view.find_contact()
                result = model.search_contact(search)
                if len(result) == 0:
                    view.change_fail()
                    continue
                view.show_contacts(result)
                               
                change_contact = view.change_contact(result)
                if len(change_contact) == 0:
                    view.change_nothing()
                    continue

                model.change_phone_book(change_contact)
                view.change_success()
            case 6:
                search = view.find_contact()
                result = model.search_contact(search)
                if len(result) == 0:
                    view.change_fail()
                    continue
                view.show_contacts(result)
                               
                delete_contact = view.delete_contact(result)
                if len(delete_contact) == 0:
                    view.delete_nothing()
                    continue
                
                model.delete_contact(delete_contact)
                view.delete_success()
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)
            case 8:
                diff = model.get_diff_book()
                if view.check_save(diff):
                    model.save_phone_book()
                    view.save_success()
            case _:
                print("not matched")
