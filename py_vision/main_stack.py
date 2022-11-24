import yaml 
import json 
import os
import time
import shutil
from types import FrameType
from py_vision.introspect import get_var_name,generate_frame_dict
class MainStack:
    frames = []   
    name = "stack"
    filetipe = "yml"
    production = False
    iteration = 0
    
    shutil.rmtree(name,ignore_errors=True)
    os.makedirs(name)
    
    @staticmethod
    def add_frame(frame:FrameType,ignore:list):
        MainStack.frames.append({
            "frame":frame,
            "ignore":ignore,
            'name':get_var_name(frame)
        })

    @staticmethod
    def remove_unexistent_frames():
        print('iteration----------------')
        for frame in MainStack.frames:
            print(frame)

    @staticmethod
    def generate_frames_dict():
        MainStack.remove_unexistent_frames()
        frames_dict = {}
        last_dict = frames_dict
        for f in MainStack.frames:
    
            last_dict[f['name']] = generate_frame_dict(f['frame'])
            last_dict = last_dict[f['name']]
        return frames_dict


    @staticmethod
    def render() -> None:
        stack = MainStack.generate_frames_dict()
        if MainStack.production:return 
        name = f"stack/{MainStack.name}{MainStack.iteration}"
        
        if MainStack.filetipe == "yml":
            with open(f"{name}.yml","w") as file:
                yaml.dump(stack,file,indent=4)

        elif MainStack.filetipe == "json":
            with open(f"{name}.json","w") as file:
                json.dump(stack,file,indent=4)
        
        else:
            raise Exception('Filetipe not supported')
    
        MainStack.iteration+=1
    