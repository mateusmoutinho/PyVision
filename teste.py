from py_vision import *
def imprimi(stack:SubStack,valor):
    s2 = stack.sub_stack(currentframe())
    #rint(valor)

def teste(stack:MainStack):
    s1 = stack.sub_stack(currentframe())
    r = 29 
    x = 10
    s1.plot()
    
    for x in range(10):
        imprimi(s1,x)
    

s = MainStack()
teste(s)
s.dump('teste.json')