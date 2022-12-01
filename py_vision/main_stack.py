from py_vision.sub_stack import SubStack
import yaml 
import json 
from types import FrameType
from copy import deepcopy
from sys import exit 

class MainStack: 

    def __init__(self) -> None:

        self._itens = []
        self._plotages = []
    

    def sub_stack(self,frame:FrameType):
        self._itens.append(SubStack(frame=frame,mother_stack=self))
        return self._itens[-1]
    
    def _render(self):
        current_frame_dict = {}
        for stack in self._itens:
            stack:SubStack
            current_frame_dict[stack._name] =stack._render()
        return current_frame_dict    
    
    def plot(self,line:int=None):
        render_result = self._render()
        render_result['line'] = line
        self._plotages.append(render_result)
    
    
    def dump(self,filename:str,ident=4):
        format = filename.split('.')[-1]
        if format == 'json':
            with open(filename,'w') as f:
                json.dump(self._plotages,f,indent=ident)