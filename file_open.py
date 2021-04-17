#!/usr/bin/env python3
import os, sys, subprocess
""" Open file using appropriate app """


def open_file(filename):

    if sys.platform == "win32":
        os.startfile(filename)

    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


if __name__ == "__main__":

    for i in range(10):
        open_file(sys.argv[1])
