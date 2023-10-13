import math

from Lab_Circle import Circle

from Lab_Rectangle import Rectangle


cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
cirkel2 = Circle(x=1,y=1, radius=1)

rektangel = Rectangle(x=0,y=0,side1=1, side2=1)
rektangel2 = Rectangle(x=0,y=0,side1=1, side2=2)

print(cirkel1.radius==cirkel2.radius) # Should be and is True
print(cirkel2==rektangel) # Should be and is False
print(cirkel1.is_inside(0.5, 0.5)) # Should be and is True

cirkel1.translate(5,5)

print(cirkel1.is_inside(0.5, 0.5)) # Should be and is False
print(rektangel.is_rectangle())
print(rektangel2.is_rectangle())


