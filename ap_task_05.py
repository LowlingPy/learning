# Mahdi Mohammadi khah 982011056


def count_divisors(num):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
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