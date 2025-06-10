# Just learn how to read and write on a file

# test = open('learn_read_and_write.txt' ,'w+')
# test.write(input('Test: ') + '\n')

#
# test.close()
#
# test = open('learn_read_and_write.txt' ,'r')
# print(test.read())
# test.close()


# while True:
#     test = open('learn_read_and_write.txt' ,'a')
#     test_list = []
#     new_data = input('Test:')
#     test_list.append(new_data)
#     print(test_list)
#     test.writelines(test_list)
#     test.close()
#     test = open('learn_read_and_write.txt' ,'r')
#     cup = test.read()
#     test_list.append(cup)
#     print(test_list)
#     test.close()
# test_list =[]
# test = open('learn_read_and_write.txt' , 'a')
# # while True:
# #     new_data = input('New Data: ')
# #     test_list.append(new_data)
# #     print(test_list)
# #     x = '#'.join(test_list)
# #     print(x)
# new_data = input('New data: ')
# test_list.append(new_data)
# x = '#'.join(test_list)
# test.write(x)
# test.close()

# l = ['1', '2']
# new = input('new: ')
# l.append(new)
# print(l)
# x = '#'.join(l)
# print(x)
# t = open('learn_read_and_write.txt' ,'w')
# t.write(x)
# t.close()
# t = open('learn_read_and_write.txt' , 'r')
# x = t.read()
# print(f'x; {x}')
# m = x.split('#')
# print(m)
# t.close()