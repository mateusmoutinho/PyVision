from cli_args_system import Args
from py_vision.key import Key
import json
import yaml

def main():

    args = Args()
    comand = args.flag_str('comand','c')
    if not comand:
        print('Comand not found')
        return
    stack_file = args.flag_str('stack_file','s')
    if not stack_file:
        print('Stack file not found')
        return
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

    while True:
        key = Key.get_key()
        if key == 'esc':
            break
        

    

if __name__ == '__main__':
    main()