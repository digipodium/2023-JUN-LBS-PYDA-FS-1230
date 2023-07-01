from turtle import *
speed('fastest')
colors = ['yellow', 'orange']
bgcolor('black')
for i in range(6):
    pencolor('red')
    fd(100)
    for i in range(6):
        pencolor('blue')
        fd(50)
        fillcolor(colors[i%2])
        begin_fill()
        for i in range(6):
            pencolor('green')
            fd(25)
            lt(360/6)
        end_fill()
        lt(360/6)
    lt(360/6)

mainloop()