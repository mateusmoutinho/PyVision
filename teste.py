from py_vision import *
import inspect

def imprime(vezes):
    Stack.add_frame(currentframe())
    if vezes == 0:
        return
    print('imprimindo pela {} vez'.format(vezes))
    imprime(vezes-1)
    Stack.pop_frame(currentframe())

def impprime_num(num:int):
    Stack.add_frame(currentframe())

    
    print('imprimindo pela {} vez'.format(num))
    Stack.pop_frame(currentframe())

def format_list():
    Stack.add_frame(currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    

    for x in range(1000):
        impprime_num(x)
        Stack.render(currentframe())  

    Stack.pop_frame(currentframe())

    

    


try:
    format_list()
except Exception as e:
    pass 
Stack.dump(ident=4)