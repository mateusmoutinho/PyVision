from py_vision import Stack,MainStack
import inspect
def soma(x,y):

    soma = Stack(inspect.currentframe())
    soma.breakpoint()
    return x+y

def format_list():
    estagio = 'entrada'
    
    s = Stack( inspect.currentframe())
    for x in range(10):
        estagio = 'loop'
        a = 20
        a1 = soma(a,10)
        s.render_and_sleep(1)

    
#MainStack.filetipe = 'json'
format_list()

