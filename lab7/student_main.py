def task1(age_str):
    try:
        age = int(age_str)
        return age
    except ValueError:
        return "Error: Please enter a valid numeric value for age."

def task2(num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        return num1 * num2
    except ValueError:
        return "Error: Please enter valid numeric values for numbers."

def task3(string):
    try:
        if not isinstance(string, str):
            raise TypeError
        return len(string)
    except TypeError:
        return "Error: Please enter a string, not a numeric value."

def task4(num_list):
    try:
        total = sum(num_list)
        return total
    except TypeError:
        return None

def task5(data):
    try:
        result = []
        for name, grades in data:
            average_grade = sum(grades) / len(grades)
            result.append((average_grade, name))
        return result
    except Exception:
        return "List processing error!"


