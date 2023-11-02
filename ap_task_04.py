# Mahdi Mohammadi khah 982011056

n, m = input().split()
n, m = int(n), int(m)
list_of_data = []
answer = ''

for i in range(m):
    data = input()
    list_of_data.append(data)

for j in range(n):
    count = 0
    for item in list_of_data:
        if item[j] == 'W':
            count += 1
    if count % 2 == 0:
        answer += 'B'
    else:
        answer += 'F'

print(answer)
