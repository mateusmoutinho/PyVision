from stack_viewer import Stack


def format_list(entrada,schema):
    s = Stack()
    entrada = s.var('entrada',entrada)
    schema = s.var('schema',schema)
    char = s.var('char',None)
    posicao_schema = s.var('posicao_schema',0)
    
    
    while posicao_schema < len(schema):
        
        posicao_schema.set(posicao_schema + 1)
        char.set(schema[posicao_schema.get()])

        
        s.sleep(1)

format_list('44107365824','NNN.NNN.NNN-24')

