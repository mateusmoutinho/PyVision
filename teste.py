from py_vision import *

def adiciona_mascara(numero:str or float):

    #tirando ponto 
    
    try:
        numero = float(numero)
    except ValueError:
        raise Exception("Valor inválido")
    numero = str(numero)
    numero = numero.replace('.',',')
    numero,centavos = numero.split(',')
    if len(centavos) == 1:
        centavos = centavos + '0'

    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    numeros_invertidos = list(reversed(numero))
    numeros = list(chunks(numeros_invertidos,3))
    numeros = list(reversed(numeros))
    numeros = '.'.join([''.join(reversed(n)) for n in numeros]) + ',' + centavos

    


adiciona_mascara(4552.4)
Stack.exec_view('teste.json')
