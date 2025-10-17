# squares = [x**2 for x in range(1, 11)]
# print(squares)

# even_numbers = [x for x in range(2, 20) if x % 2 == 0]
# print(even_numbers)

# words = ["python", "Java", "c++", "Rust", "go"]
# upper_words = [word.upper() for word in words if len(word) >= 3]
# print(upper_words)

# class Countdown:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):3
#         if self.n < 1:
#             raise StopIteration
#         current = self.n
#         self.n -= 1
#         return current
#
#
# for x in Countdown(5):
#     print(x)

# def fibonacci(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1
#
# for num in fibonacci(5):
#     print(num)

# from decimal import Decimal, getcontext
#
# getcontext().prec = 10
#
# P = Decimal(input("Начальная сумма вклада: "))
# r = Decimal(input("Процентная ставка годовых: "))
# t = Decimal(input("Срок вклада (в годах): "))
#
# S = P * (1 + r / (12 * 100)) ** (12 * t)
# S = S.quantize(Decimal('0.01'))
#
# profit = S - P
# profit = profit.quantize(Decimal('0.01'))
#
# print("Итоговая сумма вклада:", S)
# print("Общая прибыль:", profit)

# from fractions import Fraction
#
# a = Fraction(3, 4)
# b = Fraction(5, 6)
#
# print(f"Сложение: {a + b}")
# print(f"Вычитание: {a - b}")
# print(f"Умножение: {a * b}")
# print(f"Деление: {a / b}")

# from datetime import datetime
#
#
# now = datetime.now()
#
# print("Текущая дата и время:", now)
# print("Текущая дата:", now.date())
# print("Текущее время:", now.time())

# from datetime import datetime, date
#
# birthday = date(2004, 3, 15)
# today = date.today()
#
# days_passed = (today - birthday).days
#
# next_birthday = date(today.year, birthday.month, birthday.day)
#
# if next_birthday < today:
#     next_birthday = date(today.year + 1, birthday.month, birthday.day)
#
# days_until_next = (next_birthday - today).days
#
# print("Дней прошло с рождения:", days_passed)
# print("Дней до следующего дня рождения:", days_until_next)

# from datetime import datetime
#
# def format_datetime(dt):
#     months = {
#         1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
#         5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
#         9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
#     }
#     return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt.hour:02d}:{dt.minute:02d}"
#
# # Пример использования
# now = datetime.now()
# print(format_datetime(now))