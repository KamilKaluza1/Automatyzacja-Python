spam = ['jabłka', 'banany', 'tofu', 'koty','jabłka', 'banany', 'tofu', 'koty']


def creator(spam):
    for value in spam[:-2]:
        print(str(value), end=', ')
    print(f'{spam[-2]} i {spam[-1]}')


creator(spam)