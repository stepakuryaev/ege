# file = open('9.txt')
# count = 0
# for line in file:
#     podhodit = False
#     a = [int(x) for x in line.split()] #['17', '21', '16', '59']
#     #print(a)
#     for i in range(len(a) - 1): #чтобы не обратиться по индексу i+1 = 4 к массиву во вложенном цикле
#         for j in range(i + 1, len(a)):
#             for k in range(len(a)):
#                 if k != i and k != j:
#                     #print(a[k], a[i], a[j], end=" ")
#                     if a[k] > (a[i] + a[j]):
#                         podhodit = True
#
#     if podhodit:
#         count += 1
#
# print(count)

file = open("9_2.txt")
count = 0
for line in file:
    a = [int(x) for x in line.split()]
    macs = max(a)
    mini = min(a)
    ind_min = a.index(mini)
    ind_macs = a.index(macs)

    sum_1 = (macs + mini)**2

    sum = 0
    for k in range(len(a)):
        if k != ind_macs and k != ind_min:
            sum += (a[k])**2


    if sum_1>sum:
        count += 1
print(count)










