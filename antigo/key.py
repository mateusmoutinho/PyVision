from keyboard import read_key
from time import time



class Key:
    last_time_pressed = time()

    @staticmethod
    def get_key():
        LIMIT = 0.25
        while True:
            key = read_key()
            now = time()
            if now > Key.last_time_pressed + LIMIT:
                Key.last_time_pressed = now
                return key 
            
