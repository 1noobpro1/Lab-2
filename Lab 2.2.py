def process_data(data):
    if isinstance(data, list):
        even_count = sum(1 for x in data if isinstance(x, (int)) and x % 2 == 0)
        print("Количество четных чисел:", {even_count})

        numbers = [x for x in data if isinstance(x, (int))]
        if numbers:
            max_number = max(numbers)
            print("Максимальное число:", max_number)
        else:
            print("В списке нет чисел")

        result = [x for x in data if not (isinstance(x, (int)) and x < 0)]
        print("Список после удаления отрицательных элементов:", result)

    elif isinstance(data, dict):
        sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        print("Словарь после сортировки по убыванию значений:", sorted_dict)

    elif isinstance(data, (int, float)):
        if isinstance(data, int):
            reversed_num = int(str(data)[::-1]) if data >= 0 else -int(str(abs(data))[::-1])
        print("Число в обратном порядке:", reversed_num)

    elif isinstance(data, str):
        char_count = {}
        for char in data:
            char_count[char] = char_count.get(char, 0) + 1
        print("Количество вхождений символов:", char_count)

test_list = [1, -2, 3, 4, -5, 6, 7, -8, 9, 10, -11]
print("Список:")
result1 = process_data(test_list)

test_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1, 'e': 9}
print("Словарь:")
result2 = process_data(test_dict)

test_int = 12345
print("Число:")
result3 = process_data(test_int)

test_string = "hello world"
print("Строка:")
result6 = process_data(test_string)