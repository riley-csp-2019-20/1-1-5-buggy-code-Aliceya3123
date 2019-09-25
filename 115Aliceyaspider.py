#   a115_buggy_image.py
import turtle as trtl

spiderbody= trtl.Turtle()
spiderbody.pensize(40)
spiderbody.circle(20)
w = 8
length = 90
circle = 380 / w
spiderbody.pensize(5)
spiderlegs = 0
while (spiderlegs < w):
  spiderbody.goto(1,25)
  spiderbody.setheading(circle*spiderlegs)
  spiderbody.forward(length)
  spiderlegs = spiderlegs+ 1
spiderbody.hideturtle()




spiderbody.goto(1,25)
spiderbody.pencolor("red")
spiderbody.circle(8)
spiderbody.penup
spiderbody.goto(-15,20)
spiderbody.pendown
spiderbody.circle(8)


wn = trtl.Screen()
wn.mainloop()