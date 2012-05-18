#!/usr/bin/env python
# Filename: pyterm.py
# Description: This is the main class of the small library.
# Author: Daniel Bugl
# Copyright (c) 2012, Daniel Bugl

import curses

class PyTerm(object):
 def initEngine(self):
  curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.start_color()
 
 def __init__(self):
  self.initEngine()
  self.initColors()
  self.setColors()
  self.initWins()
  self.__log = []
 
 def setStatus(self, text):
  self.statwin.clear()
  for i in range(0, curses.COLS):
   self.statwin.addstr(" ", curses.color_pair(self.color_status))
  self.statwin.addstr(0, 0, text, curses.color_pair(self.color_status))
 
 def clearCmd(self):
  self.cmdwin.clear()
  for i in range(0, curses.COLS):
   self.cmdwin.addstr(" ", curses.color_pair(self.color_cmd))
  self.cmdwin.addstr(0, 0, "> ", curses.color_pair(self.color_cmd))
 
 def initStatWin(self):
  self.statwin = curses.newwin(1, curses.COLS+1, 0, 0)
 
 def initStdWin(self):
  self.stdwin = curses.newwin(curses.LINES-2, curses.COLS+1, 2, 0)
 
 def initCmdWin(self):
  self.cmdwin = curses.newwin(1, curses.COLS+1, 1, 0)
 
 def initWins(self):
  self.initStatWin()
  self.initCmdWin()
  self.initStdWin()
 
 def initColors(self):
  self.color_status = 1;
  self.color_cmd = 2;
  
 def setColors(self):
  curses.init_pair(self.color_status, curses.COLOR_BLACK, curses.COLOR_CYAN)
  curses.init_pair(self.color_cmd, curses.COLOR_WHITE, curses.COLOR_BLACK)
 
 def refresh(self):
  self.statwin.refresh()
  self.cmdwin.refresh()
  self.stdwin.refresh()
 
 def kill(self):
  curses.nocbreak()
  curses.echo()
  curses.endwin()
 
 def fillStdWin(self):
  self.stdwin.clear()
  log = reversed(self.__log)
  for l in log:
   self.stdwin.addstr(str(l))
  self.stdwin.refresh()
 
 def __rawlog(self, text, endl=True):
  if endl == True: text = str(text)+'\n'
  else: text = str(text)
  # Crop text, as text longer than the screen causes curses to crash
  # TODO: Would adding \n's instead of just cropping be better?
  self.__log.append(text[:curses.COLS])
  if len(self.__log) >= curses.LINES-2:
   toomanylines = (curses.LINES-2) - len(self.__log) + 1
   self.__log = self.__log[toomanylines:]
  self.fillStdWin()
 
 def log(self, text, endl=True):
  texts = text.split('\n')
  for t in reversed(texts):
   self.__rawlog(t, endl)
 
 def loop(self):
  self.clearCmd()
  curses.echo()
  s = self.cmdwin.getstr(0, 2, 50)
  curses.noecho()
  self.process(s)

 def process(self, cmd):
  self.log(cmd)
  self.loop()
 
 def main(self):
  self.setStatus("PyTerm")
  self.refresh()
  self.loop()

if __name__ == "__main__":
 pt = PyTerm()
 pt.main()
