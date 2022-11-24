from types import FrameType
import copy
import inspect

def get_var_name(frame:FrameType=None):
    try:
        line = frame.f_lineno
        code = inspect.getframeinfo(frame).code_context[0]
        var = code.split('=')[0].strip()
        if var.isidentifier():
            return var
        else:
            raise ValueError
    except Exception as e:
        raise Exception("You need to reference a variable to receive the answer")
    

def generate_frame_dict(frame:FrameType):
    local_vars   = dict(frame.f_locals)
    formated_locals = copy.copy(local_vars)
    SERIALIZIBLE_TYPES = (int,float,str,bool,dict,list)
    for x,y in local_vars.items():
        
        if not  isinstance(y,SERIALIZIBLE_TYPES):
            formated_locals.pop(x)
            continue
    return formated_locals