import yaml 
import json 
import os
import time
import shutil

class MainStack:
    stack = []
    names = []
    name = "stack"
    filetipe = "yml"
    production = False
    iteration = 0
    
    shutil.rmtree(name,ignore_errors=True)
    os.makedirs(name)
    
    @staticmethod
    def add_stack(name:str):
        MainStack.stack.append({})
        MainStack.names.append(name)

    def set_last_stack_value(stack:dict):
        MainStack.stack[-1] = stack
    
    @staticmethod
    def pop():
        MainStack.stack.pop()
        MainStack.names.pop()
    
    @staticmethod
    def generate_stack_dict()->dict:
        total = range(len(MainStack.names))
        print(total)
        
    @staticmethod
    def render() -> None:
        MainStack.generate_stack_dict()
        if MainStack.production:return 
        name = f"stack/{MainStack.name}{MainStack.iteration}"
        
        if MainStack.filetipe == "yml":
            with open(f"{name}.yml","w") as file:
                yaml.dump(MainStack.stack,file,indent=4)

        elif MainStack.filetipe == "json":
            with open(f"{name}.json","w") as file:
                json.dump(MainStack.stack,file,indent=4)
        
        else:
            raise Exception('Filetipe not supported')
    
        MainStack.iteration+=1
    