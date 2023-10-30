# #printing shape
#
#
# #mostatil
#
# for i in range(1, 10):
#     print()
#     for m in range(1, 10):
#         print('*' , end=' ')
#
#
#
# #mosalas ghaeme A
#
# for i in range(1, 11):
#
#     for m in range(0, i):
#         print('*', end=' ')
#     print()
#
#
#
# #mosalas ghaeme D
#
# for i in range(10, 1, -1):
#     for m in range(0, i-1):
#         print('*', end=' ')
#     print()
#
#
#
# #mostatil khali
#
# for i in range(10):
#     for m in range(10):
#         if i == 0 or i == 9:
#             print('*', end=' ')
#         else:
#             if m == 0 or m == 9:
#                 print('*', end=' ')
#             else:
#                 print('  ', end='')
#     print()

#
#
# #mosalas ghaeme B
#
# for i in range(10):
#     for k in range(10, i, -1):
#         print(' ',end='')
#     for m in range(i):
#         print('*', end='')
#     print()
#
#
#
# #mosalas ghaeme C
#
# for i in range(10):
#     for k in range(i):
#         print(' ', end='')
#     for m in range(10, i, -1):
#         print('*', end='')
#     print()
#
#
#
# # test fail
#
# for i in range(20):
#     if i < 10:
#         for k in range(10, i, -1):
#             print(' *', end='')
#         for m in range(i, 10):
#             print(' *', end='')
#         print()
#     elif i > 10:
#         for k in range(i, 20):
#             print(' *', end='')
#         for m in range(20, i, -1):
#             print(' *', end='')
#         print()
# for i in range(int(input('Enter your number: '))):
#     x = i - 1
#     y = i + 1
#     for k in range(i, y//2, -1):
#         print(' ', end='')
#     for k in range(0, x//2):
#         print(' ', end='')
#     for m in range(x,y):
#         print('* ', end='')
#     print()
#
#
#
# #lozi
#
# x = int(input('Please enter a EVEN number: '))
# for i in range(x):
#     for k in range(x, i, -1):
#         print(' ',end='')
#     for m in range(i-1):
#         print('*', end='')
#     for m in range(0, i):
#         print('*', end='')
#     print()
# for i in range(x):
#     for k in range(0, i):
#         print(' ', end='')
#     for m in range(i, x):
#         print('*', end='')
#     for m in range(x-1-i):
#         print('*', end='')
#
#     print()


# #testing git on pycharm windows


# just try

# for i in range(10):
#     for k in range(10, i, -1):
#             print(' ',end='')
#     # for m in range(i-1):
#     #     if i + m == 9:
#     #         print('*', end='')
#     for m in range(0, i):
#         if i + m == 9:
#             print('*', end='')
#     for m in range(10, i, -1):
#         if i + m == 9:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     for m in range(i):
#         if i + m == 9:
#             print('*', end='')
#         else:
#             print(' ', end='')
#
#
#     print()

# x = int(input('Please enter a EVEN number: '))
# for i in range(x):
#     for k in range(x, i, -1):
#         print(' ',end='')
#     for m in range(i-1):
#         if i + m == x - 1:
#           print('*', end='')
#         else:
#           print(' ', end='')
#     for m in range(0, i):
#         if i + x == m :
#           print('*', end='')
#         else:
#           print(' ', end='')
#     print()
# for i in range(x):
#     for k in range(0, i):
#         print(' ', end='')
#     for m in range(i, x):
#         print('*', end='')
#     for m in range(x-1-i):
#         print('*', end='')
#     print()


# lozi to khali

# x = int(input('Please enter a your number: '))
# for i in range(x):
#     for k in range(x - i, 0, -1):
#         print(' ', end='')
#     print('*', end='')
#     for k in range(2 * i):
#         print(' ', end='')
#     print('*', end='')
#     print()
# for i in range(x):
#     for m in range(i):
#         print(' ', end='')
#     print('*', end='')
#     for k in range(2 * (x - i) - 1, 0, -1):
#         print(' ', end='')
#     print('*', end='')
#     print()


# end 21/8/2023
