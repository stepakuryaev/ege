'''
"∨" = or
"∧" = and
"≡" (~) = ==
"→" = <=
"Г" = not
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


# def f(w, x, y, z):
#     l1 = (x and not y)
#     l2 = ((not z) or not w)
#     l3 = ((w <= x) or y)
#     return (l1 <= l2) and l3
#
#
# print('    w x y z | f1(w, x, y, z)')
# i = 1
# for w in 0, 1:
#     for x in 0, 1:
#         for y in 0, 1:
#             for z in 0, 1:
#                 if int(f(w, x, y, z)) == 0:
#                     print(i, ". ", w, x, y, z, "|", int(f(w, x, y, z)))
#                 i+=1



def f (x, y, z, w):
    l1 = (not x or z)
    l2 = (y and not w)
    l3 = ( z and y)
    return (( l1 == l2 ) <= l3)


print('x y z w | f1(w, x, y, z)')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if(int(f(x, y, z, w)) == 0):
                    print(x, y, z, w, "|", int(f(x, y, z, w)))


# print(0,0,0,0)
# print(int(f(0,0,0,0)))
#
# print(0,0,0,1)
# print(f(0,0,0,1))
#
# print(f(0,0,1,0))
#
# print(f(0,0,1,1))