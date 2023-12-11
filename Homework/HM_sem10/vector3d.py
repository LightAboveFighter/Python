"""
- __init__() -  инициализация экземпляра класса. Конструирует новый объект типа Vector3D 
                из трех чисел с плавающей точкой(float). По умолчанию конструирует нулевой вектор. 
                Если пользователь попытается инициализировать объект нечисловыми типами, 
                необходимо бросить исключение;  
- __repr__() -  возвращает текстовую строку: `'Vector3D(x, y, z)'`, где x, y, z - значения компонент;  
- __abs__() -   возвращает длину вектора;  
- __bool__() -  возвращает True, если вектор ненулевой, иначе - False;  
- __eq__(other) - сравнивает два вектора, возвращает True, если векторы равны покомпонентно, иначе False;  
- __neg__() -   возвращает новый объект типа Vector3D, компоненты которого равны компонентам данного вектора, 
                домноженным на минус единицу;  
- __add__(other) - складывает два вектора, возвращает новый объект типа Vector3D - сумму;  
- __sub__(other) - вычитает вектор other из данного вектора, возвращает новый объект типа Vector3D - разность;  
- __mul__(scalar) - умножение вектора на скаляр слева, возвращает новый объект типа Vector3D - произведение;  
- __rmul__(scalar) - умножение вектора на скаляр справа, возвращает новый объект типа Vector3D - произведение;  
- __truediv__(scalar) - деление вектора на скаляр, возвращает новый объект типа Vector3D - частное;  
- dot(other) - возвращает результат скалярного произведения;  
- cross(other) - возвращает векторное произведение между векторами; 

"""
from typing import Generator, Any


class Vector3D:
    __x: float
    __y: float
    __z: float
    
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        z: float = 0
    ) -> None:
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)
        
    def __iter__(self) -> Generator[float, float, float]:
        coord = (self.__x, self.__y, self.__z)

        return (coord for coord in coords)
    
    def __repr__(self) -> str:
        return f'Vector3D({self.__x}, {self.__y}, {self.__z})'
    
    def __abs__(self) -> float:
        return float((self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5)
    
    def __bool__(self) -> bool:
        return bool(abs(self))
    
    def __eq__(self, other: Any) -> bool:    
        return tuple(self) == tuple(other)
    
    def __neg__(self):
        return (-1) * self
    
    def __add__(self, other):
        return Vector3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
    
    def __sub__(self, other):
        return self + (- other)
    
    def __mul__(self, scalar: float):
        return Vector3D(scalar * self.__x, scalar * self.__y, scalar * self.__z)
    
    def __rmul__(self, scalar: float):
        return Vector3D(self.__x * scalar, self.__y * scalar, self.__z * scalar)
    
    def __truediv__(self, scalar):
        return (1 / scalar) * self
    
    def dot(self, other) -> float:
        return float(self.__x * other.x + self.__y * other.y + self.__z * other.z)
    
    def cross(self, other):
        return Vector3D(self.__y * other.z - self.__z * other.y,
                        self.__z * other.x - self.__x * other.z,
                        self.__x * other.y - self.__y * other.x)
    def cos(self, other) -> float:
        return float(self.dot(other) / (abs(self) * abs(other)))

    def sin(self, other) -> float:
        return float((1 - (self.cos(other)) ** 2) ** 0.5)
    
    def dist(self, A, B) -> float:
        if (self - A).cos(B - A)<=0 or (self - B).cos(A - B):
            return float(min(abs(self - A), abs(self - B)))
        else:
            return float(abs(self - A) * (self - A).sin(B - A))
        
    @property
    def x(self) -> float:
        return self.__x
    
    @property
    def y(self) -> float:
        return self.__y
    
    @property
    def z(self) -> float:
        return self.__z