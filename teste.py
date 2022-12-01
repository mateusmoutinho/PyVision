from py_vision import Stack
def imprimi(stack,valor):
    print(valor)

def teste(stack):
    s1 = stack.sub_stack(stack._frame)
    for x in range(10):
        print(x)
    

s = Stack()
teste(s)