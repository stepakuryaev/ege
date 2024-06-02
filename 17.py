file = open('17_1.txt')
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


min_7 = 0
for x in a:
    if str(x)[-1] == '7' and x < min_7:
        min_7 = x



count = 0
summm = 0

for i in range(len(a) - 1):
    #a[i + 1] следующий соседний элемент
    if not(str(a[i])[-1] == str(a[i + 1])[-1]):
        continue

    #условие что только один из элементов будет кратен 7
    u1 = a[i] % 7 == 0 and a[i + 1] % 7 != 0
    u2 = a[i] % 7 != 0 and a[i + 1] % 7 == 0
    if not(u1 or u2):
        continue

    sum_kr = a[i]**2 + a[i+1]**2
    if sum_kr > min_7**2:
        continue
    count += 1

    if sum_kr > summm:
        summm = sum_kr

print(count, summm)





#for i in range(len(a) - 3):