'''

from turtle import *

color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''

'''Testing git via VSC'''

if (0):
    print("True")
else:
    print("False")
print(type(range(5)))