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

    
    while posicao_schema < len(schema):
        

        char_do_schema.set(schema[posicao_schema])
        char_da_entrada.set(entrada[posicao_texto])

        numero_ou_letra.set( char_do_schema in ['N','L'])
        
        if numero_ou_letra == True:
            posicao_texto.set(posicao_texto + 1)    
            texto_final.set(texto_final + char_da_entrada)
        else:
            if char_da_entrada == char_do_schema:
                posicao_texto.set(posicao_texto + 1)

            texto_final.set(texto_final + char_do_schema)
            
        posicao_schema.set(posicao_schema + 1)            

        s.sleep(3)

format_list('441.073.65824','NNN.NNN.NNN-NN')

