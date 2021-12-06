
from math import sqrt, acos, degrees


__project__ = "vectometry"
__version__ = "2021.9"
__author__ = "InformaticFreak"
__description__ = "A Python library for simple use of common point, vector, line and plane operations in 3-dimensional space as well as for 2-dimensions."


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
			if isinstance(p, (list, tuple)):
				if len(p) == 3:
					x, y, z = p
				elif len(p) == 2:
					x, y = p
					z = 0
		elif len(args) == 2:
			x, y, z = args[0], args[1], 0
		elif len(args) == 3:
			x, y, z = args[0], args[1], args[2]
		if isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float)):
			self.__point = (x, y, z)
		else:
			raise TypeError
	
	def x(self, value=None):
		"""Returns x-coordinate value and set it to specific value, if it is given"""
		if value is not None:
			if isinstance(value, (int, float)):
				self.__point = (value, self.__point[1], self.__point[2])
			else:
				raise TypeError
		return self.__point[0]
	def y(self, value=None):
		"""Returns y-coordinate value and set it to specific value, if it is given"""
		if value is not None:
			if isinstance(value, (int, float)):
				self.__point = (self.__point[0], value, self.__point[2])
			else:
				raise TypeError
		return self.__point[1]
	def z(self, value=None):
		"""Returns z-coordinate value and set it to specific value, if it is given"""
		if value is not None:
			if isinstance(value, (int, float)):
				self.__point = (self.__point[0], self.__point[1], value)
			else:
				raise TypeError
		return self.__point[2]
	
	def copy(self):
		"""Returns an independent Point object as a copy of the original"""
		return Point(self.x(), self.y(), self.z())
	
	def __str__(self):
		"""Returns a string representing the Point object"""
		return self.__repr__()
	def __repr__(self):
		"""Returns a string representing the Point object"""
		return f"{self.__class__.__name__}({self.x()}, {self.y()}, {self.z()})"
	
	def __len__(self):
		"""Returns the amount of dimensions (always three)"""
		return len(self.__point)
	def __iter__(self):
		"""Returns an iterable object including the coordinates"""
		return iter(self.__point)
	
	def __add__(self, other):
		"""Returns a Vector object as the negated displacement of both Point objects"""
		return add(self, other)
	def __sub__(self, other):
		"""Returns a Vector object as the displacement of both Point objects"""
		return sub(self, other)	
	
	def __neg__(self):
		"""Returns a Point object with negated coordinates"""
		return neg(self)
	def __pos__(self):
		"""Returns the Point object"""
		return self
	def __round__(self, n=0):
		"""Returns a Point object, but the coordinates are rounded to the given decimal digits, default is zero decimal digits"""
		return Point(
			round(self.x(), n),
			round(self.y(), n),
			round(self.z(), n)
		)
	
	def __eq__(self, other):
		"""Returns True if every coordinate of both Point objects are equal, else False"""
		return self.x() == other.x() and self.y() == other.y() and self.z() == other.z()
	def __ne__(self, other):
		"""Returns True if not every coordinate of both Point objects are equal, else False"""
		return not self.__eq__(other)


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
			elif isinstance(p, (list, tuple)):
				self.__point = Point(p)
			else:
				raise TypeError
		elif len(args) == 2:
			p1, p2 = args[0], args[1]
			if type(p1) is Point and type(p2) is Point:
				p = sub(p2, p1)
				self.__point = p.point()
			elif isinstance(p1, (int, float)) and isinstance(p2, (int, float)):
				self.__point = Point(p1, p2, 0)
			else:
				raise TypeError
		elif len(args) == 3:
			self.__point = Point(*args)
		else:
			raise TypeError
	
	def x(self, value=None):
		"""Returns x-coordinate value and set it to specific value, if it is given"""
		return self.__point.x(value)
	def y(self, value=None):
		"""Returns y-coordinate value and set it to specific value, if it is given"""
		return self.__point.y(value)
	def z(self, value=None):
		"""Returns z-coordinate value and set it to specific value, if it is given"""
		return self.__point.z(value)
	def point(self):
		"""Returns the coordinates to which the vector pointing as a reference to the Point object"""
		return self.__point
	
	def copy(self):
		"""Returns an independent Vector object as a copy of the original"""
		return Vector(self.point().copy())
	
	def __str__(self):
		"""Returns a string representing the Vector object"""
		return self.__repr__()
	def __repr__(self):
		"""Returns a string representing the Vector object"""
		return f"{self.__class__.__name__}({self.x()}, {self.y()}, {self.z()})"
	
	def __len__(self):
		"""Returns the amount of dimensions (always three)"""
		return len(self.__point)
	def __iter__(self):
		"""Returns an iterable object including the coordinates"""
		return iter(self.__point)
	
	def __add__(self, other):
		"""Returns the addition of two Vector objects"""
		return add(self, other)
	def __sub__(self, other):
		"""Returns the difference of two Vector objects"""
		return sub(self, other)
	def __mod__(self, other):
		"""Returns the cross product of two Vector objects"""
		return cross(self, other)
	def __truediv__(self, other):
		"""Returns the multiplication of a Vector object by the reciprocal of the real number"""
		return div(self, other)
	def __rmul__(self, other):
		"""Returns the multiplication of a Vector object by a real number or by another Vector object, means the dot product"""
		return self.__mul__(other)
	def __mul__(self, other):
		"""Returns the multiplication of a Vector object by a real number or by another Vector object, means the dot product"""
		if type(other) is int or type(other) is float: 
			return mul(self, other)
		elif type(other) is Vector:
			return dot(self, other)
		else:
			raise TypeError
	
	def __neg__(self):
		"""Returns a Vector object with negated coordinates"""
		return neg(self)
	def __pos__(self):
		"""Returns the Vector object"""
		return self
	def __abs__(self):
		"""Returns the magnitude of the Vector object as a real number"""
		return norm(self)
	def __round__(self, n=0):
		"""Returns a Vector object, but the coordinates are rounded to the given decimal digits, default is zero decimal digits"""
		return Vector(
			round(self.x(), n),
			round(self.y(), n),
			round(self.z(), n)
		)
	
	def __eq__(self, other):
		"""Returns True if both points on which the vectors points are the same (same lenght and same direction), else False"""
		return self.point() == other.point()
	def __ne__(self, other):
		"""Returns True if both points on which the vectors pointing are not the same, else False"""
		return not self.__eq__(other)


