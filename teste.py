from py_vision import Stack
import inspect

def imprime(vezes):
    Stack.add_frame(inspect.currentframe())
    if vezes == 0:
        return
    print('imprimindo pela {} vez'.format(vezes))
    imprime(vezes-1)
    Stack.pop_frame(inspect.currentframe())

def impprime_num(num:int):
    Stack.add_frame(inspect.currentframe())


    print('imprimindo pela {} vez'.format(num))
    Stack.pop_frame(inspect.currentframe())

def format_list():
    Stack.add_frame(inspect.currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    
    for x in range(10):
        impprime_num(x)
        Stack.render(inspect.currentframe())  

    Stack.pop_frame(inspect.currentframe())

    

    
Stack.filetipe = 'json'
format_list()

