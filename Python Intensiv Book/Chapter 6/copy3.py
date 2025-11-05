import shutil

def my_xml(tag, content='', **kwargs):
    parameters = ''.join([f' {k}="{v}"' for k, v in kwargs.items()])
    return f'<{tag}{parameters}>{content}</{tag}>'

# print(my_xml('t', 'c', a=1, b=2, c=3))
# print(my_xml('t', 'c'))
# print(my_xml('t', a=1, b=2, c=3))
# print(my_xml('t'))

def copy_file(input_file, *args):
    for file in args:
        shutil.copy(input_file, file)
    print('Done!')

copy_file('task25.py', 'copy1.txt', 'copy2', 'copy3.py')
