from types import FrameType


class BaseStack:

    def sub_stack(self,frame:FrameType,enable:bool=True):
        if not self._enable:
            enable = False
        from py_vision.sub_stack import SubStack
        sub_stack = SubStack(frame=frame,mother_stack=self,enable=enable)
        self._itens.append(sub_stack)
        return self._itens[-1]
    