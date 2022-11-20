import yaml 
import json 
import os
class Stack:

    def __init__(self,name:str='stack',format='yml',preserve_end_file:bool=False) -> None:
        self._stack = {}
        self._name = name
        self._format = format
        self._preserve_end_file = preserve_end_file

    
    def _render(self):
        if self._format == 'yml':
            with open(self._name,'w') as f:
                yaml.dump(self._stack,f)
        elif self._format == 'json':
            with open(self._name,'w') as f:
                json.dump(self._stack,f,indent=4)
    

    def __del__(self):
        if not self._preserve_end_file:
            os.remove(self._name)