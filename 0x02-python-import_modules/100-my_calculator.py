#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    n = (sys.argv) - 1
    if n != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] != list(ops.keys()):
        print("unkown operator. Available operator: +, -, *, and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
