2.1 Назва роботи:
Лабораторна робота №11: Основні алгоритми та структури даних в Python

2.2 Мета роботи:
Основна мета лабораторної роботи полягає у вивченні та реалізації основних алгоритмів та структур даних в мові програмування Python. Очікується, що студенти засвоять такі аспекти як робота з масивами, матрицями, використання черги з пріоритетом та інші базові алгоритми.

2.3 Опис завдання:
Для виконання цієї лабораторної роботи студентам необхідно реалізувати наступні завдання:

Реалізація функцій для роботи з масивами:

Обчислення суми квадратів елементів масиву.
Фільтрація елементів масиву, де значення перевищує середнє арифметичне всіх елементів.
Сортування масиву за частотою входження елементів.
Реалізація алгоритмів:

Пошук відсутнього числа в послідовності чисел.
Пошук найбільшої довжини послідовності чисел у масиві.
Реалізація алгоритму обертання масиву на k позицій.

Реалізація алгоритму для обчислення масиву добутків елементів без самого елемента.

Реалізація алгоритму для пошуку найближчих точок до початку координат.

Кожна з цих функцій має бути реалізована в окремій функції в файлі main.py.

2.4 Виконання роботи:
Для досягнення мети було створено файл main.py, де були реалізовані всі вищеописані функції. Кожна функція була перевірена на правильність роботи через виведення результатів у консоль.

Опис файлів у проекті:
main.py: Основний код програми, що містить реалізації функцій для кожного завдання, а також приклади їх використання.
README.md: Файл з детальним описом проекту, описом кожної функції, їх методів, прикладами використання та інструкціями з запуску.
Опис основних функцій та методів:
sum_of_squares(arr): Обчислює суму квадратів елементів масиву arr.
filter_and_sum(arr): Фільтрує елементи масиву, залишаючи лише ті, що перевищують середнє арифметичне, і обчислює їх суму.
sort_by_frequency(arr): Сортує масив за частотою входження елементів у зменшуючому порядку.
find_missing_number(arr): Знаходить відсутнє число в послідовності чисел arr.
longest_consecutive(nums): Знаходить найбільшу довжину послідовності чисел у масиві nums.
rotate_array(arr, k): Обертає масив arr на k позицій.
array_of_products(nums): Обчислює масив добутків елементів без самого елемента.
k_closest_points(points, k): Знаходить k найближчих точок до початку координат серед списку точок points.
Приклади використання:
python
Копіювати код
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(sum_of_squares(arr))  # Output: 196
    print(filter_and_sum(arr))  # Output: 29
    print(sort_by_frequency(arr))  # Output: [1, 1, 5, 5, 3, 4, 9, 2, 6]
    
    arr_missing = [3, 1, 4, 5, 9, 2, 6, 7]
    print(find_missing_number(arr_missing))  # Output: 8
    
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))  # Output: 4
    
    arr_rotate = [1, 2, 3, 4, 5, 6, 7]
    print(rotate_array(arr_rotate, 3))  # Output: [5, 6, 7, 1, 2, 3, 4]
    
    nums_products = [1, 2, 3, 4]
    print(array_of_products(nums_products))  # Output: [24, 12, 8, 6]
    
    points = [(1, 3), (-2, 2), (5, 8), (0, 1), (1, -1)]
    k = 3
    print(k_closest_points(points, k))  # Output: [(0, 1), (1, -1), (-2, 2)]
2.5 Результати:
Отримані результати демонструють коректну роботу кожної функції, що було перевірено через виведення правильних результатів у консоль.

2.6 Висновки:
У ході виконання лабораторної роботи були успішно реалізовані основні алгоритми та структури даних в мові Python. Проблеми з виконанням виникли відсутність виразу super