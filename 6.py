#
# import turtle as t  # Подключим модуль черепашка
#
# k = 30  # коэффициент для настраивания более удобного масштаба
# #t.setx(-200)
# t.left(90)
# for i in range(8):  # пропишем алгоритм построения фигуры по условию
#     # t.right(60)
#     # t.forward(1 * k)
#     # t.right(60)
#     # t.forward(1 * k)
#     # t.right(270)
#
#     t.right(45)
#     t.forward(8 * k)
#
# t.up()
#
#
# t.speed(10)  # Увеличим скорость черепашки
#
#
# for x in range(20, -1, -1):  # Алгоритм построения точек
#     for y in range(7, -17, -1):
#         t.goto(x * k, y * k)
#         t.dot(4)  # точки размером 4 пикселя


#t.done()

#
# import turtle as t #импортируем библу
# t.speed(10)
# k = 30 #выбираем масштаб
# t.left(90) #поворачиваем чер-ху (right)
# for i in range(8):  #пропишем алгоритм построения фигуры по условию - "Повтори 8"
#     t.right(45) #поворот направо
#     t.forward(8 * k) #вперед 8 и указываем масштаб K
# t.up()
# for x in range(20, -1, -1):  # Алгоритм построения точек
#     for y in range(7, -17, -1):
#         t.goto(x * k, y * k)
#         t.dot(4)  # точки размером 4 пикселя
# t.done()#чтобы окно не закрывалось


import turtle as t

t.speed(10)
k = 10
t.left(90)
for i in range(9):
    t.forward(18*k)
    t.right(72)
t.up()
t.speed(100)
for x in range(30,-30,-1):
    for y in range(30, -15, -1):
        t.goto(x * k, y * k)
        t.dot(4)  # точки размером 4 пикселя

t.done()











