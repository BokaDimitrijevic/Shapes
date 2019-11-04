import math


class Point:
    """Two-Dimensional Point(x, y)"""

    def __init__(self, x=0, y=0):
        """Initialize the Point instance"""
        self.x = x
        self.y = y

    def __iter__(self):
        """Return Points that are iterable"""
        yield self.x
        yield self.y

    @property
    def magnitude(self):
        """Return the magnitude of vector from (0,0) to self."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other):
        """Returns the distance between the points"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __add__(self, other):
        """Implements addition operation for Point objects"""
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """Implements addition operation using += for Point objects"""
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, scalar):
        """Implements multiplication operation with scalars
        for Point objects"""
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Implements reverse multiplication operation with scalars
        for Point objects"""
        return Point(scalar * self.x, scalar * self.y)

    def __imul__(self, scalar):
        """Implements multiplication operation using *= with scalars
        for Point objects"""
        self.x *= scalar
        self.y *= scalar
        return self

    @classmethod
    def from_tuple(cls, coords):
        """Create Point instance objects from tuple"""
        return cls(coords[0], coords[1])

    def loc_from_tuple(self, coords):
        """Method that updates x, y values of a Point instances
        from a tuple"""
        self.x = coords[0]
        self.y = coords[1]

    def __repr__(self):
        """Developer-friendly string representation"""
        return "Point(x={}, y={})".format(self.x, self.y)

    def __str__(self):
        """Human-friendly string representation"""
        return "Point at ({}, {})".format(self.x, self.y)


class Circle:
    """Circle(center, radius) where center is a Point instance"""

    def __init__(self, center=None, radius=1):
        """Circle initializer"""
        self.center = center
        self.radius = radius

    def __add__(self, other):
        """Implements addition operation for Circle objects"""
        return Circle(self._center + other._center,
                      self._radius + other._radius)

    @property
    def area(self):
        """Calculate and return the area of the Circle"""
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        """Calculate and return the diameter of the Circle"""
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        """Set the diameter"""
        self.radius = diameter / 2

    @property
    def radius(self):
        """Return the radius of the Circle"""
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Set the radius of the Circle"""
        if radius < 0:
            raise ValueError("The radius cannot be negative!")
        self._radius = radius

    @property
    def center(self):
        """Return the center of the Circle"""
        return self._center

    @center.setter
    def center(self, center):
        """Set the center of the Circle"""
        if center is None:
            center = Point(0, 0)
            self._center = center
        else:
            if isinstance(center, Point):
                self._center = center
            else:
                raise TypeError("The center must be a Point!")

    def __iadd__(self, other):
        """Implements addition operation using +=
        for Circle objects"""
        self._center += other._center
        self._radius += other._radius
        return self

    @classmethod
    def from_tuple(cls, center, radius=1):
        """Create Circle instance objects from tuple center"""
        return cls(Point(center[0], center[1]), radius)

    def center_from_tuple(self, center):
        """Method that updates center value of a Circle instances
        from a tuple"""
        self._center.x = center[0]
        self._center.y = center[1]

    def __repr__(self):
        """Implements __repr__ for Circle objects"""
        return "Circle(center=Point({}, {}), radius={})".\
            format(self.center.x, self.center.y, self.radius)

    def __str__(self):
        """Implements __str__ for Circle objects"""
        return "Circle with center at ({}, {}) and radius {}".\
            format(self.center.x, self.center.y, self.radius)
