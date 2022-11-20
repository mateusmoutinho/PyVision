from typing import Any

class Var:

    def __init__(self,name:str,render:callable,value:Any,production:bool=False) -> None:
        self.name = name
        self._render = render
        self._production = production
        self._value = value
    
    #build in method for = operator
    def set(self,value):

        self._value = value
        if not  self._production:
            self._render()

    def get(self):
        return self._value
    
    def __str__(self) -> str:
        return str(self.get())