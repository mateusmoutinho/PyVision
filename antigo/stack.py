
from py_vision.key import Key
from py_vision.introspect import generate_frame_dict,get_function_name
import yaml 
import json 
from types import FrameType
from copy import deepcopy
from sys import exit
class Stack:
    acumulated_frames = []
    frames = []   
    write = True
    acumulate = True
    enable = True
    disable_next = False

    #dealing with list of frames


    @staticmethod
    def start(frame:FrameType,ignore:list=[]):
        if not Stack.enable:return 
        if Stack.disable_next:return

        Stack.frames.append({
            "frame":frame,
            "ignore":ignore,
            'name':get_function_name(frame)
        })
        Stack.plot(frame)

    
    @staticmethod
    def end(line:int or FrameType =None):
        if not Stack.enable:return 
        if Stack.disable_next:
            Stack.disable_next = False
            return
        Stack.plot(line)
        Stack.frames.pop()


    @staticmethod
    def plot(line:int or FrameType =None) -> None:        
        if not Stack.enable:return 
        stack = Stack.generate_frames_dict()
        if isinstance(line,FrameType):
            line = line.f_lineno
        stack['line'] = line
        if Stack.acumulate:
            Stack.acumulated_frames.append(stack)
       

    @staticmethod
    def generate_frames_dict()->dict:
        frames_dict = {}
        last_dict = frames_dict
        
        for f in Stack.frames:
            last_dict[f['name']] = generate_frame_dict(f['frame'],f['ignore'])
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
        else:
            raise Exception('type not valid')


    @staticmethod
    def dump(filename:str='stack.yml',ident:int=None):
        if not Stack.enable:return 
        if not Stack.write:return
        type = filename.split('.')[-1]
        with open(filename,'w') as f:
                f.write(Stack.dumps(type,ident))


    @staticmethod
    def exec_view(filename:str):
        if not Stack.enable:return 
        if not Stack.write:return
        type = filename.split('.')[-1]
        generated_list = Stack.generate_frames_list()
        size =(len(generated_list))
        current_frame = 0 
        NEXT = ['right','d']
        PREVIEWS = ['left','a']
        print('type >= for next frame < for previews frame or esc to exit:')

        while True:
            
            key = Key.get_key()
            if key in NEXT:
                current_frame+=1
            if key in PREVIEWS:
                current_frame-=1
            if key == 'esc':
                exit('finishing')
            
            if current_frame >=size:
                current_frame = 0 

            if current_frame < 0:
                current_frame = size-1

            iteration = deepcopy(generated_list[current_frame])
            iteration['segment'] = current_frame
            if type == 'json':
                with open(filename,'w') as arq:
                    json.dump(iteration,arq,indent=4)
            elif type =='yaml':
                with open(filename,'w') as arq:
                    yaml.dump(iteration,arq,indent=4)
            else:
                print('type not valid')
                exit()