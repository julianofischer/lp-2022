from abc import ABC, abstractmethod

#Abstract Base Class
class Poligono(ABC):
    @abstractmethod
    def calc_area(self):
        pass
#duck typying
class Retangulo(Poligono):
    def __init__(self, l1, l2):
        self.lado1=l1
        self.lado2=l2

    def calc_area(self):
        return self.lado1 * self.lado2

r = Retangulo(10, 5)
print(r.calc_area())
