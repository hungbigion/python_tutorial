import turtle as tt
tt.Screen()
tt.penup()
tt.goto(-200,200)
tt.color("red")
tt.pendown()
tt.begin_fill()
tt.forward(400)
tt.right(90)
tt.forward(250)
tt.right(90)
tt.forward(400)
tt.right(90)
tt.forward(250)
tt.right(90)
tt.end_fill()
tt.color("yellow")
tt.penup()
tt.goto(-100,100)
tt.pendown()
tt.begin_fill()
for i in range(5):
    tt.forward(200)
    tt.left(216)
tt.end_fill()

tt.done()