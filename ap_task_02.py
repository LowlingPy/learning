#Mahdi Mohammadi khah 982011056

n = int(input())

for i in range(1, n + 1, 2):
    space = " " * ((n - i) // 2)
    star = "*" * i
    left = space + star + space
    right = left[::-1]
    print(left + right)

for i in range(n - 2, 0, -2):
    space = " " * ((n - i) // 2)
    star = "*" * i
    left = space + star + space
    right = left[::-1]
    print(left + right)