class Line:
	"""Line object represents a straight line in 3-dimensional space, means x, y and z coordinates.
	
	Accepts initialization equations:
	(Upper case letters represents Points/Vectors and lower case letters represents real numbers)
	 - [P]	Parameter equation		0 = R + s*D - X			{R as Point; D as Vector}	(default mode)
									0 = R + s*(D-R) - X		{R,D as Point}
	"""
	def __init__(self, fmt="P", **kwargs):
		if type(fmt) is str:
			fmt = fmt.upper()
			if fmt == "P":
				if type(kwargs.get("R")) is Point:
					R = kwargs["R"]
				else:
					raise TypeError
				if type(kwargs.get("D")) is Point:
					D = sub(kwargs["D"], R)
				elif type(kwargs.get("D")) is Vector:
					D = kwargs["D"]
				else:
					raise TypeError
			else:
				raise ValueError
		else:
			raise TypeError
		self.__R = R
		self.__D = D
	
	def R(self, value=None):
		"""Returns the receptor Point R as real number and set it to specific value, if it is given"""
		if value is not None:
			if type(value) is Vector:
				self.__R = value
			else:
				raise TypeError
		return self.__R
	def D(self, value=None):
		"""Returns the direction Vector D and set it to specific value, if it is given"""
		if value is not None:
			if isinstance(value, (int, float)):
				self.__D = value
			else:
				raise TypeError
		return self.__D
	
	def copy(self):
		"""Returns an independent Plane object as a copy of the original"""
		return Line("P", R=self.R().copy(), D=self.D().copy())
	
	def __str__(self):
		"""Returns a string representing the Line object"""
		return self.__repr__()
	def __repr__(self):
		"""Returns a string representing the Line object"""
		return f"{self.__class__.__name__}('P', R={self.R()}, D={self.D()})"
		
	def __round__(self, n=0):
		"""Returns a Line object, but the coordinates of the receptor point R and direction Vector D are rounded to the given decimal digits, default is zero decimal digits"""
		return Line("P", R=round(self.R(), n), D=round(self.D(), n))
	
	def __eq__(self, other):
		"""Returns True if both Lines are identical to each other (means parallel and no distance), else False"""
		return is_collinear(self.D(), other.D()) and distance(self, other) == 0
	def __ne__(self, other):
		"""Returns True if both Lines are not identical to each other, else False"""
		return not self.__eq__(other)
	
	def __call__(self, X):
		"""Insert the given Point into the line function \'R + s*D - X\' and return the result for the parameter s. If the result is zero, the given Point is not located in the line."""
		if type(X) is Point:
			s1 = (X.x() - self.R.x()) / self.D.x()
			s2 = (X.y() - self.R.y()) / self.D.y()
			s3 = (X.z() - self.R.z()) / self.D.z()
			if s1 == s2 == s3:
				return s1
			else:
				return 0
		elif type(X) is Vector:
			return self.__call__(X.point())
		else:
			raise TypeError


