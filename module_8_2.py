def personal_sum(*numbers):
    # if len(numbers) == 1 and not isinstance(numbers[0], (tuple, list)):
    #     print(f'В {numbers} записан некорректный тип данных. Ожидалась коллекция.')

    result = 0
    incorrect_data = []

    for num in numbers:
        try:
            if isinstance(num, (int, float)):
                result += num
            elif isinstance(num, (tuple, list)):
                result += sum(num)
            else:
                raise TypeError('Некорректный тип данных()()()()()')
        except (ValueError, TypeError):
            incorrect_data.append(num) # Добавляем некорректный элемент в список
    for item in incorrect_data: # Выводим некорректные данные
        print(f'Некорректный тип данных для подсчета: {item} ')

    return result, len(incorrect_data)


def calculate_average(*numbers):
    if len(numbers) == 1 and not isinstance(numbers[0], (tuple, list)):
        print(f'В {numbers} записан некорректный тип данных')
        return None
    try:
        total_sum, incorrect_data = personal_sum(*numbers)
        count = len(numbers) - incorrect_data

        if count == 0:
            print(f'НЕЛЬЗЯ ДЕЛИТЬ НА НОЛЬ!!!')
            return 0
        else:
            return total_sum / count
    except ZeroDivisionError:
        print(f'Деление на ноль')
        return 0


print(f'Результат 1: {calculate_average('1', '2', '3')}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average(1, "Строка", 3, "Ещё Строка")}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
