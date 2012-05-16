#!/usr/bin/env python
# Filename: pyshell.py
# Description: This is an example for the PyTerm library.
# Author: Daniel Bugl
# Copyright (c) 2012, Daniel Bugl

from pyterm import PyTerm
from subprocess import check_output

class PyShell(PyTerm):
 def process(self, cmd):
  self.log(check_output(cmd.split(" ")), endl=False)
  self.log("> "+cmd)
  self.loop()
 
 def main(self):
  self.setStatus("PyShell -- This is a simple shell. EXECUTE COMPLEX COMMANDS AT YOUR OWN RISK!")
  self.refresh()
  self.loop()

if __name__ == "__main__":
 ps = PyShell()
 ps.main()
