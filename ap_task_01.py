# # Mahdi Mohammadi khah 982011056
#
# # code ba taqirate kam baraye zibaii nahaii
# n = int(input('Enter number (1, 100): '))
# if n in range(1, 100):
#     for j in range(n):
#         for i in range(n):
#             if j == 0 or j == n - 1:
#                 print('*', end=' ')
#             else:
#                 if i == 0 or i == n - 1:
#                     print('*', end=' ')
#                 else:
#                     print('  ', end='')
#         print()
# else:
#     print('Error')
#
# # taklife khaste shode
# n = int(input())
# if n in range(1, 100):
#     for j in range(n):
#         for i in range(n):
#             if j == 0 or j == n - 1:
#                 print('*', end='')
#             else:
#                 if i == 0 or i == n - 1:
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#         print()
# else:
#     print('Error')
#
# n = int(input('Enter number (1, 100): '))
# print('* ' * n)
# for i in range(n-2):
#     print('*', ' ' * (n - 2), '*', end='')
#     print()
# print('* ' * n)
