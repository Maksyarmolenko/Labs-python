import re

# Завдання 1
def task1(string):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, string))

# Завдання 2
def task2(string):
    pattern = r'.*[A-Z].*'
    return bool(re.match(pattern, string))

# Завдання 3
def task3(string):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, string))

# Завдання 4
def task4(string):
    pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'
    return bool(re.match(pattern, string))

# Завдання 5
def task5(string):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, string))

# Завдання 6
def task6(string):
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, string))

# Завдання 7
def task7(string):
    pattern = r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    return bool(re.match(pattern, string))

# Завдання 8
def task8(string):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, string))

# Завдання 9
def task9(string):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(pattern, string))

# Завдання 10
def task10(string):
    pattern = r'^(([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))$'
    return bool(re.match(pattern, string))

