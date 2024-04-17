# a = 4**14 + 2**32 - 4
# print(a)
# b = bin(a)[2:]
# print(b.count("1"))

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def f(N, d):
#     res = []
#     while N != 0:
#         #print(N)
#         res.append(N % d)
#         #print(N % d)
#         N //= d
#     return res[::-1]
#






# #print(f(21, 6))
#
# a = 49**7 + 7**20 - 28
# print(a)
#
# a7 = f(a, 7)
# print(a7)
# print(a7.count(0))





# a1 = bin(N)
# a2 = oct(N)
# a3 = hex(N)




# al = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# for x in al[:16]:
#     s1 = int('2' + x + "84", 19) #2x84 - 2a84, 2984
#     s2 = int('2B3' + x, 16)
#     res = s1 + s2
#     if res % 88 == 0:
#         print(x, res//88)




# def f(N, d):
#     res = []
#     while N != 0:
#         #print(N)
#         res.append(N % d)
#         #print(N % d)
#         N //= d
#     return res[::-1]
#
# a = 343**5 + 7**9 + 48
# a7 = f(a,7)
# print(a7)
# print(a7.count(6))





# 0 1
# ...
# 0 B
# 1 1
# ...
# 1 B

int("1010", 2)

#!!!Главное не выйти за пределы допустимых значений
# al = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']
# for x in al:
#     for y in al:
#         s1 = int(y + "AA" + x,12) #"AAAB"
#         s2 = int(x + "02" + y, 14)
#         res = s1 + s2
#         if res%80==0:
#             print(x,y,res, res/80)
#
# a = 9520/80
# print(a)




# al = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# for x in al[:5]:
#     for y in al[:5]:
#         s1 = int('12', 5)
#         s2 = int('34', 5)
#         s3 = s2*s1
#
#         s4 = int(x + y + '2', 5)
#         if s3 == s4:
#             print(x,y)
#
# for p in range(5,20):
#     for x in al[:p]:
#         for y in al[:p]:
#             s1 = int('12', p)
#             s2 = int('34', p)
#             s3 = s2*s1
#
#             s4 = int(x + y + '2', p)
#             if s3 == s4:
#                 print(x,y,p)
#
#                 s5 = int(y + x, p )
#                 print(s5)

