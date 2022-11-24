from py_vision.stack import Stack
from py_vision.introspect import generate_frame_dict,get_function_name
from types import FrameType


def START(frame:FrameType,ignore:list=[]):
    if not Stack.enable:return 
    Stack.frames.append({
        "frame":frame,
        "ignore":ignore,
        'name':get_function_name(frame)
    })
    PLOT(frame)


def END(line:int or FrameType =None):
    if not Stack.enable:return 
    PLOT(line)
    Stack.frames.pop()


def PLOT(line:int or FrameType =None) -> None:        
    if not Stack.enable:return 
    stack = Stack.generate_frames_dict()
    if isinstance(line,FrameType):
        line = line.f_lineno
    stack['line'] = line
    if Stack.acumulate:
        Stack.acumulated_frames.append(stack)
