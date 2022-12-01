
from py_vision.key import Key
from py_vision.introspect import generate_frame_dict,get_function_name
import yaml 
import json 
from types import FrameType
from copy import deepcopy
from sys import exit 

class Stack: 

    def __init__(self,frame:FrameType,mother_stack:'Stack'=None) -> None:
        self._frame = frame
        self._mother_stack = mother_stack
        self._itens = []
        self._plotages = []
        self._name = get_function_name(frame)
        self.plot()

    def sub_stack(self,frame:FrameType):
        self._itens.append(Stack(frame=frame,mother_stack=self))
        return self._itens[-1]
    
    def _render(self):
        current_frame_dict = generate_frame_dict(self._frame)
        for stack in self._itens:
            stack:Stack
            current_frame_dict[stack._name] =stack._render()
        return current_frame_dict    
    
    def plot(self):
        #these means is the first stack
        if self._mother_stack is None:
            self._plotages.append(self._render())
        else:
            self._mother_stack.plot()

    def dump(self,filename:str,ident=4):
        format = filename.split('.')[-1]
        if format == 'json':
            with open(filename,'w') as f:
                json.dump(self._plotages,f,indent=ident)