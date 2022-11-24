import yaml 
import json 
import os
import copy
import time
import shutil
from types import FrameType
from py_vision.introspect import generate_frame_dict,get_function_name

class Stack:
    acumulated_frames = []
    frames = []   
    filename = "stack"
    write = True
    acumulate = True
    enable = True
    

    #dealing with list of frames
    @staticmethod
    def add_frame(frame:FrameType,ignore:list=[]):
        if not Stack.enable:return 
        Stack.frames.append({
            "frame":frame,
            "ignore":ignore,
            'name':get_function_name(frame)
        })
        Stack.render(frame)

    
    @staticmethod
    def pop_frame(line:int or FrameType =None):
        if not Stack.enable:return 
        Stack.render(line)
        Stack.frames.pop()


    @staticmethod
    def generate_frames_dict()->dict:
        frames_dict = {}
        last_dict = frames_dict
        
        for f in Stack.frames:
            last_dict[f['name']] = generate_frame_dict(f['frame'])
            last_dict = last_dict[f['name']]
        
        return frames_dict
    

    @staticmethod
    def generate_frames_list()->list:
        if  Stack.acumulate:
            return  Stack.acumulated_frames
        else:
            return  [Stack.generate_frames_dict()]
         
       
    @staticmethod
    def dumps(type:str='json',ident:int=None):
        if not Stack.enable:return 
        if type == 'yaml':
            return yaml.dump(Stack.generate_frames_list(),indent=ident)
        elif type == 'json':
            return json.dumps(Stack.generate_frames_list(),indent=ident)

    @staticmethod
    def dump(type:str='json',ident:int=None):
        if not Stack.enable:return 
        if not Stack.write:return
        Stack.filename = Stack.filename.split('.')[0]
        with open(f'{Stack.filename}.{type}','w') as f:
                f.write(Stack.dumps(type,ident))

    @staticmethod
    def render(line:int or FrameType =None) -> None:        
        if not Stack.enable:return 
        stack = Stack.generate_frames_dict()
        if isinstance(line,FrameType):
            line = line.f_lineno
        stack['line'] = line
        if Stack.acumulate:
            Stack.acumulated_frames.append(stack)