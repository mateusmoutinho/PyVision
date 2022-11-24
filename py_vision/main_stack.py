import yaml 
import json 
import os
import time
import shutil

class MainStack:
    stack = {}
    pointers = [stack]
    name = "stack"
    filetipe = "yml"
    production = False
    iteration = 0
    
    shutil.rmtree('stack',ignore_errors=True)
    os.makedirs('stack')
    
    @staticmethod
    def add_pointer():
        MainStack.pointers.append(None)
        pass 

    def set_last_pointer_value(name:str,stack:dict):
        MainStack.pointers[-1] = stack
        MainStack.pointers[-2][name] = stack

    

    @staticmethod
    def pop(name:str):
        del MainStack.pointers[-2][name]        
        del MainStack.pointers[-1]

        
    @staticmethod
    def render() -> None:
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
    