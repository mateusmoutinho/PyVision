from py_vision import *
def imprimi(y):
    Stack.disable_next = True
    Stack.start(currentframe())
    print('primeira funcao',y)
    Stack.end()

def imprim2(y):
    
    Stack.start(currentframe())
    print('segunda funcao',y)
    Stack.end()
def teste():
    Stack.start(currentframe())
    for x in range(10):
        imprimi(x)
        imprim2(x)
        Stack.plot()
    Stack.end()


teste()
Stack.exec_view('teste.json')
