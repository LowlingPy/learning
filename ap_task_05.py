# Mahdi Mohammadi khah 982011056

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


def count_divisors(num):
    divisors = 0
    sqrt_num = int(math.sqrt(num))
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            divisors += 2  # Count both i and num/i as divisors
    if sqrt_num * sqrt_num == num:
        divisors -= 1  # Adjust for perfect squares
    return divisors


def find_number_with_divisors(target_divisors):
    num = 1
    good_numbers = []
    sum_ = 0

    while True:
        sum_ += num
        good_numbers.append(sum_)

        if count_divisors(good_numbers[-1]) == target_divisors:
            return good_numbers[-1]

        num += 1


input_divisors = int(input())
result = find_number_with_divisors(input_divisors)
print(result)