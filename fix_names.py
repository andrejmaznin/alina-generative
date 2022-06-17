from os import listdir, rename

for index, name in enumerate(listdir('data')):
    rename('data/' + name, f'data/{index}.png')
