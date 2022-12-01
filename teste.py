from py_vision import *

class Carro:
    def __init__(self,cor:str,rodas:int) -> None:
        self.cor = cor
        self.rodas = rodas
        self._velocidade = 0
        self._aceleracao = 0
        self._freio = 0
    
    def acelerar(self,aceleracao:int):
        self._aceleracao = aceleracao
        self._velocidade += self._aceleracao
        self._freio = 0
 
def main(stack:MainStack):
    s1 = stack.sub_stack(currentframe())
    c = Carro('vermelho',4)
    s1.plot()
    c.acelerar(10)
    s1.plot()
     

s = MainStack()
main(s)
s.dump('teste.json')