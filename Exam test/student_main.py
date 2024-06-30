import re

# Task 1: Class Creation
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Task 2: Method Implementation
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# Task 3: Graph Representation
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def get_adjacency_list(self):
        return self.adjacency_list

    # Task 9: Graph Traversal
    def dfs(self, start_vertex):
        visited = set()
        result = []

        def _dfs(vertex):
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    _dfs(neighbor)

        _dfs(start_vertex)
        return result

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend(self.adjacency_list[vertex])
        return result

# Task 4: Regular Expressions
class RegexChecker:
    def check_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

# Task 5: Inheritance
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

# Task 6: Polymorphism
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

# Task 7: Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

# Task 8: Abstract Base Class
class Employee:
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Task 10: Regular Expression Extractor
class RegexExtractor:
    def extract_phone_numbers(self, text):
        pattern = r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"
        return re.findall(pattern, text)

# Task 11: Multiple Inheritance
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    def method_c(self):
        return f"{self.method_a()}\n{self.method_b()}"

# Task 12: Exception Handling
class DivisionByZeroError(Exception):
    pass

class Calculator:
    def divide(self, numerator, denominator):
        if denominator == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return numerator / denominator

# Task 13: File Operations
class FileManager:
    def write_to_file(self, filename, content):
        with open(filename, "w") as file:
            file.write(content)

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            return file.read()

    def append_to_file(self, filename, content):
        with open(filename, "a") as file:
            file.write(content)

# Task 14: Context Managers
class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Task 15: MetaProgramming
class MetaClassExample(type):
    def __new__(cls, name, bases, dct):
        dct['class_name'] = name
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MetaClassExample):
    pass

