from py_vision.stack import Stack
import shutil
import os
def render_file(line:int):
    if Stack.filetipe == 'json':
        #copy the stack{line}.json to stack.json
        shutil.copyfile(f'stack/stack{line}.json', 'stack.json')

    elif Stack.filetipe == 'yaml':
        #copy the stack{line}.yaml to stack.yaml
        shutil.copyfile(f'stack/stack{line}.yaml', 'stack.yaml')


def exec_view():
    if Stack.production:
        return
    size = len(os.listdir('stack'))
    line= 0
    render_file(line)
    while True:
        action = input("Enter a command: ")
        if action == "e":
            break
        
        elif action == "":
            line += 1
        
        elif action == "a":
            line -= 1
        
        if line > size:
            line = 0

        if line < 0:
            line = 0
        render_file(line)
        
    

