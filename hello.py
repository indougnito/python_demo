#!/usr/bin/env python
'''
hello.py
Prints a hello message to stdout.
For help, try invoking with the '-h' flag.
'''
import argparse

def someMethod(args):
  print('Here are the arguments:')
  print(args)

if __name__ == '__main__':
  # parse arguments
  parser = argparse.ArgumentParser(description=__doc__,
                                   formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('-a', '--apple', type=str, default='granny smith',
                      help='the apple parameter')
  parser.add_argument('-b', '--banana', type=str, default='cavendish',
                      help='the banana parameter')
  args = parser.parse_args()
  # say hello
  print('Hello, world!')
  # execute a method
  someMethod(args)
  # say goodbye
  print('Goodnight, world.')
