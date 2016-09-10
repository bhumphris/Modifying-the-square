import turtle
bob = turtle.Turtle()
print(bob)
def polygon(t, n, length):
    angle = 360 / n
    t.fd(length)
    t.lt(angle)
polygon(bob, 50, 90)

turtle.mainloop()
