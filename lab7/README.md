2.1 Назва роботи:
Лабораторна робота №7: Робота з введенням, обробкою та перевіркою даних у Python
2.2 Мета роботи:
Метою цієї лабораторної роботи є ознайомлення студентів з методами обробки і перевірки введених даних у Python. Студенти навчаться використовувати конструкції обробки виключень для забезпечення надійності та коректності програмного коду.
2.3 Опис завдання:
Вам потрібно реалізувати набір функцій у мові програмування Python, кожна з яких вирішує конкретне завдання:
task1(age_str): Конвертує строку у ціле число, представляючи вік. Повертає помилку, якщо введене значення не є числом.
task2(num1_str, num2_str): Конвертує два строки у числа з плаваючою точкою і повертає їх добуток. Повертає помилку, якщо введені значення не є числами.
task3(string): Повертає довжину введеного рядка. Повертає помилку, якщо введене значення не є рядком.
task4(num_list): Обчислює суму чисел у списку. Повертає None, якщо введене значення не є списком чисел.
task5(data): Приймає список кортежів з іменами та оцінками, обчислює середній бал для кожного студента та повертає список з середніми балами іменами студентів. Повертає повідомлення про помилку, якщо обробка списку невдала.
2.4 Виконання роботи:
Створення функцій
task1: Конвертація строку в число
python
Копіювати код
def task1(age_str):
    try:
        age = int(age_str)
        return age
    except ValueError:
        return "Error: Please enter a valid numeric value for age."
task2: Конвертація строк у числа з плаваючою точкою та обчислення їх добутку
python
Копіювати код
def task2(num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        return num1 * num2
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."
task3: Обчислення довжини рядка
python
Копіювати код
def task3(string):
    try:
        if not isinstance(string, str):
            raise TypeError
        return len(string)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."
task4: Обчислення суми чисел у списку
python
Копіювати код
def task4(num_list):
    try:
        total = sum(num_list)
        return total
    except TypeError:
        return None
task5: Обчислення середнього балу студентів
python
Копіювати код
def task5(data):
    try:
        result = []
        for name, grades in data:
            average_grade = sum(grades) / len(grades)
            result.append((average_grade, name))
        return result
    except Exception:
        return "List processing error!"
        Опис основних функцій:
task1(age_str): Конвертує строку у ціле число, представляючи вік. Повертає помилку, якщо введене значення не є числом.
task2(num1_str, num2_str): Конвертує два строки у числа з плаваючою точкою і повертає їх добуток. Повертає помилку, якщо введені значення не є числами.
task3(string): Повертає довжину введеного рядка. Повертає помилку, якщо введене значення не є рядком.
task4(num_list): Обчислює суму чисел у списку. Повертає None, якщо введене значення не є списком чисел.
task5(data): Приймає список кортежів з іменами та оцінками, обчислює середній бал для кожного студента та повертає список з середніми балами іменами студентів. Повертає повідомлення про помилку, якщо обробка списку невдала.
Приклади використання:
if __name__ == "__main__":
    # Task 1
    age_str = "25"
    print("Task 1 Result:", task1(age_str))
    
    # Task 2
    num1_str = "3.14"
    num2_str = "2.71"
    print("Task 2 Result:", task2(num1_str, num2_str))
    
    # Task 3
    string = "Hello, world!"
    print("Task 3 Result:", task3(string))
    
    # Task 4
    num_list = [1, 2, 3, 4, 5]
    print("Task 4 Result:", task4(num_list))
    
    # Task 5
    data = [("Alice", [90, 80, 70]), ("Bob", [85, 75, 65])]
    print("Task 5 Result:", task5(data))
2.5 Результати:
Task 1 Result: 25
Task 2 Result: 8.5094
Task 3 Result: 13
Task 4 Result: 15
Task 5 Result: [(80.0, 'Alice'), (75.0, 'Bob')]
2.6 Висновки:
Мета роботи була досягнута. Всі функції були успішно реалізовані та протестовані. Основні проблеми виникли з коректною обробкою вхідних даних та інтеграцією функцій, але вони були вирішені шляхом детального аналізу і корекції коду.
