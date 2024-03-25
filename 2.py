'''
"∨" = or
"∧" = and
"≡" (~) = ==
"→" = <=
'''

#(x ∨ y) → (y ≡ z)
# def f(x, y, z):
#     return (x or y) <= (y == z)
#
# print(f(0, 0, 0))
#
# print('x y z | f(x, y, z)')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             if not f(x, y, z):
#                 print(x, y, z, "|", int(f(x, y, z)))

#
# def f1(w, x, y, z):
#     return (x <= y) == (w or (not z))
#
# def f2(w, x, y, z):
#     return (x <= y) and ((not w) == z)
#
# print('    w x y z | f1(w, x, y, z) | f2(w, x, y, z)')
# i = 1
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 if z == 1 and int(f2(w, x, y, z)) == 0 and i in [10,14]:
#                     print(i, ". ", w, x, y, z, "|", int(f1(w, x, y, z)), "|", int(f2(w, x, y, z)))
#                 i+=1


# def f1(w, x, y, z):
#     return (x == y) and (w <= z)
#
# def f2(w, x, y, z):
#     return (x <= y) <= (w == z)
#
# print('    w x y z | f1(w, x, y, z) | f2(w, x, y, z)')
# i = 1
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 if w == 0 and int(f1(w, x, y, z)) == 0 and int(f2(w, x, y, z)) == 0:
#                     print(i, ". ", w, x, y, z, "|", int(f1(w, x, y, z)), "|", int(f2(w, x, y, z)))
#                 i+=1


def f(w, x, y, z):
    l1 = (x and not y)
    l2 = ((not z) or not w)
    l3 = ((w <= x) or y)
    return (l1 <= l2) and l3


print('    w x y z | f1(w, x, y, z)')
i = 1
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if int(f(w, x, y, z)) == 0:
                    print(i, ". ", w, x, y, z, "|", int(f(w, x, y, z)))
                i+=1