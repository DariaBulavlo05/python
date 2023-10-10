def remove_text_in_brackets(text):
    while True:
        opening_bracket = text.find("(")
        closing_bracket = text.find(")")

        if opening_bracket == -1 or closing_bracket == -1:
            break

        if opening_bracket < closing_bracket:
            text = text[:opening_bracket] + text[closing_bracket + 1:]
        else:
            break

    return text


input_text = input("Введите строку с текстом в скобках: ")

opening_count = input_text.count("(")
closing_count = input_text.count(")")

if opening_count == 0 or closing_count == 0:
    print("Введенная строка не содержит обе скобки.")
elif opening_count != closing_count:
    print("Количество открывающих и закрывающих скобок не совпадает.")
else:
    result = remove_text_in_brackets(input_text)
    print("Результат:", result)