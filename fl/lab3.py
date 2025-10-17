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
#     def __next__(self):
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

from decimal import Decimal, getcontext

getcontext().prec = 10

P = Decimal(input("Начальная сумма вклада: "))
r = Decimal(input("Процентная ставка годовых: "))
t = Decimal(input("Срок вклада (в годах): "))

S = P * (1 + r / (12 * 100)) ** (12 * t)
S = S.quantize(Decimal('0.01'))

profit = S - P
profit = profit.quantize(Decimal('0.01'))

print("Итоговая сумма вклада:", S)
print("Общая прибыль:", profit)