class Vec3d:
    # _x: float = 0.
    # _y: float = 0.
    # _z: float = 0.

    # def vec_const(v, x: float = 0, y: float = 0, z: float = 0):
    #     v._x = x
    #     v._y = y
    #     v._z = z
    #     v.len = (x**2 + y**2 + z**2)**0.5
    
    def __init__(
            self,
            x: float = 0,
            y: float = 0,
            z: float = 0
        ) -> None:
        self._x = float(x)
        self._y = float(y)
        self._z = float(z)    
    def __str__(self):
        return f"Vec3d({self._x}; {self._y}; {self._z})"
    def __repr__(self):
        return str(self)
    def __abs__(self):
        len2 = self._x**2 + self._y**2 + self._z**2
        return len2**0.5
    def __bool__(self):
        return bool(abs(self))
    def __iter__(self):
        coordinates = (self._x, self._y, self._z)
        return (coord for coord in coordinates)
    def __eq__(self, ano):
        return tuple(self) == tuple(ano)
    def __neg__(self):
        return Vec3d(-self._x, -self._y, -self._z)
    def __add__(self, ano):
        _x = self._x + ano._x
        _y = self._y + ano._y
        _z = self._z + ano._z
        return Vec3d(_x, _y, _z)
    def __sub__(self, ano):
        return self + -ano
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError
        _x = self._x * scalar
        _y = self._y * scalar
        _z = self._z * scalar
        return Vec3d(_x, _y, _z)
    def __rmul__(self, scalar):
        return self * scalar
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError
        return self * (1/scalar)
    
    def dot(self, other):
        x = self._x * other._x
        y = self._y * other._y
        z = self._z * other._z
        return x + y + z
    def cross(self, other):
        x = self._y * other._z - other._y * self._z
        y = -( self._x * other._z - other._x * self._z )
        z = self._x * other._y - other._x * self._y
        return Vec3d(x, y, z)
    def to_line(self, start, side):
        to_start = self - start
        h = abs(to_start.cross(side)) / abs(side)
        return h
    def to_part(self, start, end):
        side = end - start
        D_start = -( start.dot(side) )
        D_end = -( end.dot(side))
        if self.dot(side) + D_start > 0 and self.dot(side) + D_end < 0:
            return self.to_line(start, side)
        
        to_start = abs(self - start)
        to_end = abs(self - end)
        return min( to_start, to_end )

    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def z(self):
        return self._z
Vec1 = Vec3d(2, 1, 0)
Vec2 = Vec3d(0, 1, 0)
Vec3 = Vec3d(0, 1, 2)
print(Vec1)
print(abs(Vec1))
print(bool(Vec1))
for i in Vec1:
    print(i)
print(tuple(Vec1))
print(Vec1 == Vec3)
print(dir(Vec1))
print(Vec1 - Vec2)
print(Vec1*3)
print(3.14*Vec2)
print(Vec3/4)
print(Vec1.x)
#функцию расстояния от точки до прямой сделать
print(Vec1.dot(Vec2))
print(Vec1.cross(Vec2))
print(Vec1.to_line(Vec2, Vec3))