class Plane:
	"""Plane object represents a plane/layer in 3-dimensional space, means x, y and z coordinates.
	
	Accepts initialization equations:
	(Upper case letters represents Points/Vectors and lower case letters represents real numbers)
	 - [P]	Parameter equation	0 = R + m*D + t*S - X						{R as Point; D,S as Vector}					(default mode)
								0 = R + m*(D-R) + t*(S-R) - X				{R,D,S as Point}
	 - [C]	Coordinate equation	0 = Nx*Xx + Ny*Xy + Nz*Xz + n0 = N ° X + n0	{N as Vector(Nx, Ny, Nz); n0 as int/float}
	 - [N]	Normal equation		0 = N ° (X-R)								{N as Vector; R as Point}
	"""
	def __init__(self, fmt="P", **kwargs):
		if type(fmt) is str:
			fmt = fmt.upper()
			if fmt == "P":
				if type(kwargs.get("R")) is Point:
					R = kwargs["R"]
				else:
					raise TypeError
				if type(kwargs.get("D")) is type(kwargs.get("S")) is Point:
					D = sub(kwargs["D"], R)
					S = sub(kwargs["S"], R)
				elif type(kwargs.get("D")) is type(kwargs.get("S")) is Vector:
					D = kwargs["D"]
					S = kwargs["S"]
				else:
					raise TypeError
				N = cross(D, S)
			elif fmt == "C":
				if type(kwargs.get("N")) is Vector and isinstance(kwargs.get("n0"), (int, float)):
					N = kwargs["N"]
					n0 = kwargs["n0"]
					x, y, z = 0, 0, 0
					if N.x() != 0:
						x = n0 / N.x()
					elif N.y() != 0:
						y = n0 / N.y()
					elif N.z() != 0:
						z = n0 / N.z()
					else:
						raise ZeroDivisionError
					R = Point(x, y, z)
				else:
					raise TypeError
			elif fmt == "N":
				if type(kwargs.get("N")) is Vector and type(kwargs.get("R")) is Point:
					N = kwargs["N"]
					R = kwargs["R"]
				else:
					raise TypeError
			else:
				raise ValueError
		else:
			raise TypeError
		self.__N = N
		self.__R = R
	
	def N(self, value=None):
		"""Returns the normal Vector N and set it to specific value, if it is given"""
		if value is not None:
			if type(value) is Vector:
				self.__N = value
			else:
				raise TypeError
		return self.__N
	def R(self, value=None):
		"""Returns the receptor Point R and set it to specific value, if it is given"""
		if value is not None:
			if type(value) is Point:
				self.__R = value
			else:
				raise TypeError
		return self.__R
	
	def fmt(self, fmt="P"):
		"""Returns for one of the initialization formats the attributes of the Plane as dictionary"""
		fmt = fmt.upper()
		if fmt == "P":
			return {
				# "R": Point(0, 0, dot(self.N(), self.R()) / self.N().z()),
				"R": self.R(),
				"D": Vector(1, 0, -(self.N().x() / self.N().z())),
				"S": Vector(0, 1, -(self.N().y() / self.N().z()))
			}
		elif fmt == "C":
			return {
				"N": self.N(),
				"n0": dot(self.N(), Vector(self.R()))
			}
		elif fmt == "N":
			return {
				"N": self.N(),
				"R": self.R()
			}
		else:
			raise ValueError
	
	def copy(self):
		"""Returns an independent Plane object as a copy of the original"""
		return Plane("N", N=self.N().copy(), R=self.R().copy())
	
	def __str__(self):
		"""Returns a string representing the Plane object"""
		return self.__repr__()
	def __repr__(self):
		"""Returns a string representing the Plane object"""
		return f"{self.__class__.__name__}('N', N={self.N()}, R={self.R()})"
		
	def __round__(self, n=0):
		"""Returns a Plane object, but the coordinates of the normal Vector N and receptor Point R are rounded to the given decimal digits, default is zero decimal digits"""
		return Plane("N", N=round(self.N(), n), R=round(self.R(), n))
	
	def __eq__(self, other):
		"""Returns True if both Planes are identical to each other (means parallel and no distance), else False"""
		return is_collinear(self.N(), other.N()) and distance(self, other) == 0
	def __ne__(self, other):
		"""Returns True if both Planes are not identical to each other, else False"""
		return not self.__eq__(other)
	
	def __call__(self, X):
		"""Insert the given Point into the plane function \'N ° (X-R)\' and return the result of it. If the result is zero, the given Point is located in the plane."""
		if type(X) is Point:
			return dot(self.N(), sub(X, self.R()))
		elif type(X) is Vector:
			return self.__call__(X.point())
		else:
			raise TypeError


