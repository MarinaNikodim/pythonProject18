def personal_sum(*numbers):
    result = 0
    incorrect_data = []

    for num in numbers:
        try:
            result += num
        except (ValueError, TypeError):
            incorrect_data.append(num) # Добавляем некорректный элемент в список
    for item in incorrect_data: # Выводим некорректные данные
        print(f'Некорректный тип данных для посчета: {item} ')

    return result, len(incorrect_data)

# def calculate_average(*numbers):
#     try:
#         if len(numbers) == 1 and not isinstance(numbers, (tuple, list)):
#             raise TypeError(f'В {numbers} записан некорректный тип данных {numbers}')
#         total_sum, incorrect_data = personal_sum(*numbers)
#         count = len(numbers)
#         if count == 0:
#             raise ZeroDivisionError(f'Деление на ноль!')
#         return total_sum / count
#     except ZeroDivisionError:
#         return 0
#     except TypeError as exc:
#         print({exc})
#         return None




result1, errors = personal_sum('1, 2, 3' )
print(f'Результат 1: {result1}')
result2, errors = personal_sum(1, "Строка", 3, "Ещё Строка") # Вывод 4
print(f'Результат 2:  {result2}')
result3, errors = personal_sum(567)
print(f'Результат 3: {result3}')
result4, errors = personal_sum(42, 15, 36, 13)
print(f'Результат 4: {result4}')

# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
# print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
