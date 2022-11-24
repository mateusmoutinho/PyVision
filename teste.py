from py_vision import Stack,MainStack
import inspect

def soma(x,y):

    soma = Stack(inspect.currentframe())
    #soma.render()
    return x+y
    
def format_list():
    format_list = Stack(inspect.currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    a = 20
    for x in range(3):
        a1 = soma(2,10)
    format_list.render()


    
MainStack.filetipe = 'json'
format_list()

