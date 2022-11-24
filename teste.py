from py_vision import Stack,MainStack
import inspect

def soma(x,y):

    soma = Stack(inspect.currentframe())
    #soma.render()
    soma.close()
    return x+y
    
def format_list():
    format_list = Stack(inspect.currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    a = 20
    a1 = soma(a,10)
    format_list.render()

    format_list.close()

    
MainStack.filetipe = 'json'
format_list()

