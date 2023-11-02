# Mahdi Mohammadi khah 982011056


n = int(input())
m = int(input())

sum_ = 0
for i in range(-10, m+1):
    for j in range(1, n+1):
        sum_ += int((pow((i + j), 3))/pow(j, 2))

print(sum_)
