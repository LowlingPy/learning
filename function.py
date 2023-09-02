def sum_i(first, Secend):
    return int(first) + int(Secend)

first = input('Your first number: ')
secend = input('Your secend number: ')
print(sum_i(first, secend))

def my_function(x):
    count = 0
    sum = 1
    answer_1 = 1
    answer = 1

    for i in range(0, x):
        if i == 0 or i == 1:
            print(answer_1, end=', ')
        else:
            answer = answer + answer_1
            answer_1 = answer - answer_1
            print(answer, end=', ')

    # print(answer)



my_function(10)