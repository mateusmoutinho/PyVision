from py_vision.stack import Stack
import keyboard
import shutil
import os
import time
import copy
import json
import yaml
import sys


class Key:
    last_time_pressed = time.time()
    @staticmethod
    def get_key():
        LIMIT = 0.25
        while True:
            key = keyboard.read_key()
            now = time.time()
            if now > Key.last_time_pressed + LIMIT:
                Key.last_time_pressed = now
                return key 
            

def exec_view(filename:str):
    if not Stack.enable:return 
    if not Stack.write:return
    type = filename.split('.')[-1]
    generated_list = Stack.generate_frames_list()
    size =(len(generated_list))
    current_frame = 0 
    NEXT = ['right','d']
    PREVIEWS = ['left','a']
    while True:
        
        key = Key.get_key()
        if key in NEXT:
            current_frame+=1
        if key in PREVIEWS:
            current_frame-=1
        if key == 'esc':
            sys.exit('finishing')
        
        if current_frame >=size:
            current_frame = 0 

        if current_frame < 0:
            current_frame = size-1

        iteration = copy.deepcopy(generated_list[current_frame])
        iteration['segment'] = current_frame
        if type == 'json':
            with open(filename,'w') as arq:
                json.dump(iteration,arq,indent=4)
        if type =='yaml':
             with open(filename,'w') as arq:
                yaml.dump(iteration,arq,indent=4)