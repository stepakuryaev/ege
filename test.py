import turtle as t
k = 30
t.left(90)
t.speed(10)
for i in range(30):
    t.right(60)
    t.forward(1*k)
    t.right(60)
    t.forward(1*k)
    t.right(270)
    t.back

t.up()

for x in range(10,-10,-1):
    for y in range(10,-10, -1):
        t.goto(x*k, y*k)
        t.dot()

t.done()
