
import inspect
from py_vision.main_stack import *
from types import FrameType
from typing import Any,List
import time 
import copy

class Stack:

    def __init__(self,stack_frame:FrameType,ignore:list=[]) -> None:
    
        self._ignore = ignore
        MainStack.add_frame(stack_frame,ignore)
        self.render()

    def render(self) -> List[Any]:
        
        if MainStack.production:return
        MainStack.render()
        pass 


