from py_vision import Stack,MainStack

def formata_resposta(input:str, padrao:str) -> str:
    #removendo caractesres especiais
    s = Stack()
    letras_input = [letra for letra in input if letra.isalpha() or letra.isalnum()]
    letras_padrao = []
    caracteres = []  
    s.render(locals())

    for idx,elemento in enumerate(padrao):

        if elemento in ['N','L']:
            letras_padrao.insert(idx, elemento)
        else:
            caracteres.append({
                'caracter': elemento,
                'posicao': idx
            })
        s.breakpoint(locals())
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
        if e['posicao'] < len(letras_input):
            letras_input.insert(e['posicao'], e['caracter'])
    letras_input = "".join(letras_input)
    return letras_input








formata_resposta('123456789','NNN.NNN.NNN-NN')