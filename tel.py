# Создаем пустой справочник
phonebook = []

def add_contact():
    """Добавляет контакт в справочник."""
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = {
        "Фамилия": last_name,
        "Имя": first_name,
        "Отчество": patronymic,
        "Номер телефона": phone_number
    }

    phonebook.append(contact)
    print("Контакт успешно добавлен!")

def search_contact():
    """Ищет контакт по фамилии или имени."""
    search_term = input("Введите фамилию или имя для поиска: ")

    for contact in phonebook:
        if search_term.lower() in contact["Фамилия"].lower() or search_term.lower() in contact["Имя"].lower():
            print(f"Найден контакт: {contact['Фамилия']} {contact['Имя']} ({contact['Номер телефона']})")

def update_contact():
    """Изменяет данные контакта."""
    search_term = input("Введите фамилию или имя контакта для изменения: ")

    for contact in phonebook:
        if search_term.lower() in contact["Фамилия"].lower() or search_term.lower() in contact["Имя"].lower():
            print(f"Текущие данные контакта: {contact['Фамилия']} {contact['Имя']} ({contact['Номер телефона']})")
            new_phone_number = input("Введите новый номер телефона: ")
            contact["Номер телефона"] = new_phone_number
            print("Данные контакта успешно обновлены!")
            return

    print("Контакт не найден.")

def delete_contact():
    """Удаляет контакт из справочника."""
    search_term = input("Введите фамилию или имя контакта для удаления: ")

    for contact in phonebook:
        if search_term.lower() in contact["Фамилия"].lower() or search_term.lower() in contact["Имя"].lower():
            phonebook.remove(contact)
            print("Контакт успешно удален!")
            return

    print("Контакт не найден.")

def show_all_contacts():
    """Отображает все контакты в справочнике."""
    if not phonebook:
        print("Справочник пуст.")
    else:
        print("Все контакты в справочнике:")
        for contact in phonebook:
            print(f"{contact['Фамилия']} {contact['Имя']} ({contact['Номер телефона']})")

def save_to_file():
    """Сохраняет данные в текстовом файле."""
    with open("phonebook.txt", "w") as file:
        for contact in phonebook:
            file.write(f"{contact['Фамилия']}, {contact['Имя']}, {contact['Отчество']}, {contact['Номер телефона']}\n")

def main():
    while True:
        print("\n1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Показать все контакты")
        print("6. Сохранить в файл")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            show_all_contacts()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
