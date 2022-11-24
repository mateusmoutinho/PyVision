from py_vision import *
import inspect


def impprime_num(num:int):
    START(currentframe())
    print('imprimindo pela {} vez'.format(num))
    END(currentframe())


def format_list():
    START(currentframe())
    estagio = 'entrada'
    estagio = 'loop'
    
    for x in range(10):
        impprime_num(10)
        PLOT(currentframe())

    END(currentframe())

    


try:
    format_list()
except Exception as e:
    pass 

Stack.dump(ident=4)
