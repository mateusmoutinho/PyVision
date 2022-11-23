from py_vision import Stack,MainStack
import inspect

def soma(x,y):

    soma = Stack(inspect.currentframe())
    #soma.render()
    return x+y

def format_list():
    estagio = 'entrada'
    
    format_list = Stack( inspect.currentframe())
    for x in range(10):
        estagio = 'loop'
        a = 20
        a1 = soma(a,10)
        format_list.render()

    
MainStack.filetipe = 'json'
format_list()

