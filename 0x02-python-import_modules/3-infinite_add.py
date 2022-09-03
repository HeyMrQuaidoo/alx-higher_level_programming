#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    out = 0
    for arg in argv[1:]:
        out += int(arg)
    print("{}".format(out))
