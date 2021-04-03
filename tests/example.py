
from vectors import *

# Define Point a and b
a = Point(1,2,3)
b = Point(4,5,6)

# Define Vector c as difference of Point a and b, means c = b - a
c = Vector(a,b)

# Define Vector d and e
d = Vector(-14,5,9)
e = c * 2

# Test location relationships between the vectors
print(f"Vector c is collinear to Vector e: {c == e}") #=> True
print(f"Vector d is orthogonal to Vector c: {is_orthogonal(d,c)}; because dot product of d and c equals {dot(d,c)}") #=> True

# Calculate area of a parallelogram spanned by Vector c and d
print(f"Area between Vector c and d: {round(area(c,d),4)}") #=> 90.2995
