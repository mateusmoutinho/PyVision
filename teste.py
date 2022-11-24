from py_vision import Stack
import inspect

def imprime(vezes):
    Stack.add_frame(inspect.currentframe())
    if vezes == 0:
        return
    print('imprimindo pela {} vez'.format(vezes))
    imprime(vezes-1)
    Stack.pop_frame()

    
    
def format_list():
    Stack.add_frame(inspect.currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    imprime(10)    
    Stack.pop_frame()

    

    
Stack.filetipe = 'json'
format_list()

