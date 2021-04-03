
from math import sqrt, acos

# Vector in R3
class Vector:
	def __init__(self, *args):
		# Vector to a point (location vector)
		x, y, z = None, None, None
		# Create from single Point or list/tuple
		if len(args) == 1:
			p = args[0]
			if type(p) is Point:
				x, y, z = p.x(), p.y(), p.z()
			elif type(p) is list or type(p) is tuple:
				if len(p) == 3:
					x, y, z = p
		# Create from two Points (difference of p1 and p2: p2 - p1)
		elif len(args) == 2:
			p1, p2 = args[0], args[1]
			if type(p1) is Point and type(p2) is Point:
				p = Vector(p2 - p1)
				x, y, z = p.x(), p.y(), p.z()
		# Create from three single variables
		elif len(args) == 3:
			x, y, z = args[0], args[1], args[2]
		# Check data type
		if x is None or y is None or z is None:
			raise TypeError("needs single Point or list/tuple with three dimensions; two Points; or three single variables")
		elif ( type(x) is float or type(x) is int ) and ( type(y) is float or type(y) is int ) and ( type(z) is float or type(z) is int ):
			self.__point = (x, y, z)
		else:
			raise TypeError("coordinate values must be float or int")
		
	# Return individual coordinate values if value is None, else set on value
	def x(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (value, self.__point[1], self.__point[2])
			return self.__point[0]
		else:
			TypeError("value must be int, float or None")
	def y(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (self.__point[0], value, self.__point[2])
			return self.__point[1]
		else:
			TypeError("value must be int, float or None")
	def z(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (self.__point[0], self.__point[1], value)
			return self.__point[2]
		else:
			TypeError("value must be int, float or None")
	
	# Data types
	def __str__(self): return self.__repr__()
	def __repr__(self): return f"Vector({self.x()}, {self.y()}, {self.z()})"
	def __len__(self): return len(self.__point)
	def __iter__(self): return iter(self.__point)
	
	# Arithmetic operations
	def __add__(self, a): return add(self, a)
	def __sub__(self, a): return sub(self, a)
	def __mod__(self, a): return cross(self, a)
	def __truediv__(self, a): return div(self, a)
	def __pow__(self, a): return pow(self, a)
	def __rmul__(self, a): return self.__mul__(a)
	def __mul__(self, a):
		if type(a) is int or type(a) is float:
			return mul(self, a)
		elif type(a) is Vector:
			return dot(self, a)
		else:
			raise TypeError("must be int, float or Vector")
	
	# Unary oprations
	def __neg__(self): return neg(self)
	def __pos__(self): return self
	def __abs__(self): return norm(self)
	
	# Comparison operations as location relationships between vectors
	def __eq__(self, a): return is_collinear(self, a)
	def __ne__(self, a): return not self.__eq__(a)
	
	# Return a copy
	def copy(self): return Vector(self.x(), self.y(), self.z())


# Point in R3
class Point:
	def __init__(self, *args):
		# Single Point
		x, y, z = None, None, None
		# Create from list/tuple
		if len(args) == 1:
			p = args[0]
			if type(p) is list or type(p) is tuple:
				if len(p) == 3:
					x, y, z = p
		# Create from three single variables
		elif len(args) == 3:
			x, y, z = args[0], args[1], args[2]
		# Check data type
		if x is None or y is None or z is None:
			raise TypeError("needs list/tuple with three dimensions; or three single variables")
		elif ( type(x) is float or type(x) is int ) and ( type(y) is float or type(y) is int ) and ( type(z) is float or type(z) is int ):
			self.__point = (x, y, z)
		else:
			raise TypeError("coordinate values must be float or int")
	
	# Return individual coordinate values if value is None, else set on value
	def x(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (value, self.__point[1], self.__point[2])
			return self.__point[0]
		else:
			TypeError("value must be int, float or None")
	def y(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (self.__point[0], value, self.__point[2])
			return self.__point[1]
		else:
			TypeError("value must be int, float or None")
	def z(self, value=None):
		if type(value) is int or type(value) is float or value is None:
			if value is not None:
				self.__point = (self.__point[0], self.__point[1], value)
			return self.__point[2]
		else:
			TypeError("value must be int, float or None")
	
	# Data types
	def __str__(self): return self.__repr__()
	def __repr__(self): return f"Point({self.x()}, {self.y()}, {self.z()})"
	def __len__(self): return len(self.__point)
	def __iter__(self): return iter(self.__point)
	
	# Arithmetic operations
	def __add__(self, a): return add(self, a)
	def __sub__(self, a): return sub(self, a)	
	
	# Unary oprations
	def __neg__(self): return neg(self)
	def __pos__(self): return self
	
	# Comparison operations
	def __eq__(self, a): return self.x() == a.x() and self.y() == a.y() and self.z() == a.z()
	def __ne__(self, a): return not self.__eq__(a)
	
	# Return a copy
	def copy(self): return Point(self.x(), self.y(), self.z())

# Basic vector operations for R3
# Norm
def norm(a):
	if type(a) is Vector:
		return sqrt(a.x()**2 + a.y()**2 + a.z()**2)
	else:
		raise TypeError("must be Vector")

# Negative
def neg(a):
	if type(a) is Vector:
		return Vector(a.x()*(-1), a.y()*(-1), a.z()*(-1))
	elif type(a) is Point:
		return Point(a.x()*(-1), a.y()*(-1), a.z()*(-1))
	else:
		raise TypeError("must be Vector or Point")

# Additon
def add(a, b):
	if ( type(a) is Vector and type(b) is Vector ) or ( type(a) is Point and type(b) is Point ):
		return Vector(a.x()+b.x(), a.y()+b.y(), a.z()+b.z())
	else:
		raise TypeError("must be two Vectors or two Points")

# Subtraction
def sub(a, b):
	if ( type(a) is Vector and type(b) is Vector ) or ( type(a) is Point and type(b) is Point ):
		return add(a, -b)
	else:
		raise TypeError("must be two Vectors or two Points")

# Multiplication
def mul(a, b):
	if ( type(a) is int or type(a) is float ) and type(b) is Vector:
		a, b = b, a
	elif ( type(b) is int or type(b) is float ) and type(a) is Vector:
		pass
	else:
		raise TypeError("must be Vector and int or float")
	return Vector(a.x()*b, a.y()*b, a.z()*b)

# Division
def div(a, b):
	if type(a) is Vector and ( type(b) is int or type(b) is float ):
		return mul(a, 1/b)
	else:
		raise TypeError("must be Vector and int or float")

# Pow: a**2 = dot(a, a)
def pow(a, b=2):
	if type(a) is Vector and type(b) is int:
		if b == 2:
			return dot(a, a)
		else:
			raise ValueError("exponent must be two")
	else:
		raise TypeError("must be Vector and int")

# Cross product
def cross(a, b):
	if type(a) is Vector and type(b) is Vector:
		return Vector(a.x()*b.y() - b.x()*a.y(), a.y()*b.z() - b.y()*a.z(), a.z()*b.x() - b.z()*a.x())
	else:
		raise TypeError("must be Vector")

# Dot product
def dot(a, b):
	if type(a) is Vector and type(b) is Vector:
		return a.x()*b.x() + a.y()*b.y() + a.z()*b.z()
	else:
		raise TypeError("must be Vector")

# Determinant or spate volume
def det(a, b, c):
	if type(a) is Vector and type(b) is Vector and type(c) is Vector:
		#a.x()*b.y()*c.z() + b.x()*c.y()*a.z() + c.x()*a.y()*b.z() - b.x()*a.y()*c.z() - a.x()*c.y()*b.z() - c.x()*b.y()*a.z()
		return dot(cross(a, b), c)
	else:
		raise TypeError("must be Vector")
def spate(a, b, c):
	if type(a) is Vector and type(b) is Vector and type(c) is Vector:
		return abs(det(a, b, c))
	else:
		raise TypeError("must be Vector")

# Non-surplus angle between a and b
def angle(a, b):
	if type(a) is Vector and type(b) is Vector:
		return acos(dot(a, b) / (norm(a) * norm(b)))
	else:
		raise TypeError("must be Vector")

# Area of a parallelogram spanned by two vectors
def area(a, b):
	if type(a) is Vector and type(b) is Vector:
		return norm(cross(a, b))
	else:
		raise TypeError("must be Vector")


# Location relationships between vectors
# is_complanar
def is_complanar(a, b, c):
	if type(a) is Vector and type(b) is Vector and type(c) is Vector:
		if spate(a, b, c) == 0:
			return True
		else:
			return False
	else:
		raise TypeError("must be Vector")

# is_collinear
def is_collinear(a, b):
	if type(a) is Vector and type(b) is Vector:
		if abs(dot(a, b)) == norm(a) * norm(b):
			return True
		else:
			return False
	else:
		raise TypeError("must be Vector")

# is_orthogonal
def is_orthogonal(a, b):
	if type(a) is Vector and type(b) is Vector:
		if dot(a, b) == 0:
			return True
		else:
			return False
	else:
		raise TypeError("must be Vector")
