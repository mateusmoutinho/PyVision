from stack_viewer.var import Var
from stack_viewer.introspect import get_var_name
from typing import Any,List
from types import FrameType
import inspect
import yaml 
import json 
import os
import time

class Stack:

    def __init__(self,name:str='stack',production:bool=False, format='yml', preserve_end_file:bool=True) -> None:
        self._stack:List(Var) = []
        self._name = name
        self._production = production
        self._format = format
        self._preserve_end_file = preserve_end_file
    
    def sleep(self,seconds:float):
        if not self._production:
            time.sleep(seconds)

    def var(self,value:Any=None,name:str =None):
        if name is None:
            frame = inspect.currentframe().f_back
            name = get_var_name(frame)
    
        created = Var(name,self._render,self._production)
        self._stack.append(created)
        created.set(value)       
        return created

    def _render(self):
        
        if  self._production:
            return 
   
        result = {}
        for var in self._stack:
            try:
                result[var.name] = var.get()
            except:
                result[var.name] = str(var)


        if self._format == 'yml':
            with open(f'{self._name}.yml','w') as f:
                yaml.dump(result,f)
        
        if self._format == 'json':
            with open(f'{self._name}.json','w') as f:
                json.dump(result,f,indent=4)
    

    def __del__(self):
        if self._production:
            return 

        if not self._preserve_end_file:
            try:
                os.remove(self._name)
            except:pass