# Mahdi Mohammadi khah 982011056

def longest_substring(strings):
    if not strings:
        return ""

    longest_string = max(strings, key=len)
    longest_common_substring = ""

    for i in range(len(longest_string)):
        for j in range(i + len(longest_common_substring), len(longest_string)):
            current_substring = longest_string[i:j + 1]
            is_common_substring = all(current_substring in s or current_substring[::-1] in s for s in strings)
            if is_common_substring:
                if current_substring[::-1] in strings:
                    longest_common_substring = current_substring
                else:
                    longest_common_substring = current_substring

    return longest_common_substring


n = int(input())
strings = []
for i in range(n):
    strings.append(input())

result = longest_substring(strings)
if result:
    print(result)
