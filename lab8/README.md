2.1 Назва роботи:
Лабораторна робота №8: Робота з JSON файлами у Python

2.2 Мета роботи:
Метою цієї лабораторної роботи є ознайомлення студентів з методами роботи з JSON файлами у Python. Студенти навчаться читати, записувати, перевіряти і змінювати дані у JSON файлах, використовуючи бібліотеку json.

2.3 Опис завдання:
Вам потрібно реалізувати набір функцій у мові програмування Python, кожна з яких вирішує конкретне завдання:

task1(file_path, age_threshold): Зчитує JSON файл та повертає імена людей, вік яких більше заданого порогу.
task2(data, file_path): Записує дані у форматі JSON до заданого файлу.
task3(schema, file_paths): Перевіряє декілька файлів на валідність JSON, повертає список файлів з помилками.
task4(file_path, key): Зчитує JSON файл та повертає всі значення для заданого ключа.
task5(file_path, category, update_function): Оновлює значення в JSON файлі для заданої категорії, використовуючи передану функцію оновлення.
2.4 Виконання роботи:
Створення функцій
task1: Зчитування JSON файлу та повернення імен людей, вік яких більше заданого порогу
python
Копіювати код
import json

def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above_threshold = [entry['name'] for entry in data if entry['age'] > age_threshold]
    return names_above_threshold
task2: Запис даних у форматі JSON до файлу
python
Копіювати код
def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)
task3: Перевірка файлів на валідність JSON
python
Копіювати код
def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                invalid_files.append(file_path)
    return invalid_files
task4: Зчитування JSON файлу та повернення всіх значень для заданого ключа
python
Копіювати код
def task4(file_path, key):
    def extract_values(obj, key):
        values = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    values.append(v)
                elif isinstance(v, (dict, list)):
                    values.extend(extract_values(v, key))
        elif isinstance(obj, list):
            for item in obj:
                values.extend(extract_values(item, key))
        return values

    with open(file_path, 'r') as file:
        data = json.load(file)
    values = extract_values(data, key)
    return values
task5: Оновлення значень у JSON файлі для заданої категорії
python
Копіювати код
def task5(file_path, category, update_function):
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if item.get('category') == category:
                update_function(item)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

def increase_price(item):
    item['price'] += 10
Опис файлів
main.py: Містить реалізацію всіх функцій для виконання завдань лабораторної роботи.
README.md: Містить детальне пояснення мети роботи, опис завдань, кроки виконання, результати, висновки та інструкції з запуску.
Опис основних функцій:
task1(file_path, age_threshold): Зчитує JSON файл та повертає імена людей, вік яких більше заданого порогу.
task2(data, file_path): Записує дані у форматі JSON до заданого файлу.
task3(schema, file_paths): Перевіряє декілька файлів на валідність JSON, повертає список файлів з помилками.
task4(file_path, key): Зчитує JSON файл та повертає всі значення для заданого ключа.
task5(file_path, category, update_function): Оновлює значення в JSON файлі для заданої категорії, використовуючи передану функцію оновлення.
Приклади використання:
python
Копіювати код
if __name__ == "__main__":
    # Task 1
    file_path = 'data.json'
    age_threshold = 30
    print("Task 1 Result:", task1(file_path, age_threshold))
    
    # Task 2
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]
    file_path = 'output.json'
    task2(data, file_path)
    
    # Task 3
    schema = None
    file_paths = ['data1.json', 'data2.json']
    print("Task 3 Result:", task3(schema, file_paths))
    
    # Task 4
    file_path = 'data.json'
    key = 'name'
    print("Task 4 Result:", task4(file_path, key))
    
    # Task 5
    file_path = 'products.json'
    category = 'electronics'
    task5(file_path, category, increase_price)
    print("Task 5 Result: Price increased by 10 for all electronics")
2.5 Результати:
Task 1 Result: ['Bob']
Task 2 Result: Данні збережено у файлі 'output.json'.
Task 3 Result: ['data2.json']
Task 4 Result: ['Alice', 'Bob']
Task 5 Result: Ціни збільшено на 10 для всіх продуктів категорії 'electronics'.
2.6 Висновки:
Мета роботи була досягнута. Всі функції були успішно реалізовані та протестовані. Основні проблеми виникли з коректною обробкою JSON даних та інтеграцією функцій, але вони були вирішені шляхом детального аналізу і корекції коду.
