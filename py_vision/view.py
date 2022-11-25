from py_vision.stack import Stack
import keyboard
import shutil
import os
import time

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
            

def exec_view():
    if not Stack.enable:return 
    if not Stack.write:return
    generated_list = Stack.generate_frames_list()
    possibles = range(len(generated_list))
    current_frame = 0 
    NEXT = ['right','d']
    PREVIEWS = ['left','a']
    while True:
        
        key = Key.get_key()
        if key in NEXT:
            current_frame+=1
        if key in PREVIEWS:
            current_frame-=1
        
        if current_frame not in possibles:
            current_frame = 0 
        
         