def norm(a):
	"""Returns the magnitude of the Vector object as a real number"""
	if type(a) is Vector:
		return sqrt(sum([ p**2 for p in a ]))
	else:
		raise TypeError
def unit(a):
	"""Returns the unit vector of the Vector object, it means a vector with the same direction but a magnitude of one"""
	if type(a) is Vector:
		return div(a, norm(a))
	else:
		raise TypeError
def neg(a):
	"""Returns the given object (Point/Vector) with negated coordinates"""
	if type(a) is Vector:
		return Vector([ -p for p in a ])
	elif type(a) is Point:
		return Point([ -p for p in a ])
	else:
		raise TypeError

def add(a, b):
	"""Cases:
	 - Two Vector objects: Returns the addition of two Vector objects
	 - Two Point objects: Returns a Vector object as the negated displacement of both Point objects
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
	 - Two Vector objects: Returns the difference of two Vector objects
	 - Two Point objects: Returns a Vector object as the displacement of both Point objects
	"""
	return add(a, neg(b))

def mul(a, b):
	"""Returns the multiplication of a Vector object by a real number"""
	if isinstance(a, (int, float)) and type(b) is Vector:
		return mul(b, a)
	elif isinstance(b, (int, float)) and type(a) is Vector:
		return Vector([ p*b for p in a ])
	else:
		raise TypeError
def div(a, b):
	"""Returns the multiplication of a Vector object by the reciprocal of the real number"""
	if isinstance(b, (int, float)):
		return mul(a, 1/b)
	else:
		raise TypeError

