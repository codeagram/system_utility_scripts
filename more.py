#!/usr/bin/env python3

""" Linux more command varient """

def more(text, numlines=15):

    """ Read a text file and display
        only the lines given as argument. If argument
        not given it will display every 10 lines. """

    lines = text.splitlines()

    while lines:

        first = lines[:numlines]
        lines = lines[numlines:]

        for line in first:
            print(line)

        if lines and input("More?") not in ["y", "Y"]:
            break


if __name__ == "__main__":
    import sys
    more(open(sys.argv[1]).read(), 10)
