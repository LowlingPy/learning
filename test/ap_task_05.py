# Mahdi Mohammadi nhah 982011056

import math


# def divisors(number):
#     '''
#     for testing number of divisor
#     '''
#     result = []
#     for i in range(1, number//2 + 1):
#         if number % i == 0:
#             result.append(i)
#     result.append(number)
#     return result


# def count_divisors(num):
#     divisors = 0
#     sqrt_num = int(math.sqrt(num))
#     for i in range(1, sqrt_num + 1):
#         if num % i == 0:
#             divisors += 2  # Count both i and num/i as divisors
#     if sqrt_num * sqrt_num == num:
#         divisors -= 1  # Adjust for perfect squares
#     return divisors
#
#
# def find_number_with_divisors(target_divisors):
#     num = 1
#     good_numbers = []
#     sum_ = 0
#
#     while True:
#         sum_ += num
#         good_numbers.append(sum_)
#
#         if count_divisors(good_numbers[-1]) == target_divisors:
#             return good_numbers[-1]
#
#         num += 1
#
#
# input_divisors = int(input())
# result = find_number_with_divisors(input_divisors)
# print(result)

n = int(input())

good_number = 0
good_number_counter = 0
is_finished = False
while not is_finished:
    good_number_counter += 1
    good_number += good_number_counter
    factor_counter = 0
    counter = 1
    counter_increasment = 1 if good_number % 2 == 0 else 2
    sqrt = int(good_number ** 0.5)
    if sqrt ** 2 == good_number:
        if n % 2 == 0:
            n2 = n // 2 + 1
        else:
            n2 = (n - 1) // 2 + 1
    else:
        if n % 2 == 0:
            n2 = n // 2
        else:
            n2 = n // 2 + 1
    while counter <= sqrt:
        if good_number % counter == 0:
            factor_counter += 1
            if factor_counter >= n2:
                print(good_number)
                is_finished = True
                break
        counter += counter_increasment
