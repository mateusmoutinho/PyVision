from py_vision import Stack,MainStack

def soma(x,y):
    soma = Stack()
    soma.breakpoint(locals())
    return x+y

def format_list(elementos):
    estagio = 'entrada'
    format_list = Stack(ignore=['elementos'])
    
    format_list.render(locals())
    for l in elementos:
        estagio = 'loop'
        r = soma(l['x'],l['y'])
        format_list.breakpoint(locals())

MainStack.filetipe = 'json'
format_list([

    {'x':1,'y':2},
    {'x':3,'y':4},
    {'x':5,'y':6},

 ])

