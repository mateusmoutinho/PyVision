from py_vision import *
def imprimi(y):
    Stack.disable_next = True
    Stack.start(currentframe())
    print('primeira funcao',y)
    Stack.end()

def imprim2(y):
    v = [10,20,30]
    Stack.start(currentframe(),ignore=['v'])
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
