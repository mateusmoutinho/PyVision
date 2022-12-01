from py_vision import *
def imprimi(stack,valor):
    s2 = stack.sub_stack(currentframe())
    #rint(valor)

def teste(stack):
    s1 = stack.sub_stack(currentframe())
    for x in range(10):
        imprimi(stack,x)
    

s = Stack(currentframe())
teste(s)
s.dump('teste.json')