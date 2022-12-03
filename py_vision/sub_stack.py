from typing import Any
from types import FrameType
from py_vision.base_stack import BaseStack

class SubStack(BaseStack): 

    def __init__(self,frame:FrameType,mother_stack:'SubStack'=None,enable:bool=True) -> None:
        self._frame = frame
        self._mother_stack = mother_stack
        self._itens = []
        self._name = frame.f_code.co_name
        self._enable = enable
        self.plot(frame)



    @staticmethod
    def _generate_serializible_frame(element:Any)->Any:
        from py_vision.main_stack import MainStack
        SERIALIZIBLE_TYPES = (int,float,str,bool)
        if isinstance(element,SERIALIZIBLE_TYPES):
            return element
        
        if isinstance(element,SubStack):
            return None 
        if isinstance(element,MainStack):
            return None

        if isinstance(element,FrameType):
            return SubStack._generate_serializible_frame(element.f_locals)

        if hasattr(element,'__dict__'):
            return SubStack._generate_serializible_frame(element.__dict__)
        
        if isinstance(element,dict):
            result = {}
            for x,y in element.items():
                generated = SubStack._generate_serializible_frame(y)
                if generated is not None:
                    result[x] = generated
            return result
        
        if isinstance(element,list):
            result = []
            for x in element:
                generated = SubStack._generate_serializible_frame(x)
                if generated is not None:
                    result.append(generated)
            return result

        try:  
            str(element)
        except:
            return None

    def _render(self):
        current_frame_dict = SubStack._generate_serializible_frame(self._frame)
        for stack in self._itens:
            stack:SubStack
            current_frame_dict[stack._name] =stack._render()
        return current_frame_dict    



    def plot(self,line:int or FrameType=None):
        if not self._enable:return
        if isinstance(line,FrameType):
            line = line.f_lineno
        self._mother_stack.plot(line)

