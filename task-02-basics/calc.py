import sys

if len(sys.argv) != 4:
    print("Usage: calc.py <a> <op> <b>")
    sys.exit(1)

a, op, b = sys.argv[1], sys.argv[2], sys.argv[3]
a, b = float(a), float(b)

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print(f"Unknown op: {op}")