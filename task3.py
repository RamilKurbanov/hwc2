def int_to_hex_string(number):
    hex_string = hex(number)
    return hex_string

# Ввод целого числа от пользователя
try:
    input_number = int(input("Введите целое число: "))
    hex_result = int_to_hex_string(input_number)
    print(f"Шестнадцатеричное представление числа {input_number} : {hex_result}")
except ValueError:
    print("Ошибка: Введите целое число.")