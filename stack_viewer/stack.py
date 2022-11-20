from stack_viewer.var import Var
from typing import Any,List
import yaml 
import json 
import os

class Stack:

    def __init__(self,name:str='stack',production:bool=False, format='yml', preserve_end_file:bool=True) -> None:
        self._stack:List(Var) = []
        self._name = name
        self._production = production
        self._format = format
        self._preserve_end_file = preserve_end_file
        

    def var(self,name:str,value:Any=None):
        self._stack.append(Var(name,self._render,value,self._production))


 

    def _render(self):
        if  self._production:
            return 
        result = {}
        for var in self._stack:
            result[var.name] = var.get()

        if self._format == 'yml':
            with open(result,'w') as f:
                yaml.dump(self._stack,f)
        
        if self._format == 'json':
            with open(result,'w') as f:
                json.dump(self._stack,f,indent=4)
    

    def __del__(self):
        if self._production:
            return 

        if not self._preserve_end_file:
            try:
                os.remove(self._name)
            except:pass