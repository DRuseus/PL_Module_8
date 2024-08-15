def personal_sum(numbers):
    result = int()
    incorrect_data = int()
    try:
        for i in range(len(numbers)):
            try:
                result += numbers[i]
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы: {numbers[i]}')
                incorrect_data += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return result, incorrect_data


def calculate_average(numbers):
    sum_nums, incorrect_data = personal_sum(numbers)
    try:
        result = sum_nums / (len(numbers) - incorrect_data)
    except TypeError:
        result = None
    except ZeroDivisionError:
        result = 0
    except:
        return 'Ну ты молодец, сломал программу...'
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
