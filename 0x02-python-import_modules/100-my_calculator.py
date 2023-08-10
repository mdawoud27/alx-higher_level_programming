#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1 as calc

    
    def switch(a, ope, b):

        if ope == '+':
            print(f'{a} + {b} = {calc.add(a, b)}')
        elif ope == '-':
            print(f'{a} - {b} = {calc.sub(a, b)}')
        elif ope == '*':
            print(f'{a} * {b} = {calc.mul(a, b)}')
        elif ope == '/':
            print(f'{a} / {b} = {calc.div(a, b)}')
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)


    argv = sys.argv
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(argv[1])
        ope = argv[2]
        b = int(argv[3])
        switch(a, ope, b)
