#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1 as calc

    argv = sys.argv
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(argv[1])
        ope = argv[2]
        b = int(argv[3])

        if ope == '+':
            print(calc.add(a, b))
        elif ope == '-':
            print(calc.sub(a, b))
        elif ope == '*':
            print(calc.mul(a, b))
        elif ope == '/':
            print(calc.div(a, b))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
