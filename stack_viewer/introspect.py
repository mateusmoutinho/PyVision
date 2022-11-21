from types import FrameType
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
