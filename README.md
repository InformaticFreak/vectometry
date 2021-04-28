
# vectometry

[![GitHub License](https://img.shields.io/github/license/informaticfreak/vectometry)](LICENSE.txt)&nbsp;
[![Python Version](https://img.shields.io/badge/python-3-blue)](https://www.python.org/downloads/)&nbsp;
[![PyPI Version](https://img.shields.io/pypi/v/vectometry)](https://pypi.org/project/vectometry/)&nbsp;
[![PyPI Downloads](https://img.shields.io/pypi/dm/vectometry)](https://pypistats.org/packages/vectometry)&nbsp;

The Python package _**vectometry**_ implements a Point object as well as a Vector object and the common vector operations in 3-dimensional space as well as for 2-dimensions. All functions can be used as the function itself, or via *Magical Functions* and *Operator Overloading*. That means, for example the magnitude of a vector A can be calculated by `vectometry.norm(A)`, but also by the Built-In function `abs(A)`. And for example the scalar product of vectors A and B can be calculated by `vectometry.dot(A,B)`, but also by the (`*`)-operator: `A*B`.

Developed by InformaticFreak (c) 2021

## Installation

```
pip install vectometry
```

## Documentation

### Creating Vector and Point

A Point object or Vector object can be initialized by different ways.

At first by three single real numbers.

```python
from vectometry import *

p1 = Point(1, 2, -3)
v1 = Vector(1, 2, -3)
```

Or by a list or tuple of three real numbers.

```python
p2 = Point([2, -4, 6])
p3 = Point((3, 3, 3))

v2 = Vector([2, -4, 6])
v3 = Vector((3, 3, 3))
```

A Vector object can also be created by two Point objects, that means a Vector from Point p1 to Point p2.

```python
v4 = Vector(p1, p2)
v4 = p2 - p1
v4 #=> Vector(1, -6, 9)
```

A point or vector for only 2-dimensions can also be created by the same Point object or Vector object, for this only two coordinates must be passed by a list/tuple or as singe	values. The remaining third coordinate will be set to zero.

```python
p2D = Point([5, 6])
p2D #=> Point(5, 6, 0)

v2D = Vector(1, 2)
v2D #=> Vector(1, 2, 0)
```

### Compare position relationships of vectors

#### Perpendicular (orthogonal)

Two vectors can be perpendicular (orthogonal) to each other, which means that the smaller angle between the two vector is 90 degrees.

```python
is_orthogonal(v1, v2) #=> False
```

#### Collinear (parallel/anti-parallel)

Two vectors are collinear, if they are parallel or anti-parallel to each other.

```python
is_collinear(v1, v2) #=> False
```

#### Complanar

Three vectors can be in the same plane, that means they are complanar.

```python
is_complanar(v1, v2, v3) #=> False
```

### Calculation of common vector operations

All operations and calculations can be used by importing the functions. The basic operations are implemented with *operator overloading*, so regular operators can be used for same result.

#### Addition

Both lines calculates the addition of two Vector objects. It returns the same Vector object in both orders.

```python
add(v1, v2) #=> Vector(3, -2, 3)
v1 + v2
```

The addition of two Point objects returns a Vector object as the negated displacement of both Point objects.

```python
add(p1, p2) #=> Vector(3, -2, 3)
p1 + p2
```

#### Subtraction

Subtracts the one Vector object from the other Vector object. It return a Vector object.

```python
sub(v1, v2) #=> Vector(-1, 6, -9)
v1 - v2
```

The difference of two Point objects returns a Vector object as the displacement of both Point objects.

```python
sub(p1, p2) #=> Vector(-1, 6, -9)
p1 - p2
```

#### Multiplication by a real number

Multiplication of a Vector object by a real number returns a Vector object. The order of both factors doesn't matter.

```python
n = 4
mul(v1, n) #=> Vector(4, 8, -12)
v1 * n
```

#### Division by a real number

A Vector object devided by a real number means the multiplication of a Vector object by the reciprocal of the same number. It returns a Vector object only be calculated in this order.

```python
m = 2
div(v1, m) #=> Vector(0.5, 1.0, -1.5)
v1 / m
v1 * (1/m)
```

#### Negative Vector or Point

It returns a Vector pointing in the negative direction, which means it is anti-parallel.

```python
neg(v1) #=> Vector(-1, -2, 3)
-v1
```

It return a Point object with negated coordinates.

```python
neg(p1) #=> Point(-1, -2, 3)
-p1
```


#### Magnitude

The magnitude of a Vector object describes the length. It can be calculated from both lines and returns a positive real number including zero.

```python
norm(v1) #=> 3.7416573867739413
abs(v1)
```

#### Unit Vector

It returns the unit vector of a Vector object, it means a vector with the same direction but a magnitude of one.

```python
v1u = unit(v1)
v1u #=> Vector(0.2672612419124244, 0.5345224838248488, -0.8017837257372732)
norm(v1u) #=> 1.0
```

#### Dot/Scalar Product

Both lines calculates the dot product of two Vector objects. The dot product returns a real number.

```python
dot(v1, v2) #=> -24
v1 * v2
```

#### Cross/Vector Product

Both lines calculates the cross product of two Vector objects. The cross product returns a Vector object.

```python
cross(v1, v2) #=> Vector(0, -12, -8)
v1 % v2
```

#### Determinant

Calculates the determinant of three Vector objects. It returns a real number.

```python
det(v1, v2, v3) #=> -60
```

The same result is calculated by a combination of the cross product and dot product:

```python
dot(cross(v1, v2), v3)
v1 % v2 * v3
```

#### Angle

The lines calculates the smaller angle between two Vector objects, the result returns a real number. At third position the mode can be specified between degree with `"deg"` and radian with `"rad"`. Degrees is optional and the default mode.

```python
angle(v1, v2) #=> 148.997280866126
angle(v1, v2, "deg")
angle(v1, v2, "rad") #=> 2.6004931276326473
```

#### Area of a parallelogram

The following function calculates the area of a parallelogram spanned by two Vector objects. It returns a positive real number including zero.

```python
area(v1, v2) #=> 14.422205101855956
```

#### Volume of a parallelepiped

It calculates the volume of a parallelepiped spanned by three Vector objects. It returns a positive real number including zero.

```python
spate(v1, v2, v3) #=> 60
```


### Miscellaneous

#### Get and set coordinates

The single coordinates of a Point object or Vector object can be set to the given value at first position of the specified x-, y- or z-method. No matter if the value is specified, the (new) coordinate is returned as a real number.

An example:

```python
v = Vector(1, 2, 3)

v.x() #=> 1
v #=> Vector(1, 2, 3)

v.x(5) #=> 5
v #=> Vector(5, 2, 3)
```

#### Get Point of a Vector

It returns the coordinates of the point on which the Vector object pointing as an independent Point object.

```python
v = Vector(1, 2, 3)
v.point() #=> Point(1, 2, 3)
```

### Round a Point or Vector

It rounds the coordinates of a Point object or Vector object to the given decimal digits, default is zero decimal digits.

```python
v = Vector(0.3454, 2.15, -7.14)
round(v, 1) #=> Vector(0.3, 2.1, -7.1)
```

#### Iteration and lists/tuples

A Point object and a Vector object can be iterated, all three coordinates are swept.

An example:

```python
p = Point(1, 2, 3)
[ c for c in p ] #=> [1, 2, 3]
```

Another way to get a list/tuple of the coordinates of a Point object or Vector object are the following functions:

```python
list(p) #=> [1, 2, 3]
tuple(p) #=> (1, 2, 3)
```

The amount of dimensions of a Point object or Vector object in 3-dimensional space are always *3*, but the length function works anyway.

```python
len(p) #=> 3
len(v) #=> 3
```

#### Copies/Duplicates

It returns an independent copy of a Point object or Vector object.

An example:

```python
v = Vector(1, 2, 3)

v_indep = v.copy()
v_indep.x(-4)

v_dep = v
v_dep.x(-8)

v #=> Vector(-8, 2, 3)
v_indep #=> Vector(-4, 2, 3)
v_dep #=> Vector(-8, 2, 3)
```
