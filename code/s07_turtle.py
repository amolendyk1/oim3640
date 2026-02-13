import turtle

from numpy import size, square

t = turtle.Turtle()
t.speed(0)

for i in range(4):
    t.forward(100)
    t.left(90)



# turtle.done() # makes the window stay open until you close it 
turtle.mainloop() # this is the same as turtle.done() but it is more cross-platform compatible


def draw_square(turtle_obj, size=100):
    """Draw a square with the given size.""""
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

def main():
    t = turtle.Turtle()
    t.speed(5)
    draw_square(t)
    draw_square(t, size 50)
    turtle.mainloop()

if __name__ == "__main__":
    main()

python -m turtledemo 