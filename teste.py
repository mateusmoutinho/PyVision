from py_vision import *
def main(stack:MainStack):
    smain = stack.sub_stack(currentframe())
    a = 1
    b = 2
    smain.plot()



if __name__ == '__main__':
    main_stack = MainStack()
    main(main_stack)
    main_stack.dump('teste.json')
