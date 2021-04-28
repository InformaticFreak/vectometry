
"""
A Python library for simple use of common vector and point operations in 3-dimensional space as well as for 2-dimensions.
Copyright (c) 2021 InformaticFreak
Version 2021.8
"""

from math import sqrt, acos, degrees


class Point:
	"""Point object represents a point in 3-dimensional space, means x, y and z coordinates
	
	Accepts initialization formats:
	 - List/tuple with three/two real numbers
	 - Three/Two single real numbers
	"""
	def __init__(self, *args):
		x, y, z = None, None, None
		if len(args) == 1:
			p = args[0]
			if type(p) is list or type(p) is tuple:
				if len(p) == 3:
					x, y, z = p
				elif len(p) == 2:
					x, y = p
					z = 0
		elif len(args) == 2:
			x, y, z = args[0], args[1], 0
		elif len(args) == 3:
			x, y, z = args[0], args[1], args[2]
		if ( type(x) is float or type(x) is int ) and ( type(y) is float or type(y) is int ) and ( type(z) is float or type(z) is int ):
			self.__point = (x, y, z)
		else:
			raise TypeError
	
	def x(self, value=None):
		"""Return x-coordinate value and set it to specific value, if it is given at first position"""
		if value is not None:
			if type(value) is int or type(value) is float:
				self.__point = (value, self.__point[1], self.__point[2])
			else:
				raise TypeError
		return self.__point[0]
	def y(self, value=None):
		"""Return y-coordinate value and set it to specific value, if it is given at first position"""
		if value is not None:
			if type(value) is int or type(value) is float:
				self.__point = (self.__point[0], value, self.__point[2])
			else:
				raise TypeError
		return self.__point[1]
	def z(self, value=None):
		"""Return z-coordinate value and set it to specific value, if it is given at first position"""
		if value is not None:
			if type(value) is int or type(value) is float:
				self.__point = (self.__point[0], self.__point[1], value)
			else:
				raise TypeError
		return self.__point[2]
	
	def __str__(self):
		"""Return a string representing the Point object"""
		return self.__repr__()
	def __repr__(self):
		"""Return a string representing the Point object"""
		return f"{self.__class__.__name__}({self.x()}, {self.y()}, {self.z()})"
	def __len__(self):
		"""Return the amount of dimensions (always three)"""
		return len(self.__point)
	def __iter__(self):
		"""Return an iterable object including the coordinates"""
		return iter(self.__point)
	
	def __add__(self, other):
		"""Return a Vector object as the negated displacement of both Point objects"""
		return add(self, other)
	def __sub__(self, other):
		"""Return a Vector object as the displacement of both Point objects"""
		return sub(self, other)	
	
	def __neg__(self):
		"""Return a Point object with negated coordinates"""
		return neg(self)
	def __pos__(self):
		"""Return the Point object"""
		return self
	def __round__(self, n=0):
		"""Return a Point object, but the coordinates are rounded to the given decimal digits, default is zero decimal digits"""
		return Point(
			round(self.x(), n),
			round(self.y(), n),
			round(self.z(), n)
		)
	
	def __eq__(self, other):
		"""Return True if every coordinate of both Point objects are equal, else False"""
		return self.x() == other.x() and self.y() == other.y() and self.z() == other.z()
	def __ne__(self, other):
		"""Return True if not every coordinate of both Point objects are equal, else False"""
		return not self.__eq__(other)
	
	def copy(self):
		"""Return an independent Point object as a copy of the original"""
		return Point(self.x(), self.y(), self.z())


class Vector:
	"""Vector object represents a vector in 3-dimensional space, means x, y and z coordinates.
	
	Accepts initialization formats:
	 - Point object (location vector)
	 - List/tuple with three/two real numbers
	 - Two Point objects (vector from first Point object to second Point object)
	 - Three/Two single real numbers
	"""
	def __init__(self, *args):
		if len(args) == 1:
			p = args[0]
			if type(p) is Point:
				self.__point = p.copy()
			elif type(p) is list or type(p) is tuple:
				self.__point = Point(p)
			else:
				raise TypeError
		elif len(args) == 2:
			p1, p2 = args[0], args[1]
			if type(p1) is Point and type(p2) is Point:
				p = p2 - p1
				self.__point = p.point()
			elif ( type(p1) is int or type(p1) is float ) and ( type(p2) is int or type(p2) is float ):
				self.__point = Point(p1, p2, 0)
			else:
				raise TypeError
		elif len(args) == 3:
			self.__point = Point(args)
		else:
			raise TypeError
	
	def x(self, value=None):
		"""Return x-coordinate value and set it to specific value, if it is given at first position"""
		return self.__point.x(value)
	def y(self, value=None):
		"""Return y-coordinate value and set it to specific value, if it is given at first position"""
		return self.__point.y(value)
	def z(self, value=None):
		"""Return z-coordinate value and set it to specific value, if it is given at first position"""
		return self.__point.z(value)
	
	def point(self):
		"""Return the coordinates on which the vector pointing as an independent Point object"""
		return self.__point.copy()
	
	def __str__(self):
		"""Return a string representing the Vector object"""
		return self.__repr__()
	def __repr__(self):
		"""Return a string representing the Vector object"""
		return f"{self.__class__.__name__}({self.x()}, {self.y()}, {self.z()})"
	def __len__(self):
		"""Return the amount of dimensions (always three)"""
		return len(self.__point)
	def __iter__(self):
		"""Return an iterable object including the coordinates"""
		return iter(self.__point)
	
	def __add__(self, other):
		"""Return the addition of two Vector objects"""
		return add(self, other)
	def __sub__(self, other):
		"""Return the difference of two Vector objects"""
		return sub(self, other)
	def __mod__(self, other):
		"""Return the cross product of two Vector objects"""
		return cross(self, other)
	def __truediv__(self, other):
		"""Return the multiplication of a Vector object by the reciprocal of the real number"""
		return div(self, other)
	def __rmul__(self, other):
		"""Return the multiplication of a Vector object by a real number"""
		return self.__mul__(other)
	def __mul__(self, other):
		"""Return the multiplication of a Vector object by a real number"""
		if type(other) is int or type(other) is float: 
			return mul(self, other)
		elif type(other) is Vector:
			return dot(self, other)
		else:
			raise TypeError
	
	def __neg__(self):
		"""Return a Vector object with negated coordinates"""
		return neg(self)
	def __pos__(self):
		"""Return the Vector object"""
		return self
	def __abs__(self):
		"""Return the magnitude of the Vector object as a real number"""
		return norm(self)
	def __round__(self, n=0):
		"""Return a Vector object, but the coordinates are rounded to the given decimal digits, default is zero decimal digits"""
		return Vector(
			round(self.x(), n),
			round(self.y(), n),
			round(self.z(), n)
		)
	
	def __eq__(self, other):
		"""Return True if both points on which the vectors pointing are the same, else False"""
		return self.point() == other.point()
	def __ne__(self, other):
		"""Return True if both points on which the vectors pointing are not the same, else False"""
		return not self.__eq__(other)
	
	def copy(self):
		"""Return an independent Vector object as a copy of the original"""
		return Vector(self.point())


