from pathlib import Path # Імпортуємо клас Path для роботи з файлами

def total_salary(path):
    file_path = Path(path) # Створюємо об'єкт шляху до файлу
    try:
        with file_path.open(encoding = 'utf-8') as file: # Відкриваємо файл з кодуванням UTF-8
            total = 0 #загальна сума зарплат
            count = 0 #лічильник кількості оброблених співробітників
            for line in file: #проходимось по файлу за допомогою циклу for
                try:
                    name, salary = line.strip().split(',') #розділяємо рядок на частини по комі
                    total += int(salary) #додаємо зарплату до загальної суми з перетвореннням в int
                    count += 1
                except ValueError:
                    continue
            if count == 0:
                return (0, None)
            average = round(total / count,) #додаємо суредню зарплату та округляємо до цілого числа
            return(total, average)
    except FileNotFoundError:
        print("File not found")
        return (0, None)

total, average = total_salary('salary.txt') #викликаємо функцію вказуючи шлях до файлу
print(f"Total salary: {total}, Average salary: {average}")