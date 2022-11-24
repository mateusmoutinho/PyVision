from py_vision2 import *
def formata_resposta(input:str, padrao:str) -> str:
    #removendo caractesres especiais
    Stack.add_frame(currentframe())

    letras_input = [letra for letra in input if letra.isalpha() or letra.isalnum()]
    letras_padrao = []
    caracteres = []  


    for idx,elemento in enumerate(padrao):
        Stack.render(currentframe())
        if elemento in ['N','L']:
            letras_padrao.insert(idx, elemento)
        else:
            caracteres.append({
                'caracter': elemento,
                'posicao': idx
            })
        Stack.render(currentframe())

    if len(letras_input) > len(letras_padrao):
        raise ValueError("O número de caracteres do input é maior que o número de caracteres do padrão")

    for l_input, l_padrao in zip(letras_input, letras_padrao):
        if l_input.isnumeric() and l_padrao == "N":
            pass
        elif l_input.isalpha() and l_padrao == "L":
            pass
        else:
            raise ValueError("Entrada não corresponde ao padrão")
    
    for e in caracteres:
        Stack.render(currentframe())
        if e['posicao'] < len(letras_input):
            letras_input.insert(e['posicao'], e['caracter'])
    letras_input = "".join(letras_input)
    return letras_input








formata_resposta('123456789','NNN.NNN.NNN-NN')
exec_view()