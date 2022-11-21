import yaml 
import json 
import os
import time


class MainStack:
    stack = {}
    pointers = [stack]
    name = "stack"
    filetipe = "yml"
    production = False
    
    

    @staticmethod
    def render() -> None:
        if MainStack.production:return 
 
        if MainStack.filetipe == "yml":
            with open(f"{MainStack.name}.yml","w") as file:
                yaml.dump(MainStack.stack,file,indent=4)
        elif MainStack.filetipe == "json":
            with open(f"{MainStack.name}.json","w") as file:
                json.dump(MainStack.stack,file,indent=4)
        
        else:
            raise Exception('Filetipe not supported')
    
    
    