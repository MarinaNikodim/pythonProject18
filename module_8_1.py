def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return result
        elif isinstance(a, str) or isinstance(b, str):
            result = str(a) + str(b)
            return result
    except TypeError as exc:
        return f'Вы складываете неверный тип данных! {exc}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
