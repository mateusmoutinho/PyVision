from cli_args_system import Args
from py_vision.key import Key
import json
import yaml
from os import system,remove

def get_stack_list(stack_file:str)->list:
    format = stack_file.split('.')[-1]
    try:
        with open(stack_file,'r') as file:
            stack = file.read()
    except FileNotFoundError:
        print('Stack file not found')
        return []
    if format == 'json':
        stack = json.loads(stack)

    elif format == 'yaml':
        stack = yaml.load(stack)
    if not isinstance(stack,list):
        print('Stack file not valid')
        return []
    return stack

def restart(comand:str,stack_file:str, out:str):
    try:
        remove(stack_file)
    except FileNotFoundError:
        pass
    try:
        remove(out)
    except FileNotFoundError:
        pass
    system(comand)
    stack = get_stack_list(stack_file)
    return stack
def main():
    #getting comands
    args = Args()
    comand = args.flag_str('comand','c')
    if not comand:
        print('Comand not found')
        return
    stack_file = args.flag_str('stack_file','s')
    if not stack_file:
        print('Stack file not found')
        return
    out = args.flag_str('out','o')
    if not out:
        out = 'stack_point.json'
      
    out_format = out.split('.')[-1]
    #executing comand


    stack = restart(comand,stack_file, out)

    index = 0
    print(
        'press: (shitf + <) to previews breakpoint',
        'press: (shitf + <) to next breakpoint '
        'press: (shitf + s) to restart ',
        'press: esc to exit'
    )
    while True:
        key = Key.get_key()
        if key == 'esc':
            break
        elif key == 'right':
            index += 1
        elif key == 'left':
            index -= 1
        elif key == 's':
            print('restarting..')
            #delete stack and out   
            stack = restart(comand,stack_file, out)

   

        if index < 0:
            index = len(stack)-1
            
        if index >= len(stack):
            index = 0

        try:
            out_dict = stack[index]
        except IndexError:
            out_dict = {}

        
        if out_format == 'json':
            with open(out,'w') as file:
                file.write(json.dumps(out_dict,indent=4))
        elif out_format == 'yaml':
            with open(out,'w') as file:
                file.write(yaml.dump(out_dict,indent=4))

    print('finished')

if __name__ == '__main__':
    main()