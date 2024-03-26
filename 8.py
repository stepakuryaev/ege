
# al = ['В', 'Л', 'Т', 'У']
# n = 1
# for a1 in al:
#     for a2 in al:
#         for a3 in al:
#             for a4 in al:
#                 #if n == 98:
#                 n += 1
#                 print(n," :" + a1 + a2 + a3 + a4)



# def f(x):
#     # if x.count('1') == 2:
#     #     return True
#     #чтобы пробежаться по строке, неоюходим цикл, например for
#     count = 0
#     for a in x:
#         #str(a)
#         if int(a) % 2 != 0:
#             count += 1
#
#     if count == 2:
#         return True
#     else:
#         return False
#
# al= ['0', '1', '2', '3', '4', '5', '6', '7', '8']
#
# count = 0
# for a1 in al[1:]: #числа не могут начинаться с нуля
#     for a2 in al:
#         for a3 in al:
#             for a4 in al:
#                 for a5 in al:
#                     for a6 in al:
#                         for a7 in al:
#                             res = a1 + a2 + a3 + a4 + a5 + a6 + a7
#                             if res.count('6') == 1:
#                                 if f(res):
#                                     count += 1
#                                     print(res)
#
# print(count)



# def f(x):
#     # if x.count('1') == 2:
#     #     return True
#     #чтобы пробежаться по строке, неоюходим цикл, например for
#
#     ind5 = x.find('5')
#
#     if ind5 == 0:
#         sosed_p = x[ind5 + 1]
#         if int(sosed_p) % 2 != 0:
#             return False
#     elif ind5 == 4:
#         sosed_l = x[ind5 - 1]
#         if int(sosed_l) % 2 != 0:
#             return False
#     else:
#         sosed_l = x[ind5 - 1]
#         sosed_p = x[ind5 + 1]
#         if int(sosed_p) % 2 != 0:
#             return False
#         if int(sosed_l) % 2 != 0:
#             return False
#
#     return True
#
# al= ['0', '1', '2', '3', '4', '5', '6', '7', '8']
#
# count = 0
# for a1 in al[1:]: #числа не могут начинаться с нуля
#     for a2 in al:
#         for a3 in al:
#             for a4 in al:
#                 for a5 in al:
#                     res = a1 + a2 + a3 + a4 + a5
#                     if res.count('5') == 1:
#                         if f(res):
#                             count += 1
#                             print(res)
#
# print(count)


def f(x): ##ДДДМММ
    ideal = "ЬМДЯЕН"
    #for a in x:
    for a in ideal:
        if ideal.count(a) == x.count(a):
            continue
            print("hello") #после continue код цикла не выполняется
        else:
            return False

    return True


al = ['Д', 'Е', 'М', 'Ь', 'Я', 'Н']

for a1 in al: #слова могут с нуля, это не число
    for a2 in al:
        for a3 in al:
            for a4 in al:
                for a5 in al:
                    for a6 in al:
                        res = a1 + a2 + a3 + a4 + a5 + a6
                        if f(res):
                            print(res)












