def get_smallest_even(numbers):
    evens = [num for num in numbers if num % 2 == 0]

    if evens:
        return min(evens)
    else:
        return numbers[0]


def move_zeros_first(numbers):
    zeros = [num for num in numbers if num == 0]
    non_zeros = [num for num in numbers if num != 0]

    return zeros + non_zeros


# Проверка, что пользователь вводит только числа
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Ввод списка чисел с проверкой
numbers = []
while True:
    user_input = input("Введите число (для завершения введите 'q'): ")
    if user_input.lower() == "q":
        break
    if is_number(user_input):
        numbers.append(float(user_input))
    else:
        print("Некорректный ввод. Введите только числа.")

# Поиск наименьшего четного элемента или первого элемента
smallest_even = get_smallest_even(numbers)
print("Наименьший четный элемент (или первый элемент):", smallest_even)

# Преобразование списка с нулевыми элементами в начале
transformed_list = move_zeros_first(numbers)
print("Преобразованный список с нулевыми элементами в начале:", transformed_list)