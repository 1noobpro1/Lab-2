def find_negative_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        all_negative = True
        negative_elements = []

        for row in range(rows):
            if matrix[row][col] >= 0:
                all_negative = False
                break
            negative_elements.append(matrix[row][col])
        if all_negative and negative_elements:
            average = sum(negative_elements) / len(negative_elements)
            return col, average
    return None, None

matrix1 = [
    [1, -2, 3],
    [4, -5, 6],
    [7, -8, 9],
    [10, -11, 12]
]
col, avg = find_negative_column(matrix1)
if col is not None:
    print("Первый столбец со всеми отрицательными элементами:", col + 1)
    print("Элементы столбца:", [matrix1[i][col] for i in range(len(matrix1))])
    print("Среднее арифметическое:", avg)
else:
    print("Столбец со всеми отрицательными элементами не найден")
