from typing import Any

class Var:

    def __init__(self,name:str,render:callable,production:bool=False) -> None:
        self.name = name
        self._render = render
        self._production = production
        self._value = None
    #build in method for = operator

    def set(self,value):
        if hasattr(value,'get'):
            value = value.get()
            
        self._value = value
        if not  self._production:
            self._render()


    def get(self):
        return self._value
    
    def __add__(self,other):
        return self.get() + other
    
    def __sub__(self,other):
        return self.get() - other
    
    def __mul__(self,other):
        return self.get() * other
    
    def __truediv__(self,other):
        return self.get() / other
    
    def __floordiv__(self,other):
        return self.get() // other
    
    def __mod__(self,other):
        return self.get() % other
    
    def __pow__(self,other):
        return self.get() ** other
    
    def __eq__(self,other):
        return self.get() == other
    
    def __ne__(self,other):
        return self.get() != other
    
    def __lt__(self,other):
        return self.get() < other
    
    def __le__(self,other):
        return self.get() <= other
    
    def __gt__(self,other):
        return self.get() > other
    
    def __ge__(self,other):
        return self.get() >= other
    
    def __repr__(self) -> str:
        return str(self.get())
    
    def __bool__(self) -> bool:
        return bool(self.get())
    
    def __int__(self) -> int:
        return int(self.get())
    
    def __float__(self) -> float:
        return float(self.get())
    
    def __len__(self) -> int:
        return len(self.get())
    
 

    def __str__(self) -> str:
        return str(self.get())