while True:
    try:
        number = int(input("Введите натуральное число: "))
        if number <= 0:
            print("Число должно быть натуральным.")
        else:
            break
    except ValueError:
        print("Некорректный ввод. Введите только числа.")

max_digit = 0
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number //= 10

print("Максимальная цифра в числе:", max_digit)
