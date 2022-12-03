from py_vision import *


def imprimi(substack:SubStack,valor):
    simprimi = substack.sub_stack(currentframe())
    print(valor)
    simprimi.plot()
    simprimi.end()

def main(stack:MainStack):
    smain = stack.sub_stack(currentframe())
    for x in range(10):
        imprimi(smain,x)
    r = 20
    smain.plot()



if __name__ == '__main__':
    main_stack = MainStack()
    main(main_stack)
    main_stack.dump('teste.json')
