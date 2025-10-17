# #Циклы
# #1
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{:3d}".format(i * j), end="")
#     print()

# #2
# sum = 0
# for i in range(1, 100, 2):
#     sum += i
# print(sum)
#
# #3
# x = int(input())
#
# for i in range(1, x + 1):
#     if x % i == 0:
#         print(i)
#
# #4
# res = 1
# x = int(input())
# for i in range(1, x + 1):
#     res *= i
# print(res)
#
# #5
# fib1 = 1
# fib2 = 1
# n = int(input())
#
# i = 0
# print(fib2, end=" ")
# while i < n - 1:
#     print(fib2, end=" ")
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# #Списки
# #1
# import random
# numbers = [random.randint(-50, 50) for _ in range(10)]
# print(numbers)
# for i in range(1, len(numbers), 2):
#     print(numbers[i], end=" ")
# print()
#
# #2
# print(max(numbers), min(numbers))
#
# #3
# z = []
# for i in range(0, 5):
#     z.append(int(input()))
# print(z)
# z.sort()
# print(z)
#
# #4
# import random
# numbers = [random.randint(-50, 50) for _ in range(10)]
# print(numbers)
# print(set(numbers))
# #
# #5
# numbers[0], numbers[len(numbers) - 1] = numbers[len(numbers) - 1], numbers[0]
# print(numbers)
#
# #Словари
# #1
# students_grades = {
#     "Анна": 85,
#     "Иван": 92,
#     "Мария": 78,
#     "Петр": 88,
#     "Елена": 95
# }
#
# average_grade = sum(students_grades.values()) / len(students_grades)
# print(average_grade)
#
# #2
# text = input()
# letter_count = {}
#
# for char in text:
#     if char.isalpha():
#         char_lower = char.lower()
#         if char_lower in letter_count:
#             letter_count[char_lower] += 1
#         else:
#             letter_count[char_lower] = 1
#
# for letter, count in letter_count.items():
#     print(f"'{letter}': {count}")
#
# #3
# squares_dict = {}
#
# for i in range(1, 11):
#     squares_dict[i] = i ** 2
#
# print(squares_dict)
#
# #4
# keys = ['name', 'age', 'city', 'country']
# values = ['Anna', 25, 'Moscow', 'Russia']
#
# result_dict = dict(zip(keys, values))
# print(result_dict)
#
# #Множества
# #1
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# intersection = set1 & set2
# union = set1 | set2
#
# print("Множество 1:", set1)
# print("Множество 2:", set2)
# print("Пересечение:", intersection)
# print("Объединение:", union)
#
# #2
# import string
#
# text = input("Введите текст: ")
#
# text = text.replace(':', '')
# cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
# words = cleaned_text.lower().split()
#
# unique_words = set(words)
#
# print(unique_words)
#
# #3
# list1 = [1, 2, 3, 4, 5, 2, 3]
# list2 = [4, 5, 6, 7, 8, 4]
#
# set1 = set(list1)
# set2 = set(list2)
# common_elements = set1 & set2
#
# print(common_elements)
#
# #4
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
#
# is_subset = A <= B
#
# print(is_subset)
#
# #5
# numbers = {1, 5, 3, 8, 2, 9, 4, 7}
# threshold = int(input())
#
# filtered_set = {x for x in numbers if x >= threshold}
#
# print(filtered_set)
#
# # #Комбинированные задания
# #1
# import random
#
#
# numbers = [random.randint(-50, 50) for _ in range(0, 20)]
# print(numbers)
# res = []
#
# for i in numbers:
#     if numbers.count(i) == 1:
#         res.append(i)
# print(res)

#2
# import collections
#
#
# items = [1, 2, 3, 2, 1, 4, 1, 2, 3, 1]
# count_dict = collections.Counter(items)
# print(dict(count_dict))
#
# #3
# words = ["apple", "banana", "cat", "dog", "elephant", "python", "hi", "programming"]
# long_words = {word for word in words if len(word) > 5}
# print(long_words)
#
# #4
# from collections import Counter
#
# sentence = input()
#
# words = sentence.split()
# word_count = Counter(words)
#
# for word, count in word_count.items():
#     print(f"'{word}': {count}")
#
# #5
# numbers = [1, 2, 3, 2, 4, 5, 3, 1, 6, 7, 5, 8]
# print(numbers)
#
# unique_set = set(numbers)
# print(unique_set)
#
# unique_list = list(unique_set)
# print(unique_list)
#
# #6
# products = {
#     'яблоки': 100,
#     'бананы': 80,
#     'апельсины': 120,
#     'мандарины': 150,
#     'груши': 90
# }
#
# most_expensive = max(products, key=products.get)
# print(most_expensive, products[most_expensive])
#
# #7
# from collections import Counter
#
#
# names = ['Анна', 'Иван', 'Мария', 'Иван', 'Петр', 'Анна', 'Мария', 'Мария', 'Анна']
#
# duplicate_names = [name for name in set(names) if names.count(name) > 1]
# print(duplicate_names)
#
# name_count = Counter(names)
# most_common = max(name_count, key=name_count.get)
# print(most_common, name_count[most_common])
#
# # #8
# text = input()
#
# char_to_first_index = {char: text.index(char) for char in text}
#
# for char, index in char_to_first_index.items():
#     print(f"'{char}': {index}")