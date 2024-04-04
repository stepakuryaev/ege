# def f(N):
#     s1 = int(str(N)[0]) + int(str(N)[1])
#     s2 = int(str(N)[1]) + int(str(N)[2])
#     s3 = int(str(N)[0]) + int(str(N)[2])
#
#     #r1, r2 = sorted([s1, s2]) # [s2, s1] [3, 5]
#
#
#     # sort1 = sorted([s1, s2, s3])
#     # r1 = sort1[0]
#     # r2 = sort1[2]
#
#     r1, r2 = sorted([s1, s2, s3])[1:]
#
#     R = str(r1) + str(r2)
#     return R
#
# print(f(123))

# for n in range(100, 1000):
#     if f(n) == '1115':
#         print(n)



'''Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.

 

1.  Складываются первая и вторая, а также вторая и третья цифры исходного числа.

2.  Полученные два числа записываются друг за другом в порядке возрастания (без разделителей).

 

Пример. Исходное число: 348. Суммы: 3+4 = 7; 4+8 = 12. Результат: 712.

Укажите наименьшее число, в результате обработки которого автомат выдаст число 1115.'''


# def f(N): #N = 348
#     new_n = str(N)
#     ch1 = int(new_n[0]) + int(new_n[1])
#     ch2 = int(new_n[1]) + int(new_n[2])
#
#     r1, r2 = sorted([ch1, ch2]) #"[::-1] #[start:end:step] [1, 2, 3, 6, 4] [1:3:-1]= [3,2]
#     r = str(r1) + str(r2)
#
#     return r
#
# #f(348)
# for n in range(100, 1000):
#     if f(n) == '1115':
#         print(n, " ", f(n))

# def f(N):
#     n = bin(N)[2:]
#
#     m = bin(5)[2:]
#     d = bin(7)[2:]
#
#
#
#     if N%5 != 0:
#         n = n + str(1)
#     else:
#         n = n + m
#
#     new_N = int(n, 2)
#
#
#
#     if new_N%7 !=0:
#         n = n + str(1)
#     else:
#         n = n + d
#
#     res = int(n, 2)
#     return res
#
#
# for n in range(1, 1000000):
#     if f(n) < 1855663:
#         print(n)



# def f(n):
#     a = bin(n)[2:]
#     #123 - 3 разряда
#     #010010 - 6 разрядов
#
#     #for i in a:
#     sum = 0
#     for i in range(len(a)):
#         sum = int(a[i]) + sum
#
#     a = a + str(sum % 2)
#
#     sum = 0
#     for i in range(len(a)):
#         sum = int(a[i]) + sum
#
#     a = a + str(sum % 2)
#
#     return int(a, 2)
#
# #7 - 111 : 1) 3 % 2 = 1 -> 1111 ; 2) 1111 -> 4 ; 3) 4 % 2 = 0 -> 11110 -> 2+4+8+16 = 30
# print(f(18))
#


def f(k):
    a = str(k)
    #было число 65123 стала строка "65123", то есть работают индексы
    sum1 = int(a[0]) + int(a[2]) + int(a[4])
    sum2 = int(a[1]) + int(a[3])

    #r1, r2 = sorted([ch1, ch2])  # "[::-1] #[start:end:step] [1, 2, 3, 6, 4] [1:3:-1]= [3,2]

    r = sorted([sum1, sum2])
    res = str(r[0]) + str(r[1])

    return res
#f(65123)
for i in range(40000, 60000):
    print(i, " | ", f(i))



50979

9676





