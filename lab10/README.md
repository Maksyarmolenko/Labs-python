2.1 Назва роботи:
Лабораторна робота №10: Основи об'єктно-орієнтованого програмування в Python

2.2 Мета роботи:
Метою цієї лабораторної роботи є вивчення основ об'єктно-орієнтованого програмування (ООП) в мові Python. Очікується, що студенти засвоять базові принципи ООП, такі як створення класів, використання конструкторів, успадкування, поліморфізм та інкапсуляція.

2.3 Опис завдання:
У цій лабораторній роботі студентам потрібно виконати наступні завдання:

Створення класу Student для зберігання інформації про студентів.
Додати метод display_info для відображення інформації про студента.
Реалізувати успадкування для класів Animal, Dog, Bird, Sparrow і Penguin.
Реалізувати поліморфізм через метод fly у класах Bird, Sparrow і Penguin.
Створити клас Encapsulation для демонстрації інкапсуляції з використанням модифікаторів доступу.
Розробити клас Rectangle для обчислення периметра прямокутника.
Реалізувати клас AverageCalculator, який обчислює середнє значення списку чисел.
2.4 Виконання роботи:
Для виконання цих завдань було реалізовано відповідні класи та методи, які визначають їхню поведінку і взаємодію. Всі класи були реалізовані у файлі main.py.

Опис файлів у проекті:
main.py: Основний код програми, який містить класи Student, Animal, Dog, Bird, Sparrow, Penguin, Encapsulation, Rectangle, AverageCalculator, а також приклади їх використання.
README.md: Файл з детальним описом проекту, описом кожного класу, їх методів, прикладами використання та інструкціями з запуску.
Опис основних функцій та методів:
Student: Клас для зберігання інформації про студента, має метод display_info для виведення цієї інформації.
Dog: Клас, який успадковує від Animal і має додаткове поле breed.
Sparrow і Penguin: Класи, що успадковують від Bird і реалізовують поліморфізм через метод fly.
Encapsulation: Клас для демонстрації інкапсуляції з використанням різних рівнів доступу.
Rectangle: Клас для обчислення периметра прямокутника.
AverageCalculator: Клас для обчислення середнього значення списку чисел.
Приклади використання:
python
Копіювати код
if __name__ == "__main__":
    # Task 1
    student = Student(name="Ivan", age=30, grade="2")
    print(student.name, student.age, student.grade)

    # Task 2
    print(student.display_info())

    # Task 3
    animal = Animal(name="Lala", sound="")
    dog = Dog(name="Lala", sound="Auuuuuuuuuu", breed="spitz")
    print(animal.make_sound())
    print(dog.make_sound(), dog.breed)

    # Task 4
    bird = Bird()
    sparrow = Sparrow()
    penguin = Penguin()
    print(bird.fly())
    print(sparrow.fly())
    print(penguin.fly())

    # Task 5
    obj = Encapsulation(1, 2, 3)
    print(obj.public)
    print(obj._private)
    print(obj._Encapsulation__protected)  # Note: accessing __protected through name mangling

    # Task 6
    rectangle = Rectangle(width=5, height=4)
    print(rectangle.calculate_perimeter())

    # Task 7
    numbers = [5, 10, 15, 20]
    avg_calculator = AverageCalculator(numbers)
    print(avg_calculator.calculate_average())
2.5 Результати:
Отримані результати демонструють правильну роботу кожного класу і його методів, що було перевірено через виведення результатів у консоль.

2.6 Висновки:
У ході виконання лабораторної роботи були успішно реалізовані основні концепції об'єктно-орієнтованого програмування в мові Python. Проблеми з виконанням виникли відсутність виразу super()
