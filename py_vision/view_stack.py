from cli_args_system import Args
from py_vision.key import Key
import json
import yaml
from os import system
def get_stack_dict(stack_file:str)->dict:
    format = stack_file.split('.')[-1]
    try:
        with open(stack_file,'r') as file:
            stack = file.read()
    except FileNotFoundError:
        print('Stack file not found')
        return
    if format == 'json':
        stack = json.loads(stack)

    elif format == 'yaml':
        stack = yaml.load(stack)
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

    system(comand)
    stack = get_stack_dict(stack_file)

    index = 0
    print('press (ctrl,>) to next and (ctrl,<) to back  (ctrl,r) to repeat or  (ctrl,esc) to exit')
    while True:
        key = Key.get_key()
        if key == 'esc':
            break
        elif key == 'right':
            index += 1
        elif key == 'left':
            index -= 1
        elif key == 'r':
            system(comand)
            stack = get_stack_dict(stack_file)
        else:
            continue

        if index < 0:
            index = len(stack)-1
            
        if index >= len(stack):
            index = 0
        
        if out_format == 'json':
            with open(out,'w') as file:
                file.write(json.dumps(stack[index],indent=4))
        elif out_format == 'yaml':
            with open(out,'w') as file:
                file.write(yaml.dump(stack[index],indent=4))

    

if __name__ == '__main__':
    main()