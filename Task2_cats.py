from pathlib import Path # Імпортуємо клас Path для роботи з файлами

def get_cats_info(path):
    file_path = Path(path) # Створюємо об'єкт шляху до файлу
    cats_list = [] # створюємо список, у який зберігатимемо інформацію про котів
    try:
        with file_path.open(encoding='utf-8') as file: # Відкриваємо файл з кодуванням UTF-8
            for line in file:
                parts = line.strip().split(',') #розділяємо рядок на частини по комі
                if len(parts) <3:
                    print(f"Incomplete data {line.strip()}")
                    continue
                cats_dict = {'id': parts[0],'name': parts[1], 'age': int(parts[2])}
                cats_list.append(cats_dict) #додаємо список у словник
        return cats_list
    except FileNotFoundError:
        print(f"File at path {path} not found.")
    except ValueError:
        print(f"Failed to convert age value to number")
    return cats_list

cats = get_cats_info('Cats_data.txt') #викликаємо функцію та передаємо шлях до файлу
for cat in cats:
    print(cat)