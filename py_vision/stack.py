import yaml 
import json 
from py_vision.introspect import generate_frame_dict,get_function_name

class Stack:
    acumulated_frames = []
    frames = []   
    filename = "stack"
    write = True
    acumulate = True
    enable = True
    


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

