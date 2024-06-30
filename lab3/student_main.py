def task1(my_list):

    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append("Башинський","Роман")
    list_length = len(my_list)
    print("Modified List:", my_list)
    print("Min Element:", min_element)
    print("Max Element:", max_element)
    print("List Length:", list_length)

    return my_list, min_element, max_element, list_length

def task2(A, B, C):

    total_cost = sum(b * c for b, c in zip(B, C))
    average_price = sum(C) / len(C)
    most_stocked_item = A[B.index(max(B))]

    return total_cost, average_price, most_stocked_item

def task3():
    numbers = list(range(-25,26))

    A1 = [num for num in numbers if num > 0]
    A2 = [num for num in numbers if num < 0]

    return A1, A2

def task4(my_string):
    return my_string.lower().count('a')

def task5(my_string):
    modified_str = my_string.replace("GOOD", "NICE")
    word_count = len(modified_str.split())

    return modified_str, word_count

def task6():
    total_sum = sum(range(1, 6))
    return total_sum

def task7(my_list):
    result = [x for x in my_list if x % 7 == 0 and x % 5 == 0]
    return result

