
import inspect
from py_vision.introspect import get_var_name
from py_vision.main_stack import MainStack
from typing import Any,List
import time 
import copy
class Stack:

    def __init__(self,ignore:list=[]) -> None:
        frame = inspect.currentframe()
        self._name = get_var_name(frame.f_back)
        self._ignore = ignore
        MainStack.stack[self._name] ={}



    def render(self,locals:dict) -> List[Any]:
        if MainStack.production:return
        formated_locals = copy.deepcopy(locals)

        formated_locals.pop(self._name)
        
        SERIALIZIBLE_TYPES = (int,float,str,bool,dict,list)
        for x,y in locals.items():
            if x in self._ignore:
                formated_locals.pop(x)
                continue

            if not  isinstance(y,SERIALIZIBLE_TYPES):
                if hasattr(y,'__dict__'):
                    formated_locals[x] = y.__dict__
                else:
                    formated_locals[x] = str(y)
        MainStack.stack[self._name] = formated_locals
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
        line = inspect.currentframe().f_back.f_lineno
        MainStack.stack[self._name]["breakpoint"] = line

        
        r = input(f'type b to break on line {line}: ')
        if r == 'b':
            raise Exception('breakpoint')
        
    def __del__(self):
        if MainStack.production:return
       
        del MainStack.stack[self._name]
        MainStack.render()