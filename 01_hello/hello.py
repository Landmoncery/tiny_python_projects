#!/usr/bin/env python
# purpose: Say Hello

import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('name', help='Name to greet')
args = parser.parse_args()

print('Hello, ' + args.name + '!')