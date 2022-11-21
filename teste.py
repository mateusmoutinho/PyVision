from stack_viewer import Stack


def format_list(entrada,schema):
    
    s = Stack()
    entrada = s.var(entrada)
    schema = s.var(schema)
    char_do_schema = s.var()
    char_da_entrada = s.var()
    posicao_schema = s.var(0)
    posicao_texto = s.var(0)
    numero_ou_letra = s.var()
    texto_final = s.var('')

    
    while posicao_texto < len(entrada):
        

        char_do_schema.v = schema[posicao_schema]
        char_da_entrada.v = entrada[posicao_texto]

        s.sleep(1)
        numero_ou_letra.v = char_do_schema in ['N','L']
        
        if numero_ou_letra == True:
            posicao_texto.v = posicao_texto + 1    
            texto_final.v = texto_final + char_da_entrada
        else:
            if char_da_entrada == char_do_schema:
                posicao_texto.v = posicao_texto + 1

            texto_final.v = texto_final + char_do_schema
            
        posicao_schema.v = posicao_schema + 1  


format_list('441.073.65824','NNN.NNN.NNN-NN')

