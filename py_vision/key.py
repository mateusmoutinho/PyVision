from keyboard import read_key, is_pressed
from time import time



class Key:
    last_time_pressed = time()

    @staticmethod
    def get_key()->str:
        LIMIT = 0.25
        while True:
            #verify if ctrl is pressed 
            
            if not is_pressed('ctrl'):
                continue
                 
            key = read_key()
            now = time()
            if now > Key.last_time_pressed + LIMIT:
                Key.last_time_pressed = now
                return key 
            
