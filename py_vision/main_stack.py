from py_vision.sub_stack import SubStack
from py_vision.base_stack import BaseStack
import yaml 
import json 

class MainStack(BaseStack): 

    def __init__(self,enable:bool=True) -> None:
        self._itens = []
        self._plotages = []
        self._enable = enable
    


    def _render(self):
        current_frame_dict = {}
        for stack in self._itens:
            stack:SubStack
            current_frame_dict[stack._name] =stack._render()
        return current_frame_dict    
    
    def plot(self,line:int=None):
        if not self._enable:return
        render_result = self._render()
        render_result['line'] = line
        self._plotages.append(render_result)
    
    
    def dump(self,filename:str,ident=4):
        if not self._enable:return
        format = filename.split('.')[-1]
        if format == 'json':
            with open(filename,'w') as f:
                json.dump(self._plotages,f,indent=ident)