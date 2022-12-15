# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, 
# сворачивая соседние по числовому ряду числа в диапазоны.

# def max_num_guests(guests):
#     guest_days = []
#     for guest in guests:
#         days = range(guest[0], guest[1])
#         guest_days.extend(days)
#     guest_num = {}
#     for d in guest_days:
#         if not d in guest_num:
#             guest_num[d] = 0
#         guest_num[d] += 1
#     return max(guest_num.values())
# input = [(1, 2), (1, 3), (2, 4), (2, 3), (1, 4)]
# output = max_num_guests(input)
# print(f"input: {input}")
# print(f"output: {output}")

# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB 
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку, 
# если на вход пришла невалидная строка.

# def convert_string(input_str):
#     prev_symbol = None
#     len_of_series = 0
#     result = ""
#     for symb in input_str:
#         if prev_symbol and symb != prev_symbol:
#             result = result + f"{prev_symbol}{len_of_series}"
#             len_of_series = 1
#         else:
#             len_of_series += 1

#         prev_symbol = symb

#     return result + f"{prev_symbol}{len_of_series}" if prev_symbol else ""
# input_str = ""
# print(input_str + " -> " + convert_string(input_str))
# input_str = "AAABBBCCCXYZA"
# print(input_str + " -> " + convert_string(input_str))
# input_str = "AAAAAAAAAAВВВВСССССССС"
# print(input_str + " -> " + convert_string(input_str))