file = open('17_3.txt')
a = [int(x) for x in file]
file.close()


# count = 0
# max_raz = 0
#
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         raz = a[i] - a[j]
#
#         if raz % 45 != 0:
#             continue
#         if not ((a[i] % 18 == 0) or (a[j] % 18 == 0)):
#             continue
#
#         count += 1
#
#         if raz > max_raz:
#             max_raz = raz
#
#
# print(count, max_raz)


# min_7 = 0
# for x in a:
#     if str(x)[-1] == '7' and x < min_7:
#         min_7 = x
#
#
#
# count = 0
# summm = 0
#
# for i in range(len(a) - 1):
#     #a[i + 1] следующий соседний элемент
#     if not(str(a[i])[-1] == str(a[i + 1])[-1]):
#         continue
#
#     #условие что только один из элементов будет кратен 7
#     u1 = a[i] % 7 == 0 and a[i + 1] % 7 != 0
#     u2 = a[i] % 7 != 0 and a[i + 1] % 7 == 0
#     if not(u1 or u2):
#         continue
#
#     sum_kr = a[i]**2 + a[i+1]**2
#     if sum_kr > min_7**2:
#         continue
#     count += 1
#
#     if sum_kr > summm:
#         summm = sum_kr
#
# print(count, summm)


#print(str(a[4])[-1] == '0' and str(a[4])[-2] == '4' and str(a[4])[-3] == '3')



# Назовём тройкой три идущих подряд элемента последовательности.
#
# Задание 17
#
# Определите количество троек, для которых выполняются следующие условия:
#
# — в тройке есть пятизначные числа, но не все числа в тройке пятизначные;
#
# — в тройке больше чисел, кратных 3, чем чисел, кратных 5;
#
# — сумма элементов тройки больше максимального элемента последовательности, запись которого заканчивается на 238. (Гарантируется, что в последовательности есть хотя бы один элемент, запись которого заканчивается на 238.)
#
# В ответе запишите два числа: сначала количество найденных троек, затем максимальную величину суммы элементов этих троек.

# max_238 = 0
# for x in a:
#     if (str(x)[-1] == '0' and str(x)[-2] == '4' and str(x)[-3] == '3') and x > max_238:
#         max_238 = x
#
#
# count = 0
# summm = 0
#
# for i in range(len(a) - 2):
#     #a[i + 1] следующий соседний элемент
#     # if not(str(a[i])[-1] == str(a[i + 1])[-1]):
#     #     continue
#
#     #условие что только один из элементов будет кратен 7
#     # u1 = a[i] % 7 == 0 and a[i + 1] % 7 != 0
#     # u2 = a[i] % 7 != 0 and a[i + 1] % 7 == 0
#     u1 = len(str(a[i])) == 5 or len(str(a[i + 1])) == 5 or len(str(a[i + 2])) == 5
#     u2 = len(str(a[i])) != 5 or len(str(a[i + 1])) != 5 or len(str(a[i + 2])) != 5
#     if not(u1 or u2):
#         continue
#
#     count_3 = int(a[i] % 3 == 0) + int(a[i + 1] % 3 == 0) + int(a[i + 2] % 3 == 0)
#     count_5 = int(a[i] % 5 == 0) + int(a[i + 1] % 5 == 0) + int(a[i + 2] % 5 == 0)
#     if not(count_5 < count_3):
#         continue
#
#     sum_troiki = a[i] + a[i+1] + a[i+2]
#
#     if not(max_238 < sum_troiki):
#         continue
#
#     count += 1
#
#     if sum_troiki > summm:
#         summm = sum_troiki
#
#
# print(count, summm)
#
#




#В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов делится без остатка на 62, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
count = 0
sum_max = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):

        if not (a[i] * a[j]) % 62 == 0:
           continue

        count += 1
        sum_pair = a[i]+a[j]
        if sum_max < sum_pair:
            sum_max = sum_pair

print(count, sum_max)