def norm(a):
	"""Return the magnitude of the Vector object as a real number"""
	if type(a) is Vector:
		return sqrt(sum([ p**2 for p in a ]))
	else:
		raise TypeError

def unit(a):
	"""Return the unit vector of the Vector object, it means a vector with the same direction but a magnitude of one"""
	if type(a) is Vector:
		return div(a, norm(a))
	else:
		raise TypeError

def neg(a):
	"""Return the given object (Point/Vector) with negated coordinates"""
	if type(a) is Vector:
		return Vector([ -p for p in a ])
	elif type(a) is Point:
		return Point([ -p for p in a ])
	else:
		raise TypeError

def add(a, b):
	"""Cases:
	
	Two Vector objects: Return the addition of two Vector objects
	Two Point objects: Return a Vector object as the negated displacement of both Point objects
	"""
	if ( type(a) is type(b) is Vector ) or ( type(a) is type(b) is Point ):
		return Vector(
			a.x()+b.x(),
			a.y()+b.y(),
			a.z()+b.z()
		)
	else:
		raise TypeError
def sub(a, b):
	"""Cases:
	
	Two Vector objects: Return the difference of two Vector objects
	Two Point objects: Return a Vector object as the displacement of both Point objects
	"""
	return add(a, neg(b))

def mul(a, b):
	"""Return the multiplication of a Vector object by a real number"""
	if ( type(a) is int or type(a) is float ) and type(b) is Vector:
		a, b = b, a
	elif ( type(b) is int or type(b) is float ) and type(a) is Vector:
		pass
	else:
		raise TypeError
	return Vector([ p*b for p in a ])
def div(a, b):
	"""Return the multiplication of a Vector object by the reciprocal of the real number"""
	return mul(a, 1/b)

def cross(a, b):
	"""Return the cross product of two Vector objects as a Vector object"""
	if type(a) is Vector and type(b) is Vector:
		return Vector(
			a.y()*b.z() - b.y()*a.z(),
			a.z()*b.x() - b.z()*a.x(),
			a.x()*b.y() - b.x()*a.y()
		)
	else:
		raise TypeError

def dot(a, b):
	"""Return the dot product of two Vector objects as a real number"""
	if type(a) is Vector and type(b) is Vector:
		return a.x()*b.x() + a.y()*b.y() + a.z()*b.z()
	else:
		raise TypeError

def det(a, b, c):
	"""Return the determinant of three Vector objects as a real number"""
	return dot(cross(a, b), c)
def spate(a, b, c):
	"""Return the volume of a parallelepiped spanned by three Vector objects as a positive real number including zero"""
	return abs(det(a, b, c))

def angle(a, b, mode="deg"):
	"""Return the smaller angle between two Vector objects as a real number
	
	Mode:
	 - In degree with mode 'deg' (default mode)
	 - In radian with mode 'rad'
	"""
	rad_angle = acos(dot(a, b) / (norm(a) * norm(b)))
	if mode == "deg":
		return degrees(rad_angle)
	elif mode == "rad":
		return rad_angle
	else:
		raise ValueError

def area(a, b):
	"""Return the area of a parallelogram spanned by two Vector objects as a position real number including zero"""
	return norm(cross(a, b))

def is_complanar(a, b, c):
	"""Return True if all three Vector objects are in the same plane, else False"""
	return spate(a, b, c) == 0
def is_collinear(a, b):
	"""Return True if both Vector objects are parallel or anti-parallel to each other, else False"""
	return abs(dot(a, b)) == norm(a) * norm(b)
def is_orthogonal(a, b):
	"""Return True if both Vector objects are perpendicular to each other, else False"""
	return dot(a, b) == 0
