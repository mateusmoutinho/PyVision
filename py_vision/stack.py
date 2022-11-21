
import inspect
from py_vision.introspect import get_var_name
from py_vision.main_stack import MainStack
from typing import Any,List
import time 

class Stack:

    def __init__(self,stack_acess:callable) -> None:
        frame = inspect.currentframe()
        self._name = get_var_name(frame.f_back)
        self._stack_acess = stack_acess
    
    def render(self) -> List[Any]:
        if MainStack.production:return
        generated:dict =  self._stack_acess(self._name)
        SERIALIZIBLE_TYPES = (int,float,str,bool)
        for x,y in generated.items():
            if not  isinstance(y,SERIALIZIBLE_TYPES):
                if hasattr(y,'__dict__'):
                    generated[x] = y.__dict__
                else:
                    generated[x] = str(y)
        MainStack.stack[self._name] = generated
    
    
    def sleep(self,seconds:float) -> None:
        if MainStack.production:return
        time.sleep(seconds)

    def __del__(self):
        del MainStack.stack[self._name]
        