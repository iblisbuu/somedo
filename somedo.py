#!/usr/bin/env python3

from tkinter import Tk
from sys import argv
from base.gui import GUI
from base.cli import CLI

if __name__ == '__main__':	# start here if called as program / app / commaand
	if len(argv) == 1:
		root = Tk()
		GUI(root)
		root.mainloop()
	else:
		CLI(argv)
