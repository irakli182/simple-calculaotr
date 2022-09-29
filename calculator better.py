import sys
print('to exit type "exit"')
while True:
    try:
        str_magaliti = input("input: ")
        if str_magaliti == "exit":
            sys.exit(0)
        splited = str_magaliti.split()
        x = splited[0]
        z = splited[1]
        y = splited[2]
    except IndexError:
        continue
    x = int(x)
    y = int(y)
    operators = ["+", "-", "*", "/", "^"]
    if z == "+":
        print("       " + str(x + y))
        continue
    elif z == "-":
        print("       " + str(x - y))
        continue
    elif z == "*":
        print("       " + str(x * y))
        continue
    elif z == "/":
        print("       " + str(x / y))
        continue
    elif z == "^":
        print("       " + str(x ** y))
        continue
