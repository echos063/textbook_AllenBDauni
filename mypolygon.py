import turtle
import math

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#
#
# def polygon(t, n, length):
#     angle = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
#     turtle.mainloop()
#
#
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = 50
#     length = circumference / n
#     polygon(t, n, length)


# def polyline(t, n, length, angle):
#     """ Рисует n отрезков с заданной длиной length и углами angle
#     (в градусах) между ними. t — это черепашка.
#     """
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
#
# def polygon(t, n, length):
#     angle = 360.0 / n
#     polyline(t, n, length, angle)
#
#
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)
#
#
# def circle(t, r):
#     arc(t, r, 360)
#
#
# if __name__ == '__main__':
#     bob = turtle.Turtle()
#
#     # # draw a circle centered on the origin
#     # radius = 100
#     # bob.pu()
#     # bob.fd(radius)
#     # bob.lt(90)
#     # bob.pd()
#     # circle(bob, radius)
#     #
#     # # wait for the user to close the window
#     arc(bob, 50, 120)
#     turtle.mainloop()


bob = turtle.Turtle()

