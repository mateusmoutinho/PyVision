
import inspect
from py_vision.introspect import get_var_name
from py_vision.main_stack import MainStack
from types import FrameType
from typing import Any,List
import time 
import copy
class Stack:

    def __init__(self,stack_frame:FrameType,ignore:list=[]) -> None:
        frame = inspect.currentframe()
        self._name = get_var_name(frame.f_back)
        self._stack_frame = stack_frame
    
        self._ignore = ignore
        MainStack.stack[self._name] ={}



    def render(self) -> List[Any]:
        
        if MainStack.production:return
        local_vars   = dict(self._stack_frame.f_locals)
        formated_locals = copy.copy(local_vars)
        
        SERIALIZIBLE_TYPES = (int,float,str,bool,dict,list)
        for x,y in local_vars.items():
            if x in self._ignore:
                formated_locals.pop(x)
                continue

            if not  isinstance(y,SERIALIZIBLE_TYPES):
                formated_locals.pop(x)
                continue

        MainStack.stack[self._name] = formated_locals
        MainStack.render()



    def sleep(self,seconds:float) -> None:
        if MainStack.production:return
        time.sleep(seconds)
   
    def render_and_sleep(self,seconds:float):
        self.render()
        self.sleep(seconds)
    
    def breakpoint(self):
        #MainStack.stack[self._name]
        if MainStack.production:return
        self.render()
        line = inspect.currentframe().f_back.f_lineno
        MainStack.stack[self._name]["breakpoint"] = line
        
        r = input(f'type b to break on line {line}: ')
        if r == 'b':
            raise Exception('breakpoint')
        


    def __del__(self):
        if MainStack.production:return
        try:
            del MainStack.stack[self._name]
        except:pass
        #MainStack.render()