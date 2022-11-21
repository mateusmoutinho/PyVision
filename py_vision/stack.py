
import inspect
from py_vision.introspect import get_var_name
from py_vision.main_stack import MainStack
from typing import Any,List
import time 

class Stack:

    def __init__(self) -> None:
        frame = inspect.currentframe()
        self._name = get_var_name(frame.f_back)
      

    def render(self,locals:dict) -> List[Any]:
        if MainStack.production:return
        locals.pop(f'{self._name}')
        
        SERIALIZIBLE_TYPES = (int,float,str,bool,dict,list)
        for x,y in locals.items():
            if not  isinstance(y,SERIALIZIBLE_TYPES):
                if hasattr(y,'__dict__'):
                    locals[x] = y.__dict__
                else:
                    locals[x] = str(y)
        MainStack.stack[self._name] = locals
        MainStack.render()



    def sleep(self,seconds:float) -> None:
        if MainStack.production:return
        time.sleep(seconds)
   
    def render_and_sleep(self,seconds:float,locals:dict):
        self.render(locals)
        self.sleep(seconds)
    
    def breakpoint(self,locals:dict):
        #MainStack.stack[self._name]
        if MainStack.production:return
        self.render(locals)
        r = input('type b to break: ')
        if r == 'b':
            raise Exception('breakpoint')
        
    def __del__(self):
        if MainStack.production:return
        try:
            del MainStack.stack[self._name]
        except KeyError:
            pass