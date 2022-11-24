import yaml 
import json 
import os
import time
import shutil
from types import FrameType
from py_vision.introspect import generate_frame_dict,get_function_name

class Stack:
    frames = []   
    name = "stack"
    filetipe = "yml"
    production = False
    iteration = 0
    
    shutil.rmtree(name,ignore_errors=True)
    os.makedirs(name)
    
    @staticmethod
    def add_frame(frame:FrameType,ignore:list=[]):
        Stack.frames.append({
            "frame":frame,
            "ignore":ignore,
            'name':get_function_name(frame)
        })
        Stack.render(frame)

    def pop_frame():
        Stack.render()
        Stack.frames.pop()
    
    @staticmethod
    def generate_frames_dict():
        frames_dict = {}
        last_dict = frames_dict
        
        for f in Stack.frames:
            last_dict[f['name']] = generate_frame_dict(f['frame'])
            last_dict = last_dict[f['name']]
        
        return frames_dict


    @staticmethod
    def render(line:int or FrameType =None) -> None:
 
        
        if Stack.production:return 
        stack = Stack.generate_frames_dict()
        if isinstance(line,FrameType):
            line = line.f_lineno
        stack['line'] = line
        name = f"stack/{Stack.name}{Stack.iteration}"
        
        if Stack.filetipe == "yml":
            with open(f"{name}.yml","w") as file:
                yaml.dump(stack,file,indent=4)

        elif Stack.filetipe == "json":
            with open(f"{name}.json","w") as file:
                json.dump(stack,file,indent=4)
        
        else:
            raise Exception('Filetipe not supported')
    
        Stack.iteration+=1
    