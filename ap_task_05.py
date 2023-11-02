# Mahdi Mohammadi khah 982011056


for i in range(n):
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def find_number_with_divisors(target_divisors):
    number = 1
    while True:
        if count_divisors(number) == target_divisors:
            return number
        number += 1

input_divisor = int(input("Enter the number of divisors: "))
result = find_number_with_divisors(input_divisor)
print(f"The smallest number with {input_divisor} divisors is: {result}")