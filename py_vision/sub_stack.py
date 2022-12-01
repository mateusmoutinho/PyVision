
from py_vision.key import Key
from py_vision.introspect import generate_frame_dict,get_function_name
import yaml 
import json 
from types import FrameType
from copy import deepcopy
from sys import exit 

class SubStack: 

    def __init__(self,frame:FrameType,mother_stack:'SubStack'=None) -> None:
        self._frame = frame
        self._mother_stack = mother_stack
        self._itens = []
        self._plotages = []
        self._name = get_function_name(frame)
        self.plot()

    def sub_stack(self,frame:FrameType):
        self._itens.append(SubStack(frame=frame,mother_stack=self))
        return self._itens[-1]
    
    def _render(self):
        current_frame_dict = generate_frame_dict(self._frame)
        for stack in self._itens:
            stack:SubStack
            current_frame_dict[stack._name] =stack._render()
        return current_frame_dict    
    
    def plot(self):
        self._mother_stack.plot()

