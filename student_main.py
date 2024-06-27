def task1(str):
    return len(str)


def task2(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    else:
        return None


lister = [1, 2, 4, 5, 8, 14]


def task3(lister):
    if not lister:
        return None
    return max(lister)


def task4(num):
    if (num % 2 == 0):
        return True
    if (num % 2 != 0):
        return False


def task5(lister):
    return list(set(lister))


def task6(n):
    if n == 0 or n == 1:
        return None
    else:
        return n * (n - 1)


def task7(lister):
    n = max(lister)
    all_numbers = set(range(1, n + 1))
    return sorted(list(all_numbers - set(lister)))
