#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    for i in range(0, len(names)):
        if names[i].startswith('__'):
            continue
        else:
            print(f'{names[i]}')
