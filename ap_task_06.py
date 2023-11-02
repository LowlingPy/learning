# Mahdi Mohammadi khah 982011056

def longest_substring(strings):
    min_len = min(len(s) for s in strings)
    answer = ""

    for i in range(min_len):
        for j in range(i + len(answer) + 1, min_len + 1):
            substring = strings[0][i:j]
            if all(substring in s or substring[::-1] in s for s in strings):
                answer = substring

    return answer


n = int(input())
strings = []
for i in range(n):
    strings.append(input())

result = longest_substring(strings)

print(result)
