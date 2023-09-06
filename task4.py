from fractions import Fraction

def operate_fractions(fraction1_str, fraction2_str):
    try:
        # Разбиваем введенные строки на числитель и знаменатель
        numerator1, denominator1 = map(int, fraction1_str.split('/'))
        numerator2, denominator2 = map(int, fraction2_str.split('/'))

        # Создаем объекты Fraction для дробей
        fraction1 = Fraction(numerator1, denominator1)
        fraction2 = Fraction(numerator2, denominator2)

        # Считаем сумму и произведение дробей
        fraction_sum = fraction1 + fraction2
        fraction_product = fraction1 * fraction2

        return fraction_sum, fraction_product
    except ValueError:
        return None

# Ввод двух дробей от пользователя
fraction1_str = input("Введите первую дробь в формате 'a/b': ")
fraction2_str = input("Введите вторую дробь в формате 'a/b': ")

result = operate_fractions(fraction1_str, fraction2_str)

if result:
    sum_result, product_result = result
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")
else:
    print("Ошибка: Введите дроби в правильном формате.")