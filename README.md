# vectometry

![PyPI - Downloads](https://img.shields.io/pypi/dm/vectometry)

The Python package _**vectometry**_ implements a Point object as well as a Vector object and the common vector operations in 3-dimensional space. All functions can be used as the function itself, or via *Magical Functions* and *Operator Overloading*. That means, for example the magnitude of a vector A can be calculated by `vectometry.norm(A)`, but also by the Built-In function `abs(A)`. And for example the scalar product of vectors A and B can be calculated by `vectometry.dot(A,B)`, but also by the (`*`)-operator: `A*B`.

Developed by InformaticFreak (c) 2021

## Installation

```batch
pip install vectometry
```

[vectometry on PyPi.org](https://pypi.org/project/vectometry/)


## Documentation

### Creating Vector and Point

```python
from vectometry import Vector, Point

# A Vector or Point can be initialized by:
# Three single int/float values
v = Vector(1, 2, 3)
p = Point(1, 2, 3)

# A list/tuple with three int/float values
v = Vector([1, 2, 3])
v = Vector((1, 2, 3))

p = Point([1, 2, 3])
p = Point((1, 2, 3))

# A vector is also created by
# Two points: Vector from p1 to p2
p1 = Point(4, 5, 6)
p2 = Point(7, 8, 9)
v = Vector(p1, p2) #=> Vector(3, 3, 3)

# Direct from the difference of two points: Vector from p1 to p2
v = p2 - p1 #=> Vector(3, 3, 3)
```

### Compare position relationships of vectors

```python
from vectometry import Vector
from vectometry import is_orthogonal, is_collinear, is_complanar

# is_orthogonal(v1, v2) returns true, if vector v1 is perpendicular to vector v2
v1 = Vector(0, 0, 1)
v2 = Vector(0, 1, 0)
is_orthogonal(v1, v2) #=> True

# is_collinear(v1, v2) returns true, if vector v1 is collinear/paralell to vector v2
v1 = Vector(0, 0, 1)
v2 = Vector(0, 0, 5)
is_collinear(v1, v2) #=> True
# alternatives
v1 == v2

# is_complanar(v1, v2, v3) returns true, if vector v1, v2 and v3 are located in the same plane
v1 = Vector(0, 0, 1)
v2 = Vector(0, 0, 5)
v3 = Vector(0, 0, -10)
is_complanar(v1, v2, v3) #=> True
```

### Calculation of common vector operations

```python
from vectometry import Vector
from vectometry import dot, cross, det, norm, angle, area, spate
from vectometry import add, sub, mul, div, neg

# Dot product
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
dot(v1, v2) #=> 16
# alternatives
v1 * v2

# Cross product
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
cross(v1, v2) #=> Vector(-11, 21, 6)
# alternatives
v1 % v2

# Determinant
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
v3 = Vector(6, 1, -4)
det(v1, v2, v3) #=> -69

# Magnitude
v = Vector(1, 2, 3)
norm(v) #=> 3.7416573867739413
# alternatives
abs(v)

# Angle in degree
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
angle(v1, v2) #=> 56.80373134602263

# Area of parallelogram spanned by 2 vectors v1 and v2
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
area(v1, v2) #=> 24.454038521274967

# Volume of spate/parallelepiped spanned by 3 vectors v1, v2 and v3
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
v3 = Vector(6, 1, -4)
spate(v1, v2, v3) #=> 69

# Addition
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
add(v1, v2) #=> Vector(5, -1, 9)
# alternatives
v1 + v2

# Subtraction
v1 = Vector(1, 2, 3)
v2 = Vector(4, -3, 6)
sub(v1, v2) #=> Vector(-3, 5, -3)
# alternatives
v1 - v2

# Multiplication of vector by a real number
v = Vector(1, 2, 3)
n = 4
mul(v, n) #=> Vector(4, 8, 12)
# alternatives
mul(n, v)
v * n
n * v

# Division of vector by a real number
v = Vector(1, 2, 3)
n = 4
div(v, n) #=> Vector(0.25, 0.5, 0.75)
# alternatives
v / n

# Negative of vector
v = Vector(1, 2, 3)
neg(v) #=> Vector(-1, -2, -3)
# alternatives
-v
```

### Miscellaneous

```python
# Returns the coordinates of a point or vector
p = Point(2, 1, 4)
p.x(); p.y(); p.z() #=> 2 1 4

v = Vector(4, 9, 1)
v.x(); v.y(); v.z() #=> 4 9 10

# Changes the coordinates of a point or vector to the given real number
p = Point(2, 1, 4)
p.x(-3); p.y(4); p.z(0)
p #=> Point(-3, 4, 0)

v = Vector(4, 9, 1)
v.x(5); v.y(8); v.z(4)
v #=> Vector(5, 8, 4)

# All coordinates of a point or volume can be iterated
p = Point(-3, 4, 0)
[ c for c in p ] #=> [-3, 4, 0]

v = Vector(5, 8, 4)
[ c for c in v ] #=> [5, 8, 4]

# Create a copy of a vector or point
p = Point(-3, 4, 0)
p1 = p.copy()
p1 #=> Point(-3, 4, 0)

v = Vector(5, 8, 4)
v1 = v.copy()
v1 #=> Vector(5, 8, 4)

# Returns the dimensions of vector or point (always 3)
p = Point(-3, 4, 0)
len(p) #=> 3

v = Vector(5, 8, 4)
len(v) #=> 3
```
