from abc import ABC, abstractclassmethod
class shape(ABC):
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimter(self):
        pass
class square(shape):
    def __init__