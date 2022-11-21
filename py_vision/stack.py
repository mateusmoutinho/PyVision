import yaml 
import json 
import os
import time


class Stack:
    stack = {}
    name = "stack"
    filetipe = "yml"
    production = True
    
    
    
    @staticmethod
    def render() -> None:
        if Stack.filetipe == 'yml':
            Stack.stack = yaml.load(open(f'{Stack.name}.yml'),Loader=yaml.FullLoader)
        
        elif Stack.filetipe == 'json':
            Stack.stack = json.load(open(f'{Stack.name}.json'))
        
        else:
            raise Exception('Filetipe not supported')
    
    
    