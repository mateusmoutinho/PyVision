from types import FrameType
import copy

def get_function_name(frame:FrameType):
    return frame.f_code.co_name

def generate_frame_dict(frame:FrameType):
    local_vars   = dict(frame.f_locals)
    formated_locals = copy.copy(local_vars)
    SERIALIZIBLE_TYPES = (int,float,str,bool,dict,list)
    for x,y in local_vars.items():
        
        if not  isinstance(y,SERIALIZIBLE_TYPES):
            formated_locals.pop(x)
            continue
    return formated_locals