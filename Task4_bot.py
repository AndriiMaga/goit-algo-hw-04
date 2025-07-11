def parse_input(user_input):
    cmd, *args = user_input.split() # Розбиваємо введений рядок на команду та аргументи
    cmd = cmd.strip().lower() #видаляємо пробіли та робимо нижній регістр
    return cmd, *args

def add_contact(args, contacts): # Додаємо новий контакт у словник
    if len(args) != 2:
        return "add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):  # Змінюємо номер телефону для наявного контакту

    if len(args) != 2:
        return "Check the correctness of the entered data."

    name = args[0]
    new_phone = args[1]

    if name in contacts:
        old_phone = contacts[name] # Зберігаємо старий номер
        contacts[name] = new_phone # Оновлюємо старий номер на новий
        return f"Updated: {old_phone} was changed to {new_phone} for {name}."
    else:
        return f"Contact {name} not found."

def show_phone(args, contacts):
    if len(args) != 1: # Показуємо номер телефону за ім'ям
        return f"Usage: phone <name>"

    name = args[0]

    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."

def show_all(contacts): #виводимо всі збережені контакти
    if contacts:
        result = []  # створюємо список для імен та номерів
        for name, phone in contacts.items():
            line = f"{name}: {phone}"
            result.append(line)
        return "\n".join(result) # об'єднуємо рядки
    else:
        return "No contacts found."

def main():
    contacts = {} # Створюємо порожній словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!") # Вихід з програми при відповідній команді
            break
        elif command == "hello":
            print("How can I help you?") # вітання
        elif command == "add":
            print(add_contact(args, contacts)) # додавання контакту
        elif command == "change":
            print(change_contact(args, contacts)) # зміна номера
        elif command == "phone":
            print(show_phone(args, contacts)) # пошук номера
        elif command == "all":
            print(show_all(contacts)) # виведення всіх номерів
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