def cross(a, b):
	"""Returns the cross product of two Vector objects as a Vector object"""
	if type(a) is Vector and type(b) is Vector:
		return Vector(
			a.y()*b.z() - b.y()*a.z(),
			a.z()*b.x() - b.z()*a.x(),
			a.x()*b.y() - b.x()*a.y()
		)
	else:
		raise TypeError
def dot(a, b):
	"""Returns the dot product of two Vector objects as a real number"""
	if type(a) is Vector and type(b) is Vector:
		return a.x()*b.x() + a.y()*b.y() + a.z()*b.z()
	else:
		raise TypeError

def det(a, b, c):
	"""Returns the determinant of three Vector objects as a real number"""
	return dot(cross(a, b), c)

def spate(a, b, c):
	"""Returns the volume of a parallelepiped spanned by three Vector objects as a positive real number including zero"""
	return abs(det(a, b, c))
def area(a, b):
	"""Returns the area of a parallelogram spanned by two Vector objects as a position real number including zero"""
	return norm(cross(a, b))

def angle(a, b, mode="DEG"):
	"""Returns the smaller angle between two vectometry objects as a real number, except Point objects
	Mode:
	 - In degree with mode \'DEG\'	(default mode)
	 - In radian with mode \'RAD\'
	"""
	if type(a) is type(b) is Vector:
		rad_angle = acos(dot(a, b) / (norm(a) * norm(b)))
	elif type(a) is type(b) is Line:
		return angle(a.D(), b.D())
	elif type(a) is type(b) is Plane:
		return angle(a.N(), b.N())
	elif type(a) is Line and type(b) is Vector:
		return angle(a.D(), b)
	elif type(a) is Plane and type(b) is Vector:
		return angle(a.N(), b)
	elif type(a) is Line and type(b) is Plane:
		return angle(a.D(), b.N())
	else:
		raise TypeError
	mode = mode.upper()
	if mode == "DEG":
		return degrees(rad_angle)
	elif mode == "RAD":
		return rad_angle
	else:
		raise ValueError

def is_complanar(a, b, c):
	"""Returns True if all three Vector objects are in the same plane, else False"""
	return spate(a, b, c) == 0
def is_collinear(a, b):
	"""Returns True if both Vector objects are parallel or anti-parallel to each other, else False"""
	return abs(dot(a, b)) == norm(a) * norm(b)
def is_orthogonal(a, b):
	"""Returns True if both Vector objects are perpendicular to each other, else False"""
	return dot(a, b) == 0

def distance(a, b):
	"""Returns the distance between two vectometry objects, except Vector objects"""
	if type(a) is type(b) is Point:
		return norm(Vector(a, b))
	elif type(a) is type(b) is Plane:
		if is_collinear(a.N(), b.N()):
			return distance(a, b.R())
	elif type(a) is type(b) is Line:
		if is_collinear(a.D(), b.D()):
			# https://www.mathebibel.de/abstand-paralleler-geraden
			pass
		elif "WINDSCHIEF": #engl.: warped?
			e = Plane("N", N=cross(a.D(), b.D()), R=a.R())
			return distance(e, b.R())
	elif type(a) is Line and type(b) is Plane:
		if is_orthogonal(a.D(), b.N()):
			return distance(b, a.R())
	elif type(a) is Plane and type(b) is Line:
		return distance(b, a)
	elif type(a) is Line and type(b) is Point:
		if a(b) == 0:
			# https://www.mathebibel.de/abstand-punkt-gerade
			e = Plane("N", N=a.D(), R=b)
	elif type(a) is Point and type(b) is Line:
		return distance(b, a)
	elif type(a) is Plane and type(b) is Point:
		e = a.copy()
		e.N(unit(e.N()))
		return abs(e(b))
	elif type(a) is Point and type(b) is Plane:
		return distance(b, a)
	else:
		raise TypeError

def intersect(a, b):
	"""Returns a list of Points defining the intersection Point/Line/Plane of two vectometry objects, except Vector objects, else an empty list"""
	return []
